Ubuntu: GoogleReader + Mail usw im MeMenu
#########################################
:date: 2010-12-14 20:37
:author: Lioman
:category: Digital
:tags: cloudsn, GoogleReader, Linux, MeMenu, PPA, Programme, Ubuntu
:slug: ubuntu-googlereader-mail-usw-im-memenu
:status: published

Das `MeMenu <http://wiki.ubuntuusers.de/Archiv/MeMenu>`__ in Ubuntu ist
praktisch, denn man kann daraus die wichtigsten Nachrichtenprogramme und
den IM-Status bequem umstellen. Zusätzlich können sich noch andere
Programme darin einnisten. Bisher habe ich mit Popper ungelesene E-Mails
anzeigen lassen und konnte dann auch Thunderbird gleich aus dem Menü
starten.

Nun habe ich eine noch komfortablere Lösung entdeckt. OMGubuntu hat
einen Artikel zu Googsystray
`veröffentlicht <http://www.omgubuntu.co.uk/2010/12/googsystray-1-3-0-released-with-tasks-support-fixes/>`__
mit diesem Programm kann man die diversen Googledienste im Systray
anzeigen lassen. Interessanter ist jedoch die Alternative:
`Cloudsn <http://chuchiperriman.github.com/cloud-services-notifications>`__

Mit diesem kleinen Programm lassen sich diverse Dienste leicht
integrieren. \ |image0| GMail, GReader, Pop3, IMAP, Twitter und
Identi.ca werden unterstützt und können recht einfach eingerichtet
werden. Außerdem kann man einstellen, wie oft nach neuen Nachrichten
gesucht werden soll und ob ein Ton gespielt wird.

Twitter scheint noch nicht zu funktionieren, da das neue
`OAuth <https://secure.wikimedia.org/wikipedia/de/wiki/Oauth>`__ noch
nicht unterstützt wird.

Die Installation:
-----------------

Für Ubuntu gibt es eine
`PPA-Quelle <https://launchpad.net/~chuchiperriman/+archive/cloudsn>`__
des Entwicklers.  Diese muss man hinzufügen und von dort installieren,
das kann man per
`Synaptic <https://secure.wikimedia.org/wikipedia/de/wiki/Synaptic>`__
machen oder man gibt folgende Befehlkette im Terminal ein:

.. code-block:: bash

    sudo apt-add-repository && sudo apt-get update && sudo apt-get install cloudsn

CloudSN findet man dann unter Anwendungen → Internet und nun kann man
einfach seine verschiedenen Konten eintragen.

.. |image0| image:: {static}/images/cloudsn_menue.png
   :class: alignright size-full wp-image-2604
   :width: 338px
   :height: 216px
   :target: {static}/images/cloudsn_menue.png
