---
Title: Datenschutz erhöhen - Invidious für alle YouTube-Videos im Blog
Date: 2022-12-05 17:39
Modified: 2022-12-05 17:39
Category: Digital
Tags: datenschutz, youtube, pelican, plugins, foss, open-source
Slug: datenschutz-erhoehen-invidious-fuer-alle-youtube-videos-im-blog
Authors: Lioman
Status: Published
---

In meinem letzten [Artikel]({filename}/Allgemein/2022-11-07-youtube-videos-datenschutzsicher-eingebunden.md),
habe ich erst darüber geschrieben, dass ich YouTube-Videos hier besser eingebunden habe.
Schon da merkte ich an, dass man das noch verbessern könnte, indem man nicht direkt Youtube verlinkt,
sondern eine [Invidious-Instanz](https://invidious.io).
[liquid-tags](https://pypi.org/project/pelican-liquid-tags/) erlaubte das aber (bisher) nicht,
deshalb habe ich das Plugin erweitert.
Installiert man nun eine Version >=1.0.4 kann man in seiner `pelicanconf.py`
die Variable `YOUTUBE_INVIDIOUS_INSTANCE` setzen.
Alle Thumbnails und Videos werden dann von dort eingebunden.
Hier im Blog habe ich derzeit die Variable wie folgt gesetzt:

```python
YOUTUBE_INVIDIOUS_INSTANCE = "https://invidious.tiekoetter.com"
```

Und der Link führt nicht mehr direkt auf youtube, sondern wird eben, wie konfiguriert ersetzt:

{% youtube DjiE1rC99dk %}

Eine Liste öffentlicher Instanzen gibt es [hier](https://docs.invidious.io/instances/)
