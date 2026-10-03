[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get Total

[Previous](Get-List.md) | [Next](Get-Group.md)

# Get the Total Number of Users

Use the request to obtain the total number of users on the trading server, available to your manager account.

## Rest API

Request format
    
    
    GET /api/user/total
    POST /api/user/total

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

Example
    
    
    //--- request to the server
    GET /api/user/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "563" }
    }

## Raw API

Request format
    
    
    USER_TOTAL\r\n

Response format
    
    
    USER_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — number of users on the server.


