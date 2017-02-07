MySQL: Einträge mit regulären Ausdrücken löschen
################################################
:date: 2015-01-04 18:36
:author: Lioman
:category: Allgemein, Open Source
:tags: datenbank, mysql, Regex, sql
:slug: mysql-eintrage-mit-regularen-ausdrucken-loschen
:status: published

Arbeitet man mit Datenbanken, speziell im Entwicklungsstadium einer
Anwendung, kann allerlei Müll anfallen, den man tunlichst loswerden möchte.
Geht es um einzelne Einträge, kann man das gut mit Befehlen wie:

.. code:: sql

    DELETE * FROM tabellenname WHERE id=xy

wenn man nur wenige oder gar einen einzelnen Eintrag loswerden möchte.
Und

.. code:: mysql

    DELETE * FROM tabellenname WHERE spaltenname=""

würde alle leeren Testeinträge verwerfen.

Hat man jedoch viele Reihen, die unerwünscht sind, kann es schnell eine
abendfüllende Aufgabe werden alles Unbenötigte loszuwerden. Und leider
sind nicht immer alle Testeinträge an der richtigen Stelle leer. Schon
ein Zeilenumbruch ("*\\n*") in einem Textfeld reicht das zweite
Statement zu vereiteln.

Besser geeignet sind für solche Vorhaben sind `Reguläre
Ausdrücke <https://de.wikipedia.org/wiki/Regul%C3%A4rer_Ausdruck>`__, so
muss man nicht von Hand zusammensuchen oder löschen. Dazu muss man
einfach in die *WHERE*-Klausel in folgender Weise modifizieren:

.. code:: mysql

    DELETE FROM tabellenname WHERE spaltenname Regexp '^[ ]*[\n]+[ ]*$';

In diesem Fall werden alle Zeilen gelöscht, die nur aus leeren Zeichen
und ein oder mehreren Zeilenumbrüchen bestehen. Das funktioniert
natürlich analog auch mit *SELECT. *
