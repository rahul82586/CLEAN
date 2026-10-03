[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Email](../Email.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Name.md)

# Get Mail Server by Index

Get the configuration of one or more mail servers by index in the list.

## Rest API

Request Format
    
    
    GET /api/email/next?index=index&count=number
    POST /api/email/next?index=index&count=number

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/email/next?index=0
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
    
    
    EMAIL_NEXT|INDEX=index|COUNT=number\r\n

Response Format
    
    
    EMAIL_NEXT|RETCODE=code description|\r\n
    Mail server configuration description in JSON format

## Request Parameters

  * index — mail server configuration index starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent configuration is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — description of the mail server configuration in JSON format. The complete description of passed server parameters is available under the ["Data structure"](Data-Structure.md) section.


