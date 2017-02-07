Inhalte auf Google+ teilen
##########################
:date: 2012-04-02 16:41
:author: Lioman
:category: Internet
:tags: Blog, Google, Share, statisch, Teilen, Wordpress
:slug: inhalte-auf-google-teilen
:status: published

Vor einiger Zeit stellte ich eine Möglichkeit vor, wie man einfach
`statische
Buttons <http://www.lioman.de/2012/01/statische-buttons-zum-teilen-einbinden/>`__
in sein Wordpress-Blog einbaut, damit Leser komfortabel Artikel in
diversen Sozialen-Netzwerken teilen können. Der Code, der hauptsächlich
auf einer Idee von
`Perun <http://www.perun.net/2011/12/15/facebook-twitter-google-statische-buttons-im-eigenbau/>`__
basiert hatte ein Problem: Teilen auf Google+ war eine Art Workaround,
da es keine eigene URL dafür gab. Das hat sich jetzt geändert den Google
hat still und heimlich die Möglichkeit mittels Link zu teilen unter
folgender URL scharfgeschaltet: *"https://plus.google.com/share?url="*

Der geänderte Code für die statischen Buttons sieht nun im Falle von
Google so aus:

::

    <li class="gp-einzeln"><a href="https://plus.google.com/share?url=<?php echo urlencode(get_permalink($post->ID)); ?>&title=<?php echo rawurlencode(strip_tags(get_the_title())) ?>" target="_top" title="Bei Google+ empfehlen"><span>Google+</span></a></li>

Eine Javascriptfreie Version von +1 gibt es aber leider immer noch
nicht. Das ist schade, denn gerade diese sind ja für eine bessere
Platzierung in der Suche wichtig.
