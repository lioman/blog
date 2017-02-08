Openlike in Wordpress einbinden
###############################
:date: 2010-04-27 13:30
:author: Lioman
:category: Internet, Open Source
:tags: Button, Facebook, like, openlike, script, Widget
:slug: openlike-in-wordpress-einbinden
:status: published

***Viele verschiedene Blogs haben über den Like-Button von Facebook
`geschrieben. <http://netzwertig.com/2010/04/22/like-button-facebooks-version-der-thank-you-economy/>`__
Per Social-Plugin kann man den bekannten Like-Button einfügen. Ist man
bei Facebook eingeloggt kann man auf den eingebundenen Button klicken
und die Daten werden an Facebook übertragen. Gibt es Alternativen und
wie bindet man sie ein?***

Nutzt man diesen kleinen Knopf häufig kann man daraus natürlich wieder
entsprechende Profile erstellen und nutzbar machen (finanziell).
Außerdem lässt sich beim einbinden leicht
`Missbrauch <http://olbertz.de/blog/2010/04/22/i-like-it-boese/>`__
treiben. Alternativen gibt es schon. Openlike ist eine Solche. Das Ziel
der Entwickler:

    An **open protocol** to allow sharing the things people like in a
    **simple** and **standard** method between web applications.

Das einbinden ist relativ einfach.

In den Header kommt:

::

| 

| 

Und nun muss man noch das Widget in das Template einfügen. Das ist bei
jedem Template unterschiedlich. Nutzt man wie ich das Theme Atahualpa
geht es unter: Atahualpa Theme Options >Style & Edit Center Column>  The
LOOP

direkt nach der Zeile

::

    ',''); ?>

.. raw:: html

   </p>

| 

| 

fügt man folgenden Code ein.

::

    OPENLIKE.Widget({url:<?php echo '\'.get_permalink().'\'; ?>,title:<?php the_title('\', '\'); ?>})

| 

| 

Hat man alles richtig gemacht sieht es aus wie bei mir und man kann auf
einen der Buttons klicken

.. raw:: html

   </p>
