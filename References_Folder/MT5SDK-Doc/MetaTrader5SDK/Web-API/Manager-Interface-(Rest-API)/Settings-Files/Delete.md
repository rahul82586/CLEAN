[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Settings Files](../Settings-Files.md) / Delete

[Previous](Update.md) | [Next](../Subscriptions.md)

# Delete Settings

The request allows deleting a settings file from the server.

## Rest API

Request Format
    
    
    GET /api/setting/delete?section=directory&key=file
    POST /api/setting/delete?section=directory&key=file

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    /api/setting/delete?section=web&key=settings.json
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    SETTING_DELETE|SECTION=directory|KEY=file|\r\n

Response Format
    
    
    SETTING_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * section — the name of the subfolder in the manager account directory, from which you want to delete the settings file.
  * key — the name of the settings file.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

The path to the settings file is formed as follows: [trade server directory]\settings\\[manager login]\section\key. section and key are the first and the second parameters of the request, manager login is the manager's account using which the application is [connected to the trade server](../../Authentication.md).
