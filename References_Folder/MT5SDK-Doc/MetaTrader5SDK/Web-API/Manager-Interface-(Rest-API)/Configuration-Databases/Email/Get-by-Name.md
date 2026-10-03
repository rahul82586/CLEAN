[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Email](../Email.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](Send.md)

# Get Mail Server by Name

The request allows receiving mail server configuration by name.

## Rest API

Request Format
    
    
    GET /api/email/get?name=name
    POST /api/email/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/email/get?name=ABC%20Broker
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "ABC Broker",
        "SenderMail" : "support@abcbroker.com",
        "SenderName" : "ABC Broker",
        "Server" : "smtp.abcbroker.com:25",
        "Login" : "support@abcbroker.com",
        "Password" : "password123",
        "Flags" : "2",
        "Stats" : {
          "TotalSend" : "20",
          "TotalFailed" : "1",
          "CurrentQueue" : "0",
          "TimeMin" : "1",
          "TimeMax" : "3",
          "TimeAvg" : "2"
        }
      }
    }

## Raw API

Request Format
    
    
    EMAIL_GET|NAME=name|\r\n

Response Format
    
    
    EMAIL_GET|RETCODE=code description|\r\n
    Mail server configuration description in JSON format

## Request Parameters

  * name — mail server configuration name.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the mail server configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.


