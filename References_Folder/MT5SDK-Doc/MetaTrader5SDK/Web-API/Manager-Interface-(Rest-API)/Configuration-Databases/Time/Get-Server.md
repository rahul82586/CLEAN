[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Get Server

[Previous](Data-Structure.md) | [Next](Get-Settings.md)

# Getting Server Time

This request is used for receiving the current time of the server.

## Rest API

Request format
    
    
    GET /api/time/server
    POST /api/time/server

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Time" : "unix-time yyyy.mm.dd hh:mm:ss" }
    }

Example
    
    
    //--- request to the server
    GET /api/time/server
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Time": "1572518788 2019.10.31 10:46:28" }
    }

## Raw API

Request format
    
    
    TIME_SERVER\r\n

Response format
    
    
    TIME_SERVER|RETCODE=code description|TIME=unix-time yyyy.mm.dd hh:mm:ss\r\n

Example
    
    
    //--- request to the server
    001c00010TIME_SERVER|
    //--- server response
    TIME_SERVER|RETCODE=0 Done|TIME=1315489916 2011.09.08 13:51:56|

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * time — current server time. In the first value the unix time is passed (number of seconds that have elapsed since 01.01.1970), in the second value the text representation of the date and time is passed.


