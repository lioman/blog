Kleine Verbesserungen am Blog
#############################
:date: 2011-04-14 13:24
:author: Lioman
:category: Internet
:tags: Blog, Google, Jquery, Sprachdatei, Syntax Highlighter, Wordpress
:slug: kleine-verbesserungen-am-blog
:status: published

[caption id="attachment\_3109" align="alignleft" width="240"]\ |Bild
eines Tachos| Das Bild von
`kusabi <https://www.flickr.com/photos/kusabi/>`__ steht unter `CC BY-SA
2.0 <https://creativecommons.org/licenses/by-sa/2.0/deed.de>`__\ [/caption]

Um mein Blog ein bisschen bequemer und vor allen Dingen schneller zu
machen, habe ich ein paar Veränderungen vorgenommen.

| Das Plugin WP-CodeBox, dass bisher für das sogenannte
  Syntaxhighlighting gesorgt hat wird schon seit einiger Zeit nicht mehr
  weiterentwickelt. Das ist ein Problem, denn obwohl es bisher noch
  funktioniert kann ein simples Wordpressupdate dazu führen, dass es
  nicht mehr kompatibel ist und auch nicht nachgebessert wird.
| Ein Neues Plugin soll also her und es soll das verpacken im "
  <pre-Container" zulassen, da ich Shortcodes nicht möchte. Falls man
  nämlich aus irgendwelchen Gründen das Plugin wechseln möchte kann das
  zu Problemen bei alten Artikeln führen. Das war schon mal ein Haufen
  Arbeit und den möchte ich mir heute und in Zukunft ersparen. Ich habe
  also auf das `Plugin Better
  Wordpress <http://betterwp.net/wordpress-plugins/bwp-syntax/>`__
  Syntax gesetzt, dass auf `GeSHi <http://qbnz.com/highlighter/>`__
  setzt. Es scheint ohne Probleme zu funktionieren, denn die bisherigen
  Codebeispiele sehen ganz gut aus. Nun sollte aber noch ein bisschen
  Geschwindigkeit rausgeholt werden. Denn das ist nicht nur für den
  Leser gut, sondern auch für den Server und die Einstufung durch
  Google. Nachdem sowieso schon ein Caching-Plugin läuft und ich alle
  Bilder vor dem Upload optimiere, habe ich die deutsche Sprachdatei
  einfach mal ausgeschaltet. Diese macht das Blog um `44%
  langsamer <http://talkpress.de/artikel/deutsche-sprachdatei-wordpress-44-prozent-langsamer>`__
  und ich habe keine Probleme mit einem englischen Adminbereich. Eine
  weitere Verbesserung soll die Umstellung der eingebauten
  `jQuery <http://jquery.com>`__ auf die von Google
  `gehostete <https://developers.google.com/speed/libraries/devguide#jquery>`__
  bringen. Dies ist aus verschiedenen Gründen schneller. Google
  unterhält ein weltweites schnelles CDN, mit dem mein Hoster niemals
  mithalten kann und die Chance steht gut, dass die Version von Google
  sich schon im Browsercache des Lesers befindet, da viele
  Internetseiten die Bibliothek von Google eingebaut haben. Der Einbau
  ist recht einfach. In der functions.php des Themes muss die Zeile
  *"wp\_enqueue\_script('jquery');"* durch folgenden Code ersetzt
  werden:

::

    if ( !is_admin() ) { 
        wp_deregister_script( 'jquery' );
            wp_register_script( 'jquery', 'http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js');
        wp_enqueue_script('jquery');

Die Prüfung is\_admin soll dabei verhindern, dass im Adminbereich die
externe Bibliothek verwendet wird (Das kann zu Problemen führen)

 

.. |Bild eines Tachos| image:: images/Tacho.jpg
   :class: wp-image-3109 size-full
   :width: 240px
   :height: 240px
   :target: images/Tacho.jpg
