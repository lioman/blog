---
Title: VSCode Dateisortierung
Date: 2022-06-23 16:39
Modified: 2022-06-23 17:40
Category: Digital
Tags: open-source, blogging, vscode, schreiben, foss
Slug: vscode-dateisortierung
Authors: Lioman
Status: Published
<!--Summary: a summary-->
---

Ich nutze hauptsächlich VSCode als IDE und auch zum Schreiben dieses Blogs.
Was mich wirklich stört, dass ich im Explorer die Dateien nicht absteigend sortieren kann.
Im letzten Artikel habe ich beschrieben, wie man alle Dateien im Blog [umbenennt]({filename}/Allgemein/2022-05-26-pelican-artikel-verschieben.md).
Nachdem ich das mit allen Artikeln in meinem Blog getan habe,
habe ich eine schöne Liste an Dateien, die sich theoretisch gut sortieren lassen.
In der Konsole und dem Dateimanager des Systems geht das natürlich sehr gut, in VSCode leider nicht.
Es gibt zwar die Option nach letzter Modifizierung zu sortieren, das führt aber eher zu einer chaotischen Liste.
![VSCode-Fileexplorer sortiert nach 'modifiziert']({static}/images/screenshot_file_explorer_vscode.png)

Nach Dateinamen in umgekehrter Reihenfolge zu sortieren, ist bedauerlicherweise nicht möglich.
Deshalb habe ich ein [Github Issue](https://github.com/microsoft/vscode/issues/149951) geöffnet und die entsprechende Funktion gleich implementiert und einen [PR](https://github.com/microsoft/vscode/pull/149952) gestellt.
Derzeit sind allerdings mehr als 5000 Tickets offen und mein Ticket wird deshalb automatisch geschlossen, wenn es nicht entsprechend viele "Upvotes" bekommt.
Es müssen insgesamt 20 sein und derzeit sind es 10.
Ich hoffe, dass hier ein paar Interessierte mitlesen und auch einen Daumen hoch da lassen.
Das würde, davon bin ich überzeugt nicht nur mir helfen.
