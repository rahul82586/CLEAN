[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](Send-Message.md)

# Get Messenger by Name

The request allows receiving manager configuration by login.

## Rest API

Request Format
    
    
    GET /api/messenger/get?name=name
    POST /api/messenger/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/messenger/get?name=BulkSMS
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
    
    
    MESSENGER_GET|NAME=name|\r\n

Response Format
    
    
    MESSENGER_GET|RETCODE=code description|\r\n
    The description of a messenger configuration in JSON format

## Request Parameters

  * name — messenger configuration name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the messenger configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.


