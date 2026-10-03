[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get by Login

[Previous](Delete.md) | [Next](Get-by-External-Account.md)

# Getting a User by Login

This request allows to get information about a client by the login.

## Rest API

Request format
    
    
    GET /api/user/get?login=login
    POST /api/user/get?login=login

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/user/get?login=764636
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
    
    
    USER_GET|LOGIN=login|\r\n

Response format
    
    
    USER_GET|RETCODE=code description|\r\n
    The user record body in JSON format

Example
    
    
    //--- request to the server
    002400010USER_GET|LOGIN=1023|
    //--- request to the server
    USER_GET|RETCODE=0 Done|
    {
    "Login" : "1023",
    "Group" : "demo\demoforex",
    "CertSerialNumber" : "0",
    "Rights" : "483",
    "Registration" : "1314700797",
    "LastAccess" : "1314700797",
    "LastIP" : "Unresolved",
    "Name" : "John Smith",
    ...
    }

## Request Parameters

  * login — the login of an account which should be obtained.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — user parameters in JSON format. The complete description of the passed client parameters is given in the ["Data structure"](Data-Structure.md) section.



## Note

Information about a user that can be obtained depends on access permissions of a manager account that is used for connection of the Web client. If the "Access to personal data of accounts" permission is absent", [some of the fields are not filled (#private-info)](../../Getting-Started.md#private-info) in the server response.

Please pay attention to the [ApiData property (#apidata)](Data-Structure.md#apidata) use specifics. The following values are returned for each of the array elements (which are always 16):

  * The required fields AppID and ID, which only contain their values.
  * Fields ValueInt, ValueUInt and ValueDouble containing the corresponding presentation of the same binary value, which was written to the ApiData cell (via any type of API).


