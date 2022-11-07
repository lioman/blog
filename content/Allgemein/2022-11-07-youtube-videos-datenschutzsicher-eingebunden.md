---
Title: Youtube-Videos datenschutzsicher eingebunden
Date: 2022-11-07 17:00
Modified: 2022-11-07 17:00
Category: Allgemein
Tags: GDPR, Datenschutz, blog, pelican, youtube
Slug: youtube-videos-datenschutzsicher-eingebunden
Authors: Lioman
Status: Published
---

YouTube-Videos waren hier bisher mit dem Plugin [pelican-youtube](https://pypi.org/project/pelican-youtube/)
eingebunden.
Mit diesem Plugin gab es zwar immerhin den no-cookie Modus, bei dem keine Cookies gesetzt werden.
Allerdings gibt es immer noch zwei Probleme:

- Es wird der Javascript-Player geladen
- Dieser bindet GoogleFonts ein

Deswegen habe ich hier nun die Implementierung geändert und setze jetzt auf [liquid-tags](https://github.com/pelican-plugins/liquid-tags).
Dieses Plugin bietet neben mehr Flexibilität im Allgemeinen auch einen Modus für YouTube,
bei dem nur das Vorschaubild angezeigt wird.

Streng genommen hat man so das eingebundene Video durch einen Link ersetzt,
aber so muss man sich hier nicht darum kümmern irgendwelche Banner auftauchen zu lassen.

Das Ganze könnte man noch verbessern, indem man entweder das Vorschaubild selbst ausliefert und/oder
den Link durch eine [Invidious](https://invidious.io/)-Instanz zu ersetzen.

Mit etwas CSS bekommt man auch noch einen schicken Knopf, der direkt zum Video führt.

```css
.youtube_video {
    margin: 0 auto;
    text-align: center;
    position: relative;
    display: inline-block;
}

.youtube_video::before {
    font-family: "Font Awesome 6 Free";
    content: "\f144";
    font-size: 5em;
    padding: .05em .2em;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    z-index: 99;
}

.youtube_video:hover::before {
    filter: invert();
}

.youtube_video::after {
    content: "Das Video auf YouTube abspielen.";
    font-size: 0.9em;
    padding: .05em .2em;
    position: absolute;
    left: 50%;
    top: 70%;
    transform: translate(-50%, -50%);
    z-index: 99;
}

.youtube_video:hover::after {
    filter: invert();
    text-decoration: underline;
}

.youtube_video>img {
    object-fit: cover;
}
```

{% youtube Ppz07UQxlEc %}
