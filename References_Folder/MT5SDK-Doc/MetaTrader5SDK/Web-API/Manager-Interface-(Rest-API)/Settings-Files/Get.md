[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Settings Files](../Settings-Files.md) / Get

[Previous](../Settings-Files.md) | [Next](Update.md)

# Get Settings

The request allows receiving a settings file from the trading server.

## Rest API

Request Format
    
    
    GET /api/setting/get?section=directory&key=file
    POST /api/setting/get?section=directory&key=file

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { JSON-description }
    }

The example
    
    
    //--- request to the server
    /api/setting/get?section=web&key=settings.json
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
    
    
    SETTING_GET|SECTION=directory|KEY=file|\r\n

Response Format
    
    
    SETTING_GET|RETCODE=code description|\r\n
    Settings in JSON format

## Request Parameters

  * section — the name of the subfolder in the manager account directory, from which you want to receive the settings file.
  * key — the name of the settings file.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. For example:


  * [3](../../../Return-Codes/Common-errors.md) — invalid parameters, for example the name of the folder or file.
  * [13](../../../Return-Codes/Common-errors.md) — the requested file is not found.
  * [6](../../../Return-Codes/Common-errors.md) — not enough memory to receive the file.
  * answer — settings in JSON format.



## Note

  * The path to the settings file is formed as follows: [trade server directory]\settings\\[manager login]\section\key. section and key are the first and the second parameters of the request, manager login is the manager's account using which the application is [connected to the trade server](../../Authentication.md).
  * The Web API only supports JSON content. If the file contents are of a different format (for example if the manager was created via [Manager API](../../../Manager-API/Manager-Interface/Settings-Files.md)), an empty field will be returned in the answer.


