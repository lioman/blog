Update Fehlgeschlagen - Ubuntu 12.10 zerstört die Installation
##############################################################
:date: 2012-10-26 13:25
:author: Lioman
:category: Digital
:tags: Open Source, 12.04, 12.10, ATI, fglrx, update, update-manager, UbuntuusersPlanet
:slug: update-fehlgeschlagen-ubuntu-12-10-zerstoert-die-installation
:status: published

|image0|\ Normalerweise klicke ich sofort auf Update, wenn eine neue
Version von Ubuntu herausgegeben wird. Mich interessiert es einfach,
meist bin ich auch mit den Neuerungen einigermaßen zufrieden und zu
guter Letzt möchte man als Blogger ja auch neue (hoffentlich positive)
Dinge berichten.

Dieses Mal habe ich ein bisschen gewartet, denn mir fehlte die Zeit und
auch die Kritik um die Shoping Lense ließ mich zögern. Nachdem aber
mehrere
`Blogs <http://noisefloor-net.blogspot.com/2012/10/upgrade-auf-ubuntu-1210.html>`__
schon vom unproblematischen Update
`berichtet <https://taach.wordpress.com/2012/10/25/kommt-ein-quantal-geflogen-eine-upgrade-geschichte/>`__\ hatten
ging ich das Ganze gestern an.

Bisher hatte ich beim Upgrade auf eine neue Version eigentlich nie
größere Probleme. Manchmal gab es Pakete nicht mehr oder man musste
hinterher über PPAs ein bisschen nachbessern, aber ich konnte mich
eigentlich nie über den Update-Manager beklagen.

Dieses Mal hat es mich leider erwischt, denn nachdem die neuen Quellen
eingerichtet waren stürzte der Update-Manager ab und ließ sich auch
nicht mehr zum starten bewegen. Ich dachte ich bin clever und starte das
Upgrade über die Konsole:

::

    sudo apt-get dist-upgrade

Es sah erst mal alles gut aus, aber nach einem Neustart startete der
Windowmanager nicht und Unity war auch nicht ganz auf der Höhe. Da ich
letztens von Problemen mit proprietären ATI Treibern gelesen hatte
entfernte ich diese über die Konsole:

::

    sudo apt-get remove fglrx

Das hat erstmal geholfen, denn nun sieht alles wie gewohnt aus und ich
kann auch schon die Neuerungen bewundern. So gehen nun die Fenster nicht
mehr so schnell zu und auf den ersten Blick scheint es tatsächlich
angenehmer zu sein. Dennoch ist nicht alles in Ordnung, denn *"ein
Problembericht liegt vor"* und das ständig und immer wieder. Man könnte
jetzt natürlich analysieren, welche Pakete fehlerhaft sind
(update-manager zickt immer noch) und diese dann beheben. Ich werde
allerdings den anderen Weg gehen und das ganze System endlich mal wieder
neu aufsetzen.

Wer gerade mit dem Gedanken spielt Ubuntu 12.10 über den Update-Manager
einzuspielen, dem rate ich proprietäre Grafiktreiber (ATI) erstmal zu
deinstallieren, um Probleme zu vermeiden. Dann kann man gleich sein
neues System genießen und die Shoping Lense deaktivieren.

.. |image0| image:: {static}/images/ubuntulogo.png
   :class: alignright size-full
   :width: 190px
   :height: 194px
   :target: {static}/images/ubuntulogo.png
