[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get by External Account

[Previous](Get-by-Login.md) | [Next](Get-Multiple.md)

# Get User by External Account

The request allows receiving information about a user based on his or her external traddng system (exchange) account.

## Rest API

Request format
    
    
    GET /api/user/get_external?account=account&gateway=identifier
    POST /api/user/get_external?account=account&gateway=identifier

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/user/get_external?account=36611
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
    
    
    USER_EXETERNAL_GET|ACCOUNT=account&GATEWAY=identifier|\R\N

Response format
    
    
    USER_EXETERNAL_GET|RETCODE=code description|\r\n
    The body of the client record in JSON format

## Request Parameters

  * account — user account number in an external trading system.
  * gateway — gateway ID via which connection to the external system is performed. An optional parameter.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — user parameters in JSON format. The full description of passed client parameters is available under the ["Data structure"](Data-Structure.md) section.



## Note

  * The external system account and the gateway ID to which the account belongs, are stored in the ["TradeAccount" field](Data-Structure.md).
  * Information about a client that can be obtained depends on access permissions of a manager account that is used for connection of the Web client. If the "Access to personal data of accounts" permission is absent", [some of the fields are not filled (#private-info)](../../Getting-Started.md#private-info) in the server response.


