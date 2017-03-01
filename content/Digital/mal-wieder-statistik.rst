Mal wieder Statistik
####################
:date: 2009-11-04 12:53
:author: Lioman
:category: Digital
:tags: Open Source, CyStats, GA, Google, Google Analytics, Piwik, Statistik, tracking software, Wordpress
:slug: mal-wieder-statistik
:status: published

***Jeder möchte die Statistik seines Blogs im Auge behalten. Vor einiger
Zeit habe ich hier Statistik-Plugins getestet und mein Sieger war
`Cystats <http://www.cywhale.de/cystats-wordpress-statistik-plugin-075/>`__.
Besonders gelungen fand ich die Boterkennung und ich habe sie auch noch
um einige erweitert*** (Blogverzeichnisse und Suchmaschinen).

Wer möchte kann sich diese optimierte Version runterladen:
`cystats\_extended.tar.gz <images/cystats_extended.tar.gz>`__.

Doch wie alle anderen Statistikplugins geht der Betrieb eines solchen zu
Lasten der Performance und der Datenbank. Zur Zeit möchte ich aber genau
das optimieren. Ich möchte nicht, dass man ewig auf meine Artikel warten
muss wenn man sie aufruft.

Wenn man sich zu einer externen Lösung entscheidet gibt es das
Nonplusultra und viele andere. Das Nonplusultra ist bisher einfach
`GoogleAnalytics <http://www.google.com/intl/de_ALL/analytics/>`__ (GA).
Der Einsatz der Tracking-Software ist jedoch mehr als bedenklich, wie
das
`Datenschutzzentrum <https://www.datenschutzzentrum.de/material/tb/tb31/kap07.htm#72>`__
feststellte. Das Problem dabei eine Menge an Daten werden an Google
übertragen und man hat als Nutzer des keinen Einfluss mehr wie die Daten
verwendet werden.

In einem
`Artikel <http://www.gutestun.org/2008/10/17-google-analytics-alternativen/>`__\ bin
ich auf verschiedene Alternativen gestoßen doch der Großteil kommt
wieder nicht in Frage, da auch hier die Daten an externe Betreiber
gehen. Das Dilemma kann ich also nur Umgehen, wenn ich auch die
Statistiksoftware selbst hoste. Nur kann ich einen anderen Server und
vor allen Dingen eine andere Datenbank nutzen und mein Blog wird davon
nicht verlangsamt.

Nach langer Recherche kommt nun nur ein einziges Tool für mich in Frage:

` <http://piwik.org/>`__\ |piwik1|\ Piwik . Piwik ist noch in einem
frühem Betastadium und deswegen sind die Funktionen noch ziemlich
rudimentär. Doch die Applikation ist Open-Source, es gibt eine API, die
Pluginprogrammierung möglich macht und eine schnell arbeitende
Community. Die Entwickler habe sich das Ziel gesetzt, die führende
Open-Source Alternative zu GA zu werden. Es könnte klappen und deswegen
habe ich nun darauf umgestellt. Die Installation ist supersimpel (ca. 5
Minuten). Noch den Tracking-Code integrieren und fertig. das Tool
übernimmt den Rest. Und wie Piwik aussieht, kann man in einer
`Online-Demo <http://piwik.org/demo/>`__ sehen.

.. |piwik1| image:: {filename}/images/piwik1.jpg
   :class: alignright size-full wp-image-1060
   :width: 182px
   :height: 80px
   :target: {filename}/images/piwik1.jpg
