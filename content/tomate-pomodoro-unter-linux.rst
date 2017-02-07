Tomate - Pomodoro unter Linux
#############################
:date: 2015-01-17 19:44
:author: Lioman
:category: Allgemein, Open Source, PC und Technik, Ubuntuusers Planet
:tags: Arbeitstechnik, Disziplin, Linux, Open Source, Pomodoro, Python, Ubuntu
:slug: tomate-pomodoro-unter-linux
:status: published

Ich habe die `Pomodoro-Technik <http://pomodorotechnique.com>`__ für
mich entdeckt. Diese wird immer mal wieder als die neuste Idee der
Zeiteinteilung angepriesen, aber an sich ist der Trick uralt. Aber
zuerst zur Technik an sich. Man stellt sich einen Kurzzeitwecker auf 25
Minuten (oder eine andere sinnvolle nicht zu lange Zeiteinheit). In
dieser Zeit tut man nichts anderes, als die gestellte Aufgabe(n) zu
erledigen. Man surft nicht auf YouTube herum, checkt nicht schnell mal
die Mails oder schaut auf das Handy. Klingelt der Wecker, stellt man ihn
gleich wieder. Dieses mal auf 5 Minuten und verhält sich genau
umgekehrt. Sprich man macht echt Pause und vermeidet alle Arbeit. Holt
sich einen Kaffee, bewegt sich ein bisschen, lässt frische Luft herein
usw. Nach vier *Pomodoros* macht man eine längere Pause von 20-30
Minuten und lässt auch hier alle Arbeit ruhen.

[caption id="attachment\_5700" align="alignright" width="300"]\ |Logo
des Programms Tomate| Logo des Programms Tomate[/caption]

Das funktioniert wirklich gut und die Produktivität steigt sehr schnell,
wenn man sich mal daran gewöhnt hat. Die klassische Low-Tech-Variante
mit Zettel Papier und Kurzzeitwecker ist wahrscheinlich die intensivste
und Beste. Leider ist sie nicht ganz bürokompatibel. Wenn ständig
irgendwo ein Wecker klingeln würde, wäre es um die konzentrierte
Arbeitsatmosphäre schnell schlecht bestellt. Für solche Gelegenheiten
bieten sich diverse Mobilapplikationen an oder, wenn man eh am Rechner
sitzt, ein kleines Programm. Neben diversen Browsererweiterungen gibt es
eben auch native Anwendungen. Für Linux/ Ubuntu hat sich
`Tomate <https://launchpad.net/tomate>`__ als das derzeit Beste erwiesen
(Oder das was mir am meisten zusagt). Tomate ist mit Python und Gtk3
entwickelt und beherrscht die wichtigsten Funktionen. Es ist nicht in
den Paketquellen enthalten, kann aber per
`PPA <http://wiki.ubuntuusers.de/Paketquellen_freischalten/PPA>`__
hinzugefügt und installiert werden.  Dazu im Terminal folgende Zeilen
eingeben.

.. code:: bash

    sudo add-apt-repository ppa:stvs/tomate
    sudo apt-get update && sudo apt-get install -y tomate

In den Einstellungen kann man nun die Zeiten ändern, oder die kleine
Tomate im Indicator dazu bringen den Fortschritt anzuzeigen. Außerdem
ist es möglich die Art der Benachrichtigung zu ändern, leider ist eine
Änderung des Tones (noch) nicht möglich. Was leider auch noch etwas
unschön ist. Klickt man auf das Kreuz oben rechts schließt man das
Programm. Möchte man es nur in der Benachrichtigungsleiste haben, muss
man auf das Icon klicken und kann dann mit einem Klick auf "*Hide*" das
Fenster verstecken.

.. |Logo des Programms Tomate| image:: http://www.lioman.de/wp-content/uploads/tomate-300x300.png
   :class: wp-image-5700 size-medium
   :width: 300px
   :height: 300px
   :target: http://www.lioman.de/wp-content/uploads/tomate.png
