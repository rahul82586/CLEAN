[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Delete

[Previous](Update.md) | [Next](Get-Backups-List.md)

# Delete a Position

The request allows deleting one or more positions by ticket.

## Rest API

Request Format
    
    
    GET /api/position/delete?ticket=tickets
    POST /api/position/delete?ticket=tickets
    POST /api/position/delete
    [
      1012,
      4034
    ]

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/position/delete?ticket=73339,73340
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    POSITION_DELETE|TICKET=tickets\r\n

Response Format
    
    
    POSITION_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * ticket — the ticket of the position to be deleted. Multiple IDs can be specified as separated by commas. Tickets can also be specified as an array in the POST request body.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * A position can only be deleted when connected to the same trade server on which it was created. If the position with the specified ticket is not found, response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * To use the function, the manager account used by the Web API application must have the following permissions: [RIGHT_TRADE_DELETE (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) and [RIGHT_TRADES_MANAGER (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights).


