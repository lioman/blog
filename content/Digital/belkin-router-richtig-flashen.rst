Belkin-Router richtig Flashen
#############################
:date: 2013-01-14 15:11
:author: Lioman
:category: Digital
:tags: Open Source, Belkin, dd-wrt, F7D4301, Firmware, MiniCFE, Router, UbuntuusersPlanet
:slug: belkin-router-richtig-flashen
:status: published

Vielleicht sollte der Titel anders lauten: "*Wie startet man beim
F7D4301 (und manch anderen Belkin Routern) den MiniCFE-Server um*
`dd-wrt <https://dd-wrt.com>`_ *richtig aufzuspielen",* denn bei diesem
Router habe ich es getestet. Allerdings sollte die Vorgehensweise auch
bei anderen Routern dieser Firma funktionieren und so ist der Titel eher
Allgemein gehalten. Wer einen anderen Router hat, kann es gerne
ausprobieren und

|dd-wrt_logo| In meinem Artikel `Befreie deinen
Router <https://www.lioman.de/2012/05/befreie-deinen-router/>`_ hatte
ich beschrieben, wie man den Router aus dem Hause Belkin mit deutlich
mehr Funktionen und/oder Performanz ausstatten kann. Die freie
Router-Software werkelt seitdem  auf meinem Router vor mich hin und wenn
ich Zeit und Muße hätte, könnte man mit den entsprechenden Funktionen
noch alles mögliche anstellen. Leider hatte ich letztens beim
Konfigurieren einen Fehler gemacht und *Afterburner* eingestellt. Der
Router blieb daraufhin beim Hochfahren hängen und man kam weder per
WebGUI noch per Telnet dran.

Die Lösung des Problems war ein Neuaufspielen der Software und da das
dieses Mal nicht per WebGUI ging, blieb mir nichts anderes übrig, als
den Start des MiniCFE-Servers zu versuchen. Das letzte Mal ist es mir
aus irgendwelchen Gründen (wahrscheinlich zu wenig Geduld) nicht
gelungen, nun ging es ohne Probleme.

-  Man muss den PC zuerst mit einer statischen IP im Adressraum des
   Routers versehen. Dieser kann unterschiedlich sein und man muss es
   schlicht ausprobieren. Entweder **192.168.1.x** oder **192.168.2.x**,
   wobei  x durch irgendeine Zahl größer 1 ersetzt werden muss.
-  Nun verbindet man den Rechner per Ethernetkabel mit dem Router, an
   dem sonst nichts hängen darf  (Auch kein Stromkabel)
-  Drückt man nun die WPS-Taste, steckt das Gerät ein und hält die Taste
   dabei für 5-15 Sekunden gedrückt, bleibt das Licht auf grün und der
   Server ist gestartet.
-  unter **192.168.1.1** oder **192.168.2.1** ist das Gerät nun
   erreichbar und man kann **Rebooten**, **NVRAM löschen** oder eine
   neue **Firmware** aufspielen.

Diese Methode sollte man auf jeden Fall beim flashen nutzen, denn unter
Umständen kann man sonst den Router bricken.

Wie immer gilt: Wer nicht weiß was er beim aufspielen alternativer
Firmwares tut und was das für Folgen haben kann, sollte es lieber
lassen. Ich übernehme keine Garantien für eventuell zerstörte Geräte.

.. |dd-wrt_logo| image:: {static}/images/dd-wrt_logo.png
   :class: alignright size-full wp-image-4561
   :width: 208px
   :height: 40px
   :target: {static}/images/dd-wrt_logo.png
