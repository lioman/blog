Android: Kontakte aus einem Nandroid-Backup extrahieren
#######################################################
:date: 2015-08-30 17:44
:modified: 2022-09-05 09:50
:author: Lioman
:category: Digital
:tags: Open Source, android, Backup, kontakte, UbuntuusersPlanet
:slug: android-kontakte-aus-einem-nandroid-backup-extrahieren
:status: published

.. figure:: {static}/images/Android_robot-252x300.png
   :alt: Android-Logo
   :class: size-medium
   :width: 252px
   :height: 300px
   :target: {static}/images/Android_robot.png

   Bild von `Google <http://www.android.com/branding.html>`__ steht unter
   `CC-BY-SA <http://creativecommons.org/licenses/by-sa/3.0/deed.de>`__

Bevor man irgend eine neue ROM auf einem Android-Handy installiert macht
man natürlich ein Backup vom alten System.
Das kann man über
`adb <http://www.lioman.de/2014/07/android-backups-per-konsole/>`__ oder
natürlich über das Recoverysystem, das man ja eh für das Flashen
braucht, erledigen

`ClockworkMod
Recovery <http://forum.xda-developers.com/wiki/ClockworkMod_Recovery>`__ erstellt
dabei ein
`Nandroid <http://forum.xda-developers.com/wiki/NANDroid>`__-Image.
Dieses ist eine Sicherung des kompletten Systems mit allen System- und App-Daten.
Nach dem Backup habe ich auf einem Galaxy S2 Cyanogenmod installiert und
viele Daten waren noch drauf, aber anscheinend waren die Kontakte nicht
synchronisiert.

Ich wollte an die Daten aus dem Backup kommen, ohne gleich alles
wieder rückgängig machen zu müssen.
Der erste Versuch dies über die App Nandroid Manager (Diese ist nicht mehr im PlayStore) zu erledigen scheiterte.
Kontakte kann man zwar anschauen, aber noch nicht wieder zurück ins System holen.

Also erstmal die Daten per USB auf den Rechner holen. In dem von CWM
erstellten Ordner liegen die Dateien:

-  *data.ext4.tar*
-  *data.ext4.tar.a*
-  *data.ext4.tar.b*

*data.ext4.tar.a* habe ich in data.ext4.tar umbenannt und konnte diese
dann mit dem Archivmanager öffnen. 
Nun muss man die Datei :code:`/data/data/com.android.providers.contacts/databases/contacts2.db`
entpacken. Dahinter verbirgt sich eine
`Sqlite-Datenbank <https://sqlite.org>`__ mit allen Kontakten.
Um diese wieder in Android zu importieren zu könne muss man eine VCF Datei erstellen.

Das kann mit dem Script
`dumb-contacts2db <https://github.com/stachre/dump-contacts2db>`__ tun.
Nach dem Download muss man es nur noch mit :code:`chmod +x dump-contacts2db.sh`
ausführbar machen und kann dann alle Daten einfach durch Aufruf des Skriptes extrahieren.
Dazu reicht es dieses folgendermaßen auszuführen:

.. code:: bash

    dump-contacts2db.sh pfad/zur/contacts2.db > contacts.vcf

Kopiert man die erhaltene Datei auf das Mobiltelefon kann die Kontakte-App
diese dann wieder importieren und man hat alle alten Kontakte
wieder.
