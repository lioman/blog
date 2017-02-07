Befreie deinen Router
#####################
:date: 2012-05-03 15:44
:author: Lioman
:category: Open Source, PC und Technik, Ubuntuusers Planet
:tags: befreien, dd-wrt, F7D4301, Firmware, Hardware, Linux, Router
:slug: befreie-deinen-router
:status: published

| Viele Geräte haben ein Problem: Die Software. Hersteller kreieren ein
  Produkt und fesseln es dann mit einer proprietären Firmware, die nicht
  erlaubt, dass das Gerät kann was es kann sondern nur das was der
  Hersteller erlaubt. Zudem kommt, dass viele Hersteller kein Geld in
  weiteren Support älterer Hardware stecken wollen, sonder ihre
  Programmierer lieber auf neue Geräte ansetzen. Möchte man also eine
  neue Funktion, die zwar technisch Möglich ist aber Softwaretechnisch
  trotzdem nicht unterstützt, muss man sich ein neues Gerät kaufen. Das
  ist aus Kunden- und Umweltsicht schade, denn so landen noch nutzbare
  Geräte auf dem Müll aber die Hersteller freuen sich, da so Geld in
  ihre Kassen gespült wird. Möchte man sich also nicht den Restriktionen
  der Hersteller beugen bleibt einem nichts anderes übrig, als auf
  Garantien zu verzichten und zu rooten, jailbraken, debranden oder
  anderweitig von den auferlegten Fesseln zu befreien.\ |image0|
  Entweder werden eingebaute Sperren der Hersteller gelöscht oder
  umgangen oder gleich eine alternative Firmware aufgespielt.
| Am Ende sind nämlich viele Geräte auch nichts anderes als ein kleiner
  Rechner, mit CPU, Arbeitspeicher und Anschlüssen auf einer Platine und
  so kann man in vielen Fällen eine Software basierend auf einem
  Linuxkernel über die Updatefunktion oder eine Hintertür einschleusen
  und aufspielen. In den meisten Fällen verliert man die Garantie aber
  gewinnt eine Fülle von neuen Funktionen. Bei alten Geräten lohnt es
  sich in jedem Fall, bei neueren muss man abwägen, denn die Gefahr,
  dass man das Gerät
  `"brickt" <https://en.wikipedia.org/wiki/Brick_%28electronics%29>`__
  und es so unbenutzbar macht besteht in jedem Fall.
| In meinem Fall ging es um einen Router der Firma `Belkin
  F7D4301 <http://www.belkin.com/de/IWCatProductPage.process?Product_Id=509942>`__.
  Die Packung verspricht großmächtig alles Mögliche, aber für viele
  Dinge ist eine Windowssoftware nötig oder es funktioniert gleich gar
  nicht richtig. So soll der Router z.B. Torrents herunterladen können,
  wenn der Rechner aus ist. Mein Test unter WindowsXP zeigte aber, dass
  das auch mit der mitgelieferten Software nicht funktioniert und
  zahlreiche Forenbeiträge scheinen das zu bestätigen. Viel Zeit habe
  ich diese Tests nicht investiert, denn ich will ja den Router befreien
  und eine andere Software aufspielen.
| Für viele Router gibt es diverse Alternativen. Der Klassiker ist
  sicher `OpenWRT <https://openwrt.org/>`__, aber
  `Tomato <http://www.polarcloud.com/tomato>`__ scheint einfacher zu
  konfigurieren sein, wenn man sich auf der Konsole nicht so auskennt.
| |image1|\ Der Belkin F7D4301 wird von
  `dd-wrt <http://dd-wrt.com/site/index>`__ unterstützt. Dafür muss man
  das build von eko nutzen. Laut seinem
  `Foren-Beitrag <http://www.dd-wrt.com/phpBB2/viewtopic.php?t=78042&postdays=0&postorder=asc&start=0>`__,
  soll man nicht per GUI, sondern per Mini CFE-Server die Firmware auf
  den Router aufspielen. Leider führte die Erklärung *"(press wps
  button, plug in power, keep it pressed for 6-7 s, open browser at
  192.168.2.1.)* nicht zum gewünschten Erfolg und der CFE-Server
  startete einfach nicht. (**Update:** `Anleitung zum Start des
  MiniCFE <http://www.lioman.de/2013/01/belkin-router-richtig-flashen/>`__)
  Das einspielen, des mini-builds über das Webinterface des Routers
  funktionierte aber ohne Probleme und auch das Upgrade auf die
  komplette Version war unproblematisch.
| Der Router läuft nun stabiler, das WLAN-Netz bricht nicht so häufig ab
  und die
  `Feature-Liste <http://www.dd-wrt.com/wiki/index.php/DD-WRT_Doku_%28DE%29#Komplette_Featureliste>`__
  macht jeden Technikjunkie glücklich.
| Für mich ein echtes Highlight ist der CRON-Dienst. So kann man alle
  möglichen Zeitgesteuerten Abläufe einfach realisieren. Nachts ist das
  WLAN z.B. aus und
  `Transmission <http://www.dd-wrt.com/wiki/index.php/Transmission_daemon>`__
  ist an. So bekommt man die von Belkin versprochene Funktionalität doch
  noch und der Router verteilt nachts (wenn ich die Bandbreite nicht
  benötige) brav Ubuntu-Images über das Torrentnetzwerk.
| DD-WRT lohnt sich also wirklich, denn nun kann man recht einfach
  Programme auf dem Router aufspielen, hat Zugriff auf den Router per
  ssh und bekommt noch einige andere Vorteile. Der F7D4301 wird damit
  plötzlich wirklich zu einem guten Router im Heimnetzwerk.

.. |image0| image:: images/handschellen.png
   :class: alignright size-full wp-image-4560
   :width: 300px
   :height: 221px
   :target: images/handschellen.png
.. |image1| image:: images/dd-wrt_logo.png
   :class: alignleft size-full wp-image-4561
   :width: 208px
   :height: 40px
   :target: images/dd-wrt_logo.png
