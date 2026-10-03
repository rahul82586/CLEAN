[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Get by Name or Mask

[Previous](Get-by-Index.md) | [Next](Get-by-Group.md)

# Get symbols by name or mask

Use this request to receive a configuration of one or more symbols by name or mask.

## Rest API

Request format
    
    
    GET /api/symbol/get?symbol=name
    GET /api/symbol/get?mask=mask
    POST /api/symbol/get?symbol=name
    POST /api/symbol/get?mask=mask

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/symbol/get?symbol=EURUSD
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
    //--- request to the server
    GET /api/symbol/get?mask=*
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
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
        },
        {
        "Symbol" : "GBPUSD",
         "Path" : "Forex\\Major\\GBPUSD",
         "ISIN" : "",
         "Description" : "Pound vs US Dollar",
         "International" : "",
         "Basis" : "",
         "Source" : "",
         "Page" : "http://www.google.com/finance?q=GBPUSD",
         ...
        },
      ]
    }

## Raw API

Request format
    
    
    SYMBOL_GET|SYMBOL=name|\r\n

Response format
    
    
    SYMBOL_GET|RETCODE=code description|\r\n
    The body of the symbol configuration in JSON format

Example
    
    
    //--- request to the server
    003600010SYMBOL_GET|SYMBOL=EURUSD|
    //--- server response
    SYMBOL_GET|RETCODE=0 Done|
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

  * symbol — symbol name when requesting one configuration.
  * mask — one or more symbols separated by commas. Specify the full name of the symbol, including the path. For example, Forex\EURUSD. Symbols can also be specified using wildcard characters: "*" (any value) and "!" (exclude). For example, Forex\*,!Forex\EURUSD — all symbols in the Forex subgroup except EURUSD.  
For queries by mask, the server can return no more than 5,000 configurations. If the limit is exceeded, the first 5,000 records will be returned and the command will additionally return [response code 14](../../../../Return-Codes/Common-errors.md).



> Use only one of the parameters in the query: symbol or mask. If both parameters are specified, the request will only return information for the symbol specified in 'symbol'.

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — symbol configuration in JSON format. A complete description of the passed parameters of symbols is given in the ["Data structure"](Data-Structure.md) section. For queries by mask, the response is always sent as a JSON list (array), even if the request resulted in one or no configuration.


