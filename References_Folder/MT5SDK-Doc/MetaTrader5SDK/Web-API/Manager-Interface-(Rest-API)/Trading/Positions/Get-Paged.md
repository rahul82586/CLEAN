[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Get Paged

[Previous](Get-Total.md) | [Next](Get-Multiple.md)

# Getting Positions Page by Page

This request allows to get positions of a client with the specified login.

## Rest API

Request format
    
    
    GET /api/position/get_page?login=login&offset=index&total=number
    POST /api/position/get_page?login=login&offset=index&total=number

Response format
    
    
    {
     "retcode" : "code description",
      "answer" : [
       { description },
       { description },
       { description },
    ...
      ]
    }

Example
    
    
    //--- request to the server
    GET /api/position/get_page?login=1020&offset=0&total=3
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

Request format
    
    
    POSITION_GET_PAGE|LOGIN=xxxx|OFFSET=yyyy|TOTAL=zzzz\r\n

Response format
    
    
    POSITION_GET_PAGE|RETCODE=xxxx yyyy|\r\n
    Position bodies in JSON format

## Request Parameters

  * login — the login of the client whose positions you need to obtain.
  * offset — the index of the position starting from which you need to obtain positions. Numbering starts with 0.
  * total — the number of positions that should be obtained. The maximum number of positions that can be requested in one command is 100.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — position array in JSON format. The complete description of the passed position parameters is given in the ["Data structure"](Data-Structure.md) section.



## Note

  * This method allows to easily arrange a paged output of resulting positions. First you should get the total number of a client's positions using the [/api/position/get_total](Get-Total.md) method. After defining the number of positions that should be shown on one page (set by the total parameter), you can easily find the offset parameter for each page.
  * The request only works with open positions on the client's account. The history of positions is formed on the side of client terminals based on the history of trades. It is impossible to obtain it.


