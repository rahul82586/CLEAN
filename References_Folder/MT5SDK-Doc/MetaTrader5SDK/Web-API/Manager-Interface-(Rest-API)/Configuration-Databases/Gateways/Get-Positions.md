[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Gateways](../Gateways.md) / Get Positions

[Previous](Get-Module-by-Name.md) | [Next](../Data-Feeds.md)

# Request Gateway Trade Positions

# The request allows receiving the current state of positions on trading accounts which are used by the gateway in an external system. Depending on the gateway tab, positions can be displayed via one or several accounts.

## Rest API

Request Format
    
    
    GET /api/gateway/get_position?gateway_id=identifier
    POST /api/gateway/get_position?gateway_id=identifier

Response Format
    
    
    {
     "time" : "snapshot time",
     "positons" : [ description of positions ]
    }

Example
    
    
    //--- request to the server
    GET /api/gateway/get_position?gateway_id=6
    //--- server response
    {
      "time": 1574775746,
      "positions": [
        {
          "Position": "0",
          "ExternalID": "",
          "Login": "0",
          "Dealer": "0",
          "Symbol": "AUDNZD",
          ...
        }
      ]
    }

## Raw API

Request Format
    
    
    GATEWAY_POSITION_GET|GATEWAY_ID=identifier|\r\n

Response Format
    
    
    GATEWAY_POSITION_GET|\r\n
    Snapshot time and position descriptions in JSON format

## Request Parameters

  * gateway_id — gateway ID for which position statuses in an external system should be requested.



## Response Parameters

  * time — Position status snapshot in the number of seconds elapsed since 01.01.1970. Depending on the gateway (and external trading system), position statuses can be submitted either in real time mode or only at the end of a trading session.
  * positions — array of positions. The complete description of passed server parameters is available under the ["Data structure"](../../Trading/Positions/Data-Structure.md) section.



## Note

Positions requests should be supported by the gateway.
