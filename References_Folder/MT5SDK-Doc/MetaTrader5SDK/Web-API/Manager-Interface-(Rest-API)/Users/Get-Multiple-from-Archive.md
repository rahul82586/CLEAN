[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get Multiple from Archive

[Previous](Get-from-Archive.md) | [Next](Restore-from-Archive.md)

# Get multiple users from an archive

This query enables a bulk query of user data from an archive database, using a list of logins or groups.

## Rest API

Request Format
    
    
    GET /api/user/archive/get_batch?login=logins
    GET /api/user/archive/get_batch?group=groups
     
    POST /api/user/archive/get_batch?login=logins
    POST /api/user/archive/get_batch?group=groups

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ user description ]
    }

The example
    
    
    //--- request to the server
    GET /api/user/archive/get_batch?login=764636,764637
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        {
         "Login": "764636",
         "Group": "demo\\forex",
         "CertSerialNumber": "0",
         "Rights": "6627",
         "MQID": "F5986B14",
         "Registration": "1527173711",
         "LastAccess": "1527173713",
         "LastPassChange": "1527173711",
         ...
        },
        {
         "Login": "764637",
         "Group": "demo\\forex",
         "CertSerialNumber": "0",
         "Rights": "6627",
         "MQID": "H5926B36",
         "Registration": "1527186511",
         "LastAccess": "1527186513",
         "LastPassChange": "1527186511",
         ...
        },
      ]
    }

## Raw API

Request Format
    
    
    USER_ARCHIVE_GET_BATCH|LOGIN=logins|\r\n
    USER_GET_BATCH|GROUP=groups|\r\n

Response Format
    
    
    USER_ARCHIVE_GET_BATCH|RETCODE=code description|\r\n
    Array of users in JSON format

## Request Parameters

  * login — list of user logins whose data you want to receive. A commas separated list.
  * group — the list of groups, for users from which you want to receive data. A commas separated list.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of user descriptions in JSON format. The full description of the passed client parameters is given in the [Data structure](Data-Structure.md) section.



## Note

Only one of the parameters can be used in the request. Multiple lists are not allowed.
