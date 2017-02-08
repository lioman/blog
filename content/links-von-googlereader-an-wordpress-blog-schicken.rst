Links von GoogleReader an Wordpress-Blog schicken
#################################################
:date: 2011-12-13 14:10
:author: Lioman
:category: Internet
:tags: Blog, Google Reader, Links, Linksammlung, senden an, Wordpress
:slug: links-von-googlereader-an-wordpress-blog-schicken
:status: published

Google hat ja leider die\ `Empfehlen-Möglichkeiten stark
verändert <http://googlereader.blogspot.com/2011/10/new-in-reader-fresh-design-and-google.html>`__
und man kann im Reader leider keinem mehr einfach so folgen. Ähnliches
geht nun nur noch über Google+. Sucht man nun eine Möglichkeit Linktipps
zu verteilen, kann man dies über ein eigenes (Wordpress-)Blog
realisieren.

Wordpress verfügt von Haus aus über eine eigene Blogroll/Linkdatenbank,
man muss diese nur noch befüllen. Das ist händisch per C&P recht mühsam
und eine einfache Lösung in Verbindung mit dem GoogleReader wäre
wünschenswert.

Möchte man Links direkt aus dem Reader an das eigene Blog übertragen
muss man in den "*Reader-Einstellungen"* unter "*Senden an"* einen
*"Benutzerdefinierten Link erstellen" *

*|image0|*

In das Formular trägt man einen

-  Beliebigen Namen (z.B. Blog)
-  die URL:
   http://DEINEBLOGURL/wp-admin/link-add.php?action=popup&linkurl=${url}&name=${title}
-  und eventuell ein Icon (z.B. Link zum eigenen favicon.ico) ein und
   klickt auf speichern.

Unter jedem Artikel im Reader kann man über *"Senden an"* nun den Link
an Wordpress weiterschicken. Dabei öffnet sich ein neues Browserfenster
indem man noch fehlende Daten eintragen kann, wenn man möchte.

.. |image0| image:: {filename}/images/greader_benutzerdefinierter-link.png
   :class: wp-image-4068 aligncenter
   :width: 480px
   :height: 289px
   :target: {filename}/images/greader_benutzerdefinierter-link.png
