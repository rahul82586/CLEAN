[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Get by Group

[Previous](Get-by-Name-or-Mask.md) | [Next](Add-Subgroup.md)

# Get a Symbol by Group

This request allows to receive symbol configuration for a group by the symbol name.

## Rest API

Request format
    
    
    GET /api/symbol/get_group?symbol=name&group=name
    POST /api/symbol/get?symbol=name&group=name

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/symbol/get_group?symbol=EURUSD&group=demo\\forex
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Symbol" : "EURUSD",
        "Path" : "Forex\\Major\\EURUSD",
        "ISIN" : "",
        "Description" : "Euro vs US Dollar",
        "International" : "",
        "Basis" : "",
        "Source" : "",
        "Page" : "http://www.google.com/finance?q=EURUSD",
    ...
    }

## Raw API

Request format
    
    
    SYMBOL_GET_GROUP|SYMBOL=name|GROUP=name|\r\n

Response format
    
    
    SYMBOL_GET_GROUP|RETCODE=code description|\r\n
    The body of the symbol configuration in JSON format

Example
    
    
    //--- request to the server
    007e00010SYMBOL_GET_GROUP|SYMBOL=EURUSD|GROUP=demo\\forex|
    //--- server response
    SYMBOL_GET_GROUP|RETCODE=0 Done|
    {
    "Symbol" : "EURUSD",
    "Path" : "Forex\\Major\\EURUSD",
    "ISIN" : "",
    "Description" : "Euro vs US Dollar",
    "International" : "",
    "Basis" : "",
    "Source" : "",
    "Page" : "http://www.google.com/finance?q=EURUSD",
    ...
    }

## Request Parameters

  * symbol — symbol name.
  * group — the name of the group for which we get the symbol configuration.



## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — symbol configuration in JSON format. A complete description of the passed parameters of symbols is given in the ["Data structure"](Data-Structure.md) section.


