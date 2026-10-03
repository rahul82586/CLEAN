[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Delete Subgroup

[Previous](Add-Subgroup.md) | [Next](Shift-Subgroup.md)

Delete a Subgroup

Delete a subgroup of symbols by name or index.

## Rest API

Request Format
    
    
    GET /api/symbol_group/delete?index=index
    GET /api/symbol_group/delete?name=names
    POST /api/symbol_group/delete?index=index
    POST /api/symbol_group/delete?name=names
    [ list of names ]

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ response code for each group ]
    }

Examples
    
    
    //--- request to the server
    GETT /api/symbol_group/delete?name=Group1,Group2
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [0,0]
    }

## Raw API

Request Format
    
    
    SYMBOL_GROUP_DELETE|INDEX=index|NAME=names|\r\n

Response Format
    
    
    SYMBOL_GROUP_DELETE|RETCODE=code description|\r\n
    List of response codes in JSON format

## Query Parameters

  * index — the position of the subgroup you want to delete, starting from 0.
  * name — one or more subgroup names separated by commas. 



The list of subgroup names to be deleted can also be passed in JSON format as an additional command body.

The 'name' and 'index' parameters can only be used separately.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — a list of response codes corresponding to the result of deleting each of the specified subgroups.



## Note

  * The command only works when connected to the main trading server. Otherwise, error [12001](../../../../Return-Codes/API.md) is returned.
  * A subgroup is deleted along with all the symbols it contains.


