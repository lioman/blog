Wordpress-Plugin: GetLinkMeta
#############################
:date: 2012-01-10 10:46
:author: Lioman
:category: Digital
:slug: wordpress-plugin-getlinkmeta
:lang: en
:status: published

Update: This Plug in is not maintained any more!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| This is my first Wordpress-plugin. If you want to save your link
  discoveries to your Blog it is exhausting to copy and paste the
  description of these sites. But there is an easy way. Many sites
  provide meta-tags like this:
| ``<meta charset=""UTF-8"" /> <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"> <meta name="geo.placename" content="Münsterplatz, 79098 Freiburg im Breisgau, Deutschland" /> <meta name="geo.position" content="47.995416;7.853244" /> <meta name="geo.region" content="DE-Baden-Württemberg" /> <meta name="ICBM" content="47.995416, 7.853244" /> <title>Liomans Blog</title> <meta name="description" content="42 ist die Antwort - aber wie lautet die Frage?"/>``

My plugin: `Get Link
Meta <http://wordpress.org/extend/plugins/get-link-meta/>`__ offers a
simple solution to get the description.

A small meta box is created on all link-editing
admin-sites:\ |image0|\ If you click the button. JS gives the link to a
simple PHP-script, which reads the information out of the wanted site
and creates an IFRAME in your Get Link Meta-Box. |image1|\ If you click
on *"Submit & Save"* , the description is copied to link-edit form and
and the link is saved to your Wordpress-DB.

The plugin is hosted by
`wordpress.org <http://wordpress.org/extend/plugins/get-link-meta/>`__.
If you have any questions ask me by commenting here.


.. |image0| image:: {static}/images/getlinkmetabox.png
   :class: aligncenter size-full wp-image-4259
   :width: 283px
   :height: 99px
   :target: {static}/images/getlinkmetabox.png
.. |image1| image:: {static}/images/getlinkmeta_description.png
   :class: aligncenter wp-image-4260
   :width: 299px
   :height: 298px
   :target: {static}/images/getlinkmeta_description.png
