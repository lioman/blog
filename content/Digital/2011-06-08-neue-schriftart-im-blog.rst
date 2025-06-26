Neue Schriftart im Blog
#######################
:date: 2011-06-08 15:11
:author: Lioman
:category: Digital
:tags: Blog, CSS, Fonts, Linux, Style, Ubuntu, Webfont, Wordpress
:slug: neue-schriftart-im-blog
:status: published

|image0|\ Seit einiger Zeit hatte ich die wunderschöne freie Schriftart
`LinuxLibertine <http://linuxlibertine.org>`__ per @font-face
eingebunden. Die Schrift ist frei und schön und sehr umfassend. Das
führte zu längeren Ladezeiten, da die Schriftart doch recht groß ist und
viele sie nicht installiert haben (muss also jedesmal neu geladen
werden).

Trotzdem wollte ich nicht auf sie verzichten, denn die ewig gleichen
Fonts die so im Netz rumgeistern (courier, arial usw.) finde ich auf
dauer langweilig.

| Jetzt habe ich einfach mal umgestellt und die Seite wird nun mit der
  `Ubuntu-Schriftart <http://www.ubuntu.com/project/ubuntufont>`__
  dargestellt. Möglich ist dies per `Google Web Font
  API <http://www.google.com/webfonts/>`__. Die Server sind einfach
  schneller und verbreiteter, als der meines Hosters und das Einbinden
  ist Kinderleicht.
| Dazu musste ich nur folgenden Code nach eintragen:

.. code:: html

   <link href="https://fonts.googleapis.com/css?family=Ubuntu|Ubuntu+Condensed|Ubuntu+Mono" rel="stylesheet">

Per @font-face ist es schon komplizierter, denn das sah in meiner css so
aus (Kann man auch kürzen, aber für volle Browserkompatibilität musste
es so lange sein):

.. code:: css

    @font-face {
        font-family: 'LinuxLibertine';
        src: url('/wp-content/fonts/linlibertine_it-webfont.eot');
        font-weight: normal;
        font-style: italic;
    }

    @font-face {
        font-family: 'LinuxLibertine';
        src: url(//:) format('no404'), url('/wp-content/fonts/linlibertine_it-webfont.woff') format('woff'), url('/wp-content/fonts/linlibertine_it-webfont.ttf') format('truetype'), url('/wp-content/fonts/linlibertine_it-webfont.svg#webfont2kZfKjw9') format('svg');
        font-weight: normal;
        font-style: italic;
    }

    @font-face {
        font-family: 'LinuxLibertineC';
        src: url('/wp-content/fonts/linlibertine_c-webfont.eot');
        font-weight: normal;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxLibertineC';
        src: url(//:) format('no404'), url('/wp-content/fonts/linlibertine_c-webfont.woff') format('woff'), url('/wp-content/fonts/linlibertine_c-webfont.ttf') format('truetype'), url('/wp-content/fonts/linlibertine_c-webfont.svg#webfontXhTRoXGS') format('svg');
        font-weight: normal;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxLibertine';
        src: url('/wp-content/fonts/linlibertine_bi-webfont.eot');
        font-weight: bold;
        font-style: italic;
    }

    @font-face {
        font-family: 'LinuxLibertine';
        src: url(//:) format('no404'), url('/wp-content/fonts/linlibertine_bi-webfont.woff') format('woff'), url('/wp-content/fonts/linlibertine_bi-webfont.ttf') format('truetype'), url('/wp-content/fonts/linlibertine_bi-webfont.svg#webfontt6kWjhxv') format('svg');
        font-weight: bold;
        font-style: italic;
    }

    @font-face {
        font-family: 'LinuxLibertine';
        src: url('/wp-content/fonts/linlibertine_bd-webfont.eot');
        font-weight: bold;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxLibertine';
        src: url(//:) format('no404'), url('/wp-content/fonts/linlibertine_bd-webfont.woff') format('woff'), url('/wp-content/fonts/linlibertine_bd-webfont.ttf') format('truetype'), url('/wp-content/fonts/linlibertine_bd-webfont.svg#webfontjqfR7YQm') format('svg');
        font-weight: bold;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxLibertine';
        src: url('/wp-content/fonts/linlibertine-webfont.eot');
        font-weight: normal;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxLibertine';
        src: url(//:) format('no404'), url('/wp-content/fonts/linlibertine-webfont.woff') format('woff'), url('/wp-content/fonts/linlibertine-webfont.ttf') format('truetype'), url('/wp-content/fonts/linlibertine-webfont.svg#webfont6b4IXqEV') format('svg');
        font-weight: normal;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxBiolinumSlanted';
        src: url('/wp-content/fonts/linbiolinum_sl-webfont.eot');
        font-weight: normal;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxBiolinumSlanted';
        src: url(//:) format('no404'), url('/wp-content/fonts/linbiolinum_sl-webfont.woff') format('woff'), url('/wp-content/fonts/linbiolinum_sl-webfont.ttf') format('truetype'), url('/wp-content/fonts/linbiolinum_sl-webfont.svg#webfontEdJ4yq8E') format('svg');
        font-weight: normal;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxBiolinum';
        src: url('/wp-content/fonts/linbiolinum_re-webfont.eot');
        font-weight: normal;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxBiolinum';
        src: url(//:) format('no404'), url('/wp-content/fonts/linbiolinum_re-webfont.woff') format('woff'), url('/wp-content/fonts/linbiolinum_re-webfont.ttf') format('truetype'), url('/wp-content/fonts/linbiolinum_re-webfont.svg#webfontxwfEhz2z') format('svg');
        font-weight: normal;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxBiolinum';
        src: url('/wp-content/fonts/linbiolinum_it-webfont.eot');
        font-weight: normal;
        font-style: italic;
    }

    @font-face {
        font-family: 'LinuxBiolinum';
        src: url(//:) format('no404'), url('/wp-content/fonts/linbiolinum_it-webfont.woff') format('woff'), url('/wp-content/fonts/linbiolinum_it-webfont.ttf') format('truetype'), url('/wp-content/fonts/linbiolinum_it-webfont.svg#webfontHzw9ykXB') format('svg');
        font-weight: normal;
        font-style: italic;
    }

    @font-face {
        font-family: 'LinuxBiolinum';
        src: url('/wp-content/fonts/linbiolinum_bd-webfont.eot');
        font-weight: bold;
        font-style: normal;
    }

    @font-face {
        font-family: 'LinuxBiolinum';
        src: url(//:) format('no404'), url('/wp-content/fonts/linbiolinum_bd-webfont.woff') format('woff'), url('/wp-content/fonts/linbiolinum_bd-webfont.ttf') format('truetype'), url('/wp-content/fonts/linbiolinum_bd-webfont.svg#webfontbsa1NPcJ') format('svg');
        font-weight: bold;
        font-style: normal;
    }

Das Ergebnis war gleich spürbar. Das Blog ist deutlich schneller im
Seitenaufbau und gut sieht es immer noch aus - Oder gibt es da andere
Meinungen?

.. |image0| image:: {static}/images/ubuntufont.png
   :class: alignleft size-full
   :width: 208px
   :height: 798px
   :target: {static}/images/ubuntufont.png
