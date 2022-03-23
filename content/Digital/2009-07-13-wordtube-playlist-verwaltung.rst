Wordtube Playlist-Verwaltung:Problem und Lösung
###############################################
:date: 2009-07-13 10:06
:author: Lioman
:category: Digital
:tags: 2.8, 2.8.1, Blog, Plugin, Wordpress, wordtube
:slug: wordtube-playlist-verwaltung
:status: published

***Das Plugin Wordtube macht seit dem Update auf WP 2.8 Probleme***.
***Man kann im Verwaltungsdialog keine Playlisten zuordnen. Hier ist die
Lösung.***

`go to English-Howto <#English>`__

Um Videos hier sinnvoll einzubinden nutze ich das Plugin
`Wordtube <http://wordpress.org/extend/plugins/wordtube/>`__\ von `Alex
Rabe <http://alexrabe.boelinger.com/wordpress-plugins/wordtube/>`__.
Seit dem Wordpress-Update auf die Version 2.8 treten jedoch Probleme
auf. Im Video-Verwaltungs-Dialog war in einer Art Sidebar der Dialog um
das Video einer bestimmten Playlist zuzuordnen. Dieser Dialog fehlte nun
und das Update auf 2.8.1 hatte keine Änderung gebracht. Komischerweise
steht die Dialogbox im Quelltext, wenn man sich diesen Anzeigen lässt.
:(

Da ich nicht auf das Update warten wollte (Ohne Playlist ist es nicht
Nutzbar) habe ich den Plugincode verändert und die Auswahl aus der
Sidbar gehohlt und unten direkt angefügt. Hier ist die verbesserte
``manage.php`` (verpackt) zum Download. Einfach in
/BLOGVERZEICHNIS/wp-content/plugins/wordtube/admin kopieren, dann sollte
alles wieder gehen.

| ---------------------------------------
| ` <>`__\ Description in english: if you have problems with the
  playlistdialog in wordtube (invisible) copy the ``manage.php``
  (packed) in /wp-directory/wp-content/plugins/wordtube/admin over the
  existing version. This will fix the problem and the settings is now
  under the managing section.
