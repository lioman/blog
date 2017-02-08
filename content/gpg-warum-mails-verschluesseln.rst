GPG: Warum Mails verschlüsseln
##############################
:date: 2011-01-19 16:01
:author: Lioman
:category: Internet, PC und Technik
:tags: E-Mail, GnuPG, GPG, Mail, Privatspähre, Sicherheit, Verschlüsselung
:slug: gpg-warum-mails-verschluesseln
:status: published

Vor nicht allzulanger Zeit habe ich hier ein kleines
`Erklärvideo </erklaervideo-was-e-mailverschluesselung-heisst>`__ zu
Mailverschlüsselung/\ `GPG <http://www.gnupg.org/>`__ gepostet. Da ich
das Thema für wirklich wichtig halte, möchte ich es noch ein bisschen
weiter vertiefen. Doch ein Bild sagt mehr als tausend Worte und so habe
ich eine kleine Grafik erstellt:

|image0|\ Geht die Mail unverschlüsselt auf die Reise, kann jede 
Zwischenstation die Nachricht auch auslesen, scannen und
weiterverarbeiten. Und es sind wirklich viele Stationen. Das kann man
recht einfach mit dem Programm
`traceroute <https://secure.wikimedia.org/wikipedia/de/wiki/Traceroute>`__
testen.

Hier einfach mal zwei Beispiele:

#. Von der Uni zu mail.gmx.de - Ergebnis: 11 Stationen
#. Von der Uni bis zu smtp.googlemail.com - Ergebnis 12 Stationen

Liegt die Empfängeradresse nicht auf dem gleichen Server kommen noch die
Stationen von Mailserver zu Mailserver und in jedem Fall die von
Empfängermailserver zum eigentlichen Empfänger dazu. Das sind also im
Endeffekt sicher mehr als 20 Zwischenstationen, die die Mail passiert
und jedes Mal kann sie im Reintext gelesen werden, von
Leuten/Stellen/Firmen, die das gar nicht sollen. Dazu kommt - jede
Zwischenstation ist ein Ziel für Hacker - es reicht eine einzige
Zwischenstation und unbefugte können alles mitlesen  - kopieren usw.
Viele Mails enthalten keine wichtigen Informationen - doch einige sind
vollgestopft mit sensiblen Daten - diese sollte man wirklich
verschlüsseln, dass nur der Empfänger sie öffnen kann. Im Bild sieht das
ganze so aus:

|image1|

Der Absender verschlüsselt die Nachricht per GPG und nur der Empfänger
hat den Schlüssel. Halten sich Absender und Empfänger an ein paar
einfache Sicherheitsregeln ist es so gut wie unmöglich den Mailverkehr
mitzulesen.

Verschlüsselt man den Artikel bis hierhin kommt folgende Ausgabe heraus:

::

    -----BEGIN PGP MESSAGE-----
    Version: GnuPG v1.4.10 (GNU/Linux)

    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
    cynkpoRP47Vax9a9f4DC9XOhHXwX08cIGQ==
    =hy3h
    -----END PGP MESSAGE-----

Ohne die Schlüssel ist das im Grunde nicht zu knacken (sofern das
Passwort sinnvoll- und nicht wie hier "test"- gewählt ist).

| Gerade sensible Daten sollten so verschlüsselt werden. Ärgerlich ist
  es nur, dass viele Behörden, dies gar nicht anbieten. Obwohl es
  einfach und kostenlos ist.
| Wie einfach das ist und ohne, dass es ohne allzu große "Nerdigkeit" zu
  bewerkstelligen ist soll der nächsten Artikel zum `Thema
  GPG </tag/gpg>`__ zeigen.

.. |image0| image:: {filename}/images/mail_ohne_verschluesselung.png
   :class: aligncenter size-full wp-image-2723
   :width: 671px
   :height: 258px
   :target: {filename}/images/mail_ohne_verschluesselung.png
.. |image1| image:: {filename}/images/mail_mit_verschluesselung.png
   :class: aligncenter size-full wp-image-2730
   :width: 671px
   :height: 238px
   :target: {filename}/images/mail_mit_verschluesselung.png
