Konsolentipps #002 Alle Dateien eines Typs bearbeiten
#####################################################
:date: 2010-11-18 18:01
:author: Lioman
:category: Allgemein, Konsolentipps
:tags: Konsolentipps, Linux, Schleife, terminal
:slug: konsolentipps-002-alle-dateien-eines-typs-bearbeiten
:status: published

|image0|\ Es kommt immer mal wieder vor, dass man alle Dateien eines
Typs in einem Ordner bearbeiten muss.

Das geht mit folgender Schleife

::

    for i in *.dateiendung; do IrgendeinBefehl $i;done

Möchte man zum Beispiel alle FLAC in Ogg konvertieren geht das so:

::

    for i in *.flac; do oggconvert $i;done

.. |image0| image:: http://www.lioman.de/wp-content/uploads/Konsole-300x213.png
   :class: size-medium wp-image-2201 alignleft
   :width: 300px
   :height: 213px
   :target: http://www.lioman.de/wp-content/uploads/Konsole.png
