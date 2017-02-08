Skript: Aktuelle Version von Chromium runterladen
#################################################
:date: 2011-11-18 14:00
:author: Lioman
:tags: bash, Chromium, Linux, Skript, Ubuntu, UbuntuusersPlanet
:slug: skript-aktuelle-version-von-chromium-runterladen
:status: published

In der Uni habe ich das Problem, dass auf den Rechnern nicht die
aktuellsten Versionen aller Programme installiert sind. Bei manchen
macht das nicht so viel aus, bei anderen ist das nicht so gut, denn
bestimmte Funktionen bieten nur die aktuelleren Programme.

`Chromium <http://www.chromium.org>`__ ist da so ein Fall (Sync
Funktioniert z.B.nicht) und da ich, auf den Uni-Rechnern mangels Rechten
nicht einfach ein Programm installieren kann, habe ich mir ein kleines
Skript gebastelt, dass einen aktuellen Snapshot runterlädt und dann die
neuste Version ausführt.

::

    #!/bin/bash
    #Get the latest Chromium-Version
    latest=`curl http://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux/LAST_CHANGE`
    #Download Chromium
    wget --progress=bar:force -O /tmp/chrome-linux.zip http://commondatastorage.googleapis.com/chromium-browser-snapshots/Linux/$latest/chrome-linux.zip 2>&1 | zenity --title="Download Chromium-Version $latest!" --progress --auto-close --auto-kill --width=400
    #Unzip
    #Exclude Erstellen
    exclude=`unzip -Z -1 /tmp/chrome-linux.zip |grep -E 'locales.[^d]+[^e]*pak'| tr "\n" " "`
    #Menge der Dateien bestimmen
    filecount=`unzip -l /tmp/chrome-linux.zip |grep -v -E 'locales.[^d]+[^e]*pak'|tail -n 1|tr -s " " |cut -d " "  -f 2`
    #Lösche alte Version
    rm -R $HOME/chrome-linux/
    unzip -qq -o /tmp/chrome-linux.zip -d /$HOME/ -x $exclude &
    exec 3> >(zenity --progress --title="Entpacken" --percentage=0 --auto-close --width=400)
    while [ `ps -A |grep -c unzip` = "1" ]; 
    do
    count=$((`ls -R /$HOME/chrome-linux/ |wc -w`-4))
    Prozent=$((($count*100/$filecount)))
    echo "$Prozent" >&3
    done
    killall zenity
    #Aufräumen
    rm -R /tmp/chrome-linux*
    #Öffne neue Version
    cd $HOME/chrome-linux/
    ./chrome-wrapper --allow-outdated-plugins &
    exit 0

Dies ist sicher nicht die eleganteste Lösung, aber das Skript gibt aus
was es gerade tut und macht das was es soll zufriedenstellend. Der Umweg
über das /tmp Verzeichnis ist nötig, weil die Quotas nicht gerade
großzügig bemessen sind. Hat man eh eine aktuelle Version der diversen
Plugins (Flash) auf dem Rechner oder Sicherheitsbedenken sollte man beim
Aufruf von Chromium das *--allow-outdated-plugins* entfernen.

**Update:** Habe das Skript nochmal deutlich aufgeräumt und nun ist es
nicht nur kürzer (27 statt 42 Zeilen), sondern auch deutlich schneller.
Statt die Dateien erst zu entpacken und dann ohne die Sprachpakete zu
verschieben entpacke nun direkt in den Zielordner ohne die überflüssigen
Dateien mitzuentpacken. Dazu habe ich ein bisschen mit Regulären
Ausdrücken rumexpiremntieren müssen. Ich konnte mich bisher mit denen
noch nicht anfreunden und so entwischt mir auch jetzt immer noch eine
Datei. Nicht nur *"de.pak"* wird entpackt sondern auch *"da.pak"*. Hat
jemand Verbesserungsvorschläge?
