[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Main Interface](../Main-Interface.md) / User Settings

[Previous](Mail-Database/MailSend.md) | [Next](User-Settings/SettingsAdd.md)

# Custom Settings

The functions described in this section allow managing additional custom settings of gateways and data feeds. These settings are saved in the file settings.dat, which is created in the [working directory](../Exported-Functions/MTGatewayCreateLocal.md) of the application. The working directory is in the same directory where the executable file of the gateway or data feed is located.

> Custom settings are not associated with [configurations of gateways](../../Configuration-Interfaces/Gateways.md) and [data feeds](../../Configuration-Interfaces/Data-Feeds.md). They allow storing data in a local file.

The following functions are available for working with custom settings:

Function | Purpose  
---|---  
[SettingsAdd](User-Settings/SettingsAdd.md) | Add a setting.  
[SettingsUpdate](User-Settings/SettingsUpdate.md) | Change a setting by its position and name.  
[SettingsDelete](User-Settings/SettingsDelete.md) | Delete a setting by its position and name.  
[SettingsClear](User-Settings/SettingsClear.md) | Delete all settings.  
[SettingsTotal](User-Settings/SettingsTotal.md) | Get the number of settings.  
[SettingsNext](User-Settings/SettingsNext.md) | Get a setting by its position.  
[SettingsGet](User-Settings/SettingsGet.md) | Get a setting by its name.
