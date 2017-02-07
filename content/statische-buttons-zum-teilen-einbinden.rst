Statische Buttons zum teilen einbinden
######################################
:date: 2012-01-16 12:39
:author: Lioman
:category: Allgemein, Internet
:tags: Blog, Buttons, Flattr, Share, statisch
:slug: statische-buttons-zum-teilen-einbinden
:status: published

Ich hatte eine Weile überlegt, ob ich nicht alle Buttons entfernen
sollte. Viel wird von hier aus nicht geteilt und ich bin eigentlich der
Meinung solche Knöpfe gehören in den Browser und nicht auf die Seite
selbst. Außerdem gibt es ja durchaus auch Datenschutz bedenken. So hatte
ich eine Weile die 2-Klick-Lösung eingebunden, aber erstens hat mir das
Design nicht gefallen und zweitens machte es ein paar Probleme.
(Doppelte Opengraph-Tags, Javascript "biss" sich mit anderen Plugins)

Nun habe ich mich für die statische Variante entschieden. Der Vorteil:
einigermaßen Datenschutzkonform (Daten werden erst bei Klick übertragen)
und verdammt schnell,denn es wird dank
`CSS-Sprites <http://de.wikipedia.org/wiki/CSS-Sprites>`__ nur eine
einzige schlanke Grafik\ |image0| vom Webserver geladen und nicht, wie
bei dynamischen Lösungen, mehrere Grafiken von externen Servern per
Javascript.

Realisiert habe ich das anhand der Anleitung von
`Perun <http://www.perun.net/2011/12/15/facebook-twitter-google-statische-buttons-im-eigenbau/>`__,
allerdings habe ich Grafik (siehe rechts) und Code um Flattr erweitert
und Xing aus beidem eliminiert.

**Update:** +1 geht leider nicht, denn dafür müsste man doch einen
JS-Button einbinden. Man kann im sich öffnenden Fenster nur die Seite
auf GPlus teilen.

Hier ist der Code für die single.php (Flattr UserID **muss** ersetzt
werden):

::

    <div class="weiterempfehlen">
        <p>Diesen Artikel weiterempfehlen:</p>
        <ul>
            <li><a href="https://flattr.com/submit/auto?user_id=lioman&amp;url=<?php echo rawurlencode(get_permalink()) ?>&amp;title=<?php echo rawurlencode(strip_tags(get_the_title())) ?>&amp;description=<?php echo rawurlencode(strip_tags(get_the_excerpt(), true)) ?>&amp;tags=<?php $posttags = get_the_tags();if ($posttags) {foreach($posttags as $tag) { echo $tag->name . ',';   }}?>&amp;category=text&amp;language=de_DE" target="blank" title="Flattrn"><span>Flattr</span></a></li>
            <li class="tw-einzeln"><a href="https://twitter.com/intent/tweet?source=webclient&text=<?php echo rawurlencode(strip_tags(get_the_title())).'&amp;via=lioman&amp;url=' , urlencode(get_permalink($post->ID))?>&amp;hashtags='<?php $posttags = get_the_tags();$count=0;if ($posttags) {foreach($posttags as $tag) {$count++;if ($count <= 3) {echo $tag->name . ',';}}}?>" target="blank" title="Bei Twitter empfehlen"><span>Twitter</span></a></li>
            <li class="fb-einzeln"><a href="https://www.facebook.com/sharer/sharer.php?u=<?php echo urlencode(get_permalink($post->ID)); ?>&t=<?php echo rawurlencode(strip_tags(get_the_title())) ?>" target="blank" title="Bei Facebook empfehlen"><span>Facebook</span></a></li>
            <li><a href="https://plus.google.com/share?url=<?php echo urlencode(get_permalink($post->ID)); ?>&title=<?php echo rawurlencode(strip_tags(get_the_title())) ?>" target="_top" title="Bei Google+ empfehlen"><span>Google+</span></a></li>
            <li class="del-einzeln"><a href="http://del.icio.us/post?url=<?php echo urlencode(get_permalink($post->ID)); ?>&title=<?php echo rawurlencode(strip_tags(get_the_title())) ?>" target="blank" title="Bei Delicious empfehlen"><span>Delicious</span></a></li>
        </ul>
        <div class="clearer"></div>
    </div>

Und ins Theme muss folgender Code:

::

    .weiterempfehlen        {margin-bottom: 19px;}
    .weiterempfehlen p      {font-weight: bold; margin-bottom: 4px !important;}
    .weiterempfehlen ul     {list-style: none; line-height: 24px; margin: 5px 0 15px 0; padding-left: 0;}
    .weiterempfehlen li     {display: inline;}
    .weiterempfehlen a      {float: left; width: 24px; height: 24px; margin-right: 25px; background: url('/wp-content/uploads/2011/12/perun-social-einzelansicht.png') no-repeat; border-bottom: none !important;}
    .weiterempfehlen span   {display: none;}

    .tw-einzeln a   {background-position: left -26px;}
    .fb-einzeln a   {background-position: left -52px;}
    .gp-einzeln a   {background-position: left -78px;}
    .del-einzeln a  {background-position: left -104px;}

    .weiterempfehlen a:hover {position: relative; top: -1px;}

**Update:** Den Twittercode habe ich angepasst, damit auch die URL und
die Tags entsprechend übernommen werden.

**Update2:** Der Code ist so angepasst, dass nun auch die
Google+-Teilen-URL unterstützt wird. näheres `siehe in meinem Artikel
dazu <http://www.lioman.de/2012/04/inhalte-auf-google-teilen/>`__.

.. |image0| image:: http://www.lioman.de/wp-content/themes/yoko_lioman/images/weiterempfehlen.png
   :class: alignright
   :width: 24px
   :height: 130px
   :target: http://www.lioman.de/wp-content/themes/yoko_lioman/images/weiterempfehlen.png
