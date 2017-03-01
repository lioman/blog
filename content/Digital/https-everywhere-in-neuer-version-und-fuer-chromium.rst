HTTPS Everywhere in neuer Version und für Chromium
##################################################
:date: 2012-04-23 16:15
:author: Lioman
:category: Digital
:tags: Open Source, Add-on, Erweiterung, firefox, https, Sicherheit, Verschlüsselung, UbuntuusersPlanet
:slug: https-everywhere-in-neuer-version-und-fuer-chromium
:status: published

| `HTTPS Everywhere <https://www.eff.org/https-everywhere>`__ ist für
  mich eine absolute Must-Have-Erweiterung für den Firefox-Browser.
  |image0|\ Sie nistet sich oben in der Leiste ein und sorgt anhand
  `tausender <https://gitweb.torproject.org/https-everywhere.git/tree/HEAD:/src/chrome/content/rules>`__
  Regeln dafür, dass (falls verfügbar) nur die verschlüsselte Seite
  aufgerufen wird. Das erhöht die Sicherheit deutlich, denn so können
  nicht so einfach Passwörter und Nutzerdaten abgegriffen werden. Der
  Name ist leider ein bisschen irreführend, denn HTTPS gibt es eben
  nicht überall, sondern nur für Domains die
  `https <https://de.wikipedia.org/wiki/HTTPS>`__ überhaupt anbieten und
  auch durch ein "Ruleset" definiert sind (Was man jedoch sehr einfach
  auch selbst hinzufügen kann).
| Die neuste Version ([STRIKEOUT:2.0.2] 2.0.3) gilt als stabil und
  enthält keine neuen Funktionalitäten, sondern beschränkt sich auf
  einige Bugfixes..
| Neu ist jedoch eine Beta-Version für Chromium/Google Chrome, denn
  derzeit gab es noch keine Erweiterung, die ähnliches wie HTTPS
  Everywhere bewerkstelligen konnte. `KB SSL
  Enforcer <https://chrome.google.com/extensions/detail/flcpelgcagfhfoegekianiofphddckof?hl=en>`__
  soll laut EFF nicht können, da http vor https genutz wird. Sicherheit
  ist nur gewährleistet, wenn alles **nur**\ über eine verschlüsselte
  Verbindung geladen wird. Wie immer sind solche Betas mit vorsicht zu
  genießen, da sie noch nicht vollkommen fertig sind und daher auch noch
  nicht 100%ig stabil funktionieren.

.. |image0| image:: {filename}/images/httpseverywhere_icon.jpg
   :class: alignright size-full wp-image-4495
   :width: 71px
   :height: 60px
   :target: {filename}/images/httpseverywhere_icon.jpg
