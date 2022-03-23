Facebook Like und Share blockieren
##################################
:date: 2010-11-29 18:22
:author: Lioman
:category: Digital
:tags: Blockieren, Datenschutz, Erweiterung, Facebook, Privatsphäre, Sicherheit
:slug: facebook-like-und-share-blockieren
:status: published

Überall im Netz tauchen die Like und Share-Knöpfe des Sozialen
Netzwerkes Facebook auf. Und das ist problematisch, denn mit diesen
können die Datensammler sehr genau sagen, welche Seiten man ansurft - ob
man in FB eingeloggt ist oder nicht. Obwohl ich das Netzwerk selbst
nutze möchte ich eigentlich immer die Kontrolle darüber haben, welche
Daten ich dort veröffentliche und an die Server schicke. Deswegen blocke
ich Facebook ab jetzt überall - außer auf Facebook.

Für Chromium/Chrome gibt es die netter Erweiterung `Facebook
Disconnect <https://chrome.google.com/extensions/detail/ejpepffjfmamnambagiibghpglaidiec>`__

Surft man meistens mit dem Firefox ist es einfacher einen Filter in
`AdblockPlus <https://addons.mozilla.org/en-US/firefox/addon/1865/>`__
einzustellen.

Einfach folgende Zeilen eintragen:

::

    ||fbcdn.net$domain=~www.facebook.com

    ||facebook.net$domain=~www.facebook.com

    ||facebook.com$domain=~www.facebook.com
