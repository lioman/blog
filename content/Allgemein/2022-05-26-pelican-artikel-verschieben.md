---
Title: Pelican: Artikel verschieben
Date: 2022-05-26 18:25
Modified: 2022-05-27 10:19
Category: Allgemein
Tags: pelican, python, blog, invoke
Slug: pelican-artikel-verschieben
Authors: Lioman
Status: Published
Summary: Dieses Blog wird nun seit einiger Zeit mit pelican gerendert. Initial hatte ich auf *.rst-Dateien gesetzt, inzwischen bin ich dazu übergegangen doch Markdown zu verwenden. Die meisten Dateien werden vermutlich nie konvertiert werden, doch hier und da halte ich es für sinnvoll die Datei umzubenennen. Um Artikel in pelican zu verschieben, habe ich einen einfachen Task erstellt...
---

Dieses Blog wird nun seit einiger Zeit mit [pelican](https://getpelican.com) gerendert.
Initial hatte ich auf `*.rst`-Dateien gesetzt,
inzwischen bin ich dazu übergegangen doch Markdown zu verwenden.
Die meisten Dateien werden vermutlich nie konvertiert werden,
doch hier und da halte ich es für sinnvoll die Datei umzubenennen.
Dazu kommt, dass ich nun in allen Dateinamen das Erscheinungsdatum am Anfang haben möchte.
Bringt man dann noch der IDE/der Shell/dem Filemanager das absteigende Sortieren bei,
hat man immer die aktuellsten Artikel ganz oben.
Das macht, das Auffinden schlicht einfacher.

Wie man das Datum extrahiert, werde ich eventuell in einem anderen Artikel beschreiben.
Hier soll es um die Lösung eines anderen Problems gehen.
Interne Links referenzieren bei pelican die Datei
und die ist nach dem Umbenennen einfach nicht mehr richtig.
Man, müsste also durch alle Artikel-Dateien gehen, den alten Dateinamen suchen und durch den Neuen ersetzen.
Das ist selbst bei einigen wenigen Dateien sehr aufwendig und lässt sich wunderbar automatisieren.
Da ich schon [invoke](https://www.pyinvoke.org/) als Taskrunner im Stack habe,
habe ich hierfür einen Task geschrieben:

    :::python
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

Nun kann ich mit `invoke movefile  /pfad/zum/Artikel.md /pfad/zum/Neuen-Artikel.md`
die Datei umbenennen
und in allen anderen Posts, wird der Link ersetzt.
Eine kleine Warnung: Ich habe den Task nur bei mir getestet und er funktioniert soweit.
Aber es ist doch eher eine schnelle Lösung
und man sollte sich das Ergebnis genau anschauen, bevor man es benutzt.
