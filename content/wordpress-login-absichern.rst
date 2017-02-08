Wordpress Login absichern
#########################
:date: 2011-06-18 18:38
:author: Lioman
:category: Internet
:tags: Blog, Login, Plugin, Sicherheit, Wordpress
:slug: wordpress-login-absichern
:status: published

| |image0|\ Vor einiger Zeit, als ich Wordpress nicht gleich
  aktualisiert hatte, bekam ich Mails von meinem Blog. Jemand hatte
  versucht den Adminaccount zu hacken und an mein Passwort zu kommen.
  Ich hatte danach aktualisiert, die Lücke war geschlossen und ich habe
  eigentlich keinen weiteren Gedanken darauf verschwendet.
| Durch einen Artikel bei
  `Perun <http://www.perun.net/2011/06/15/wordpress-absichern-mit-limit-login-attempts/>`__
  bin ich wieder auf das Problem aufmerksam geworden.
| Die Lösung ist eigentlich recht simpel. Da ein Angreifer das Passwort
  nicht kennt, muss er es ausprobieren. Entweder durch manuelles raten,
  oder mit einem Skript.

Dem kann man dem Spaß verderben, wenn man eine kleine Hürde einbaut, die
nach einer bestimmten Anzahl von Versuchen greift. Das Plugin *`Limit
Login
Attempts <https://wordpress.org/extend/plugins/limit-login-attempts/>`__*
macht genau das und sperrt den Loginbereich nach einer bestimmten Anzahl
von Falscheingaben.

Das bietet keine absolute Sicherheit, macht aber dieses private
Kleinblog noch ein wenig uninteressanter für einen Angreifer.

.. |image0| image:: {filename}/images/artikelbild_wordpress.png
   :class: alignleft size-full wp-image-3306
   :width: 160px
   :height: 160px
   :target: {filename}/images/artikelbild_wordpress.png
