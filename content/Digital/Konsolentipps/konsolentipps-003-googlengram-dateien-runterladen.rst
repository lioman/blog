Konsolentipps #003: GoogleNgram-Dateien runterladen
###################################################
:date: 2010-12-21 14:45
:author: Lioman
:category: Digital
:tags: Bücher, GoogleNgram, Konsole, Konsolentipps, Linux, Ngram, Statistik
:slug: konsolentipps-003-googlengram-dateien-runterladen
:status: published

| Bei
  `Commandlinefu <http://www.commandlinefu.com/commands/view/7363/download-all-data-from-google-ngram-viewer>`__
  habe ich einen Befehl entdeckt, wie man die Daten des wirklich
  interessanten Tool GoogleNgram runterladen kann.
| Möchte man nicht gleich alle, sondern nur die in einer bestimmten
  Sprache, auf den heimischen Rechner ziehen möchte hilft folgender
  Befehl:

::

    wget -qO - http://ngrams.googlelabs.com/datasets | grep -E href='(.+ger.+\.zip)' | sed -r "s/.*href='(.+ger.+\.zip)'.*/\1/" | uniq | while read line; do echo $line >> liste.txt; done && wget -i liste.txt && rm liste.txt

Nun wird der komplette Datensatz in Deutsch runtergeladen. Möchte man
andere Sprachen haben muss man sich die Links auf der
`Ngram-Datasetseite <http://ngrams.googlelabs.com/datasets>`__ anschauen
und die beiden "ger" durch die gewünschte Sprache ersetzen (z.B. "fra"
für Französisch)
