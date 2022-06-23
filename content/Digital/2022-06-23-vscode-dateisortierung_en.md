---
Title: VSCode File Order
Date: 2022-06-23 16:39
Modified: 2022-06-23 17:40
Category: Digital
Tags: open-source, blogging, vscode, writing, foss
Slug: vscode-dateisortierung
Authors: Lioman
Status: Published
Lang: en
Translation: true
---

Most of the time I use VSCode as IDE and additionally to write this blog.
The thing that is really annoying is the fact, that it is not possible to set the order to 'descending' in file explorer.
In my last post, I've described, how to [rename]({filename}/Allgemein/2022-05-26-pelican-artikel-verschieben.md) all files.
After doing this on all blog posts, I got a neat list, and theoretically it can be sorted quite well.
In a terminal application or in the file manager of your system this works in VSCode it does not.
There is an option to change the order to 'last modified' but this results in a rather chaotic list.
![VSCode file explorer sort order 'last modified']({static}/images/screenshot_file_explorer_vscode.png)

Changing this to reversed order is not possible and this is why I created an [issue](https://github.com/microsoft/vscode/issues/149951) on GitHub and implemented the functionallity as well and raised a [PR](https://github.com/microsoft/vscode/pull/149952).
Since there are more than 500 issues open, mine will be closed if there are not more then 20 upvotes. In the time of writing this article, the issue has 10 up votes, so I hope that some of you are interested in this feature as well.
Please react with 'thumbs up' on the issue, as in my opinion it would not help only me.
