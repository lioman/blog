Amazon Prime Instant Video unter Ubuntu ohne Pipelight
######################################################
:date: 2014-11-02 15:28
:author: Lioman
:category: Digital
:tags: Open Source, amazon, Flash, pipelight, streamen, Video, UbuntuusersPlanet
:slug: amazon-prime-instant-video-unter-ubuntu-ohne-pipelight
:status: published

Ich habe immer noch einen Prime-Account und ab und zu ist es doch ganz
nett bei Amazon auch Videos zu streamen. Leider ist die Umsetzung noch
nicht so optimal, wie ich es von so einem mächtigen Konzern erwarten
würde. Gerade was Komfort, Stabilität (ruckelte schon zu Unzeiten bei
bester eigener Internetverbindung, so dass ich doch lieber ausgeschaltet
hatte) und aber auch die Auswahl anging kann der Dienst noch deutlich
verbessert werden.

Wieso kann ich zum Beispiel nicht jede Serie einfach auf Englisch
umschalten, sondern muss mir die Serie in der Sprache extra raussuchen?

Dazu kam immer das wechseln auf Windows, denn Silverlight gibt es ja
offiziell nicht für Linux. Die Lösungen mit
`Pipelight <http://pipelight.net/cms/>`__ hatten bei mir nie
zufriedenstellende Ergebnisse gebracht.

.. figure:: {static}/images/amazon_video_einstellungen-1024x207.png
   :alt: Amazon-Einstellungen
   :class: size-large wp-image-5637
   :width: 620px
   :height: 125px
   :target: {static}/images/amazon_video_einstellungen.png

   Amazon Videoplayer-Einstellungen

Nun hat Amazon einen Schritt in die (falsche) richtige Richtung
vollzogen. Nun kann man in den eigenen Einstellungen einen Flashplayer
aktivieren. Längere Tests habe ich noch nicht durchgeführt, aber das
Abspielen geht im Firefox, wenn man den `User
Agent <http://de.wikipedia.org/wiki/User_Agent>`__ zusätzlich auf den
eines unter Windows laufenden Browsers stellt.

Schöner wäre natürlich etwas moderneres als Flash gewesen. Es gibt ja
durchaus Dienste, `die auf HTML5
setzen <http://linuxundich.de/gnu-linux/netflix-startet-deutschland-dank-html5-player-tut-der-dienst-unter-linux-ohne-silverlight/>`__,
aber vielleicht kommt das noch

**Update:** Scheint so als wäre die Flashoption wieder
`zurück. <http://www.raspitux.de/amazon-prime-instant-video-wieder-mit-flash-unterstuetzung/>`__
Dafür funktioniert sie nicht mehr unter Linux. Im Firefox soll die
Version zu alt sein und in Chrome läd der Player aber kein Videostream.
