Eine freie Suche
################
:date: 2009-04-27 12:58
:author: Lioman
:category: Digital
:tags: Open Source, Crawler, Google, Index, P2P, Suchmaschine, verteiltes Rechnen, Yacy
:slug: ein-freie-suche
:status: published

Viele sind wahrscheinlich mit folgenden Begriffen vertraut: `Verteiltes
Rechnen <http://de.wikipedia.org/wiki/Verteiltes%20Rechnen>`__ und
`P2P <http://de.wikipedia.org/wiki/Peer-to-Peer>`__. Wenn man diese
beiden Techniken kombiniert und noch einen
`Crawler <http://de.wikipedia.org/wiki/Crawler>`__ und eine Suchmaske
hinzufügt erhält man die perfekte Internetsuchmaschine. Sie ist von
keinem Unternehmen kontrollierbar, durch Dezentralität vor Ausfällen und
Angriffen sicher, kostenlos, quelloffen und eine Zensur ist nicht
möglich.

Soweit die Theorie. Die Praxis liefert die Suchmaschine YaCy - **Y**\ et
**a**\ nother **Cy**\ berspace.

Unter `yacy.net <http://yacy.net>`__ läd man sich den Client runter, der
- Dank Java - auf allen gängigen
`OS <http://de.wikipedia.org/wiki/Betriebssystem>`__ läuft.

Unter Linux verläuft die Installation problemlos. Einfach entpacken und
das Skript *startYACY.sh* starten.

Das war es schon nun kann man den Weltweiten Index nutzen und dazu
beitragen indem man  eigene Crawler losschickt oder über einen Proxy
crawlt. Eine umfassende Wiki zur Konfiguration des Clients findet man
`hier <http://www.yacy-websuche.de/wiki/index.php/De:Start>`__.

Doch das ganze hat leider auch Nachteile.

Mit älteren und schwächeren Rechnern hat man Probleme, da die JVM
ordentlich Sprit frisst und der Crawler dann das ganze System in die
Knie zwingt. Man kann zwar den benutzten Arbeitsspeicher kontrollieren
nur wird damit der Client auch langsamer.

Da es gar keinen zentralen Index gibt und kein Trust-Modell dauert die
Suche etwas länger (kontaktieren anderer Peers) und das System ist
anfällig für Spammer. Und der größte Nachteil: Es gibt keine Zentrale
Suchmaske, es ist und bleibt damit eine Nischenlösung, wer will denn
erst Clients starten und rumkonfigurieren wenn er nur mal schnell ein
Kochrezept raussuchen möchte.

Fazit: Interessanter Ansatz aber für Otto-Normalverbraucher zu
unpraktikabel.

Alternative: `Wikia Search <http://search.wikia.com/>`__ (freier Index,
Offen, Bewertung der Ergebnisse, zwar kein P2P aber mit GrubNG kann man
auch dazu beitragen
