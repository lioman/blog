Wie rette ich meine Daten
#########################
:date: 2009-01-09 19:06
:author: Lioman
:category: PC und Technik
:tags: Datenrettung, festplatte, Linux, PC
:slug: wie-rette-ich-meine-daten
:status: published

Folgendes Problem: Ich starte eines Morgens den PC und bis auf einen
Haufen Fehlermeldungen tut sich nicht viel. I/O Error in Blockdevice
oder so ähnlich. Was heißt das?

Die Festplatte ist entgültig abgeschmiert und man kann den PC nicht mehr
booten.

Ich habe mir also die neuste ***SystemRescueCD***
`hier <http://www.sysresccd.org/Download>`__ runtergeladen und auf CD
gebrannt.

Dann habe ich mit `TestDisk <http://www.cgsecurity.org/wiki/TestDisk>`__
mir mal die Platte angesehen.

Das komplette Partitionsverzeichnis war weg. Aber genau dazu ist das
Programm ja da. Erstmal hat es gar nichts gefunden auch eine
*DeeperSearch* brachte nichts zu Tage. Jetzt hieß es experimentieren!

Die Lösung brachte die Einstellung unter *Geometry.* Ich musste dort
unter *Heads* die Anzahl der Köpfe ändern.

Dann fand Testdisk mit Hilfe der *Tieferen Suche* alle Partitionen
problemlos. Ich habe schon gejubelt und dachte, das wars alle Daten
wieder da und Schluss mit der Arbeit.

Der geneigte Leser kann sich nun denken, dass das noch nicht das Ende
vom Lied war.

Die Festplatte war folgendermaßen aufgeteilt:

+------------------------+---------------------------+--------------+------------+
| **hda1**               | **hda2**                  | **hda3**     | **hda4**   |
+------------------------+---------------------------+--------------+------------+
| **HOME-Verzeichnis**   | **Dokumente und Musik**   | **System**   | **Swap**   |
+------------------------+---------------------------+--------------+------------+

Ich kam an die Dateien von *hda1* -  das war schon mal gut, das System
hätte ich auch retten können und *hda4* ist ja nur der
Auslagerungsspeicher. Nur hda2 konnte nicht eindeutig zugeordnet werden,
da wohl die Platte physisch genau am Anfang dieser Partition defekt war.
Ich habe die Größe der Partition also einfach festlegen müssen, auch
wenn ich damit vielleicht ein paar Daten gekillt habe. Damit kam ich
aber noch immer nicht an die Dateien ran.

Wie das ging kommt nach der nächsten Maus :-)

Ich musste zuerst die defekten Teile Block für Block auf einen nutzbaren
Teil der Platte auslesen.

Es gelang mit
`dd\_rescue <http://www.garloff.de/kurt/linux/ddrescue/>`__ und
`dd\_rhelp <http://www.kalysto.org/utilities/dd_rhelp/index.en.html>`__
(Ein Skript, dass das Auslesen vereinfacht und beschleunigt)

Folgender Befehl war der richtige:

::

     dd_rhelp /dev/hda2 /dev/hda1

Meine ganze Musik lagerte sowieso auf der externen Festplatte, das
wichtigste war nun also die Dokumente wieder zu bekommen,  die im
**ODT-Format** vorlagen.

Das Programm
`***magicrescue*** <http://www.itu.dk/~jobr/magicrescue/>`__ hilft dabei
ungemein. Es scannt die Blöcke nach "magic bytes" d.h. ganz bestimmte
Zeichenfolgen, die auf einen Dateitypen hinweisen.  Dazu nutzt das
Programm Rezepte von denen auch schon einige mitgeliefert werden z.B.
für jpeg-jfif, pdf und eben auch zip Dateien, die ähnlich wie odt's
aufgebaut sind..

Das Rezept ist sogar so gut,  dass es die Dateien gleich in \*.ooo
umbenennt. Man startet also die Rettung mit dem Befehl:

::

     magicrescue -r zip -d RETTUNGSVERZEICHNIS /dev/hda1

Jetzt dauert es eine gaaaaaaaaaaaaaaaaaaaaaaaanze Weile, aber danach hat
man im Verzeichnis einen Haufen Dateien, die man dann nur noch sortieren
muss. Die Namen bleiben nämlich leider nicht mehr erhalten und dazu
kommen viele mehrfach vertretende. Bei mir kamen zusätzlich noch
zip-Dateien raus, die ich aber getrost löschen konnte. Dies waren kleine
Fehlerdateien (das Programm hat wohl nur einen Anfang gefunden und diese
dann als "MiniZip-Datei" ausgegeben) ich hatte nämlich vorher keine
einzige Zip-Datei.

Naja, alle Daten wieder da und ich bin glücklich :-D


