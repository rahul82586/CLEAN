[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Deals](../Deals.md) / Update

[Previous](Get-Multiple.md) | [Next](Delete.md)

# Deal Update

The request allows changing a deal on the server.

## Rest API

Request Format
    
    
    POST /api/deal/update
    { Description of the deal to be changed in JSON format }

Response Format
    
    
    {
      "retcode" : "0 Done",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/position/update
    {
       "Deal" : "11918642",
       "ExternalID" : '',
       "Login" : "1020",
       ...
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Deal" : "11918642",
        "ExternalID" : '',
        "Login" : "1020",
        ...
      }
    }

## Raw API

Request Format
    
    
    DEAL_UPDATE|\r\n
    Description of the deal to be changed in JSON format

Response Format
    
    
    DEAL_UPDATE|RETCODE=code description|\r\n
    Description of a changed deal in JSON format

## Request Parameters

The request has no parameters. The description of the deal to be changed is passed in JSON format as an additional body. The complete description of the possible deal parameters is provided under the [Data Structure](Data-Structure.md) section.

  * The record to be changed is identified based on the ticket.
  * If the parameter value is not specified, the corresponding parameter will not be changed.

  
---  
  
## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — updated position parameters in JSON format. The complete description of the deal parameters is given under the [Data Structure](Data-Structure.md) section.



## Note

A deal can only be updated when connected to the same trade server on which it was created. If the deal with the specified ticket is not found, response code [13](../../../../Return-Codes/Common-errors.md) is returned.
