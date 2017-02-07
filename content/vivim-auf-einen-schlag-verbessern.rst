Vi/Vim auf einen Schlag verbessern
##################################
:date: 2014-08-17 21:29
:author: Lioman
:category: Open Source, Ubuntuusers Planet
:tags: Editor, Konsole, Linux, vim
:slug: vivim-auf-einen-schlag-verbessern
:status: published

[caption id="attachment\_5601" align="alignright"
width="256"]\ |„Icon-Vim“ von User:ZyMOS, for the Open Icon Library -
Open Icon Library. Lizenziert unter Public domain über Wikimedia
Commons.|
„\ `Icon-Vim <https://commons.wikimedia.org/wiki/File:Icon-Vim.svg#mediaviewer/File:Icon-Vim.svg>`__\ “
von `User:ZyMOS <//commons.wikimedia.org/wiki/User:ZyMOS>`__, for the
`Open Icon Library <http://openiconlibrary.sourceforge.net/>`__ - `Open
Icon Library <http://openiconlibrary.sourceforge.net/>`__. Lizenziert
unter Public domain über `Wikimedia
Commons <//commons.wikimedia.org/wiki/>`__.[/caption]

Es gibt derzeit alle halbe Jahr irgendeinen neuen Texteditor, der
irgendwas besonders toll oder schön machen soll.
`Github <https://github.com>`__  hat erst kürzlich
`Atom <https://atom.io/>`__ veröffentlicht und zuvor galt `Sublime
Text <http://www.sublimetext.com/>`__ als das Nonplusultra. Doch man
muss eigentlich gar nicht so weit suchen, wenn man einen schnellen an
die eigenen Bedürfnisse angepassten Texteditor braucht. Jede
Linuxdistribution (und damit auch die meisten Server, die man so zu
verwalten hat) bringen Vi bzw. `Vim <http://www.vim.org/>`__ (die
verbesserte Variante) mit. Neben
`emacs <https://de.wikipedia.org/wiki/Emacs>`__ ist das 
Textbearbeitungsurgestein und eigentlich ein Konsoleneditor, der ohne
graphische Oberfläche daherkommt.

Neben der Mausunabhängikeit ist eine besondere Stärke die
Erweiterbarkeit mit speziellen Modulen. So beschrieb ich hier schon
einmal, wie man mit
`blogit.vim <http://www.lioman.de/2012/02/nerdiger-wordpressclient-blogit-vim/>`__
Blogposts in Wordpress absetzt. Das ist aber nur eines von vielen
Erweiterungen, die man für Vim
`herunterladen <http://www.vim.org/vimscriptlinks.php>`__ kann, um
Autovervollständigung, Syntaxhighlighting oder besondere Themes zu
aktivieren. Ist Vim einmal mit  sudo apt-get install vim installiert,
kann man  das Programm perfekt auf die eigenen Bedürfnisse anpassen und
der Editor bleibt trotzdem sehr schlank und performant.

[caption id="attachment\_5599" align="alignleft" width="300"]\ |mit ",z"
kommt man in den Zenmode| mit ",z" kommt man in den Zenmode[/caption]

Möchte man mit der Konfiguration nicht bei null beginnen, gibt es mit 
*The Ultimate Vimrc* schon mal ein gutes Anfangsset. Das Projekt wird
von `amix <https://github.com/amix>`__ auf
`github <https://github.com/amix/vimrc>`__ gehostet und ist mit nur zwei
Befehlen ganz einfach installiert.

.. code:: bash

    git clone git://github.com/amix/vimrc.git ~/.vim_runtime
    # Volles Paket:
    sh ~/.vim_runtime/install_awesome_vimrc.sh
    # Nur die Basics installieren:
    sh ~/.vim_runtime/install_basic_vimrc.sh

Das Paket bringt neben fünf Colorthemes und einer direkten Gitanbindung
eine ganze Reihe von Erweiterungen, die ich hier nicht gesondert
aufzähle, denn die vollständige Liste befindet sich auf der `Seite des
Projekts <https://github.com/amix/vimrc>`__. Aber auch was Komfort
angeht wird ein bisschen etwas geändert. Der *<leader>* wird von "\\"
auf ","  gestellt, was gerade auf der deutschen Tastatur viel einfacher
( und damit schneller ) handzuhaben ist.

.. |„Icon-Vim“ von User:ZyMOS, for the Open Icon Library - Open Icon Library. Lizenziert unter Public domain über Wikimedia Commons.| image:: http://www.lioman.de/wp-content/uploads/Icon-Vim.png
   :class: wp-image-5601 size-full
   :width: 256px
   :height: 256px
   :target: http://www.lioman.de/wp-content/uploads/Icon-Vim.png
.. |mit ",z" kommt man in den Zenmode| image:: http://www.lioman.de/wp-content/uploads/vim_zenmode-300x159.png
   :class: wp-image-5599 size-medium
   :width: 300px
   :height: 159px
   :target: http://www.lioman.de/wp-content/uploads/vim_zenmode.png
