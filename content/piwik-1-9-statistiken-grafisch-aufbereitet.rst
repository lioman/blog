Piwik 1.9 - Statistiken grafisch aufbereitet
############################################
:date: 2012-10-23 09:48
:author: Lioman
:category: Internet, Open Source
:tags: Blog, Piwik, Statistik, Transitions, update
:slug: piwik-1-9-statistiken-grafisch-aufbereitet
:status: published

***Die Open-Source Webanalysesoftware `Piwik <http://piwik.org>`__ ist
in der neuen Version 1.9 erschienen und hat tolle neue Funktionen mit an
Bord.***

Da alle Statistikplugins für Wordpress die Datenbank aufblasen und
externe Dienste meist aus Datenschutzgründen nicht in Frage kommen,
setze ich schon seit einiger Zeit auf eine selbstgehostete Lösung.
Zuerst war es noch
`Pagelogger <http://www.lioman.de/2009/11/statistiktool-pagelogger/>`__,
aber seit Piwik auf dem Markt ist habe ich
`umgestellt <http://www.lioman.de/2010/11/blogstatistik-wieder-umgestellt/>`__
und es bisher nicht bereut. Piwik ist leistungsstark, anpassbar,
datenschutzkonform und featurereich, hinkte aber GoogleAnalytics
hinterher, da es bisher versucht hat Kernfunktionen des Platzhirsches
nachzubilden. Inzwischen haben die Entwickler wohl Zeit gefunden auch
wirklich Neues zu entwerfen. Neben kleinerer Verbesserungen und
Integrieren von Pluginfunktionen in den Core wartet 1.9 mit einer
Funktion auf, die wirklich nützlich ist.

Wenn man seine Statistiken anschaut, sind natürlich erstmal die
absoluten Kennzahlen (Wieviele kommen/ kamen wann auf welche Seite) und
deren Entwicklung wichtig. Das kann aber inzwischen jedes kleine
Statistikskript und eigentlich würden dazu sogar Serverlogs reichen. Oft
viel interessannter und wichtiger sind Antworten auf die Frage: Woher
kamen Besucher und wohin gehen sie? Für ein privates Blog ist das nur
spannend für komerzielle Seiten (vor allen Dingen Internetshops) ist
diese Analyse geradezu essentiell. Natürlich konnte Piwik solche Daten
auch schon in der Vergangenheit anzeigen und auch andere Tools zeigen
Referrer, Ein- und Ausstiegseiten oder gar die Verweildauer an. Sich
aber durch alle möglichen ´Tabellen und Tools zu klicken ist nicht nur
aufwändig, sondern auch unübersichtlich. Hier setzt nun
`Transitions <http://piwik.org/docs/transitions/>`__ an und bereitet die
schon vorhandenen Statistiken grafisch auf.

|image0|\ Transitions aktiviert man einfach unter "*Einstellungen >>
Plugins*". Bei mir hat es dann ein bisschen gedauert, bis ich mir die
ersten Grafiken anschauen konnte. Woran das lag weiß ich nicht. Auf
jeden Fall erscheint nun ein neuer Link hinter jedem Seitentitel (z.B
unter *Aktionen >> Seitentitel*), wenn man mit der Maus darüberfährt.

Die sich öffnende Grafik zeigt dann schön übersichtlich woher (mit
welchen Suchbegriffen) Seitenbesucher kommen und wohin sie danach gehen.
Mit diesen Daten kann man dann weiter arbeiten und seine Seite
optimieren, um die Verweildauer zu erhöhen. Oder man kann es einfach
interessant finden und sich an den schicken Grafiken erfreuen.

[caption id="attachment\_5100" align="aligncenter"
width="800"]\ |image1| Dieses Bild zeigt Transitions zum Artikel `Hallo
OSBN.de <http://www.lioman.de/2012/10/hallo-osbn-de/>`__ an. In Piwik
ist diese Grafik interaktiv.[/caption]

Das Update lohnt sich also dieses Mal wirklich, denn es gibt nicht nur
kleinere Bugfixes sondern mal ein echtes neues Feature. Allen Bloggern,
die Piwik nutzen wollen empfehle ich übrigens das Plugin
`WP-Piwik <http://wordpress.org/extend/plugins/wp-piwik/>`__

 

.. |image0| image:: http://www.lioman.de/wp-content/uploads/transitions_icon.png
   :class: alignleft size-full wp-image-5099
   :width: 91px
   :height: 50px
   :target: http://www.lioman.de/wp-content/uploads/transitions_icon.png
.. |image1| image:: http://www.lioman.de/wp-content/uploads/transitions.png
   :class: size-full wp-image-5100
   :width: 800px
   :height: 519px
   :target: http://www.lioman.de/wp-content/uploads/transitions.png
