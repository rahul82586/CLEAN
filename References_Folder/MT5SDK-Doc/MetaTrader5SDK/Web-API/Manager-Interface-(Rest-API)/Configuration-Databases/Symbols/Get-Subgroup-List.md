[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Get Subgroup List

[Previous](Get-Subgroup-by-Index.md) | [Next](../Floating-Margin.md)

# Get a List of Subgroups

Get a list of symbol subgroups available on the trading server.

## Rest API

Request Format
    
    
    GET /api/symbol_group/list
    POST /api/symbol_group/list

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ list of subgroups ]
    }

Example
    
    
    //--- request to the server
    GET /api/symbol_group/list
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [ 
        "Forex",
        "Futures",
        "Preliminary",
        "Collateral"
      ]
    }

## Raw API

Request Format
    
    
    SYMBOL_GROUP_LIST|\r\n

Response Format
    
    
    SYMBOL_GROUP_LIST|RETCODE=code description|\r\n
    List of subgroups in JSON format

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a non-existent symbol is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — list of available subgroups.


