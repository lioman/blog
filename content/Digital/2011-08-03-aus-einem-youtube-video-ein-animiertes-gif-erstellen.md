---
Title: Aus einem Youtube-Video ein animiertes GIF erstellen
Date: 2011-08-03 19:41
Author: Lioman
Category: Digital
Tags: Anleitung, Bilder, Gif, Google, Konsole, Linux
Slug: aus-einem-youtube-video-ein-animiertes-gif-erstellen
Status: published
---

Google+ kann netterweise animierte
[GIF](https://secure.wikimedia.org/wikipedia/de/wiki/Graphics_Interchange_Format#Animationen) darstellen.
Doch oft hat man nur ein Video zur Verfügung und muss daraus noch ein animiertes GIF erstellen.

Das geht unter Linux sehr gut mit klassischen Bordmitteln.

Benötigt wird erst einmal ein Video, welches nicht zu lange ist. Es
sollte eher nur eine kurze Sequenz sein, da das Bild sonst schnell zu
groß wird.

Zuerst habe ich folgendes Video heruntergeladen, dies geht mit einem der vielen
[Add-ons](https://addons.mozilla.org/en-US/firefox/search/?q=youtube+download&cat=1%2C0&x=0&y=0)
für den Firefox oder mit dem kleinen Python-Skript
[youtube-dl](http://rg3.github.com/youtube-dl/download.html)

{% youtube HLDG5sNMX2M %}

Das lange Video kann man mit dem Videoschnittprogramm (Ich habe
[avidemux](http://avidemux.org/) benutzt)seiner Wahl beschneiden,
dass nur noch die benötigte Sequenz übrigbleibt.

Nun exportiert man aus dem Video alle Einzelbilder als \*.png mit dem
Befehl `mplayer -vo png FILMDATEI`

Hat man ein großes Video kann man mit `for i in *.png; do convert -resize 400 $i $i; done`

alle Bilder auf eine handliche Größe einschrumpfen (hier 400px Breite)

Der Befehl `convert -verbose -delay 5 -loop 0 *.png AUSGABE.gif`

macht schließlich aus den vielen Einzelbildern im Ordner das GIF.
Wobei `-delay` die Zeit zwischen den Einzelbildern angibt.
Das Ergebnis sieht dann so aus:

![Ein Spaceshuttle bei der Landung]({static}/images/landing.gif)

und kann bei Google+ oder sonst wo hochgeladen werden.
