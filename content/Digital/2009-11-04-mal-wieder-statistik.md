---
Title: Mal wieder Statistik
Date: 2009-11-04 12:53
Author: lioman
Category: digital
Tags: open source, cystats, ga, google, google analytics, piwik, statistik, tracking software, wordpress
Slug: mal-wieder-statistik
Status: published
---

Jeder möchte die Statistik seines Blogs im Auge behalten. Vor einiger
Zeit habe ich hier Statistik-Plugins getestet und mein Sieger war
~~[Cystats]()~~.
Besonders gelungen fand ich die Boterkennung und ich habe sie auch noch
um einige erweitert (Blogverzeichnisse und Suchmaschinen).

Wer möchte kann sich diese optimierte Version herunterladen:
[cystats_extended.tar.gz]({attach}/downloads/cystats_extended.tar.gz).

Doch wie alle anderen Statistik-Plugins geht der Betrieb eines solchen zu
Lasten der Performance und der Datenbank. Zur Zeit möchte ich aber genau
das optimieren. Ich möchte nicht, dass man ewig auf meine Artikel warten
muss wenn man sie aufruft.

Wenn man sich zu einer externen Lösung entscheidet, gibt es das
Nonplusultra und viele andere. Das Nonplusultra ist bisher einfach
[GoogleAnalytics](http://www.google.com/intl/de_ALL/analytics/) (GA).
Der Einsatz der Tracking-Software ist jedoch mehr als bedenklich, wie
das
[Datenschutzzentrum](https://web.archive.org/web/20150113174126/https://www.datenschutzzentrum.de/material/tb/tb31/kap07.htm#72)
feststellte. Das Problem dabei eine Menge an Daten werden an Google
übertragen und man hat als Nutzer des keinen Einfluss mehr wie die Daten
verwendet werden.

In einem
~~[Artikel]()~~ bin
ich auf verschiedene Alternativen gestoßen doch der Großteil kommt
wieder nicht in Frage, da auch hier die Daten an externe Betreiber
gehen. Das Dilemma kann ich also nur Umgehen, wenn ich auch die
Statistiksoftware selbst hoste. Nur kann ich einen anderen Server und
vor allen Dingen eine andere Datenbank nutzen und mein Blog wird davon
nicht verlangsamt.

Nach langer Recherche kommt nun nur ein einziges Tool für mich in Frage:

![Piwik]({static}/images/piwik1.jpg){class="alignleft"}
Piwik ist noch in einem frühem Betastadium und deswegen sind die Funktionen noch ziemlich
rudimentär. Doch die Applikation ist Open-Source, es gibt eine API, die
Pluginprogrammierung möglich macht und eine schnell arbeitende
Community. Die Entwickler habe sich das Ziel gesetzt, die führende
Open-Source Alternative zu GA zu werden. Es könnte klappen und deswegen
habe ich nun darauf umgestellt. Die Installation ist supersimpel (ca. 5
Minuten). Noch den Tracking-Code integrieren und fertig. Das Tool
übernimmt den Rest. Und wie Piwik aussieht, kann man in einer
[Online-Demo](http://piwik.org/demo/) sehen.
