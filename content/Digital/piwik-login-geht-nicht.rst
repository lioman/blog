Piwik Login geht nicht
######################
:date: 2010-12-09 16:05
:author: Lioman
:category: Digital
:tags: error, Erweiterung, Fehler, firefox, Login, Piwik, refControl, Referrer, Statistik
:slug: piwik-login-geht-nicht
:status: published

|image0|\ Letztens kam ich nicht mehr auf meine Piwikinstallation. Nach
Eingabe des Passworts kam nur folgende Nachricht in einem roten Kasten:

    Fehler: Der Sicherheitsschlüssel des Formulars ist ungültig oder
    abgelaufen. Bitte aktualisieren Sie das Formular und überprüfen Sie,
    dass Cookies aktiviert sind.

Oder bei einer englischen Installation wäre es :

    Form security key is invalid or has expired. Please reload the form
    and check that your cookies are enabled.

Ich konnte mir das nicht erklären, da bisher alles wunderbar klappte und
die Daten auch über andere Kanäle abrufbar waren. Nach einer Weile habe
ich des Rätsels  Lösung gefunden: Das Piwikfrontend braucht anscheinend
den
`Referrer <https://secure.wikimedia.org/wikipedia/de/wiki/Referrer>`__
und die kürzlich `hier </den-referer-kontrolieren>`__ Vorgestellte
Erweiterung
`RefControl <https://addons.mozilla.org/en-US/firefox/addon/953/>`__
verhinderte das natürlich. Erstellt man für die Piwikinstanz eine Regel,
die den Referrer sendet, funktioniert alles wieder normal.

.. |image0| image:: {filename}/images/piwik1-150x80.jpg
   :class: alignright size-thumbnail wp-image-1921
   :width: 150px
   :height: 80px
   :target: {filename}/images/piwik1.jpg
