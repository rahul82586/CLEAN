[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Delete Multiple

[Previous](Delete.md) | [Next](Shift.md)

# Delete multiple symbols

The request allows deleting multiple symbols from the server.

## Rest API

Request format
    
    
    GET /api/symbol/delete_batch?symbol=list of names
    GET /api/symbol/delete_batch?name=list of names
    GET /api/symbol/delete_batch?index=list of indexes
     
    POST /api/symbol/delete_batch?symbol=list of names
    POST /api/symbol/delete_batch?name=list of names
    POST /api/symbol/delete_batch?index=list of indexes
    POST
    [list of indexes]

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [ response codes ]
    }

Example
    
    
    //--- request to the server
    GET /api/symbol/delete_batch?symbol=EURUSD,GBPUSD
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [ 0, 13, 0 
      ]
    }

## Raw API

Request format
    
    
    SYMBOL_DELETE_BATCH|SYMBOL=list of names|\r\n
    SYMBOL_DELETE_BATCH|NAME=list of names|\r\n
    SYMBOL_DELETE_BATCH|INDEX=list of indexes|\r\n

Response format
    
    
    SYMBOL_DELETE_BATCH|RETCODE=code description|\r\n

## Request Parameters

  * symbol — names of symbols to be deleted, separated by commas. The names are specified together with the path.
  * name — names of symbols to be deleted, separated by commas. The names are specified together with the path.
  * index — indexes of symbols to be deleted, separated by commas. Symbol Group numbering starts with 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of response codes regarding deletion of each of the specified groups.



## Note

  * This request works only when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator and edit symbol configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.


