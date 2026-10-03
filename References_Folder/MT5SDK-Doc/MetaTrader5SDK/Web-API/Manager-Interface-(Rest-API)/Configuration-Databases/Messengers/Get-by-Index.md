[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Name.md)

# Get Messenger by Index

The request allows receiving a messenger configuration by an index in the list.

## Rest API

Request Format
    
    
    GET /api/messenger/next?index=index
    POST /api/messenger/next?index=index

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/messenger/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "BulkSMS",
        "Sender" : "123456789",
        "ProviderType" : "0",
        "ProviderAddress" : "https:\/\/api.bulksms.com\/v1",
        "ProviderLogin" : "",
        "ProviderPassword" : "",
        "ProviderToken" : "xp23kPa",
        "ProviderSubid" : "broker",
        "ProviderCurrency" : "CRD",
        "ProviderCurrencyRate" : "0.030",
        "Flags" : "1",
        "Countries" : [],
        "Groups" : []
      }
    }

## Raw API

Request Format
    
    
    MESSENGER_NEXT|INDEX=index\r\n

Response Format
    
    
    MESSENGER_NEXT|RETCODE=code description|\r\n
    The description of a messenger configuration in JSON format

## Request Parameters

  * index — messenger configuration index starting with 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent messenger is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — description of the messenger configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.


