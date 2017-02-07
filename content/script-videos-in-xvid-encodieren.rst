Script: Videos in XVID encodieren
#################################
:date: 2009-11-09 18:40
:author: Lioman
:category: Allgemein, PC und Technik
:tags: bash, encodieren, Linux, script, Video, videocodecs, xvid
:slug: script-videos-in-xvid-encodieren
:status: published

***Platzsparende Videocodecs wie***
`x264 <http://de.wikipedia.org/wiki/X264>`__ ***verpackt in einem
MP4-Container bieten hochqualitative Videos bei kleiner Größe. So ist es
nicht verwunderlich, dass Videos mit diesem Format im Netz weit
verbreitet sind. Das Problem dabei: Viele Standaloneplayer können es
nicht lesen. Man muss also umencodieren.***

Da ich immer mal wieder Videos in verschiedensten Formaten aus dem Netz
lade, sie aber mit dem DVD-Recorder anschauen möchte, habe ich ein
kleines Script geschrieben, dass alles automatisch erledigt.

Der Player kann wie die meisten XVID/DIVX - Avicontainer lesen. Es
sollen also alle Videos in dieses Format überführt werden. Das Problem:
Es gibt viele verschiedene Quellen und Qualitätsstufen. HDTV-Videos wie
`HOME <http://www.home-2009.com/>`__\ über
`Legaltorrents.com <http://www.legaltorrents.com/torrents/547-home-2009>`__
(Sehr groß, mp4, aac), Youtube/ Vimeo videos (kleine flv, zT.
HQ-Videos/mp4) , Streammitschnitte (unterschiedlicher Ausführung) und
natürlich TV-Mitschnitte in DVD-Qualität. Die verschieden Quellen sollen
alle jeweils so optimal wie möglich verarbeitet werden und von Hand ist
es viel zu viel Arbeit.

Ich möchte als Ergebnis eine möglichst hohe Qualität haben, bei
vernünftiger Videogröße und natürlich absoluter Kompatibilität.

Dazu folgende Erkenntnis: Das Ergebnis wird nie besser als die Quelle
werden. Es macht also keinen Sinn aus einem kleinen \*.flv-Video ein
1280x720-Video mit ac3-Sound und einer Bitrate von 1000 zu machen.
Andererseits kann der Player nicht mit zu Großen Bildern umgehen und ich
will ja auch Platz sparen.

Was macht das Script:

#. Quelle prüfen
#. Qualität festsetzen
   nicht besser als Quelle aber höchstens 720 in der Breite bei einer
   Bitrate von 750
#. 2-pass-Encodieren und danach aufräumen

Wie nutzt man das Script?

#. runterladen
#. entpacken
#. ::

       chmod +x #(Ausfuehrbar machen)

#. 

   ::

       ./Video2xvid video1 video2 video3

   .. raw:: html

      <p>

#. Das Script Encodiert alle Videos nacheinander

Über Vorschläge zur verbesserung des Scriptes oder Fragen nach Hilfe
freue ich mich.

Nun das Script, ich hoffe ich habe es ausreichend kommentiert:

(Weiter unten nochmal als Download)

::

    #!/bin/bash
    #Lösche logdatei um Störungen zu vermeiden
    rm -v divx2pass.log
    Gesamtdauer=0
    while [ ${1} != '' ]
      do
    #Bestimme Breite
    BREITE=`mplayer -identify \$1\ -ao null -vo null -frames 0 2>/dev/null | grep ^ID_VIDEO_WIDTH | cut -c16-`; echo \Orginalbreite= $BREITE\
    if [ $BREITE -le 720 ]; then
    VBREITE=$BREITE
    else
    VBREITE=720
    fi

    # Bestimme Audio-Codec
    ACODEC=`mplayer -identify \$1\ -ao null -vo null -frames 0 2>/dev/null | grep ^ID_AUDIO_CODEC | cut -c16-`; echo \Audiocodec= $ACODEC\
    if [ \$ACODEC\ == \a52\ -o \$ACODEC\ == \faad\ ]; then
    AOPTS=\lavc -lavcopts acodec=ac3 -af volnorm=1\
    else
    AOPTS=\mp3lame -lameopts abr:br=196 -af lavcresample=44100,volnorm=1\
    fi

    #Bestime Bitrate
    RATE=`mplayer -identify \$1\ -ao null -vo null -frames 0 2>/dev/null | grep ^ID_VIDEO_BITRATE | cut -c18-`;
    echo \Orginalbitrate= $RATE\
    if [ $RATE == 0 ]; then
        BRATE=750
        else
        if [ $RATE -le 800000 ]; then
            BRATE=$((RATE/1000))
            else
            BRATE=750
        fi
    fi

    # Bestimme Namen
    NAME=`echo \$1\ | sed 's/\.[^\.]*$//'`; echo $NAME

    #Bestimme Startzeit
    START=$(date +\%s\);

    #Starte Codieren
    echo \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    echo \Encodiere $1 in $NAME-xvid.avi\
    echo
    echo \Beginne mit erstem Durchgang\
    echo
    echo \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    mencoder  -ffourcc XVID -oac $AOPTS -ovc xvid -xvidencopts pass=1:trellis:hq_ac -vf scale=$VBREITE:-3 -o /dev/null $1

    echo \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    echo \Nun folgt Durchgang Nummer Zwei\
    echo \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    mencoder  -ffourcc XVID -oac $AOPTS -af lavcresample=44100,volnorm=1 -ovc xvid -xvidencopts pass=2:bitrate=$BRATE:hq_ac:trellis:chroma_opt:vhq=2:bvhq=1:quant_type=mpeg -vf scale=$VBREITE:-3 -o $NAME-xvid.avi $1

    #Berechne Dauer
    ENDE=$(date +\%s\);
    DAUER=$(((ENDE-START)/60));
    echo \************************************\
    echo \**Encodieren in XVID abgeschlossen**\
    echo \**                                **\
    echo \** es dauerte ca. $DAUER Minuten     **\
    echo \************************************\
    echo
    Gesamtdauer=$((Gesamtdauer+DAUER))

    # Aufräumen
    echo -e \Logdatei wird gelöscht\
    rm -v divx2pass.log

    # Auswahl anzeigen
    echo \Soll Orginaldatei gelöscht werden [y/n]\
    echo \Nach 15 Sekunden ohne Eingabe wird ohne Löschen beendet\
    read -t 15 -n 1 TASTE
    if [ \$TASTE\ == \y\ ] ; then
    echo \Lösche $1\
    rm -f $1
    shift
    else
    shift
    fi
    done
    # Beenden
    echo \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\
    echo
    echo \Encodieren beendet\
    echo
    echo \Gesamtdauer ca. $Gesamtdauer Minuten\
    echo \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\

Und hier die Datei zum Download:
`Video2xvid.tar.gz <http://www.lioman.de/wp-content/uploads/Video2xvid.tar.gz>`__
