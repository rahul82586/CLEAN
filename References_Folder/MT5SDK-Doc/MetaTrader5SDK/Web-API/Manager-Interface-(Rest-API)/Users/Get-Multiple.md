[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get Multiple

[Previous](Get-by-External-Account.md) | [Next](Check-Password.md)

# Get Multiple Users

The request allows receiving information related to multiple users, based on a list of logins or groups.

## Rest API

Request format
    
    
    GET /api/user/get_batch?login=logins
    GET /api/user/get_batch?group=groups
     
    POST /api/user/get_batch?login=logins
    POST /api/user/get_batch?group=groups

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [ user description ]
    }

Example
    
    
    //--- request to the server
    GET /api/user/get_batch?login=764636,764637
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

Request format
    
    
    USER_GET_BATCH|LOGIN=logins|\r\n
    USER_GET_BATCH|GROUP=groups|\r\n

Response format
    
    
    USER_GET_BATCH|RETCODE=description code|\r\n
    Array of users in JSON format

## Request Parameters

  * login — list of user logins data of which you want to receive data. A commas separated list.
  * group — the list of groups, for users from which you want to receive data. A commas separated list.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of user descriptions in JSON format. The full description of passed client parameters is available under the ["Data structure"](Data-Structure.md) section.



## Note

  * The user data that can be obtained depends on access permissions of a manager account that is used for Web client connection. If the "Access to personal data of accounts" permission is absent", [some of the fields are not filled (#private-info)](../../Getting-Started.md#private-info) in the server response.
  * Only one of the parameters can be used in the request. Multiple lists are not allowed.
  * Please pay attention to the [ApiData property (#apidata)](Data-Structure.md#apidata) use specifics. The following values are returned for each of the array elements (which are always 16):


  * The required fields AppID and ID, which only contain their values.
  * Fields ValueInt, ValueUInt and ValueDouble containing the corresponding presentation of the same binary value, which was written to the ApiData cell (via any type of API).


