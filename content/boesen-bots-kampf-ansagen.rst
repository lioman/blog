Bösen Bots den Kampf ansagen!
#############################
:date: 2009-04-28 13:24
:author: Lioman
:category: Internet
:tags: Bot, Crawler, robots.txt, Spam, Spider
:slug: boesen-bots-kampf-ansagen
:status: published

Beim Test der Statistik-Plugins ist mir aufgefallen, dass sich doch
einiges an Bots, Robots und Spidern auf diesem Blog rumtreibt. Da man
nicht bei allen weiß, wer sich dahinter verbirgt und was sie mit den
gewonnenen Daten so treiben, habe ich mich entschlossen "böse Bots"
auszusperren. Doch was ist ein böser Bot?

Sie haben alle eigentlich eines gemeinsam: sie achten nicht die
`robots.txt <http://de.wikipedia.org/wiki/Robots%20Exclusion%20Standard>`__
und probieren eventuell sich noch zu verschleiern.

In der robots.txt kann man gezielt Seiten vom Spidern ausschließen, weil
man da zum Beispiel Kontaktdaten hat, die nicht durch jede Suchmaschine
gefunden werden soll. Ein "böser" Bot sucht aber oft genau nach solchen
Seiten und achtet deshalb nicht auf die robots.txt.

Wenn aber ein Bot nicht darauf hört, brauch man ihn gar nicht erst
verbieten. Man muss radikaler vorgehen und den entsprechenden durch die
`.htaccess <http://de.wikipedia.org/wiki/Htaccess>`__ aussperren. Genau
da setzt `Spider-Trap <http://www.spider-trap.de/>`__ an. Man fügt ein
kleines Bild mit Link auf seiner Startseite ein und verbietet deren
crawling durch die robots.txt.

Die Arbeit übernimmt ein PHP-Skript dass man auf seinen Webspace
installieren muss. Man bekommt es
`hier <http://www.spider-trap.de/download.html>`__ und auf `dieser
Seite <http://www.spider-trap.de/Installation-2.html>`__ ist die
Installation hinreichend erklärt.

Die Falle ist gestellt und wenn nun ein Crawler diesen Link
verbotenerweise aufruft, wandert sein User-Agent und seine
`IP <http://de.wikipedia.org/wiki/Internet%20Protocol>`__ schnurstracks
in die Blacklist und die .htaccess. In Zukunft  bekommt der
entsprechende Spider nur noch eine Fehlerseite zu sehen. Damit sich aber
niemand versehentlich aussperrt, kann man sich auf dieser selbst wieder
freischalten. Einem Bot ist das nicht möglich, da er über den
`CAPTCHA <http://de.wikipedia.org/wiki/Captcha>`__-Code stolpern würde.

Hoffen wir das es hilft.

Ein weiteres Projekt mit ähnlichen Zielen ist
`Bot-Trap <http://www.bot-trap.de>`__ welches auch vom inzwischen
eingestellten Dissalow vorgeschlagen wurde. Allerdings muss man sich
aufwendig anmelden. :-(

| Und hier nochmal der Link, um das Projekt zu unterstützen:
| :arrow: |image0|
| 

.. |image0| image:: http://www.spider-trap.de/images/no-badbot.gif
   :target: http://www.spider-trap.de
