Commit wieder herstellen nach git reset --hard HEAD
###################################################
:date: 2014-11-25 17:49
:author: Lioman
:category: Digital
:tags: Open Source, Entwicklung, git, VCS, Wiederherstellen
:slug: commit-wieder-herstellen-nach-git-reset-hard-head
:status: published

Es kommt schon mal vor, dass man in der Eile schnell schnell was dummes
macht!

Folgende Situation:

.. figure:: {filename}/images/Git-logo.png
   :align: right
   :alt: Git logo
   :width: 512px
   :height: 214px

   `Git-logo <https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png>`__ von
   `Jason Long <https://twitter.com/jasonlong>`__. Lizenziert unter
   `CC BY 3.0 <https://creativecommons.org/licenses/by/3.0/>`__ .


Ich hatte ein paar LaTeX-Dateien bearbeitet und in dieser alles mögliche
hin und her geschoben, während mein Kollege eine kleine Einleitung
schrieb. Außerdem hatten wir festgestellt, das eine Datei an falscher
Stelle war. Wir löschten sie beide, er pushte und ich arbeitete weiter.
Dann konnte ich nicht mehr pushen, weil mein Repostitory natürlich vom
Server divergiert war. Es war eilig, wir wollten gehen und es sollte
aber einigermaßen sauber sein, damit wir daran weiterarbeiten können.
Also hatte ich mit git reset --hard HEAD mein Repository zurückgesetzt
und wollte dann die Änderungen wieder zurück spielen. Problem: es ging
nicht! Die Zwischenablage ist halt kein so sicherer Speicher.

Schaute man sich das git log jedoch an, war mein Commit komplett
verschwunden. Das ist durchaus richtig so, denn das macht nun mal ein
Reset. Der komplette Baum wurde umgehängt auf die Reihenfolge vom
origin/master.

Das Schöne bei git (oder einem
`VCS <https://de.wikipedia.org/wiki/Versionsverwaltung>`__ im
Allgemeinen) was einmal hinzugefügt wurde sollte auch wiederherzustellen
sein. Nach ein bisschen Suchen stieß ich auf die Anleitung von `git
ready. <http://gitready.com/advanced/2009/01/17/restoring-lost-commits.html>`__

Zuerst muss man die Revisionsnummer des "verlorenen"  Commits
herausbekommen,

.. code:: bash

    git fsck --lost-found

Dieser Befehl liefert die Liste der *dangling* also der baumelnden
(nicht mehr verbundenen) Revisionen

Hat man die entsprechende Versionsnummer ist der Rest einfach. Man muss
den aktuellen Stand nur noch mit dem benötigten zusammenführen.

.. code:: bash

    git merge $REVISIONSNUMMER

erledigt das und nach einem push ist auch auf dem Server alles so wie es
sein sollte.
