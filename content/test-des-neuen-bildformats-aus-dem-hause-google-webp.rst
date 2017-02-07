Test des neuen Bildformats aus dem Hause Google: WebP
#####################################################
:date: 2010-10-06 22:10
:author: Lioman
:category: Internet, PC und Technik
:tags: Bild, Codec, Google, JPEG, Komprimierung, PNG, VP8, WebM, WebP
:slug: test-des-neuen-bildformats-aus-dem-hause-google-webp
:status: published

***Google hat ein neues Bildformat angekündigt:***
`WebP <https://developers.google.com/speed/webp/>`__\ ***. Die Idee ist
einfach und konsequent. Man nutzt den freien VP8-Videocodec für ein
Einzelbild und packt das ganze in einen***
`***RIFF*** <http://de.wikipedia.org/wiki/Resource%20Interchange%20File%20Format>`__\ ***-Container.
Es soll ein möglichst kleines Bild bei möglichst guter Qualität
herauskommen. Hier nun ein kleiner Test des neuen Formats.***

Direkt zum `Testergebnis <#Ergebnis>`__

Installation
------------

Es gibt vorkompilierte Dateien auf der
`Downloadseite <http://code.google.com/p/webp/downloads/list>`__. Bei
mir hat es mit der Datei leider nicht geklappt, da bleibt nur
selbstkompilieren.

Voraussetzungen:
~~~~~~~~~~~~~~~~

Zuerst wird libvpx benötigt.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. `Runterladen <http://code.google.com/p/webm/downloads/list>`__
   (libvpx-vX.X.X.tar.bz2)
#. Entpacken
#. mit

   ::

        ./configure && make

   .. raw:: html

      <p>

   installieren (Dies geht nur, wenn man
   `Yasm <http://www.tortall.net/projects/yasm/wiki/Download>`__
   installiert hat)

libjpeg + libpng
^^^^^^^^^^^^^^^^

unter Ubuntu oder ähnlichen Distributionen genügt der Befehl:

::

    sudo apt-get install libjpeg62-dev libpng12-dev

Kompilieren:
~~~~~~~~~~~~

#. `Runterladen <http://code.google.com/p/webp/downloads/list>`__
   (webp-leptonica-X.X.X.tar.gz)
#. Entpacken
#. In Ordner webp/leptonlib-X.0XX/src/ wechseln
#. Und wieder

   ::

        ./configure && make

   .. raw:: html

      <p>

#. Danach in webp/libwebp wechseln und hier reicht der Befehl make aus,
   um das Programm zu kompilieren. Man findet nun das Programm webpconv
   im Ordner.

Benutzung
---------

Für den Test habe ich ein qualitativ möglichst gutes Bild gewählt. Dazu
habe ich ein
`RAW-Foto <http://www.lioman.de/wp-content/uploads/rose_orginal.tar.gz>`__
kompressionsfrei in eine
`PNG </wp-content/uploads/rose_orginal.png>`__-Datei überführt. Nun
kommt das frischkompilierte Programm zum Einsatz. Ich komprimiere das
Bild einmal als webp mit dem Befehl:

::

    ./webpconv -quality 80 /home/elias/Desktop/rose.png

und einmal als jpeg mit dem Kommando:

::

    ./webpconv -quality 80 -format jpeg /home/elias/Desktop/rose.png

. Dabei habe ich beides Mal eine Qualität von 80 gewählt.

` <>`__\ Ergebnis
-----------------

Das Ergebnis lässt sich sehen. Die Größe schrumpft ganz schön. Doch ist
das nur interessant, wenn auch die Qualität des Bildes zufriedenstellend
ist. Da es noch keine Programme gibt, die das neue Format anzeigen
können wird das WebP-Bild wieder in ein PNG überführt.

::

    ./webpconv -format PNG /home/elias/Desktop/rose.webp

Und hier ist das Ergebnis in 4-facher Vergrößerung:

|image0|\ |image1|

WebP ist deutlich kleiner (in meinem Beispiel Faktor 1,86 gegenüber
JPEG) und hat weniger Artefakte Und erscheint damit schärfer. Zwar sieht
man den Verlust in dieser Vergrößerung gegenüber dem Original deutlich,
doch ist das bei der Kompressionsrate durchaus akzeptabel. Sicher ist
noch mehr aus dem Codec rauszuholen, doch sind die jetzigen Ergebnise
schon sehr gut. Es könnte eine echte Alternative zu dem Webstandard JPEG
sein., da die Dateien nochmals deutlich schrumpfen und sich somit
schneller zwischen Server und Browser übertragen lassen. Jetzt muss das
Format noch in möglichst viele Browser integriert werden.

Google Chrome macht da vermutlich den Anfang.

.. |image0| image:: http://www.lioman.de/wp-content/uploads/webp_vergleich.png
   :class: aligncenter size-full wp-image-2127
   :target: http://www.lioman.de/wp-content/uploads/webp_vergleich.png
.. |image1| image:: /wp-content/uploads/webp_vergleich.png
   :class: alignnone
   :width: 950px
   :height: 391px
   :target: http://www.lioman.de/wp-content/uploads/webp_vergleich.png
