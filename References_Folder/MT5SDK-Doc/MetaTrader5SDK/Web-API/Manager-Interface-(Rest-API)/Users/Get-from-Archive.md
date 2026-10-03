[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get from Archive

[Previous](Move-to-Archvie.md) | [Next](Get-Multiple-from-Archive.md)

# Get User from the Archive

The request allows receiving information about a user from an archive database.

## Rest API

Request format
    
    
    GET /api/user/archive/get?login=login
    POST /api/user/archive/get?login=login

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/user/archive/get?login=764636
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
    
    
    USER_ARCHIVE_GET|LOGIN=login|\r\n

Response format
    
    
    USER_ARCHIVE_GET|RETCODE=code description|\r\n
    The body of the client record in JSON format

## Request Parameters

  * login — the login of the user whose data should be retrieved from the archive database.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — user parameters in JSON format. The full description of passed client parameters is available under the ["Data structure"](Data-Structure.md) section.


