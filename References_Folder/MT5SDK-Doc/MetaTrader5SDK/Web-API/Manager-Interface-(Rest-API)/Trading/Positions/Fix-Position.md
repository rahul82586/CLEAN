[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Fix Position

[Previous](Check.md) | [Next](../Trade-Requests.md)

# Fix Positions

This request allows correcting account's trading positions based on the history of deals.

## Rest API

Request Format
    
    
    GET /api/position/fix?login=login
    POST /api/position/fix?login=login

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ description of positions ]
    }

Example
    
    
    //--- request to the server
    GET /api/position/fix?login=73339
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        { 
        "Position" : "618",
        "ExternalID" : "",
        "Login" : "73339",
         ...
        },
        { 
        "Position" : "617",
        "ExternalID" : "",
        "Login" : "73339",
         ...
        },
    ...

## Raw API

Request Format
    
    
    POSITION_FIX|LOGIN=login\r\n

Response Format
    
    
    POSITION_FIX|RETCODE=code description|\r\n
    Description of positions in JSON format

## Request Parameters

  * login — login of the user whose positions should be fixed.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of positions after correction based on history, in JSON format. The complete description of the passed position parameters is provided under the [Data Structure](Data-Structure.md) section.



## Note

Upon the execution of the request, the platform calculates a client's positions based on the history of his deals, and corrects current positions if necessary.
