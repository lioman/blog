VirtualBox: Virtuelle Maschine startet nicht
############################################
:date: 2012-04-05 10:36
:author: Lioman
:category: PC und Technik, Ubuntuusers Planet
:tags: Fehler, Linux, Lösung, Rechte, Ubuntu, VirtualBox
:slug: virtualbox-virtuelle-maschine-startet-nicht
:status: published

| Erst kürzlich habe ich eine `Virtuelle
  Maschine <https://de.wikipedia.org/wiki/Virtuelle_Maschine>`__ mit
  `VirtualBox <http://wiki.ubuntuusers.de/VirtualBox>`__ eingerichtet.
  Doch anstatt zu starten gab VirtualBox nur folgende Fehlermeldung aus:
| |image0|

    Für die virtuelle Maschine w konnte keine neue Sitzung eröffnet
    werden.  Failed to load VMMR0.r0 (VERR\_SUPLIB\_OWNER\_NOT\_ROOT). 
    Fehlercode:NS\_ERROR\_FAILURE (0x80004005) Komponente:Console
    Interface:IConsole {1968b7d3-e3bf-4ceb-99e0-cb7c913317bb}

Ich habe eine ganze Weile gebraucht, bis ich des Rätsels Lösung gefunden
hatte und deswegen möchte ich sie hier teilen (um sie auch zur Not
selbst schnell wiederzufinden)

*/usr* und */usr/lib* müssen root gehören. Vermutlich hatte ich mal aus
irgendeinem Grund (aus Versehen) den Besitzer geändert.

``sudo chown root:root /usr /usr/lib``

löste das Problem und die VM startet wie sie soll.

Den entscheidendeen Tipp hatte
`skierpage <http://ubuntuforums.org/member.php?s=a13ed0ec93c0d6adb1f13785bfda9e87&u=874671>`__
auf Ubuntuforums

.. |image0| image:: http://www.lioman.de/wp-content/uploads/virtualbox2.png
   :class: wp-image-4448 alignleft
   :width: 63px
   :height: 75px
   :target: http://www.lioman.de/wp-content/uploads/virtualbox2.png
