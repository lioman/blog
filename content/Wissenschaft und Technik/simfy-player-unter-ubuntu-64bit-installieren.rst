Simfy-Player unter Ubuntu-64bit installieren
############################################
:date: 2011-05-04 20:57
:author: Lioman
:category: Wissenschaft &amp; Technik
:tags: 64bit, AdobeAir, Installation, Linux, Simfy, Starter, Ubuntu, Unity
:slug: simfy-player-unter-ubuntu-64bit-installieren
:status: published

|image0|\ Ich habe den Musikstreamingdienst
`Simfy <http://www.simfy.de>`__ schätzen gelernt. Aus verschiedenen
Gründen  hat er für mich `Last.fm <http://last.fm>`__ abgelöst. Der
Desktopclient basiert auf
`AdobeAir <http://www.adobe.com/de/products/air/>`__ und es gibt auch
ein \*.deb Paket, um den Player unter Linux zu installieren. Nachdem ich
mit Ubuntu 11.04 auch gleich auf die 64bit-Version umgestiegen bin stieß
ich auf zwei Probleme: Es gibt von AdobeAir und von Simfy kein 64bit
Paket.

Man muss aber nicht auf den Streamingdienst verzichten, denn für
AdobeAir gibt es eine
`Anleitung <http://wiki.ubuntuusers.de/Archiv/Adobe_Air#64-Bit>`__ und
Simfy kann man recht leicht wie folgt über die Konsole installieren:

Erst das neuste Paket
`hier <http://www.simfy.de/player/install/linux>`__ runterladen und
entpacken.

Nun kann man das Paket mit dem Befehl

::

    sudo dpkg --force-architecture --force-depends -i simfy_VERSION.deb

installieren.

Leider wird kein Starter angelegt, aber auch das geht recht Problemlos.

Einfach die Datei
`simfy.desktop <images/simfy.desktop>`__
runterladen und in den Ordner  */usr/share/applications* kopieren
(Root-Rechte nötig).

Nun wird Simfy von Unity gefunden und kann wie gewohnt per Dash
aufgerufen bzw. im Launcher abgelegt werden.

Einen anderen Ansatz zur Installation kann man
`frantzen <http://www.frantzen.info/index.php?url=archives/10-simfy-Player-unter-Ubuntu-10.10-64bit-Installieren.html>`__
lesen.

**Update:** Kommt es zu Problemen mit Abhängigkeiten unter Ubuntu 11.10
sind weitere (andere) Schritte nötig. `Siehe
hier. <http://www.lioman.de/2011/10/simfy-64bit-unter-ubuntu-11-10-installieren/>`__

.. |image0| image:: {filename}/images/ubuntulogo.png
   :class: size-full wp-image-3180 alignright
   :width: 133px
   :height: 137px
   :target: {filename}/images/ubuntulogo.png
