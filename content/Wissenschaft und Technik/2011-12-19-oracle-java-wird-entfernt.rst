Oracle Java wird entfernt!
##########################
:date: 2011-12-19 17:44
:author: Lioman
:tags: Java, Linux, OpenJDK, Oracle, Ubuntu, UbuntuusersPlanet
:slug: oracle-java-wird-entfernt
:status: published

|image0|\ Hatte man das Partner-Repository unter Ubuntu aktiviert konnte
man bisher das Paket sun-java6 installieren. Oracle hatte Sun
`übernommen <http://www.heise.de/newsticker/meldung/Oracle-uebernimmt-Sun-214120.html>`__ und
damit die Rechte an Programmen wie Java und
`OpenOffice.org <http://www.openoffice.org/>`__ erstanden. OpenOffice
ist inzwischen an die
`Apache-Foundation <https://blogs.apache.org/foundation/entry/the_apache_software_foundation_statement>`__
übergeben, nachdem sich die meisten Entwickler vom Projekt losgesagt
haben und den Fork `LibreOffice <http://de.libreoffice.org/>`__
erfolgreich weiterentwickeln.

Oracle hat sich also in letzter Zeit nicht gerade Freunde in der
Open-Source-Szene gemacht und das Auslaufen lassen der
`DLJ <http://jdk-distros.java.net/>`__ ab dem 24. August diesen Jahres
erlaubt es Canonical nicht mehr das Paket so zu verändern, dass z.B.
Sicherheitsupdates eingespielt werden können.

Aus diesem Grund hat sich Canonical zu Recht dazu
`entschieden <https://lists.ubuntu.com/archives/ubuntu-security-announce/2011-December/001528.html>`__,
mit Hilfe eines Sicherheitsupdates sun-java aus den Distibutionen Ubuntu
10.04 LTS, Ubuntu 10.10 and Ubuntu 11.04 zu entfernen.  Nutzte man
bisher nicht eh schon OpenJDK kann man entweder dieses Installieren oder
sich das entsprechende Paket direkt auf der Oracle-Seite holen und
installieren.

Mit dieser Entscheidung ist Ubuntu nicht ganz alleine. Auch Debian hat
`angekündigt <http://www.debian.org/News/weekly/2011/15/#javarm>`__,
dass sun-java nicht mehr Bestandteil der Distribution sein soll.

Falsch finde ich das nicht, denn so wird das freie
`OpenJDK <http://openjdk.java.net/>`__ stärker verbreitet, was die
Entwicklung nur begünstigen kann.

.. |image0| image:: {static}/images/ubuntulogo.png
   :class: alignright size-full
   :width: 190px
   :height: 194px
   :target: {static}/images/ubuntulogo.png
