GooglePlus: Titel doppelt beim einfügen von Links
#################################################
:date: 2011-11-15 17:08
:author: Lioman
:category: Internet
:tags: Facebook, Gplus, OG, Opengraph
:slug: googleplus-titel-doppelt-beim-einfuegen-von-links
:status: published

Nachdem ich bei GooglePlus mein Blog als Seite
`hinzugefügt <http://www.lioman.de/2011/11/www-lioman-de-auf-googleplus/>`__
habe, befülle ich diese fleißig mit Links zu diesem Blog.

Dabei ist mir ein kleiner Fehler aufgefallen. All meine Titel waren
doppelt und das sieht nicht gerade schön aus.\ |image0|\ Eine Suche
brachte folgende
`Lösung <http://d76.de/blogs/about/probleme-wp-link-google-plus-opengraph/>`__
zu Tage: Di OpengraphTags waren doppelt und G+ fügt doppelte title Tags
direkt hintereinander ein.

Hat man dieses Problem muss man schauen welche Plugins die Tags
einbinden. In meinem Falle war es Yoast SEO Plugin welches ich abstellen
musste (bzw. dessen Opengraphfunktion).

 

 

.. |image0| image:: {filename}/images/titeldoppeltgplus.jpg
   :class: aligncenter size-full wp-image-3964
   :width: 300px
   :height: 147px
   :target: {filename}/images/titeldoppeltgplus.jpg
