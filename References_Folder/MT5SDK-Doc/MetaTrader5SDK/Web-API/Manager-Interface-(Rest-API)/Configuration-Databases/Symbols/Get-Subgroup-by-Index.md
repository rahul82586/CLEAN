[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Get Subgroup by Index

[Previous](Get-Subgroup-Total.md) | [Next](Get-Subgroup-List.md)

# Get a Subgroup by Index

Get the name of a subgroup of symbols by index.

## Rest API

Request Format
    
    
    GET /api/symbol_group/next?index=index
    POST /api/symbol_group/next?index=index

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/symbol_group/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Name" : "Forex\\Major"
      }
    }

## Raw API

Request Format
    
    
    SYMBOL_GROUP_NEXT|INDEX=index|\r\n

Response Format
    
    
    SYMBOL_GROUP_NEXT|RETCODE=code description|\r\n
    Symbol subgroup name in JSON format

## Query Parameters

  * index — index of the symbol subgroup, starting from 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a non-existent symbol is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * name — the name of a subgroup of symbols in JSON format.


