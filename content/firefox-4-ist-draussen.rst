Firefox 4 ist draußen
#####################
:date: 2011-03-23 18:48
:author: Lioman
:category: Internet, Open Source, PC und Technik
:tags: Browser, firefox, Firefox 4, Linux, Mozilla, PPA, Ubuntu
:slug: firefox-4-ist-draussen
:status: published

|image0|\ Mozilla hat die neuste Version des bekannten Browser
`Firefox <https://www.mozilla.com/de/firefox/>`__ in der vierten Version
veröffentlicht. Es gibt einige Änderungen an der Oberfläche - ob die
einem gefallen muss man selbst ausprobieren. Einige kritisieren jedoch
die Änderungen und halten sie eher für
`Verschlimbesserungen <http://www.knetfeder.de/magazin/2011/internet/firefox-4-chaos/>`__.
Die interessantesten neuen Features sind sicher die Implementierung von
`HTML5 <https://secure.wikimedia.org/wikipedia/de/wiki/HTML5>`__
inklusive `WebM <http://www.webmproject.org/>`__-Codec und
`WebGL <https://secure.wikimedia.org/wikipedia/de/wiki/WebGL>`__. Aber
auch die Panorama-View (erreichbar durch die Tastenkombination Strg+
Umschalt+ E\ `\* <#*>`__) habe ich seit den ersten Betas schätzen
gelernt.

 

Möchte man unter `Ubuntu <http://www.ubuntu.com>`__ immer die neuste
Version des Browser installiert haben, kann man das
`PPA <http://wiki.ubuntuusers.de/Paketquellen_freischalten/PPA>`__ der
Entwickler den Paketquellen hinzufügen.

Das geht am einfachsten  mit dem Befehl

::

    sudo add-apt-repository ppa:mozillateam/firefox-stable

in der Konsole. Hinterher muss man nur noch mit

::

    sudo apt-get update && sudo apt-get upgrade

die Paketquellen neu laden und alle Möglichen Pakete updaten.

**Nachtrag:** Möchte man den Browser auf Deutsch umstellen, muss man
noch das Sprachpaket von Mozilla runterladen und installieren: de.xpi

` <>`__\ \* Ist die Erweiterung AdBlockPlus installiert muss man in der
*about:config* die Variable extensions.adblockplus.settings\_key auf
eine andere Tastenkombination umstellen, da sich sonst nur das
Einstellungsfenster der Erweiterung öffnet.

.. |image0| image:: {filename}/images/firefox.png
   :class: alignleft size-full wp-image-3038
   :width: 128px
   :height: 128px
   :target: {filename}/images/firefox.png
