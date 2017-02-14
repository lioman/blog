Skript: DVD/Video in XVID umwandeln
###################################
:date: 2011-01-27 17:46
:author: Lioman
:category: Gesellschaft, PC und Technik
:tags: divx, DVD, encodieren, Konsole, Linux, Mplayer, rippen, Skript, Video, xvid
:slug: skript-dvdvideo-in-xvid-umwandeln
:status: published

Vor einiger Zeit habe ich `hier </script-videos-in-xvid-encodieren>`__
beschrieben, wie man einfach ein oder mehrere Videos in XVID umwandeln
kann, damit sie auch ein DVD-Player abspielen kann.

Mein Skript habe ich ein wenig verbessert:

#. 

   #. man kann direkt den ersten Titel einer DVD rippen und umrechnen
      lassen wenn man als ersten Parameter *dvd* eingibt. So kann man
      Aufnahmen einfach archivieren.
   #. Schwarze Balken werden automatisch abgeschnitten. Das spart Größe
      und verbessert die Qualität. Dazu habe ich
      `dieses <http://lists.mplayerhq.hu/pipermail/mplayer-users/2005-November/056636.html>`__
      Skript in meines integriert.
   #. Die Bitrate habe ich ein bisschen nach oben geschraubt.

Ansonsten ist die Benutzung gleich geblieben.  Also Skript runterladen -
ausführbar machen und mit

::

    ./Video2xvid video1 video2 video3

oder

::

    ./Video2xvid dvd

starten.

Hier das Skript (Download:
`Video2xvid\_update.tar.gz <images/Video2xvid_update.tar.gz>`__):

::

    #!/bin/bash
    #Lösche logdatei um Störungen zu vermeiden
    rm -v divx2pass.log
    Gesamtdauer=0
    while [ ${1} != '' ]
    do
    if [ "$1" = "dvd" ]; then
    echo "Filmname eingeben:"
    read Filmname
    mplayer -dvd-device /dev/sr0 dvd://1 -v -dumpstream -dumpfile $Filmname.vob
    set "$Filmname.vob"
    fi
    ###Bestimme Breite
    BREITE=`mplayer -identify "$1" -ao null -vo null -frames 0 2>/dev/null | grep ^ID_VIDEO_WIDTH | cut -c16-`; echo "Orginalbreite= $BREITE"
    if [ $BREITE -le 720 ]; then
    VBREITE=$BREITE
    else
    VBREITE=720
    fi

    ###Bestimme Höhe
    HOEHE=`mplayer -identify "$1" -ao null -vo null -frames 0 2>/dev/null | grep ^ID_VIDEO_HEIGHT | cut -c17-`; echo "Orginalhöhe= $HOEHE"
    CROPHOEHE=$((HOEHE-8)); echo "Crophöhe -$CROPHOEHE-"

    ####### Crop
    TOTAL_LOOPS="40"
    NICE_PRI="10"

    ######### CROP Settings #############

    echo "Please wait.  It make take a couple minutes to detect crop parameters."
    A=20
    while [ "$A" -lt "$TOTAL_LOOPS" ] ; do
    A="$(( $A + 1 ))"
    SKIP_SECS="$(( 35 * $A ))"

    nice -n $NICE_PRI nohup mplayer $1 -ss $SKIP_SECS -identify -frames 20 -vo md5sum -ao null -nocache -vf crop=$BREITE:$CROPHOEHE:0:8,cropdetect=20:2 2>&1 > mplayer.log < /dev/null

    # echo DEBUG ; cat mplayer.log

    CROP[$A]=`awk -F 'crop=' '/crop/ {print $2}' < mplayer.log| awk -F ')' '{print $1}' | tail -n 1`
    echo "A= ${CROP[$A]}"

    done
    rm md5sums mplayer.log

    B=20
    while [ "$B" -lt "$TOTAL_LOOPS" ] ; do
    B="$(( $B + 1 ))"
    echo "B= ${CROP[$B]}"
    C=20
    while [ "$C" -lt "$TOTAL_LOOPS" ] ; do
    C="$(( $C + 1 ))"

    if [ "${CROP[$B]}" == "${CROP[$C]}" ] ; then
    COUNT_CROP[$B]="$(( ${COUNT_CROP[$B]} + 1 ))"
    fi
    done
    done

    HIGHEST_COUNT=0

    D=20
    while [ "$D" -lt "$TOTAL_LOOPS" ] ; do
    D="$(( $D + 1 ))"

    if [ "${COUNT_CROP[$D]}" -gt "$HIGHEST_COUNT" ] ; then
    HIGHEST_COUNT="${COUNT_CROP[$D]}"
    GREATEST="$D"
    fi
    done

    CROP="${CROP[$GREATEST]}"

    echo -e "\n\nCrop Setting is: $CROP ... \n\n"
    ####Crop-Ende##

    # Bestimme Audio-Codec
    ACODEC=`mplayer -identify "$1" -ao null -vo null -frames 0 2>/dev/null | grep ^ID_AUDIO_CODEC | cut -c16-`; echo "Audiocodec= $ACODEC"
    if [ "$ACODEC" == "a52" -o "$ACODEC" == "faad" ]; then
    AOPTS="lavc -lavcopts acodec=ac3"
    #"lavc -lavcopts acodec=ac3:abitrate=192 -af volnorm=1"
    else
    AOPTS="mp3lame -lameopts abr:br=196 -af lavcresample=44100,volnorm=1"
    fi

    #Bestime Bitrate
    RATE=`mplayer -identify "$1" -ao null -vo null -frames 0 2>/dev/null | grep ^ID_VIDEO_BITRATE | cut -c18-`;
    echo "Orginalbitrate= $RATE"
    if [ $RATE == 0 ]; then
    BRATE=900
    else
    if [ $RATE -le 1500000 ]; then
    BRATE=$((RATE/1000))
    else
    BRATE=900
    fi
    fi

    # Bestimme Namen
    NAME=`echo "$1" | sed 's/\.[^\.]*$//'`; echo $NAME

    #Bestimme Startzeit
    START=$(date +"%s");

    #Starte Codieren
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "Encodiere $1 in $NAME-xvid.avi"
    echo
    echo "Beginne mit erstem Durchgang"
    echo
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    mencoder  -ffourcc XVID -oac $AOPTS -ovc xvid -xvidencopts pass=1:trellis:hq_ac -vf crop=$BREITE:$CROPHOEHE:0:8,crop=$CROP,scale=$VBREITE:-3 -o /dev/null $1

    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo "Nun folgt Durchgang Nummer Zwei"
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    mencoder  -ffourcc XVID -oac $AOPTS -af lavcresample=44100,volnorm=1 -ovc xvid -xvidencopts pass=2:bitrate=$BRATE:hq_ac:trellis:chroma_opt:vhq=2:bvhq=1:quant_type=mpeg -vf crop=$BREITE:$CROPHOEHE:0:8,crop=$CROP,scale=$VBREITE:-3 -o $NAME-xvid.avi $1

    #Berechne Dauer
    ENDE=$(date +"%s");
    DAUER=$(((ENDE-START)/60));
    echo "************************************"
    echo "**Encodieren in XVID abgeschlossen**"
    echo "**                                **"
    echo "** es dauerte ca. $DAUER Minuten     **"
    echo "************************************"
    echo
    Gesamtdauer=$((Gesamtdauer+DAUER))

    # Aufräumen
    echo -e "Logdatei wird gelöscht"
    rm -v divx2pass.log

    # Auswahl anzeigen
    echo "Soll Orginaldatei gelöscht werden [y/n]"
    echo "Nach 25 Sekunden ohne Eingabe wird ohne Löschen beendet"
    read -t 25 -n 1 TASTE
    if [ "$TASTE" == "y" ] ; then
    echo "Lösche $1"
    rm -f $1
    shift
    else
    shift
    fi
    done
    # Beenden
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    echo
    echo "Encodieren beendet"
    echo
    echo "Gesamtdauer ca. $Gesamtdauer Minuten"
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
