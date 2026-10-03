[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Update Closed

[Previous](Get-Multiple-Closed.md) | [Next](Delete-Closed.md)

# Update a Closed Order

The request allows changing an closed order (in history) on the server.

## Rest API

Request Format
    
    
    POST /api/history/update
    { Description of the order to be changed in JSON format }

Response Format
    
    
    {
      "retcode" : "0 Done",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/history/update
    {
       "Order" : "12832917",
       "ExternalID" : "",
       "Login" : "1020",
       ...
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Order" : "12832917",
        "ExternalID" : "",
        "Login" : "1020",
        ...
      }
    }

## Raw API

Request Format
    
    
    HISTORY_UPDATE|\r\n
    Description of the order to be changed in JSON format

Response Format
    
    
    HISTORY_UPDATE|RETCODE=code description|\r\n
    Description of the changed order in JSON format

## Request Parameters

The request has no parameters. The description of the order to be changed is passed in JSON format as an additional body. The complete description of the possible order parameters is provided under the ["Data structure"](Data-Structure.md) section.

  * The record to be changed is identified based on the ticket.
  * If the parameter value is not specified, the corresponding parameter will not be changed.

  
---  
  
## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — parameters of the updated order in JSON format. The full description of order parameters is available under the [Data Structure](Data-Structure.md) section.



## Note

An order can only be updated when connected to the same trade server on which it was created. If the order with the specified ticket is not found, response code [13](../../../../Return-Codes/Common-errors.md) is returned.
