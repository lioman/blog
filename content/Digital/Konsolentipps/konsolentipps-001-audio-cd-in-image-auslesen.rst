Konsolentipps #001: Audio-Cd in Image auslesen
##############################################
:date: 2010-10-25 14:14
:author: Lioman
:category: Digital
:tags: Konsolentipps, Audio-Cd, auslesen, brennen, CD, Image, Konsolentipps, Linux, rippen
:slug: konsolentipps-001-audio-cd-in-image-auslesen
:status: published

|image0|\ Möchte man eine komplette CD in eine Datei schreiben bietet
sich normalerweise ein Iso-Image an. Handelt es sich jedoch um eine
Audio-CD ist das nicht möglich. Für Audio-CDs ist das Format .bin/cue
bzw. bin/toc vorgesehen, wobei die eigentlichen Daten jeweils in der bin
liegen und die Trackinformationen (wie die CD eingeteilt ist) in der
\*.cue oder \*.toc Datei.

Das Auslesen
------------

Man liest die CD mit dem Program cdrdao aus. Das geht in der Konsole
einfach mit diesem Befehl (wobei der Pfad zum Laufwerk angepasst werden
muss).

::

     cdrdao read-cd --device ATAPI:/dev/sr0 --datafile CD.bin CD.cue

Das Brennen
-----------

Brennen ist ebenso einfach. Hier genügt folgender Befehl:

::

    cdrdao write --device /dev/sr0 --speed 8 --driver generic-mmc CD.cue

.. |image0| image:: {filename}/images/Konsole-300x213.png
   :class: alignleft size-medium wp-image-2201
   :width: 210px
   :height: 149px
   :target: {filename}/images/Konsole.png
