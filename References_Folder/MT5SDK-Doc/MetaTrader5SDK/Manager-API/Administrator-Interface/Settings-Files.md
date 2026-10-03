[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Administrator Interface](../Administrator-Interface.md) / Settings Files

[Previous](Tick-Data/TickReplace.md) | [Next](Settings-Files/SettingGet.md)

# Settings Files

The Manager API allows saving application settings on a trade server and accessing them at any time. Settings are stored in a special directory separately for each manager account, which uses the application: [trade server directory]\settings\\[manager login]\\.

This option allows you to quickly configure the manager's workplace. For example, if the manager changes the computer, there will be no need to re-configure the application. Instead, you can easily apply settings, which were saved previously on the trade server. It is also possible to create several sets of manager settings for performing certain tasks.

  * Only one level of nesting and no more than 128 folders can be stored inside each manager directory. The maximum number of settings files is 1024. The size of each configuration file is no more than 16 MB.
  * Settings are saved and accessed on the server, to which the Manager API application is connected (on which the connected manager account is located). If you have multiple servers, you need to save the settings on each server.
  * This function is secure for the trade server: the Manager API does not allow sending potentially dangerous file types to the server (for example, *.exe). Only files with the following extensions are allowed: ini, cfg, dat, json, config, sqlite, xml, conf, settings, key, db, txt and log, as well as files without extensions.

  
---  
  
## The General Scheme of working with settings

Settings are stored in a special directory of the trade server: [trade server directory]\settings\\[manager login]\\.

  * The application receives the file with settings using the [IMTAdminAPI::SettingGet](Settings-Files/SettingGet.md) method. For example, during the application launch or when the user executes an appropriate command.
  * The settings are read from the file and applied.
  * If the user edits settings during the application operation, the application can update the settings file on the trade server via the [IMTAdminAPI::SettingSet](Settings-Files/SettingSet.md) method.



Please note that settings comprise one whole file. You cannot update a separate setting on the server. To update a setting, it is necessary to generate a whole file with all settings. The format of the settings file and its parsing methods are determined by the file creator. IMTAdminAPI::Setting* methods work with arbitrary data.

Settings should not be updated on the server too often, i.e. every time when settings are edited on the application side. After editing settings, the user can immediately change some other settings or revert changes. It is recommended to send updates not more than once in 5 minutes.

Several applications can work with the same settings files. The Manager API does not track changes in files on the server side. Every call of [IMTAdminAPI::SettingSet](Settings-Files/SettingSet.md) re-writes the specified settings file, even if it has already been changed by another application. Only the last submitted version is always stored on the server.

## Functions for working with the settings files

The function | Purpose  
---|---  
[SettingGet](Settings-Files/SettingGet.md) | Receives the settings file from the trade server.  
[SettingSet](Settings-Files/SettingSet.md) | Sends the settings file to the trade server.  
[SettingDelete](Settings-Files/SettingDelete.md) | Deletes the settings file on the trade server.
