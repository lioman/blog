Wordpress for Android in Version 2.2.7
######################################
:date: 2013-01-29 10:42
:author: Lioman
:category: Open Source
:tags: android, update, Wordpress
:slug: wordpress-for-android-in-version-2-2-7
:status: published

Die Anwendung für Android ist ziemlich praktisch, wenn man ein Blog
verwalten möchte. Gerade wenn es mal eine aktuelle Diskussion gibt und
man viele Kommentare freischalten muss, aber nicht vor dem PC sitzen
kann. Heute kam ein Update auf die Version 2.2.7 und da ich kein
`Changelog <http://de.wikipedia.org/wiki/Changelog>`__ gefunden habe,
habe ich mal ein bisschen im
`Trac <http://android.trac.wordpress.org/query?status=closed&group=resolution&milestone=2.2.7>`__
gewühlt. Die neuste Version behebt zwei Fehler.

Version 2.2.6 hat nicht überprüft, ob das eingegebene Passwort immer
noch korrekt ist. Änderte man also das Passwort im Adminbereich hat sich
die Anwendung nicht verbunden, da sie davon ausging das richtige
Passwort zu haben. Das Problem hatte ich auch schon, wusste aber nicht
woran es lag und hatte damals einfach das Blog entfernt, dann die Daten
komplett neu eingegeben.

Fehler zwei war eine *java.lang.nullpointerexception* eine Variable
konnte also leer sein, die es nicht sein durfte.

 
