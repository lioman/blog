---
Title: Filter Nextcloud News
Date: 2024-08-05 17:00
Modified: 2024-08-05 17:00
Category: Digital
Tags: nextcloud, FOSS, project, RSS, News, Python, nextcloud_news_filter, open-source
Slug: filter-nextcloud-news
Authors: Lioman
Lang: en
Translation: true
---

![Nextcloud News Filter Logo]({static}/images/nextcloud_news_filter_logo.svg){class="alignleft", style="width: 8vw"} Some time ago I have used [Newsblur](https://newsblur.com) as my RSS feed reader.
Even if I had no huge complains about this service, I migrated all my subscriptions to nextcloud.
The only feature I really missed, was the possibility to filter articles in feeds.
Advertisements, old articles in newspapers or certain topics are things I don't want to see.
Since [Nextcloud News](https://nextcloud.github.io/news/) just don't give you that option I developed a small tool to just do that.

## How does `nextcloud_news_filter` work?

`nextcloud_news_filter` connects to a configured instance of nextcloud and fetches all unread news.
Then it checks all of them, if they are matching the configured filter.
It is possible to provide regular expressions for title or body and one can check if an entry is older than a certain time.
Every filter can be tied to a certain feed.

After that all those matching articles are just marked as read and don't show up in your clients.

## How-to

Version [0.2.0](https://gitlab.com/lioman/nextcloud_news_filter/-/releases/v0.2.0) is the most recent one, during the time of writing this article.
The following description is adapted to said version and may be not valid for future versions.
The current description can be retrieved [here](https://gitlab.com/lioman/nextcloud_news_filter/-/blob/main/README.md).

### Installation and Usage

There are two modes.
One can install the program with `pipx install nextcloud_news_filter[cli]` or `pip install nextcloud_news_filter[cli]`, and can use it manually or by using a cron job.
This is good, if you operate nextcloud on your own server or have an already running Raspberry Pi (or similar).

I am using the second variant of operation.
The newest version is installed as "_Serverless-Function_" on [Scaleway](https://www.scaleway.com/en/serverless-functions/).
Mostly because I want to experiment with that technic.
Additionally, it is very cheap for me as the provided free tier is most of the time enough for me.
My setup is running `nextcloud_news_filter` every 30 min.

### Configuration

The connection to nextcloud needs to be set via environment variables.
These are:

- `NEXTCLOUD_URL` - URL of your nextcloud instance
- `NEXTCLOUD_USER` - the username
- `NEXTCLOUD_PASS` - the password

After that one need to provide the filter in JSON format.
In `skipFeeds` one can configure the IDs of Feeds, that should not be filtered.
The field `filter`, should contain a list of all your filter configurations.
These contain:

- `name`: Name of the filter. _Mandatory_
- `feedId`: Id of the Feed, this filter should be limited too. _Optional_
- `bodyRegex`: Regex matching the article body. _Optional_
- `titleRegex`: Regex matching the article title. _Optional_
- `hoursAge`: max age of the article in hours. _Optional_

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

If you want to view the source or documentation, or if you want to contribute you can find the [repository](https://gitlab.com/lioman/nextcloud_news_filter/) on Gitlab.

Issues or wishes can be created [here](https://gitlab.com/lioman/nextcloud_news_filter/-/issues).

The package itself can be retrieved via [PyPi](https://pypi.org/project/nextcloud_news_filter/) or if you need the scaleway bundle, you can download the current version: [0.2.0](https://gitlab.com/lioman/nextcloud_news_filter/-/jobs/7463888405/artifacts/download).
