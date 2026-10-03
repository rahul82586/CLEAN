[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Get by Symbol

[Previous](Data-Structure.md) | [Next](Get-Total.md)

# Getting a Position by Symbol

This request allows to receive a client's position by the symbol name.

## Rest API

Request format
    
    
    GET /api/position/get?login=login&symbol=name
    POST /api/position/get?login=login&symbol=name

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/position/get?login=764636&symbol=EURUSD
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Position" : "617",
        "ExternalID" : "",
        "Login" : "764636",
        "Dealer" : "0",
        "Symbol" : "EURUSD",
        "Action" : "0",
        "Digits" : "5",
        "DigitsCurrency" : "2",
        "Reason" : "16",
    ...
    }

## Raw API

Request format
    
    
    POSITION_GET|LOGIN=xxxx|SYMBOL=yyyy|\r\n

Response format
    
    
    POSITION_GET|RETCODE=xxxx yyyy|\r\n
    Position body in JSON format

## Request Parameters

  * login — the login of a client.
  * symbol — the name of the symbol for which you need to get a position.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — position parameters in JSON format. The complete description of the passed position parameters is given in the ["Data structure"](Data-Structure.md) section.



## Note

  * The request should only be used for [netting accounts (#netting)](../../../../Database-Interfaces/Trade/General-Principles/Position-Accounting-System.md#netting), in which only one position per symbol can be open at a time. For hedging accounts, use [/api/position/get_batch](Get-Multiple.md). When using [/api/position/get](Get-by-Symbol.md) for hedging accounts having multiple positions for the specified symbol, the request will only return the first of them.


  * The request only works with open positions on the client's account. The history of positions is formed on the side of client terminals based on the history of trades. It is impossible to obtain it.


