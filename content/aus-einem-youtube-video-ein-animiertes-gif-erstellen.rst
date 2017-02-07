Aus einem Youtube-Video ein animiertes GIF erstellen
####################################################
:date: 2011-08-03 19:41
:author: Lioman
:category: Allgemein, Internet, PC und Technik
:tags: Anleitung, Bilder, Gif, Google, Konsole, Linux
:slug: aus-einem-youtube-video-ein-animiertes-gif-erstellen
:status: published

Google+ kann netterweise animierte
`Gif <https://secure.wikimedia.org/wikipedia/de/wiki/Graphics_Interchange_Format#Animationen>`__
darstellen. Doch oft hat man nur ein Video zur Verfügung und muss daraus
noch ein animiertes Gif erstellen.

Das geht unter Linux sehr gut mit klassischen Bordmitteln.

Benötigt wird erst einmal ein Video, welches nicht zu lange ist. Es
sollte eher nur eine kurze Sequenz sein, da das Bild sonst schnell zu
groß wird.

Zuerst habe ich folgendes Video runtergeladen, dies geht mit einem der
vielen
`Add-ons <https://addons.mozilla.org/en-US/firefox/search/?q=youtube+download&cat=1%2C0&x=0&y=0>`__
für den Firefox oder mit dem kleinen Python-Skript
`youtube-dl <http://rg3.github.com/youtube-dl/download.html>`__

http://www.youtube.com/watch?v=HLDG5sNMX2M

Das lange Video kann man mit dem Videoschnittprogramm ( Ich habe
`avidemux <http://avidemux.org/>`__ benutzt)seiner Wahl beschneiden,
dass nur noch die benötigte Sequenz übrigbleibt.

Nun exportiert man aus dem Video alle Einzelbilder als \*.png mit dem
Befehl

::

    mplayer -vo png FILMDATEI

Hat man ein großes Video kann man mit

::

    for i in *.png; do convert -resize 400 $i $i; done

alle Bilder auf eine handliche Größe einschrumpfen ( hier 400px Breite)

Der Befehl

::

    convert -verbose -delay 5 -loop 0 *.png AUSGABE.gif

macht schließlich aus den vielen Einzelbildern im Ordner das GIF. wobei
-delay die Zeit zwischen den Einzelbildern angibt. Das Ergebnis sieht
dann so aus:

|image0| und kann bei Google+ oder sonstwo hochgeladen werden.

.. |image0| image:: http://www.lioman.de/wp-content/uploads/landing.gif
   :class: aligncenter size-full wp-image-3532
   :width: 300px
   :height: 132px
   :target: http://www.lioman.de/2011/08/aus-einem-youtube-video-ein-animiertes-gif-erstellen/landing/
