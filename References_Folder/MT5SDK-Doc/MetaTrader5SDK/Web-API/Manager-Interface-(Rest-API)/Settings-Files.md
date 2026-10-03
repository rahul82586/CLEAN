[🏠 Document Start](../../README.md) / [Web API](../README.md) / [Manager Interface (Rest API)](../Manager-Interface-(Rest-API).md) / Settings Files

[Previous](Daily-Reports/Get-Light.md) | [Next](Settings-Files/Get.md)

# Settings Files

The Web API allows saving application settings on a trade server and accessing them at any time. Settings are stored in a special directory separately for each manager account, which uses the API: [trade server directory]\settings\\[manager login]\\.

This option enables quickly setup of the manager's workplace. For example, if the manager changes the computer, there will be no need to re-configure the web-application. Instead, you can easily apply settings, which were saved previously on the trade server. It is also possible to create several sets of manager settings for performing certain tasks.

  * Only one level of nesting and no more than 128 folders can be stored inside each manager directory. The maximum number of settings files is 1024. The size of each configuration file is no more than 16 MB.
  * Settings are saved and accessed on the server, to which the Web API client is connected (on which the connected manager account is located). If you have multiple servers, you need to save the settings on each server.
  * This function is secure for the trade server: the Web API does not allow sending potentially dangerous file types to the server (for example, *.exe). Only files with the following extensions are allowed: ini, cfg, dat, json, config, sqlite, xml, conf, settings, key, db, txt and log, as well as files without extensions. Furthermore, the content can only be represented as a JSON document.


  * The Web API allows you to receive configuration files which were set via the [Manager API](../../Manager-API/Manager-Interface/Settings-Files.md), but only if the file contents are a JSON document.

  
---  
  
## The General Scheme of operations with the settings

Settings are stored in a special directory of the trade server: [trade server directory]\settings\\[manager login]\\.

  * A web application can receive the settings file via the [/api/setting/get](Settings-Files/Get.md) request. For example, during the application launch or when the user executes an appropriate command.
  * The settings are read from the file and applied.
  * If the user edits settings during the application operation, the application can update the settings file on the trade server via the [/api/setting/set](Settings-Files/Update.md) method.



Please note that settings comprise one whole file. You cannot update an individual setting on the server. To update a setting, it is necessary to generate a whole file with all settings. For the Web API, file contents can only be a valid JSON document.

Settings should not be updated on the server too often, i.e. every time when settings are edited on the application side. After editing settings, the user can immediately change some other settings or revert changes. It is recommended to send updates not more than once in 5 minutes.

Several applications can work with the same settings files, including different types of APIs. The Web API does not track changes in files on the server side. Every call of [/api/setting/set](Settings-Files/Update.md) rewrites the specified settings file, even if it has already been changed by another application. The server always stores the last submitted version.

## Requests for working with the settings files

Request | Purpose  
---|---  
[/api/setting/get](Settings-Files/Get.md) | Receive the settings file from the trade server.  
[/api/setting/set](Settings-Files/Update.md) | Send the settings file to the trade server.  
[/api/setting/delete](Settings-Files/Delete.md) | Delete the settings file on the trade server.
