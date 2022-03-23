Wordtube abgeschafft - Vodpod ist Ersatz
########################################
:date: 2010-01-13 14:47
:author: Lioman
:category: Digital
:tags: Blog, oembed, Plugin, Video, vodpod, wordtube
:slug: wordtube-abgeschafft-vodpod-ist-ersatz
:status: published

***Ich hatte auf diesem Blog bisher das Wortube-Plugin im Einsatz. Trotz
einiger Vorteile muss es nun weg.***

Wordtube hat den Vorteil, dass es einfach zu bedienen ist, einen
eigenständigen Player nutzt (Also alle Videos genau optisch gleich
eingebettet werden können). Und es unterstützt Playlisten und so kann
man bestimmte Kanäle generieren, Videosammlungen bestimmten Themen
zuordnen und einfach einblenden.

Warum sollte man ein solch praktisches Plugin einfach abschaffen?

Also zum Ersten: Lizenzgründe -  Der benutzte `JW
Player <http://www.longtailvideo.com/players/jw-flv-player/>`__ darf
nicht frei genutzt werden, wenn man GoogleAdsense einblendet. Das Blog
gilt damit automatisch als kommerziell (auch wenn die Einnahmen niemals
die Kosten des Blogs decken).

Und zum Zweiten: Weiterentwicklung und Abhängigkeit - Das Plugin wird in
letzter Zeit nicht mehr aktiv weiterentwickelt. So musste ich selbst
schon im PHP-Code herumbasteln, damit das Interface an den Adminbereich
ab Wordpress 2.7 angepasst ist (vgl
`hier </wordtube-playlist-verwaltung>`__). Baut man seine kompletten
Einbettungen auf ein Plugin aus, das nicht einen simplen Tag wie
"[videotag] VIDEOURL [/videortag]" nutzt, auf ist man abhängig von
dessen Funktionalität und Weiterentwicklung. (Einen einfachen Tag kann
man leicht durch ein paar SQL-Befehle ersetzen falls dies nötig wäre).

In Zukunft binde ich also alle Videos direkt ein. Das geht ohne
Probleme, da `Wordpress
2.9+ <http://blog.wordpress-deutschland.org/2009/10/15/noch-einfacher-videos-bilder-einbinden-mit-oembed-in-wordpress-2-9.html>`__
`oEmbed <http://www.oembed.com/>`__ unterstützt.

Um Playlisten einzufügen nutze ich den Dienst vodpod.com in Verbindung
mit dem Plugin von `Xondie <http://www.xondie.com/resources/>`__. Das
Ergebnis kann man oben unter dem Link *Liotube* bestaunen.

Vodpod hat noch ein paar andere Vorteile: Man kann von vielen Portalen
Videos einfach per Button zur eigenen Sammlung hinzufügen, kommentieren
und mit Tags versehen. Man kann mit VodSpot ein eigenes Videoportal
erstellen und man kann die gesammelten Videos an diverse Soziale
Netzwerke verteilen, bzw per Knopfdruck direkt an sein eigenes Blog
schicken.
