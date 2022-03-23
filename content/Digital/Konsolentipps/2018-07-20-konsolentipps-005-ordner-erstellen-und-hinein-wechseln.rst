Konsolentipps #005: Ordner erstellen und hinein wechseln
########################################################
:date: 2018-07-20 18:50
:author: Lioman
:category: Digital
:tags: Konsole, Konsolentipps, Linux, Bash, Open Source
:slug: konsolentipps-005-ordner-erstellen-und-hinein-wechseln
:status: published
:series: Konsolentipps

Wenn ich auf der Konsole einen Ordner erstelle,
tue ich das meistens um entweder etwas hineinzukopieren 
oder um dort zu arbeiten und neue Dateien zu erstellen.

Im ersten Fall ist es egal, wo ich mich befinde.
Im Zweiten werde ich oft direkt in den gerade kreierten Arbeitsplatz wechseln.

Ich benötige, also oft den Zweischritt: 

#. ``mkdir example_folder``
#. ``cd example_folder``

Das ist natürlich nicht ganz zufriedenstellend.
Aus diesem Grund habe ich mir die Funktion ``mkcd`` erstellt
(In ``.bash_profile`` oder ``.bashrc`` eintragen).

.. code-block:: bash

   mkcd () {
     mkdir -p "$*"
     cd "$*"
   }

Diese sehr einfache Version funktioniert gut 
und ich hatte bisher noch keine Probleme damit.
Es gibt allerdings noch komplexere Beispiele, 
die allerlei Extras hinzufüge um etwaige Fehler abzufangen. 
Leider habe ich den Eintrag in meiner Browserhistorie nicht mehr gefunden.
Wer die etwas sichere Variante benötigt, 
sollte auf `Stackoverflow <https://stackoverflow.com>`_ suchen.
