# -*- coding: utf-8 -*-

from datetime import datetime
import os
from pathlib import Path
from jinja2 import Template
import shutil
import sys
import click
from slugify import slugify
from invoke import task

from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    # Local path configuration (can be absolute or relative to tasks.py)
    "deploy_path": "output",
    # Host and port for `serve`
    "host": "localhost",
    "port": 8001,
}
CATEGORIES = (
    "Allgemein",
    "Digital",
    "Kunst und Kultur",
    "Politik und Gesellschaft",
    "Wissenschaft und Technik",
)


@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(c):
    """Build local version of site"""
    c.run("pelican -s pelicanconf.py", pty=True)


@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run("pelican -d -s pelicanconf.py")


@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run("pelican -r -s pelicanconf.py")


@task
def serve(c):
    """Serve site at http://localhost:8000/"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG["deploy_path"], ("", CONFIG["port"]), ComplexHTTPRequestHandler
    )

    sys.stderr.write("Serving on port {port} ...\n".format(**CONFIG))
    server.serve_forever()


@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)


@task
def preview(c):
    """Build production version of site"""
    c.run("pelican -s publishconf.py")


@task
def publish(c):
    """Publish to production via rsync"""
    c.run("pelican -s publishconf.py")


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG["settings_base"], lambda: build(c))
    # Watch content source files
    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_blob = "{0}/**/*{1}".format(SETTINGS["PATH"], extension)
        server.watch(content_blob, lambda: build(c))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS["THEME"]
    server.watch("{}/templates/*.html".format(theme_path), lambda: build(c))
    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file = "{0}/static/**/*{1}".format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured host and port
    server.serve(host=CONFIG["host"], port=CONFIG["port"], root=CONFIG["deploy_path"])


@task
def movefile(c, old, new):
    """Move an file and update all references"""
    try:
        old = Path(old)
        new = Path(new)
        print(f"Copy file {old} to {new}")
        new.write_text(old.read_text())
        print(f"Delete {old}")
        old.unlink()
        print("replace all links")
        all_articles = filter(
            lambda p: p.suffix in [".rst", ".md"], Path("./content").glob("**/*")
        )
        for f in all_articles:
            text = f.read_text()
            if old.name in text:
                f.write_text(text.replace(old.name, new.name))

    except Exception as e:
        print(f"Ups: {e}")


@task
def new(c, title=None, category=None, tags=None):
    """Create new article"""
    if title is None:
        title = click.prompt("Titel", type=str)
    if category is None:
        category = click.prompt("Kategorie", type=click.Choice(CATEGORIES))
    if tags is None:
        tags = click.prompt("Tags", type=str)
    tags = [tag.strip() for tag in tags.split(",")]
    root_folder = Path(__file__).resolve().parent
    template_file = root_folder / "new.md.j2"
    template = Template(source=template_file.read_text())
    slug = slugify(
        title,
        replacements=[
            ["??", "UE"],
            ["??", "ue"],
            ["??", "ae"],
            ["??", "AE"],
            ["??", "oe"],
            ["??", "OE"],
            ["??", "ss"],
        ],
    )
    now = datetime.now()
    t = template.render(title=title, category=category, today=now, tags=tags, slug=slug)
    out_file = root_folder / f"content/{category}/{now.strftime('%Y-%m-%d')}-{slug}.md"
    out_file.write_text(t)
    c.run(f"code {out_file}")
