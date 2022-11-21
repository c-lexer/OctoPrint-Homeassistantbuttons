/*
 * View model for OctoPrint-Homeassistantbuttons
 *
 * Author: Christian Lexer
 * License: AGPLv3
 */
$(function () {
    function HomeassistantbuttonsViewModel(parameters) {
        var self = this;

        self.toggle = function (device) {
            OctoPrint.simpleApiCommand("homeassistantbuttons", "toggle", { "device": device });
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: HomeassistantbuttonsViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#navbar_plugin_homeassistantbuttons", "#settings_plugin_homeassistantbuttons"]
    });
});
