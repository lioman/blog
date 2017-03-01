OpenID-Ersatz
#############
:date: 2009-10-01 14:32
:author: Lioman
:category: Digital
:tags: Blog, Facebook, OpenID, Plugin, twitter
:slug: openid-ersatz
:status: published

***Das OpenID-Plugin hat große Probleme gemacht und deswegen habe ich es
ausgeschaltet (siehe `hier </plugin-problem-openid>`__). Nun gibt es
Ersatz***.

Man muss im Netz einfach viel zu viele Formulare ausfüllen und sich
ständig irgendwo neu registrieren. Hier setzt
`OpenID <http://www.openid.net>`__ an und stellt ein Protokoll bereit,
dass es ermöglicht sich mit den Zugangsdaten eines OpenID-Providers bei
einer anderen Seite einzuloggen. Diese Idee finde ich genial und so
wollte ich auch dies hier realisieren.

Doch nach anfänglichen Erfolgen, machte das
`OpenID-Plugin <http://wordpress.org/extend/plugins/openid/>`__ so
Probleme, dass ich es abschalten musste. Statt der bisherigen lokalen
Lösung habe ich mich nun für eine Externe entschieden. Dazu habe ich das
Plugin: `JanRain RPX <http://wordpress.org/extend/plugins/rpx/>`__
installiert.

Das ging so:

-  Downloaden und in den Ordner Blogverzeichnis/wp-content/plugins/
   hochkopieren
-  Plugin aktivieren
-  Auf der Seite `rpxnow.com <https://rpxnow.com/>`__ einen Accounnt
   einrichten
-  Dann dort eine "Application" (Basic ist kostenlos und völlig
   ausreichend) einrichten
-  Noch den API-Key in den RPX-Plugin-Einstellungen eintragen.

Im Grunde sollte es nun schon funktionieren. Es empfiehlt sich jedoch
noch die angezeigten Provider einzustellen. Dazu geht man auf
*RPX>MyAccount>Dein Blog> Configure Providers* und schiebt bis zu sechs
verschiedene Dienste von links nach rechts (Für Facebook, Twitter,
Yahoo, Myspace und Windows Live muss man eine Anwendung kreieren - dies
wird jedoch ausreichend erklärt).

Nun kann man hier mit seinem Facebook-, Twitter-, Google-, Yahoo-,
AOL-Zugang oder jeder OpenID kommentieren und sich einloggen.

Damit ich mich bei anderen Seiten mit meiner URL einloggen kann setze
ich auf den Dienst myOpenID (der zu RPX gehört) und das dazugehörige
Plugin.
