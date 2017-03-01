Wordpress: Kommentieren mit sozialen Netzwerken erlauben
########################################################
:date: 2013-02-04 13:26
:author: Lioman
:category: Digital
:tags: Open Source, Login, OAuth, Persona, Plugin, Wordpress
:slug: wordpress-kommentieren-mit-sozialen-netzwerken-erlauben
:status: published

Ist man viel im Netz unterwegs, kommen innerhalb kurzer Zeit eine ganze
Menge an unterschiedlichen Logindaten zusammen. Damit man sich nicht
jedes mal neue Zugangsdaten merken muss bieten viele größeren Netzwerke,
wie Twitter, Google und Facebook eine OAuth-API an. Wird diese jetzt von
anderen Seiten und Diensten in eingebaut, kann man sich recht einfach
mit dem großen Netzwerk anmelden oder registrieren. Das ist praktisch
und senkt die Hürde sich anzumelden ungemein.

[caption id="attachment\_5332" align="alignright"
width="300"]\ |Wordpress.com Kommentarformular| Wordpress.com
Kommentarformular[/caption]

Dies kann man sich in Blogs zu Nutze machen und potentiellen
Kommentatoren das Kommentieren erleichtern.
`Wordpress.com <https://wordpress.com>`__ hat deswegen auch schon länger
mit Hilfe von Twitter und Facebook Kommentare absetzen. Hat man ein
selbst gehostetes Blog gibt es von
`Automattic <http://automattic.com/>`__, der Firma hinter WordPress.com,
die Pluginsammlung
`Jetpack <http://wordpress.org/extend/plugins/jetpack/>`__ mit der man
unter anderem das von WordPress.com bekannte Formular aktivieren kann.
Passt dieses aber nicht zum Theme oder möchte man größere Freiheiten/
eigene Kontrolle und will man vielleicht noch andere Netzwerke
aktivieren, gibt es eine nette Alternative. Die Bibliothek
`Hybridauth <http://hybridauth.sourceforge.net/>`__ versammelt eine
ganze Reihe an OAuth-Providern unter einem Dach. Neden den größeren
Diensten gibt es ganze Reihe kleinere aber, je nach Blogausrichtung,
nicht unwichtige Dienste. Hat man zum Beispiel ein Fotoblog ist das
Anmelden mit Instagram oder 500px relevanter als Twitter.

Der Einbau in ein selbstgehostetes WordPress-Blog geht einfach von der
Hand. Man installiert das Plugin: `Wordpress Social
Login <http://wordpress.org/extend/plugins/wordpress-social-login/>`__\ über
das Dashboard. Nun muss man noch die Daten der unterschiedlichen
Netzwerke eingeben. Auf der Einstellungsseite des Plugins ist eigentlich
alles hinreichend für jedes einzelne Netzwerk erklärt.

[caption id="attachment\_5333" align="alignright"
width="300"]\ |Einstellungen des "Wordpress Social Login" Plugins|
Einstellungen des *"Wordpress Social Login"* Plugins[/caption]

Der Ablauf ist allerdings immer gleich und geht in drei Schritten:

#. Im Entwicklerbereich des Dienstes (nach Anleitung) eine Anwendung
   registrieren
#. API-Key und API-Secret per Copy&Paste übertragen.
#. Netzwerk anstellen & Speichern

Hat man all das aktiviert, was man möchte sollte man alles testen, denn
es gibt nichts frustrierenderes als ein nichtfunktionierender Plugin und
der potentielle Kommentator wird vermutlich einfach weiterziehen ohne
seine wertvolle Meinung kundgetan zu haben. Kommt es zu einer
Endlosschleife (z.B.: Twitter-Blog-Twitter-usw.) muss man in der
PHP-Konfiguration die Variable *REGISTER\_GLOBALS* auf *"Off"* stellen
kommt es zu anderen Problemen hilft der Diagnosemodus des Plugins unter
"Help & Support" weiter.

[caption id="attachment\_5336" align="alignleft"
width="300"]\ |Kommentarfeld mit Social Logins| Kommentarfeld mit Social
Logins[/caption]

Leider bietet die Bibliothek im Hintergrund noch keine Unterstützung für
das, von Mozilla entwickelte, `Persona <https://login.persona.org/>`__
(ehemals *BrowserID*) an. Über ein extra
`Plugin <http://wordpress.org/extend/plugins/browserid/>`__ kann man
aber auch Persona aktivieren. Der Nachteil: Die Icons von WSL befinden
sich oberhalb des Kommentarfeldes Persona jedoch unterhalb. Möchte man
dies verbessern sind Änderungen am Theme notwendig und ich hoffe einfach
darauf, dass Persona bald in Hybridauth eingebaut wird.

.. |Wordpress.com Kommentarformular| image:: {filename}/images/wordpress_com-commentform-300x144.png
   :class: size-medium wp-image-5332
   :width: 300px
   :height: 144px
   :target: {filename}/images/wordpress_com-commentform.png
.. |Einstellungen des "Wordpress Social Login" Plugins| image:: {filename}/images/wps_facebook-einstellungen-300x195.png
   :class: size-medium wp-image-5333
   :width: 300px
   :height: 195px
   :target: {filename}/images/wps_facebook-einstellungen.png
.. |Kommentarfeld mit Social Logins| image:: {filename}/images/wordpress_social_logins_kommentarfeld-300x254.png
   :class: size-medium wp-image-5336
   :width: 300px
   :height: 254px
   :target: {filename}/images/wordpress_social_logins_kommentarfeld.png
