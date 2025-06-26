Skript: mp3 in ogg konvertieren
###############################
:date: 2011-01-12 14:52
:author: Lioman
:category: Digital
:tags: Open Source, Linux, mp3, ogg, script, Skript
:slug: skript-mp3-in-ogg-konvertieren
:status: published

|image0|\ Unter Linux gibt es immer mal wieder Probleme mit dem dem
Audioformat `MP3 <http://de.wikipedia.org/wiki/MP3>`__. Schuld sind
Patentstreitigkeiten und die eingeschränkende Lizenzierung. Als
Alternative bietet sich das Format
`Ogg-Vorbis <http://de.wikipedia.org/wiki/Vorbis>`__ an. Es ist
quelloffen und kann mit Mp3 durchaus mithalten. Möchte man also diesen
Codec nutzen, muss man die vorhandenen MP3s einfach konvertieren.
Entsprechende Programme sind schnell installiert und so ist das Ganze
komfortabel zu erledigen. Arbeitet man jedoch auf einem eingeschränkten
System, bei dem die Installation von neuen Programmen nicht möglich ist
(z.B. in der Uni) - muss man mit dem Arbeiten was vorhanden ist und auch
mal einen Umweg gehen.

Hier also ein kleines Skript, welches alle Mp3 in dem Ordner in dem es
sich befindet in Ogg konvertiert. Benötigt wird mplayer und oggenc (bei
vielen Distributionen mit dabei).

::

     #!/bin/bash
    #
    # Dump mp3 to ogg
    #Alle Leerzeichen und Sonderzeichen aus Dateinamen enfernen
    rename "s/ *//g" *
    rename "s/ä/ae/g" *
    rename "s/ö/oe/g" *
    rename "s/ü/ue/g" *
    rename "s/ß/ss/g" *
    rename "s/é/e/g" *
    rename "s/è/e/g" *


    for i in *.mp3
    do 

    #Alten Audiodump entfernen
    rm -fv audiodump.wav

    #Titelinformationen auslesen
    Title=`mplayer -identify $i -ao null -vo null -frames 0 2>/dev/null | grep Title: | cut -c9- |tr " " "_"`
    Album=`mplayer -identify $i -ao null -vo null -frames 0 2>/dev/null | grep Album: | cut -c9- |tr " " "_"`
    Artist=`mplayer -identify $i -ao null -vo null -frames 0 2>/dev/null | grep Artist: | cut -c10- |tr " " "_"`
    Track=`mplayer -identify $i -ao null -vo null -frames 0 2>/dev/null | grep Track: | cut -c9- |tr " " "_"`

    #mp3 --> wav
    mplayer -quiet -vo null -vc null -ao pcm:waveheader $i

    #mp3 --> ogg mit Titelinformationen
    oggenc -q5 -n "%a-%l-%n-%t.ogg" -a "$Artist" -N "$Track" -t "$Title" -l "$Album" audiodump.wav

    #mp3 + wav entfernen
    rm -fv audiodump.wav
    rm -fv $i
    done
    exit 0

Dieses Skript behält nichts. Alle alten Daten werden gelöscht. Möchte
man das nicht muss man *rm -fv $i* entfernen.

.. |image0| image:: {static}/images/mp3tovorbis.png
   :class: alignleft size-full
   :width: 236px
   :height: 76px
   :target: {static}/images/mp3tovorbis.png
