[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Check

[Previous](Restore-from-Backup.md) | [Next](Fix-Position.md)

# Check Positions

This request allows checking the correctness of account's trading positions based on the history of deals.

## Rest API

Request Format
    
    
    GET /api/position/check?login=login
    POST /api/position/check?login=login

Response Format
    
    
    {
     "retcode" : "code description",
     "current" : [ description of positions ]
     "invalid" : [ description of positions ]
     "missed" : [ description of positions ]
     "nonexsit" : [ description of positions ]
    }

Example
    
    
    //--- request to the server
    GET /api/position/check?login=73339
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
         ...
        ],
      "invalid" : [
        { 
        "Position" : "619",
        "ExternalID" : "",
        "Login" : "764636",
         ...
        },
         ...
        ],
      "missed" : [
        { 
        "Position" : "620",
        "ExternalID" : "",
        "Login" : "764636",
         ...
        },
        ],
      "nonexist" : [
        { 
        "Position" : "621",
        "ExternalID" : "",
        "Login" : "764636",
         ...
        },
        ]
    ]

## Raw API

Request Format
    
    
    POSITION_CHECK|LOGIN=login\r\n

Response Format
    
    
    POSITION_CHECK|RETCODE=code description|\r\n
    Description of positions in JSON format

## Request Parameters

  * login — login of the user whose positions you want to check.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * current — array of current positions on the account, in JSON format. The complete description of the passed position parameters is provided under the [Data Structure](Data-Structure.md) section.
  * invalid — during the check, the platform calculates what positions a client should have based on his history of trades. Calculated positions are compared with actual ones. If the calculate list contains positions that do not match actual positions, such records will be passed to the invalid array.
  * missed — positions that were calculated based on the client's history and that are not found among actual positions are placed into this array. In other words, missing positions are placed into the 'missed' array.
  * nonexist — the client's actual positions that are not found in the calculated list based on the history of deals are added to this array. In other words, the client's odd positions that do not exist in the history are added to the 'nonexist' array.



## Note

If you need to correct positions based on the history of deals, you should use the [/api/position/fix](Fix-Position.md) request.
