Nerdiger Wordpressclient: blogit.vim
####################################
:date: 2012-02-08 22:04
:author: Lioman
:category: Open Source, PC und Technik, Ubuntuusers Planet
:tags: Konsole, Linux, vim, Wordpress
:slug: nerdiger-wordpressclient-blogit-vim
:status: published

| Unser Umzug hat mich derzeit (fast) vom Netz getrennt. Kein
  ordentliches DSL mehr, sondern übergangsweise nur ein Webstick. Das
  funktioniert soweit ganz gut, die Verbindung ist allerdings zum großen
  Teil sehr langsam (morgens scheint es ein bisschen schneller zu
  gehen). Wenn man Mails abfragen will, kann man sich in der Zeit
  eigentlich erstmal einen Tee machen.
| Ich war also auf der Suche nach einem Programm mit dem man ohne
  Netzverbindung WP-Artikel verfassen kann, denn schon das Aufrufen des
  Adminbereiches ist eigentlich eine Zumutung für die Mobilverbindung.
  `Drivel <http://dropline.net/past-projects/drivel-blog-editor/>`__
  hatte ich schon installiert und so probierte ich es zuerst mit diesem
  Editor.
| Er sieht ganz gut aus und man kann auch einen Artikel verfassen, alte
  Artikel konnte ich jedoch nicht bearbeiten, da das Programm die
  Verbindung verweigerte.
| Blogilo sieht vielversprechend aus, kommt aber nicht in Frage, denn es
  müssen eine ganze Menge KDE-Bibliotheken mitinstalliert werden und
  diese runterladen möchte ich wegen deren Größe nicht.
| Auf `Wordpress.org <http://wordpress.org>`__ stieß ich dann auf eine
  kleine Erweiterung für `Vim <http://wiki.ubuntuusers.de/vim>`__.

| `blogit.vim <http://www.vim.org/scripts/script.php?script_id=2582>`__
  entpackt man einfach in *~./vim* und legt noch eine Datei mit dem
  Namen passwords.vim in dem selben Ordner an. Dort trägt man seine
  Blogzugangsdatem nach folgendem Schema ein:
| let blogit\_username="Your blog user name"
| let blogit\_password="Your blog password. Not the API-key."
| let blogit\_url="https://your.path.to/xmlrpc.php"
| und schränkt am Besten die Leserechte der Datei so ein, dass nur der
  Besitzer diese lesen kann. Dies ist notwendig, da das Passwort in
  Klartext abgelegt ist.
| Nun kann man in vim mit *:Blogit new* einen neuen Artikel anlegen und
  diesen dann mit *:Blogit commit* ins Blog übertragen, wobei man
  beachten muss, dass nach *"Date"* eine Leerzeile steht, dann sonst nur
  ein Fehler ausgegeben wird.
| Zu guter Letzt muss man den Artikel noch mit *:Blogit push*
  veröffentlichen.

Vorteile: Es ist ein reiner Texteditor und man kann so recht schnell in
der Konsole einen Blogartikel verfassen. Es gibt sogar eine
Autocompletefunktion für Tags und Kategorien, die man mit STRG+X und
dann STRG+U aufrufen kann.

Nachteile: Es ist ein reiner Texteditor, man muss sich also mit html ein
bisschen auskennen, wenn man den Text formatieren will und man kann
keinerlei Bilder hochladen. Dies muss man dann doch über das
Webinterface oder per FTP machen.Außerdem ist die Steuerung von vim
recht speziell und gewöhnungsbedürftig. Hat man sich aber mal
zurechtgefundenkann man gut und flott mit diesem Editor arbeiten.
