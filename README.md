# boxwich

Sandwiches delivered with the push of a button.

![The box](http://jonjonsonjr.github.io/boxwich/img/gh_box.jpg)

## Background

This daemon was part of our project at [HackNC 2014](http://hacknc.us/),
the [boxwich](https://github.com/jonjonsonjr/boxwich), which won 3rd place overall as well as the sponsor's choice awards from
[Mailjet](https://www.mailjet.com/) and
[Digital Ocean](https://www.digitalocean.com/).

We wanted to make something that solved a serious problem: deciding what to eat.
With the boxwich, you don't have to worry about where to go or what to order,
you just have to press the button! The boxwich will randomly select a sandwich
from Jimmy John's and have it delivered to you!

The switch acts as a safety mechanism, so you have to flip it to arm the box
before it will work. We had several people just come up and immediately push
the button during HackNC, so it was very useful.



This daemon runs on a Raspberry Pi to take user input through the boxwich and send HTTP requests to order Jimmy John's sandwiches via a Node.js [app](https://github.com/jonjonsonjr/boxwich) written by [Jon Johnson](https://github.com/jonjonsonjr).
