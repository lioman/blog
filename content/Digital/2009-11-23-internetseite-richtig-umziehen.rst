Internetseite richtig umziehen
##############################
:date: 2009-11-23 15:38
:author: Lioman
:category: Digital
:tags: 301, Blog, Domain, php header, robot, SEO, tipp, Umziehen
:slug: internetseite-richtig-umziehen
:status: published

Vor einiger Zeit habe ich mit diesem Blog die Domain gewechselt. Ich
fand lioman.de einfach passender als blog.familie-kirchgaessner.de,
schon einfach weil die alte Domain einfach zu lange war. Doch leider
sind damit auch weniger Leser hier gelandet. Warum? - Ich bin falsch
umgezogen.

Ich habe hier wohl nicht viele regelmäßige Leser. Die Nutzer kommen
doch eher per Suchmaschine, Blogverzeichnis oder ähnliche
Internetdienste auf meine Seite. Ich bin also darauf angewiesen, dass
Suchmaschinen alle Themen ordentlich indexieren und dann publizieren.
Nun habe ich folgenden Fehler gemacht. Ich habe die neue Domain
aufgeschaltet und die alte einfach so gelassen. Das führt dazu, dass
alles bleibt wie bisher. Die Crawler durchforsten die alte Domain und
Backlinks werden dieser oder der neuen zugeordnet aber nicht als
zueinander zugehörig gesehen. Im Gegenteil es gibt nun plötzlich zwei
Seiten mit tupfengleichem Inhalt, Das erkennen die modernen
Suchalgorythmen und schmeißen den bösen Kopierer (neue Domain) raus bzw.
schieben die Ergebnisse im Ranking nach unten.

Die Lösung für dieses Problem ist eigentlich ganz einfach: Der
Error-Code 301.

Die Übersetzung für diesen Code ist: Moved Permanently. Es ist also
nicht nur eine einfache Umleitung, sondern gleich auch eine Übermittlung
der neuen Adresse. Der Vorteil dabei ist, dass ein Mensch die neue Seite
sieht und auch alle Artikel erreichen kann. Jeder Robot bekommt aber
alle Informationen, die ich ihm mitgeben möchte: "*Suche hier nicht mehr
sondern ersetze in deinem Index alle alten Einträge durch die neue
Adresse*"

Das ganze kann man unterschiedlich umsetzen. Eine Möglichkeit wäre per
*.htacces* einfacher jedoch geht es mit folgendem  PHP-Script:

.. code:: php

   <?php
    header("HTTP/1.1 301 Moved Permanently");
    header("Location: http://www.NEUEADRESSE.TLD");
    header("Connection: close");?>;


**WICHTIG**: Umleitung prüfen

Man muss sein kleines Script umbedingt mit einem Webtool wie
`web-sniffer.net <http://web-sniffer.net/>`__ prüfen. Ich hatte einen
Copy + Paste Fehler und so sieht es bei diversen Suchmaschinen so aus:

|blog_google_umleitungsfehler|\ Genau das wollte ich ja verhindern.
Eine Unerreichbarkeit meiner alten Adresse

.. |blog_google_umleitungsfehler| image:: {static}/images/blog_google_umleitungsfehler.png
   :class: aligncenter size-full wp-image-1128
   :width: 552px
   :height: 75px
   :target: {static}/images/blog_google_umleitungsfehler.png
