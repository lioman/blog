Android: Backups per Konsole
############################
:date: 2014-07-01 10:25
:author: Lioman
:category: Wissenschaft &amp; Technik
:tags: android, Backup, Ubuntu
:slug: android-backups-per-konsole
:status: published

[caption id="attachment\_5563" align="alignright" width="252"]\ |Android
logo| Bild von `Google <http://www.android.com/branding.html>`__ steht
unter
`CC-BY-SA <http://creativecommons.org/licenses/by-sa/3.0/deed.de>`__\ [/caption]

Mal wieder ein Artikel, eher in die Kategorie: Notiz-an-mich-selbst
fällt.  Immer mal wieder, wenn ich auf meinem HTC OneX eine neue
alternative ROM einspielen möchte, möchte ich zur Sicherheit ein
vollständiges Backup machen. Jedes mal schmeiße ich Google an, um mir
den entsprechenden Befehl herauszusuchen (Meistens lande ich bei `Linux
Und
Ich <http://linuxundich.de/android/komplettes-backup-eines-android-4-0-handys-oder-tablets-ohne-root-rechte-erstellen/>`__).

In Zukunft kann ich das hier hoffentlich einfacher finden. Aber nun zur
Anleitung:

Das Gerät muss im USB-Debuggingmodus an den Rechner angeschlossen
werden. Mit dem Befehl:

.. code:: bash

    adb backup -apk -shared -all -f backup_$(date +%d%m%Y).ab

wird im aktuellen Verzeichnis die Backupdatei mit aktuellem Datum als
Name erstellt. Unter Ubuntu muss man noch ein sudo  voranstellen, da
sonst das System den Zugriff auf das Gerät verwaltet. Nun muss man nur
noch auf dem Androiden das Backup bestätigen und das Backup läuft.

Das kann dann aber (je nach Gerät und "Füllstand") ein bisschen
dauern...

::

    $ time sudo adb backup -apk -shared -all -f backup_$(date +%d%m%Y).ab
    Now unlock your device and confirm the backup operation.
    real 142m10.044s
    user 0m1.349s
    sys 1m13.988s
    $

Möchte man ein Backup wieder einspielen, kann man dies mit adb restore
BACKUPDATEI.adb  tun

.. |Android logo| image:: {filename}/images/Android_robot-252x300.png
   :class: wp-image-5563 size-medium
   :width: 252px
   :height: 300px
   :target: {filename}/images/Android_robot.png
