pageLogger Boterkennung verbessern
##################################
:date: 2009-11-24 14:04
:author: Lioman
:category: Internet
:tags: Bots, Crawler, Download, PageLogger, Regex, robots, Statistik
:slug: pagelogger-boterkennung-verbessern
:status: published

**Ich habe schon über die Statistiksoftware pageLogger berichtet und bin
auch bisher damit zufrieden. Allerdings stellte ich fest, dass die
Bot-Erkennungsliste etwas mager ist.**

Im Verzeichnis PAGELOGGER/includes/robots liegt die Datei robots.txt.
Sie ist gefüllt mit RegEx - also kleinen Textschnipseln die in einem
`User Agent <http://de.wikipedia.org/wiki/User%20Agent>`__ auftauchen
können - und einer Erklärung die dann im Frontend auftaucht.

Bsp:

::

    gaisbot/#Gaisbot
     geckobot#GeckoBot
     gencrawler#GenDoor
     gigabaz/#GigaBaz
     gigabot#GigaBot
     googlebot#Googlebot
     griffon#navi.ocn.ne.jp

Doch 271 Bots sind etwas wenig sind doch mehrere Tausende inzwischen
bekannt. Es sind zwar nicht alle wichtig und einige kommen sicher sehr
selten auf einem kleinen Blog vorbei. trotzdem ist es sinnvoll die Liste
ein wenig zu erweitern.

Ich habe mir verschiedene Listen im Netz angeschaut und sie dann mit ein
paar Konsolenbefehlen zusammengefügt. Dann noch eine kleine Reinigung
der Liste von Hand und nun werden ganze 871
`Spider <http://de.wikipedia.org/wiki/Webcrawler>`__ unterstützt.

Wer sie möchte kann sie ``hier`` herunterladen und in sein
pageLoggerinstallation einfügen.

PS: Bei mir ging dies nicht über pageLogger direkt. Ich habe die Datei
per `FTP <http://de.wikipedia.org/wiki/File%20Transfer%20Protocol>`__
hochgeladen.
