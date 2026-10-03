[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Get Multiple

[Previous](Get-Paged.md) | [Next](Update.md)

# Get Multiple Positions

The request allows receiving information related to multiple positions, based on a list of logins, tickets or groups.

## Rest API

Request Format
    
    
    GET /api/position/get_batch?login=logins&group=groups&ticket=tickets&symbol=symbols
    POST /api/position/get_batch?login=logins&group=groups&ticket=tickets&symbol=symbol
    POST /api/position/get_batch?symbol=symbol
    {
      "ticket": [
        1012,
        4034
      ],
      "group": [
        demoforex-eur,
        demoforex-usd
      ],
      "ticket": [
        96639,
        13549
      ],
    }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ description of positions ]
    }

Example
    
    
    //--- request to the server
    GET /api/position/get_batch?login=764636,764637
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        { 
        "Position" : "618",
        "ExternalID" : "",
        "Login" : "764636",
         ...
        },
        { 
        "Position" : "617",
        "ExternalID" : "",
        "Login" : "764636",
         ...
        },
    ...
      ]
    }

## Raw API

Request Format
    
    
    POSITION_GET_BATCH|LOGIN=logins|GROUP=groups|TICKET=tickets|SYMBOL=symbol|\r\n

Response Format
    
    
    POSITION_GET_BATCH|RETCODE=code description|\r\n
    Array of positions in JSON format

## Request Parameters

  * login — the list of logins, the positions of which you want to receive. A commas separated list. Can also be specified as an array in the POST request body.
  * group — the list of groups, for users from which you want to receive positions. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex. Groups Can also be specified as an array in the POST request body.
  * ticket — the list of order tickets to receive. Can be specified as an array in the POST request body.
  * symbol — the symbol positions for which you want to receive. You can specify multiple symbols separated by commas. Only make sense in combination with the 'login' or 'group' parameter.



> Operations can be requested with only one parameter: by logins, by groups, or by tickets. You cannot specify all the three parameters together.

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — position array in JSON format. The complete description of the passed position parameters is provided under the [Data Structure](Data-Structure.md) section.



## Note

The request only works with open positions on the client's account. The history of positions is formed on the side of client terminals based on the history of trades. It is impossible to obtain it.
