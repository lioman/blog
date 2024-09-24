---
Title: Endlich gemerged - VSCode kann umgekehrt sortieren
Date: 2024-09-23 18:54
Modified: 2024-09-24 17:00
Category: Digital
Tags: vscode, FOSS, open-source, IDE
Slug: endlich-gemerged-vscode-kann-umgekehrt-sortieren
Authors: Lioman
Status: Published
Summary: Vor einiger Zeit habe ich ein Issue auf Github erstellt, um den _Visual Studio Code_ um eine kleine Verbesserung zu erweitern. Fast in jedem Dateimanager unter so ziemlich jedem OS, kann man die Sortierreihenfolge einfach umdrehen. In VSCode ging das nicht.
---

Vor einiger Zeit habe ich ein [Issue](https://github.com/microsoft/vscode/issues/149951) auf Github erstellt,
um den _Visual Studio Code_ um eine kleine Verbesserung zu erweitern.
Fast in jedem Dateimanager unter so ziemlich jedem OS, kann man die Sortierreihenfolge einfach umdrehen.
In VSCode ging das nicht.
Was, gerade wenn man die IDE auch zum Schreiben eines Blogs benutzen möchte ziemlich unpraktisch ist,
denn aktuelle Inhalte sind dann immer ganz unten im Verzeichnisbaum.
Die Implementierung habe ich gleich selbst erledigt und am 19. Mai 2022
einen [PR](https://github.com/microsoft/vscode/pull/149952) erstellt.
Es gab am Code selbst keine Einwände, aber gemerged wurde erst mal trotzdem nicht.
Immer wieder habe ich den _Branch_ aktualisiert und nachgefragt, was fehlt.
Ende Juli dieses Jahres, also mehr als zwei Jahre später, wurde mein Feature endlich integriert.

In den Release Notes der [Version 1.93](https://code.visualstudio.com/updates/v1_93#_reverse-sort-in-explorer)
kann man endlich folgendes lesen:

> Reverse sort in Explorer
>
> We added an additional sort option, explorer.sortOrderReverse,
> which enables you to reverse any of the various Explorer sort configurations, providing further sorting flexibility.

![VSCode-Fileexplorer sortiert in umgekehrter Reihenfolge]({static}/images/vscode_reverse_order.png){class="alignleft" width="300px"}
Um dieses Blog zu schreiben, habe ich in den _Workspace_-Einstellungen, die Sortierung auf _filesFirst_ gestellt und die Sortierung mit der neuen Funktion invertiert.
So habe ich eine Liste aller Ordner und danach alle Artikel mit absteigender Aktualität.

Dass ein Beitrag zu einem (großen) FOSS-Projekt mal etwas länger geht, ist erwartbar. Dass allerdings so viel Zeit ins Land geht, empfand ich doch als anstrengend.
