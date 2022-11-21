# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from requests import post


class HomeassistantbuttonsPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.SimpleApiPlugin,
):
    ##~~ SimpleApiPlugin mixin

    def get_api_commands(self):
        return dict(toggle=["device"])

    def on_api_command(self, command, data):
        if command == "toggle":
            post(
                self._settings.get(["url"]) + "/api/services/switch/toggle",
                json={
                    "entity_id": self._settings.get(["lightsid"])
                    if data["device"] == "lights"
                    else self._settings.get(["printerid"])
                },
                headers={"Authorization": "Bearer " + self._settings.get(["token"])},
                timeout=5,
            )

    ##~~ TemplatePlugin mixin

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False),
        ]

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(url=None, token=None, lightsid=None, printerid=None)

    ##~~ AssetPlugin mixin

    def get_assets(self):
        return {
            "js": ["js/homeassistantbuttons.js"],
            "css": ["css/homeassistantbuttons.css"],
            "less": ["less/homeassistantbuttons.less"],
        }

    ##~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "homeassistantbuttons": {
                "displayName": self._plugin_name,
                "displayVersion": self._plugin_version,
                # version check: github repository
                "type": "github_release",
                "user": "c-lexer",
                "repo": "OctoPrint-Homeassistantbuttons",
                "current": self._plugin_version,
                # update method: pip
                "pip": "https://github.com/you/OctoPrint-Homeassistantbuttons/archive/{target_version}.zip",
            }
        }


__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = HomeassistantbuttonsPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
