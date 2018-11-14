Mit OpenSource Projekte planen
##############################
:date: 2014-06-15 21:42
:author: Lioman
:category: Digital
:tags: Open Source, Entwicklung, LibrePlan, OpenProject, Projekt, Projektmanagment, Software, UbuntuusersPlanet
:slug: mit-opensource-projekte-planen
:status: published

Muss man ein Projekt planen, kann man das natürlich mit allerlei
Software tun. Es gibt kommerzielle Produkte und auch allerlei freie bzw.
quelloffene Programme, die einen Projektmanager bei seiner Arbeit
unterstützen sollen. Da man aber bei jeder Art von Projekt mit mehreren
Personen zusammen arbeiten muss, bietet es sich eigentlich an, eben
nicht alles auf dem heimischen Rechner im stillen Kämmerlein zu
installieren, sondern auf einem Server eine wie auch immer geartete
Planungssuite zu haben, auf dass dann alle Projektteilnehmer zugreifen
können. Es gibt gerade für große Planungen sicher auch alle möglichen
(kommerziellen) Dienste, aber die sollen hier kein Thema sein.

Bei meiner Recherche bin ich auf zwei interessante Möglichkeiten, die
hier kurz vorstellen möchte.

.. figure:: {static}/images/libreplan_logo.png
   :align: right
   :class: size-full wp-image-5500
   :width: 205px
   :height: 60px
   :target: https://en.wikipedia.org/wiki/File:LibrePlan_Logo.png

   Das Bild von `Regocasasnovas <https://commons.wikimedia.org/w/index.php?title=User:Regocasasnovas&action=edit&redlink=1>`__
   steht unter `CC-BY-SA <https://creativecommons.org/licenses/by-sa/3.0/deed.en>`__

LibrePlan
---------

Ursprünglich hieß die Software *NavalPlan* und wurde ursprünglich vom
Industrieministerium der `galicischen
Regionalregierung <https://de.wikipedia.org/wiki/Xunta_de_Galicia>`__
finanziert. Der Name lässt schon vermuten, dass es ursprünglich um
Schiffe ging. Da das Ergebnis der Entwicklung aber universell einsetzbar
war, benannte man die in Java geschriebene Software um und
veröffentlichte sie 2010 auf
`Sourceforge.net <https://sourceforge.net/projects/libreplan/>`__. Nun
steht die sehr umfangreiche Planungssuite unter
`AGPL <http://www.gnu.org/licenses/agpl.html>`__ und kann kann frei
`runtergeladen <http://www.libreplan.com/download/>`__ und unter Ubuntu
sehr einfach über ein
`PPA <https://launchpad.net/~libreplan/+archive/ppa>`__ installiert
werden.

Um sie zu testen und mit ihr lokal zu arbeiten (es ging nur um ein
Planspiel, so wurden alle Netzfunktionalitäten nicht gebraucht) hatte
ich sie in einer virtuellen Maschine installiert. Das ging ohne Probleme
und erste Tests waren wirklich vielversprechend. Man kann gut
Abhängigkeiten von Phasen, etc abbilden, Milestones setzen und recht
einfach per

.. figure:: {static}/images/zeitplanung-300x195.png
   :align: left
   :alt: Gantt-Chart
   :width: 300px
   :height: 195px
   :target: {static}/images/zeitplanung.png

   Gantt-Chart in LibrePlan

Drag&Drop umplanen. Generell merkt man, dass LibrePlan durchdacht ist
und gerade für große Infrastrukurprojekte entworfen ist. So kann man
externe Firmen, Materialien, Kunden und eigene Ressourcen unter einer
Oberfläche verwalten und auch QS-Maßnahmen durch entsprechende Formulare
und Zuständigkeiten durchführen. Und für Kommunikation mit Kunden und
Partnern, bzw. für die Dokumentation kann man, sofern man vorher fleißig
Daten eingepflegt hat Berichte generieren und in diversen Formaten auch
exportieren und per E-Mail verschicken.

Muss man mehr als ein Projekt planen, womöglich sogar ähnliche direkt
hintereinander bietet LibrePlan auch die Möglichkeit Vorlagen zu
erstellen, so muss man sich die gleiche Arbeit nicht zwei mal machen.
Ein weiteres "Gimmick" ist eine `App für
Android <https://play.google.com/store/apps/details?id=org.libreplan.mobile>`__,
mit der jeder Mitarbeiter seine Arbeitspakete anschauen und bearbeiten
kann.

Fazit
~~~~~

Ausgereifte Software, mit vielen Funktionen. Eher geeignet für große
Projekte und/oder für Unternehmungen, die oft Projekte durchführen
müssen. LibrePlan braucht allerdings ein paar Ressourcen, da ein
Applikationsserver benötigt wird. So kann man die Projektsoftware nicht
so einfach auf einem shared Hoster installieren.


|Logo OpenProject|\ OpenProject
-------------------------------

Da ich nun für ein zweites Projekt wirklich auf einen Webdienst
angewiesen war, also nicht Lokal in der VM arbeiten konnte, und bei
`uberspace.de <http://uberspace.de>`__ keinen eigenen Tomcat habe, fiel
die Nutzung von LibrePlan ins Wasser und ich musste mich nach anderen
Möglichkeiten umsehen. Schon nach kurzer Recherche stieß ich auf
`OpenProject <https://www.openproject.org/>`__, dass kurz zuvor in
Version 3.0 erschienen war. Da die beiden Projekte sich ähneln, werde
ich jetzt eher auf die Unterschiede eingehen. Auch hier kann man
Arbeitspakete und deren Abhängigkeiten abbilden, die Software ist jedoch
eher auf Softwareentwicklung ausgelegt. So gibt es direkte Anbindung an
svn und git, sofern diese auf dem gleichen Server installiert sind
(Commits können direkt im Paket angezeigt werden, wenn man in die
Nachricht die Nummer angibt). Und es gibt ein Plugin, die die
Arbeitsweise mit agiler Softwareschmieden (Strichwort: SCRUM) leicht
machen sollen. Überhaupt gibt es ein paar spannende
`Plugins <https://www.openproject.org/projects/openproject/wiki/Feature%20tour>`__,
die man hinzuschalten kann. Möchte man z.B. auch Dateien hinzufügen,
Besprechungen verwalten (sehr praktisch!), eine eigene Projektwiki oder
`github.com <http://github.com>`__ anbinden kann man bei der
Installation diese Extramodule aktivieren. Im Umkehrschluss heißt das:
Benötigt man bestimmte Funktionen nicht, kann man sich den Serverplatz
einfach sparen.

Auch OpenProject kann man vor der Installation auf dem eigenen Server
testen. Und das noch komfortabler als LibrePlan. Man bekommt mit nur
e\ `in paar Klicks eine eigene
Testinstanz <https://start.openproject.com/>`__, mit der man rumspielen
kann. Nach 30 Tagen wird dann die Instanz und mit ihr alle Daten
gelöscht.

Nachteile gibt es allerdings auch hier: OpenProject ist einfach noch
nicht so komfortabel wie LibrePlan. Das fängt schon bei der
`Installation <https://www.openproject.org/projects/openproject/wiki/Installation_OpenProject_3_0>`__
an. Es gibt zwar
neuerdings\ `deb-Pakete <https://www.openproject.org/projects/openproject/wiki/Installation_Ubuntu_Package>`__,
dieses beinhaltet aber keine Plugins und man müsste diese dann von Hand
nachinstallieren. Auch sonst ist alles ein bisschen starrer. So kann man
Paketnamen und Beschreibungen nicht einfach editieren. Vielleicht ist
dies auch beabsichtigt, ich hätte aber gerne die Option dazu. Auch kann
man nicht so schön einfach Pakete oder ganze Arbeitspaketbäume per Drag
& Drop umplanen. In vielen Fällen bleibt nichts anderes übrig, als
Duplikate zu erstellen und die Originale dann zu löschen. Das ist
besonders ärgerlich, wenn schon auf das Paket gearbeitet wurde und mit
veränderter Paketnummer auch alle Verweise flöten gehen.

Fazit
~~~~~

Gute Software, die das Planen und Durchführen, vor allen Dingen von
Softwareprojekten leicht macht. Gute Integration von VCS und nützliche
Features, die sich durch Plugins an und ausschalten lassen. Dazu auch
Shared Hoster geeignet. Wären die Abzüge in der B-Note nicht, wäre es
eine perfekte Software. Aber schon jetzt ist OpenProject für kleinere
und mittlere Unternehmungen geeignet.

.. |Logo OpenProject| image:: {static}/images/logo_openproject_foundation.png
   :class: alignright size-full wp-image-5518
   :width: 314px
   :height: 96px
   :target: https://www.openproject.org
