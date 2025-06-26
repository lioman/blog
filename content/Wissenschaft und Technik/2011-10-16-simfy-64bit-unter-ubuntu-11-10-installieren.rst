Simfy 64bit unter Ubuntu 11.10 installieren
###########################################
:date: 2011-10-16 19:17
:author: Lioman
:tags: 64bit, Anleitung, Installation, Linux, Simfy, Ubuntu
:slug: simfy-64bit-unter-ubuntu-11-10-installieren
:status: published

|image0| In diesem `Artikel <{filename}2011-05-04-simfy-player-unter-ubuntu-64bit-installieren.rst>`__
habe ich beschrieben wie man den Simfy-Player in der 64bit Version installiert.
Mit Ubuntu 11.10 scheint das nicht mehr so ganz zu funktionieren.

| Das System zeigt nicht erfüllbare Abhängigkeiten an wenn die derzeit
  verfügbare AdobeAir-Version installiert ist. Was mich verwundert, da
  sich eigentlich nichts geändert hat und das Programm an sich ohne
  Probleme läuft. Vielleicht reicht es wenn man an den Befehl bei der
  Installation --ignore-depends anhängt und der ganze Befehl dann so
  aussieht:
| ``sudo dpkg --force-architecture --force-depends --ignore-depends -i simfy_VERSION.deb``
| Geht das nicht kann man es wie
  `frantzen <http://www.frantzen.info/archives/10-simfy-Player-unter-Ubuntu-10.10-64bit-Installieren.html>`__
  machen und die deb-Datei selbst bearbeiten. In der Control-Datei muss
  zusätzlich zur Architektur bei den Abhängigkeiten die Adobeair-version
  auf die aktuelle ändern.

In meinem Fall sieht die Datei dann so aus:

::

    Package: simfy
    Version: 1.6.0
    Section: Applications
    Priority: extra
    Architecture: all
    Source: simfy
    Maintainer: simfy GmbH
    Description: <>
    Pre-Depends: adobeair (>= 1:2.6.0.19170)
    Installed-Size: 2796

Wem das zu mühsam ist, der kann die von mir so veränderte Datei
benutzen: `simfy\_1\_6\_0\_64bit.deb <{attach}/downloads/simfy_1_6_0_64bit.deb>`__

**Update**: Version auf 1.6.0 aktualisiert

.. |image0| image:: {static}/images/ubuntulogo.png
   :class: alignright size-full 
   :width: 190px
   :height: 194px
   :target: {static}/images/ubuntulogo.png
