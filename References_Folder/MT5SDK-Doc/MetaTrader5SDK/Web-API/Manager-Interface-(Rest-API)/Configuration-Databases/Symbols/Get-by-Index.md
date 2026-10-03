[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Get by Index

[Previous](Get-List.md) | [Next](Get-by-Name-or-Mask.md)

# Getting a Symbol by Index

Get the configuration of one or more symbols by index in the list.

## Rest API

Request format
    
    
    GET /api/symbol/next?index=index&count=number
    POST /api/symbol/next?index=index&count=number

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/symbol/next?index=0
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
    
    
    SYMBOL_NEXT|INDEX=index|COUNT=number\r\n

Response format
    
    
    SYMBOL_NEXT|RETCODE=code description|\r\n
    The body of the symbol configuration in JSON format

Example
    
    
    //--- request to the server
    002c00010SYMBOL_NEXT|INDEX=0|
    //--- server response
    SYMBOL_NEXT|RETCODE=0 Done|
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

  * index — index of the symbol starting with 0.
  * count — the number of configurations to get. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code will be returned. If an index of a nonexistent symbol is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — symbol configuration in JSON format. A complete description of the passed parameters of symbols is given in the ["Data structure"](Data-Structure.md) section.


