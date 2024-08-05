---
Title: Filter Nextcloud News
Date: 2024-08-05 17:00
Modified: 2024-08-05 17:00
Category: Digital
Tags: nextcloud, FOSS, project, RSS, News, Python, nextcloud_news_filter, open-source
Slug: filter-nextcloud-news
Authors: Lioman
---

![Nextcloud News Filter Logo]({static}/images/nextcloud_news_filter_logo.svg){class="alignleft", style="width: 8vw"} Vor einiger Zeit habe ich [Newsblur](https://newsblur.com) als RSS-Feedreader genutzt.
Auch wenn ich nicht viel an dem Dienst auszusetzen hatte,
habe ich alle Abonnements auf eine Nextcloud-Instanz umgezogen.
Das einzige Feature, das ich wirklich vermisst habe, ist die Möglichkeit die vielen RSS-Feeds zu filtern.
Hat man viele Feeds abonniert, wird es schnell unübersichtlich.
Beispiele für Dinge, die ich nicht mehr sehen möchte, sind ältere Artikel von online Zeitungen, Werbung oder einfach bestimmte Themen.
[Nextcloud News](https://nextcloud.github.io/news/) bietet diese Möglichkeit einfach nicht und so habe ich ein kleines Tool entwickelt, um genau das zu tun.

## Was macht `nextcloud_news_filter`?

`nextcloud_news_filter` verbindet sich mit der konfigurierten Nextcloud-Instanz und holt sich alle ungelesenen Artikel. Dann geht es durch alle Artikel durch und schaut, ob es zu einem Filter passt.
Konfigurieren kann man reguläre Ausdrücke für den Titel und den Text, außerdem kann man schauen, ob ein Artikel älter als eine bestimmte Zeit ist.
Jeden Filter kann man zudem auf einen definierten Feed begrenzen.

Danach werden alle zu Filter passenden Artikel einfach als gelesen markiert und tauchen so erstmal nicht mehr in den entsprechenden Clients auf.

## Anleitung

Zum Zeitpunkt des Erscheinens diese Artikels, ist `nextcloud_news_filter` in der Version [0.2.0](https://gitlab.com/lioman/nextcloud_news_filter/-/releases/v0.2.0) verfügbar.
Die folgende Anleitung ist daran angepasst und mag für zukünftige Versionen nicht mehr gültig sein. Eine aktuelle Beschreibung auf Englisch befindet sich [hier](https://gitlab.com/lioman/nextcloud_news_filter/-/blob/main/README.md).

### Installation und Benutzung

Es gibt zwei mögliche Modi, um das Filterprogramm zu nutzen.
Installiert man das Programm mit `pipx install nextcloud_news_filter[cli]` oder `pip install nextcloud_news_filter[cli]` kann man neben der händischen Nutzung einen Cronjob erstellen. Das geht gut, wenn man Nextcloud auf einem eigenen Server installiert hat oder eh einen Raspberry Pi oder ähnliches läuft.

Ich benutze Variante zwei und installiere die aktuellste Version als "_Serverless-Function_" auf [Scaleway](https://www.scaleway.com/en/serverless-functions/).
Hauptsächlich, um mit damit zu experimentieren.
Zudem ist es vergleichsweise günstig, denn Scaleway bietet ein kostenloses Budget an Ressourcen an.
Diese überschreite ich derzeit mit einem Aufruf alle 30 min nicht (oder nur selten).

### Konfiguration

Die Verbindung zu Nextcloud muss über Umgebungsvariablen gesteuert werden.
Dazu setzt man

- `NEXTCLOUD_URL` - Die URL der Nextcloud-Instanz
- `NEXTCLOUD_USER` - Der Nutzername
- `NEXTCLOUD_PASS` - Das Passwort

Dann muss man noch die Filter im JSON-Format konfigurieren.
In `skipFeeds` kann man IDs von Feeds konfigurieren, die man von allen Filtern ausschließen möchte.
Unter `filter` konfiguriert man dann die eigentlichen Filter.
Diese bestehen aus:

- `name`: Name des Filters. _Obligatorisch_
- `feedId`: Id des Feeds auf den dieser Filter beschränkt werden soll. _Optional_
- `bodyRegex`: Regex die den Text des Artikels durchsucht. _Optional_
- `titleRegex`: Regex die nur den Titel betrachtet. _Optional_
- `hoursAge`: maximales alter des Artikels in Stunden. _Optional_

```json
{
  "skipFeeds": [
    1678, 1683, 1681, 1682, 1684, 1680, 1659, 1654, 1658, 1657, 1656, 1660, 1655
  ],
  "filter": [
    {
      "name": "heise+",
      "feedId": 1592,
      "titleRegex": "heise\\+|heise\\-Angebot|TechStage"
    },
    {
      "name": "All with Advertisement in Body",
      "feedId": 1594,
      "bodyRegex": "^Advertisement: "
    },
    {
      "name": "Feed older than one day, for feed 1595",
      "feedId": 1595,
      "hoursAge": 24
    },
    {
      "name": "all > 20 Days all feeds (except for skipped ones)",
      "hoursAge": 480
    }
  ]
}
```

### Links

Wer sich die Quelle bzw. Dokumentation anschauen möchte oder eventuell sogar etwas beitragen kann, findet das [Repository](https://gitlab.com/lioman/nextcloud_news_filter/) auf Gitlab.

Fehler oder Wünsche können [hier](https://gitlab.com/lioman/nextcloud_news_filter/-/issues) erstellt werden.

Installation erfolgt am besten über [PyPi](https://pypi.org/project/nextcloud_news_filter/) oder man kann sich das Scaleway Bundle der aktuellen Version [0.2.0](https://gitlab.com/lioman/nextcloud_news_filter/-/jobs/7463888405/artifacts/download) holen.
