[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get User from Backup

[Previous](Get-Backups-List.md) | [Next](Send-Push-Notifications.md)

# Get User from Backup

The request allows receiving information about a user from a specific backup on the server.

## Rest API

Request format
    
    
    GET /api/user/backup/get?backup=data&login=login
    POST /api/user/backup/get?backup=data&login=login

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/user/backup/get?backup=1574122620&login=104366
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Login": "764636",
        "Group": "demo\\forex",
        "CertSerialNumber": "0",
        "Rights": "6627",
        "MQID": "F5986B14",
        "Registration": "1527173711",
        "LastAccess": "1527173713",
        "LastPassChange": "1527173711",
    ...
      }
    }

## Raw API

Request format
    
    
    USER_BACKUP_GET|BACKUP=data|LOGIN=login|\r\n

Response format
    
    
    USER_BACKUP_GET|RETCODE=code description|\r\n
    The body of the client record in JSON format

## Request Parameters

  * backup — backup copy date. To get the list of available backups, use the [/user_back_list](Get-Backups-List.md) request. To request data from archive, specify the 0 value.
  * login — the login of the user whose data should be retrieved from the archive database.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — user parameters in JSON format. The full description of passed client parameters is available under the ["Data structure"](Data-Structure.md) section.


