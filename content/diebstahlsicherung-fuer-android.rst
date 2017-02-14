"Diebstahlsicherung" für Android
################################
:date: 2012-07-12 14:30
:author: Lioman
:category: Open Source
:tags: android, Diebstahl, Linux, Prey, Sicherheit, Ubuntu, UbuntuusersPlanet
:slug: diebstahlsicherung-fuer-android
:status: published

Nach dem ich mit dem letzte
`Artikel <http://www.lioman.de/2012/07/mein-erster-androide-und-wie-soll-ich-ihn-befuellen-2/>`__
ein paar nützliche Tipps zu diversen Androidanwendungen ergattert habe,
möchte ich nun selbst einen kleinen Tipp abgeben.

Es gibt diverse "Diebstahlsicherungen" im Market. Wobei die  Bezeichnung
an sich etwas irreführend ist, denn ein bisschen Software kann keinen
Dieb davon abhalten, ein mobiles Gerät zu entwenden.  Möchte man dies
tun sollte man das Gerät immer in einem Safe an das eigene Handgelenk
schmieden. Trotzdem können solche Systeme sinnvoll sein, wenn man ein
entwendetes oder verlorenen Gerät wieder zurückbekommen möchte.
Grundsätzlich funktionieren alle Programme ungefähr gleich. Fehlt das
Gerät, senden man über irgendeinen Kanal einen Aktivierungsbefehl und
das Gerät sendet Daten zum eigenen Ort über das Netz zurück an den
Besitzer.

Zwei Probleme gibt es dabei.

#. Wenn ein Dieb schlau genug ist und gleich alle Verbindungen kappt,
   hilft einem das beste Programm nichts.
#. Man weiß nie genau welche Daten denn der Dienst sammelt und ob er das
   nicht auch permanent tut, um die User zu überwachen und deren
   ortsbezogene Daten anderweitig zu mutzen.

| Problem Nummer 1 ist eigentlich nicht zu lösen, bei Problem Nummer 2
  schaft Open-Source entsprechendes Vertrauen, da der Quellcode offen
  liegt und der (kundige) Nutzer überprüfen kann, was das Programm so
  tut.
| |image0|\ Hier kommt die Software `Prey <http://preyproject.com/>`__
  ins Spiel. Diese ist nicht nur für Android, sondern auch für
  Ubuntu/Linux, Mac, iOS und Windows erhältlich. Der SourceCode kann bei
  `github <https://github.com/tomas/prey>`__ betrachtet werden.
| Am Besten man installiert Prey über `Google
  Play <https://play.google.com/store/apps/details?id=com.prey>`__\ und
  konfiguriert auch das Gerät darüber.  Da dies selbsterklärend ist,
  verliere ich keine weiteren Worte dazu.

[caption id="attachment\_4875" align="alignleft" width="216"]\ |image1|
Übersichtsdialog in Prey[/caption]

Aber einen Tipp habe ich noch. Standardmäßig wartet das Programm auf
eine SMS mit dem Inhalt "GO PREY", der Satz ist frei konfigurierbar und
ich empfehle etwas unverfängliches zu nahmen, was dem Dieb/Finder nicht
gleich verrät, dass das Gerät ab jetzt überwacht wird. Dies kann man
auch mit dem Deaktivierungssatz in der Übersicht tun. Auch dies ist
sinnvoll, sonst kann jeder, der den Standardsatz per SMS schickt das
Tracking deaktivieren. Dabei ist es übrigens nicht weiter schlimm, wenn
man den Satz vergisst. Auf der Website ist dieser jederzeit nachzulesen
und man kann auch dort das Gerät aktivieren. Möchte man das ganze mal
testen kann man es auch über das Gerät selbst machen. Über "Execution
control" in der Übersicht, ist es möglich die Überwachung zu stoppen.
|image2|\ Das ist nützlich, wenn man das Smartphone wiedergefunden hat
und nicht dazu ins Netz gehen möchte (oder kann).

Für alle Änderungen ist übrigens immer das Passwort von Prey nötig, da
die Daten auch immer an die Server Fork Ltd. übertragen werden müssen
und damit ein unbefugter nicht die Einstellungen ändern kann.

Jetzt zu den Eigenschaften:

Je nach Gerät (Handy/Tablet oder PC) sind diese unterschiedlich. Bei PCs
bekommt man keine genauen Ortsdaten, da ja ein kein GPSmodul verfügbar
ist. Logt sich der Dieb aber in einem öffentlichen WLAN ein (bzw.
befindet sich in der Nähe von bekannten SSIDs), sollte das hinreichend
genau sein. Dafür kann man die Webcam bei Laptops (falls vorhanden) ein
und ausstellen und Screenshots anfertigen. Die Bilder bekommt man dann
mit dem Report geliefert. Dies kann nicht nur praktisch für eine etwaige
Strafverfolgung (Bild des Diebs, Identität über Facebook/ Email oder
sonstige Seiten die der Dieb besucht) sein, sondern auch weitere
Hinweise zum Ort geben.

Das geht leider bei Android- und iOS-Geräten (noch) nicht, dafür ist die
Aktivierung über SMS (Nur bei Android verfügbar!!) recht einfach und man
bekommt den genauen Aufenthaltsort angezeigt. Zudem gibt es ein
SIM-Karten-Wechselalarm. Möchte der Dieb mit einem SIM-Kartenwechsel die
PIN-Sperre umgehen, wird dessen Nummer an das System übertragen und kann
somit auch an Strafverfolgungsbehörden weitergeleitet werden. Außerdem
ist es dadurch möglich mit dem "Finder" in Kontakt zu treten. Davon
würde ich aber eher absehen und mich lieber direkt an die Polizei
wenden. Aber ein Kommentator im bei GooglePlay hat so sein Handy recht
schnell zurückbekommen.

Möchte man mehr Geräte überwachen oder weitergehende Features gibt es
auch Bezahlaccounts ab 5$/Monat dann wäre sogar eine Liveüberwachung
über das Dashboard möglich.

Erfolgsgeschichten gibt es übrigens\ `auch
schon <http://preyproject.com/blog/cat/recoveries>`__ und hier ist noch
ein Erklärvideo:

http://vimeo.com/18728980

.. |image0| image:: {filename}/images/prey_logo.png
   :class: alignright size-full wp-image-4870
   :width: 600px
   :height: 188px
.. |image1| image:: {filename}/images/prey_uebersicht.png
   :class: wp-image-4875
   :width: 216px
   :height: 384px
   :target: {filename}/images/prey_uebersicht.png
.. |image2| image:: {filename}/images/prey_test-168x300.png
   :class: alignright size-medium wp-image-4877
   :width: 168px
   :height: 300px
   :target: {filename}/images/prey_test.png
