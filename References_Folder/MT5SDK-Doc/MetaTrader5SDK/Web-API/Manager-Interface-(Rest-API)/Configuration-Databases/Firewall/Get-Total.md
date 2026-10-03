[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Get Total

[Previous](Shift.md) | [Next](Get-by-Index.md)

# Get the Total Number of Firewall Rules

The request allows receiving the number of firewall rules available in the platform.

## Rest API

Request Format
    
    
    GET /api/firewall/total
    POST /api/firewall/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "Total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /fiewall_total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "Total" : "11" }
    }

## Raw API

Request Format
    
    
    FIREWALL_TOTAL\r\n

Response Format
    
    
    FIREWALL_TOTAL|RETCODE=code description |TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — number of firewall rules in the trading platform.


