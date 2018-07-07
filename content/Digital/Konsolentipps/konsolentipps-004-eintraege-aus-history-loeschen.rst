Konsolentipps #004: Einträge aus Konsolenhistorie löschen
#########################################################
:date: 2018-07-07 15:45
:author: Lioman
:category: Digital
:tags: History, Konsole, Konsolentipps, Linux, Bash, Open Source
:slug: konsolentipps-004-eintraege-aus-konsolenhistorie-loeschen
:status: published
:series: Konsolentipps

Die History im Terminal ist wirklich praktisch, denn der gewünschte Befehl ist nicht viele Buchstaben,
sondern nur ein paar Pfeiltasten entfernt. Noch angenehmer ist es, wenn man die Suche mit ``CTRL+R`` nutzt.
Leider landen auch mal Dinge in der Historie, die da gar nicht hingehören: kopierte Passwörter zum Beispiel.
Man möchte dieses natürlich nicht gerade da lassen, sondern möglichst schnell entfernen.

Zuerst kann man sich dazu die fünf letzten Einträge anzeigen lassen: ``history | tail -n 5``

Die Ausgabe sieht ungefär so aus:

.. code-block:: bash

   248  su root
   249  SuperSecurePassword123
   250  history | tail -n 5

SuperSecurePassword123 soll am Besten verschwinden.
Das kann man nun mit ``history -d 249`` erreichen.
Danach ist der Eintrag Nummer 249 Geschichte.
