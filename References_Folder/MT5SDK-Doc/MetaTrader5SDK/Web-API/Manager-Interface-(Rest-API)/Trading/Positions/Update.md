[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Update

[Previous](Get-Multiple.md) | [Next](Delete.md)

# Position Update

The request allows changing a position on the server.

## Rest API

Request Format
    
    
    POST /api/position/update
    { Description of the position to be changed in JSON format }

Response Format
    
    
    {
      "retcode" : "0 Done",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/position/update
    {
       "Position" : "618",
       "ExternalID" : "",
       "Login" : "764636",
       ...
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Position" : "618",
        "ExternalID" : "",
        "Login" : "764636",
        ...
      }
    }

## Raw API

Request Format
    
    
    POSITION_UPDATE|\r\n
    Description of a position to be changed, in JSON format

Response Format
    
    
    POSITION_UPDATE|RETCODE=code description|\r\n
    Description of the changed position in JSON format

## Request Parameters

The request has no parameters. The description of the position to be changed is passed in JSON format as an additional body. The complete description of the possible position parameters is provided under the ["Data structure"](Data-Structure.md) section.

  * The record to be changed is identified based on the ticket.
  * If the parameter value is not specified, the corresponding parameter will not be changed.

  
---  
  
## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — updated position parameters in JSON format. The full description of position parameters is available under the [Data Structure](Data-Structure.md) section.



## Note

A position can only be updated when connected to the same trade server on which it was created. If the position with the specified ticket is not found, response code [13](../../../../Return-Codes/Common-errors.md) is returned.
