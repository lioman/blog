Plugin-Problem OpenID
#####################
:date: 2009-08-05 13:13
:author: Lioman
:category: Internet
:tags: Fail, OpenID, Plugin, Trackback, Wordpress
:slug: plugin-problem-openid
:status: published

***Tja es gibt immer wieder Wordpress-Plugins die Probleme verursachen,
auch wenn man es erstmal nicht sieht. Heute ist mir mal wieder eines
aufgefallen.***

Ich hatte schon länger den Verdacht, dass bei mir Track- bzw. Pingbacks
nicht funktionieren. Ich habe meine nicht auf anderen Blogs gefunden und
bei mir kamen keine an, obwohl ich wusste, dass sie gesetzt wurden. Nun
habe ich mir ein `Testtool <http://kalsey.com/tools/trackback/>`__ im
Netz gesucht und ein Trackback gesendet. Es hat nicht funktioniert. Um
die Plugins auszuschließen habe ich alle deaktiviert bevor ich an meinen
Webhost schreibe. Und nun ging es. Also einzeln wieder aktivieren , um
das Fehlerplugin zu identifizieren.
`OpenID <http://wordpress.org/extend/plugins/openid/>`__ ist der
Bösewicht. Ich habe auch alle Einstellungen deaktiviert, was nichts
geändert hat. So muss OpenID erstmal weichen. Die Trackbackfunktion ist
einfach wichtiger.
