Nautilusabstürze unter Ubuntu 11.10 (Oneric Ocelot)
###################################################
:date: 2011-10-16 17:46
:author: Lioman
:category: Digital
:tags: Open Source, 11.10, Bug, Linux, Nautilus, Ubuntu
:slug: nautilusabstuerze-unter-ubuntu-11-10-oneric-ocelot
:status: published

|image0|\ Seit ein paar Tagen ist die neue Version des freien
Betriebssystems `Ubuntu <http://ubuntu.com>`__ erschienen und das Update
lief soweit ohne Probleme, auch wenn der Download ziemlich lange dauerte
was aber nicht verwunderlich war, da ich das Update noch in der ersten
Stunde gestartet hatte.

Einziges Problem waren Abstürze des Dateimanagers
`Nautilus <http://live.gnome.org/Nautilus>`__. Wechselte man auch nur
den Ordner stürzte er ab und man musste von neuem beginnen (oder gleich
in die Konsole wechseln).

Jetzt habe ich bei `Linux und
ich <http://linuxundich.de/de/software/absturze-des-nautilus-dateimanagers-in-ubuntu-oneiric-11-10-abstellen>`__
eine mögliche Lösung des Problems entdeckt.

Schuld an den Abstürzen ist die Erweiterung nautilus-open-terminal und
bisher hilft wohl nur die Deinstallation.

also einfach mit

``sudo apt-get remove nautilus-open-terminal``

das Paket erstmal entfernen. Nährere Informationen zu diesem Fehler und
eventuell andere Lösungen beschreibt  `Bug
#869131 <https://bugs.launchpad.net/ubuntu/+source/nautilus-open-terminal/+bug/869131>`__.

Update: Nautilus muss erstmal neu gestartet werden. Ein einfaches
 ``pkill nautilus``  genügt da

.. |image0| image:: {static}/images/ubuntulogo.png
   :class: alignright size-full wp-image-3180
   :width: 190px
   :height: 194px
   :target: {static}/images/ubuntulogo.png
