---
Title: Konsolentipps #002 Alle Dateien eines Typs bearbeiten
Date: 2010-11-18 18:01
Author: lioman
Category: digital
Tags: konsolentipps, linux, schleife, terminal
Slug: konsolentipps-002-alle-dateien-eines-typs-bearbeiten
Status: published
Series: konsolentipps
---

![Konsole]({static}/images/Konsole-300x213.png){class="alignright"}
Es kommt immer mal wieder vor, dass man alle Dateien eines Typs in einem Ordner bearbeiten muss.

Das geht mit folgender Schleife

```bash
for i in *.dateiendung; do IrgendeinBefehl $i;done
```

Möchte man zum Beispiel alle FLAC in Ogg konvertieren geht das so:

```bash
for i in *.flac; do oggconvert $i;done
```
