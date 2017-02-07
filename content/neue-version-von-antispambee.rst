Neue Version von AntispamBee
############################
:date: 2012-11-21 11:22
:author: Lioman
:category: Open Source
:tags: Antispam, AntispamBee, Plugin, Wordpress
:slug: neue-version-von-antispambee
:status: published

Gerade habe ich das Update des inzwischen recht beliebten und vor allen
Dingen gut funktionierenden Antispam-Plugins für Wordpress hier auf dem
Blog eingespielt. Und es hat sich dieses Mal einiges getan. Schon
optisch sieht das ganze deutlich anders aus, denn die
Konfigurationsseite wurde komplett überarbeitet. Die verschiedenen
Filter des Plugins sind nun in ihrer Reihenfolge aufgelistet (Und es
sieht so aus, als könnte man diese in folgenden Versionen sogar
bearbeiten).

Doch nicht nur die Oberfläche ist überarbeitet. Im
`Changelog <http://wordpress.org/extend/plugins/antispam-bee/changelog/>`__
zu Version 2.4.5 finden sich folgende Punkte:

-  Streichung von Project Honey Pot
-  TornevallNET als neuer DNSBL-Dienst

| Ich weiß nicht, ob das der Tatsache geschuldet ist, dass vermehrt
  Spamkommentare
  `durchkommen <http://www.perun.net/2012/11/08/gestiegenes-spamaufkommen-in-den-letzten-wochen/>`__.
| Denn ich habe auf die Schnelle keine Infos zum Vorteil von
  `Tornevall <https://dnsbl.tornevall.org/>`__ gegenüber `Project Honey
  Pot <http://www.projecthoneypot.net/>`__ gefunden, aber in den FAQ
  steht als Begründung die Registrierungspflicht von Honeypot, habe wohl
  viele Nutzer abgeschreckt:

    | **Warum wurde auf Project Honet Pot verzichtet?**
    | Die öffentliche Spammer-Datenbank *Project Honet Pot*\ ist eine
      sehr gute Quelle für die Erkennung aktiver Spam-Versender. Anhand
      der IP-Adresse kann prompt herausgefunden werden, ob ein
      Kommentator im Blog anderswo bereits als Bösewicht gemeldet wurde.

    Bedauerlicherweise setzt *Project Honet Pot* für die Nutzung einen
    registrierungspflichtigen Account voraus. Nach einer trivialen
    Anmeldung erhält jeder Account-Inhaber einen kostenlosen
    API-Schlüssel, der ihn für die Nutzung des Dienstes autorisiert.

    Genau diese Registrierung empfanden sehr viele *Antispam Bee* Nutzer
    als störend – eben aus Angst vor eventuellen Verpflichtungen,
    Zahlungen und Spam-Zusendungen an die hinterlassene E-Mail-Adresse.
    Heutzutage auch irgendwie verständlich.

    Mit `TornevallNET <http://opm.tornevall.org/>`__ wurde eine
    brauchbare Alternative gefunden, die gleicherweise über einen
    qualitativ hochfertigen und aktuellen Datenbestand verfügt – seit
    2006. Dabei verlangt der Dienst keine Authentifizierung der
    Anwender.

    Die Nutzung der öffentlichen Spammer-Datenbank steht als
    Plugin-Option *“Öffentliche Spamdatenbank berücksichtigen”* zur
    Verfügung und wird oben detailliert vorgestellt.

Ich kann das Plugin weiterhin nur empfehlen, vor allen Dingen wei\ `l
Akismet auch aus Datenschutzgründen weiterhin keine
Alternative <http://www.lioman.de/2010/11/neuer-spamfilter-antispambee/>`__
ist.
