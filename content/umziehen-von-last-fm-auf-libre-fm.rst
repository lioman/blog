Umziehen von Last.fm auf Libre.fm
#################################
:date: 2010-09-22 16:59
:author: Lioman
:category: Internet, Medien, Open Source
:tags: daten, Datenschutz, lastfm, Libre.fm, Linux, migrieren, Musik, Scrobbeln, Umziehen
:slug: umziehen-von-last-fm-auf-libre-fm
:status: published

Früher habe ich den Dienst Last.fm gerne und viel genutzt. Man hat seine
Hörgewohnheiten hochgeladen, um im Gegenzug Vorschläge und Empfehlungen
zu bekommen. Das ging einfach wie bei einem Webradio und konnte ebenso
legal mitgeschnitten werden. Doch inzwischen hat last.fm einiges an der
API verändert und es ist so weniger attraktiv. Zudem kommen noch
Datenschutzprobleme. Ich habe nicht volle Kontrolle über die Daten bei
Last.fm und kann auch nicht deren Verkauf an dritte verhindern. Möchte
man aber trotzdem ein eigenes Musikprofil erstellen und wie auch immer
nutzen bietet sich der Dienst Libre.fm an.

Wenn man schon umzieht ist es natürlich schön alles mitzunehmen, damit
man nicht bei null beginnen muss. Die Daten bei Last.fm sind nicht gegen
maschinelles auslesen geschützt und das machen wir uns jetzt zu nutze.

Dank
`OMGUbuntu <http://www.omgubuntu.co.uk/2010/09/easily-export-you-last-fm-scrobbles-to-libre-fm/>`__
gibt es eine einfache Anleitung, die ich hier kurz ins Deutsche
übertragen will.

#. Programm
   runterladen:\ `lastscrape-gui <https://github.com/encukou/lastscrape-gui/tarball/master>`__\ (Es
   nutzt Python und PyQt4 unter Ubuntu einfach mit

   ::

       sudo apt-get install python-pyqt4

   .. raw:: html

      <p>

   nachinstallieren.

#. Entpacken
#. und dann *gui.py* ausführen
#. Nun muss man den Nutzernamen eingeben und mit *"Grab the scrobbled"*
   die Musikstücke holen.
   |image0|
   Das kann, je nach Menge, eine ganze Weile dauern.
#. Im neuen Fenster klickt man nach dem Holen auf Save und wechselt zum
   Reiter "Push"
   |image1|
   Daten eingeben und mit einem Klick auf "Go" Startet der Prozess!

Update: Links geändert. Es wird immer die aktuellste angezeigt

.. |image0| image:: {filename}/images/LastScrape_Bildschirm1.png
   :class: aligncenter size-full wp-image-1981
   :width: 521px
   :height: 414px
.. |image1| image:: {filename}/images/LastScrape_Bildschirm2.png
   :class: aligncenter size-full wp-image-1982
   :width: 500px
   :height: 400px
   :target: http://www.lioman.de/2010/09/umziehen-von-last-fm-auf-libre-fm/lastscrape_bildschirm2/
