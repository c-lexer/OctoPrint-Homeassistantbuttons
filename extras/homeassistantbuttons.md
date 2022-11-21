---
layout: plugin

id: homeassistantbuttons
title: OctoPrint-Homeassistantbuttons
description: Adds two buttons to navbar, allowing toggling of two Home Assistant entities.
authors:
- Christian Lexer
license: AGPLv3

date: 2022-11-21

homepage: https://github.com/c-lexer/OctoPrint-Homeassistantbuttons
source: https://github.com/c-lexer/OctoPrint-Homeassistantbuttons
archive: https://github.com/c-lexer/OctoPrint-Homeassistantbuttons/archive/master.zip


tags:
- control
- homeassistant
- power
- lights

# TODO
# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
screenshots:
- url: /assets/img/buttons.png
  alt: screencap of extra buttons
  caption: Extra buttons

# TODO
featuredimage: /assets/img/buttons.png

# TODO
# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:
  octoprint:
  - 1.4.0

  python: ">=3,<4"

---

Adds two buttons to navbar, allowing toggling of two Home Assistant entities. Not very sophisticated, but does the job for my specific use-case (two smart outlets controlling lights/printer toggled via Home Assistant)
