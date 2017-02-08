Sicherheitsleck bei Piwik
#########################
:date: 2012-11-27 11:54
:author: Lioman
:category: Internet, Open Source, PC und Technik 
:tags: 1.9.2, Piwik, Sicherheitslücke, update, UbuntuusersPlanet
:slug: sicherheitsleck-bei-piwik
:status: published

Nachdem ich die Software |image0| hier schon\ `häufiger empfohlen
habe </tag/piwik/>`__ muss ich heute leider eine schlechte Nachricht
verkünden. Die Version 1.9.2 wurde mit ein paar Zeilen Schadcode
versehen.

Laut `seeseekey <http://seeseekey.net/blog/11714>`__ muss die Infektion
nach 15:18 am 26. November 2012 passiert sein, denn da hat er das Update
eingespielt und diese Installation ist noch nicht betroffen. Auch die
Meinige ist verschont geblieben, allerdings hatte ich diese
Aktualisierung auch schon lange eingespielt gehabt.

Genaue Informationen zu der Attacke gibt es im `PIWIK
Forum <http://forum.piwik.org/read.php?2,97666>`__. Auf jeden Fall
sollte man die eigene Installation schnellstmöglich überprüfen.

Befindet sich eine Zeile mit

::

    eval(gzuncompress(base64_decode

in der Datei *piwik/core/Loader.php* hat man leider die modifizierte
Version installiert. Sollte das so sein, muss man auf jeden Fall die
Dateien *piwik/core/DataTable/Filter/Megre.php* und */lic.log* löschen,
denn diese wurden vom Angreifer generiert.

Am Besten löscht man aber gleich alle Dateien und installiert alles neu.
Dazu kann man die die neuste
`latest.zip <http://piwik.org/latest.zip>`__ nehmen, denn diese soll
sauber sein. Da aber noch nicht klar  ist wie der Code eingeschleust
wurde (und ob das wieder geschen kann) ist es sicherer die Dateien
direkt von
`github <https://github.com/piwik/piwik/tags>`__\ herunterzuladen, denn
das Repository war nie kompromitiert.

 

*Ich habe mich entschlossen diesen Artikel im UbuntuusersPlaneten
erscheinen zu lassen, auch wenn er Ubuntufern ist. Die Software ist
unter Bloggern doch recht beliebt und diese Backdoor kann man leider
nicht mehr harmlos nennen.*

**Update**: Artikel leicht modifiziert

.. |image0| image:: {filename}/images/piwik1.jpg
   :class: alignright size-full wp-image-1921
   :width: 182px
   :height: 80px
   :target: {filename}/images/piwik1.jpg
