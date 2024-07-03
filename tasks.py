# -*- coding: utf-8 -*-

from datetime import datetime
from pathlib import Path
import random
import re
import webbrowser
from bs4 import BeautifulSoup
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
    deploy_path = Path(CONFIG["deploy_path"])
    if deploy_path.is_dir():
        shutil.rmtree(CONFIG["deploy_path"])
        deploy_path.mkdir()


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

    sys.stderr.write("Serving on http://localhost:{port} ...\n".format(**CONFIG))
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
    c.run("pelican -s publishconf.py", pty=True)


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    build(c)
    server = Server()
    watch_paths = [CONFIG["settings_base"]]

    # Watch content source files
    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_files = f"{SETTINGS['PATH']}/**/*{extension}"
        watch_paths.append(content_files)
    # Watch the theme's templates and static assets
    theme_path = SETTINGS["THEME"]
    watch_paths.append(f"{theme_path}/templates/*.html")
    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        theme_static_file = f"{theme_path}/static/**/*{extension}"
        custom_static_files = f"{SETTINGS['PATH']}/static/*{extension}"
        watch_paths.append(theme_static_file)
        watch_paths.append(custom_static_files)
    for path in watch_paths:
        server.watch(path, lambda: build(c))
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
def convert2md(c, file: str):
    rst_file = Path(file)
    md_file = rst_file.with_suffix(".md")
    if not rst_file.exists():
        print(f"File: {file} does not exist")
        sys.exit(1)
    movefile(c, rst_file, md_file)

    text = ""
    with md_file.open() as f:
        headers_parsed = False
        print("Migrate Frontmatter")
        for idx, line in enumerate(f.readlines()):
            if not headers_parsed:
                if idx == 0:
                    line = f"---\nTitle: {line}"
                if re.match("^#+$", line):
                    print("delete line")
                    continue
                if line.startswith(":"):
                    print("Replace Meta")
                    line = line[1:].capitalize()
                if line == "\n":
                    print("header finished")
                    line = f"---\n\n"
                    headers_parsed = True
            line = re.sub(r"`(.*?) <(.*?)>`__", r"[\1](\2)", line)
            line = re.sub(r"\.\. youtube:: (.*?)\n", r"{% youtube \1 %}\n", line)
            if not re.match("   :(.+): (.+)\n", line):
                text = f"{text}{line}"
    md_file.write_text(text)
    c.run(f"code '{md_file}'")


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
            ["Ü", "UE"],
            ["ü", "ue"],
            ["ä", "ae"],
            ["Ä", "AE"],
            ["ö", "oe"],
            ["Ö", "OE"],
            ["ß", "ss"],
        ],
    )
    now = datetime.now()
    t = template.render(title=title, category=category, today=now, tags=tags, slug=slug)
    out_file = root_folder / f"content/{category}/{now.strftime('%Y-%m-%d')}-{slug}.md"
    out_file.write_text(t)
    c.run(f"code {out_file}")


@task
def openrandom(c):
    sitemap = Path(CONFIG["deploy_path"]) / "sitemap.xml"
    with open(sitemap) as f:
        xml = BeautifulSoup(f.read(), "lxml-xml")
        pages = [
            url.loc.string
            for url in xml.find_all("url")
            if re.match("^/\d\d\d\d/\d\d/.*/$", url.loc.string)
        ]
        webbrowser.open(
            f"http://{CONFIG['host']}:{CONFIG['port']}{pages[random.randint(0, len(pages))]}"
        )
