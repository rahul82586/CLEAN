[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Settings Files](../Settings-Files.md) / Update

[Previous](Get.md) | [Next](Delete.md)

# Update Settings

The request allows sending a settings file to the trading server.

## Rest API

Request Format
    
    
    POST /api/setting/set?section=directory&key=file
    { Settings in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { JSON-description }
    }

The example
    
    
    //--- request to the server
    /api/setting/set?section=web&key=settings.json
    {
       "RecordID" : "100",
       "Flags" : "1",
       "Windows" : "10"
    }
    //--- server response
    {
       "retcode" : "0 Done",
       "answer" : 
         {
           "RecordID" : "100",
           "Flags" : "1",
           "Windows" : "10"
         }
    }

## Raw API

Request Format
    
    
    SETTING_SET|SECTION=directory|KEY=file|\r\n

Response Format
    
    
    SETTING_SET|RETCODE=code description|\r\n
    Settings in JSON format

## Request Parameters

  * section — the name of the subfolder in the manager account directory to which you want to write the settings file.
  * key — the name of the settings file.



The settings description is passed in JSON format as an additional body. Its structure can be arbitrary, while the only requirement is JSON validity.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. For example:


  * [3](../../../Return-Codes/Common-errors.md) — invalid parameters, for example the name of the folder or file.


  * [2008](../../../Return-Codes/Configuration-Management.md) — the [maximum number of files or folders (#limit)](Update.md#limit) has been reached.
  * [5](../../../Return-Codes/Common-errors.md) — writing the file to the disk failed.
  * answer — settings in JSON format.



## Note

  * The path to the settings file is formed as follows: [trade server directory]\settings\\[manager login]\section\key. section and key are the first and the second parameters of the request, manager login is the manager's account using which the application is [connected to the trade server](../../Authentication.md).
  * The Web API only supports JSON content.
  * Only one level of nesting and no more than 128 folders can be stored inside each manager directory. The maximum number of settings files is 1024. The size of each configuration file is no more than 16 MB.
  * The request works with files, not with individual settings. Therefore, a whole settings file needs to be formed to send changes to the server.
  * Settings should not be updated on the server too often, i.e. every time when settings are edited on the application side. After editing settings, the user can immediately change some other settings or revert changes. It is recommended to send updates not more than once in 5 minutes.


