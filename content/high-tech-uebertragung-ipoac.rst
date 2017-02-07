High-Tech Übertragung: IPoAC
############################
:date: 2009-06-24 16:03
:author: Lioman
:category: Allgemein, Internet
:tags: Internet, Lustig, RFC
:slug: high-tech-uebertragung-ipoac
:status: published

Über
`info-tain.de <http://www.info-tain.de/revolutionr-ip-avian-carriers>`__
bin ich auf den Wikipediaartikel
`IPoAC <http://de.wikipedia.org/wiki/IPoAC>`__ gestoßen.

Dazu muss ich ein bisschen ausholen. Für die Übertragung von Daten gibt
es gewisse Standards, die von der
`RFC <http://de.wikipedia.org/wiki/RFC-Editor>`__ dokumentiert werden.
Das wichtigste Protokoll ist das IP - das Internet Protokoll - welches
im `RFC 791 <http://tools.ietf.org/html/rfc791>`__ beschrieben ist.

    Zitat aus Wikipedia:

    IP bildet die erste vom
    `Übertragungsmedium <http://de.wikipedia.org/wiki/%C3%9Cbertragungsmedium>`__
    unabhängige Schicht der
    `Internetprotokoll-Familie <http://de.wikipedia.org/wiki/Internetprotokollfamilie>`__.

Im Allgemeinen werden die Daten über Kabel + Server usw übertragen. Doch
es sind auch andere Techniken möglich. Drahtlos zum Beispiel, per WLAN
direkt zwischen zwei Computern oder wirklich "High-Tech" - in 200 m Höhe
mit einer Brieftaube als Übertragungsmedium. Das soll nicht gehen? Was
als Aprilscherz in RFC 1149 begonnen hatte wurde am 28. April
implementiert.

    ::

        ping -i 900 10.0.3.1
        PING 10.0.3.1 (10.0.3.1): 56 data bytes
        64 bytes from 10.0.3.1: icmp_seq=0 ttl=255 time=6165731.1 ms
        64 bytes from 10.0.3.1: icmp_seq=4 ttl=255 time=3211900.8 ms
        64 bytes from 10.0.3.1: icmp_seq=2 ttl=255 time=5124922.8 ms
        64 bytes from 10.0.3.1: icmp_seq=1 ttl=255 time=6388671.9 ms

        --- 10.0.3.1 ping statistics ---
        9 packets transmitted, 4 packets received, 55% packet loss
        round-trip min/avg/max = 3211900.8/5222806.6/6388671.9 ms

Da zeigen sich aber auch die Probleme dieses Mediums: 55% Datenverlust
und eine mittlere Pingzeit von knapp 90 min. Da geht es schneller über
das `Sneakernet <http://de.wikipedia.org/wiki/Sneakernet>`__.  Mit dem
direkten Transport von Datenträgern kann die Taube sogar ADSL
`schlagen <http://www.notes.co.il/benbasat/5240.asp>`__. :D
