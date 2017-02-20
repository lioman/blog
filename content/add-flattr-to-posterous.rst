Add Flattr to Posterous
#######################
:date: 2011-05-12 12:11
:author: Lioman
:category: Internet
:tags: Anleitung, Button, Flattr, HowTo, Posterous, Theme
:slug: add-flattr-to-posterous
:status: published

|image0|\ There are many Plugins an HowTos to include Flattr to
different webservices and platforms.

Here is the HowTo for `Posterous.com: <http://posterous.com/>`__

To enlarge pictures click on it!

-  Login to your posterous Account and click on "*Settings"*! And then
   on Customize in the gearwheel-menu behind your posterous space
   |image1|
-  Then first choose your prefered theme (I choose Dakhar) and then
   click on *"Advanced"*
   |image2|
-  Click on *"Enable advanced theming"* and give your new theme a name
   |image3|
-  Click on Expand to view theme-code
   |image4|
-  Scroll to {block:Tweet /} or to any other place wherever you want
   your button
   |image5|
-  Add Button CodeNormal:

  .. code:: html

   <iframe src= "http://api.flattr.com/button/view/?uid=lioman&amp;url={Permalink}&amp;title={Title}&amp;description=Posterous post&amp;language=de_DE&amp;tags={block:TagList}{block:TagListing}{TagName},{/block:TagListing}{/block:TagList}" frameborder="0" scrolling="no" width="55px" height="62px"></iframe>

   **Update: Don't use compact mode! Webkit-Browser don't show it
   properly. Use the default code or resize (much bigger) the iframe if
   you have to use the compact button.**

   Compact:

   .. code:: html

   <iframe src= "http://api.flattr.com/button/view/?uid=lioman&amp;url={Permalink}&amp;title={Title}&amp;button=compact&amp;description=Posterous post&amp;language=de_DE&amp;tags={block:TagList}{block:TagListing}{TagName},{/block:TagListing}{/block:TagList}" frameborder="0" scrolling="no" width="55px" height="62px"></iframe>

   | **Change the *"uid"* to your Flattr-ID (or I get the reward :-) )**
   | Change category  to your preferred type: text, images, video,
     audio, software, rest

-  Preview your theme and if everything looks nice -  save it !
   |image6|

 

Everything is done and your readers can flattr your Posterousblog

**Update7:** Image and description updatet on new posterous design

**Update6:** Code Updated, Tags are now supported!

| **Update5:** It seems that Posterous changed the way the how the title
  is displayed. You have to change the code back to previous version.
  "{TitleCssEscaped}" must be replaced by "{Title}"
| **Update4:** Code updated! Titels with additional characters like "#"
  are now supported
| **Update3:** Code updated there has to be an space after *src=*
| **Update2:** Everything works fine with default button.
| **Update:** Code dosen't work for Chrome/Chromium. Wegkit-browsers
  ignore the scrolling= no attribute. I try to improve that.
| |Share_on_Posterous|

.. |image0| image:: {filename}/images/posterous2flattr.jpg
   :class: size-full wp-image-3214 alignright
   :width: 200px
   :height: 99px
   :target: {filename}/images/posterous2flattr.jpg
.. |image1| image:: {filename}/images/posterousnewsettings-300x158.jpg
   :class: aligncenter size-medium wp-image-3802
   :width: 300px
   :height: 158px
   :target: {filename}/images/posterousnewsettings.jpg
.. |image2| image:: {filename}/images/posterous2flattr02-300x207.png
   :class: aligncenter size-medium wp-image-3198
   :width: 300px
   :height: 207px
   :target: {filename}/images/posterous2flattr02.png
.. |image3| image:: {filename}/images/posterous2flattr03-300x207.png
   :class: aligncenter size-medium wp-image-3199
   :width: 300px
   :height: 207px
   :target: {filename}/images/posterous2flattr03.png
.. |image4| image:: {filename}/images/posterous2flattr04-300x207.png
   :class: aligncenter size-medium wp-image-3201
   :width: 300px
   :height: 207px
   :target: {filename}/images/posterous2flattr04.png
.. |image5| image:: {filename}/images/posterous2flattr05-300x207.png
   :class: aligncenter size-medium wp-image-3202
   :width: 300px
   :height: 207px
   :target: {filename}/images/posterous2flattr05.png
.. |image6| image:: {filename}/images/posterous2flattr06-300x207.png
   :class: aligncenter size-medium wp-image-3203
   :width: 300px
   :height: 207px
   :target: {filename}/images/posterous2flattr06.png
.. |Share_on_Posterous| image:: http://posterous.com/images/share/share_posterous.png
   :target: http://posterous.com/share?linkto=http://www.lioman.de/add-flattr-to-posterous/
