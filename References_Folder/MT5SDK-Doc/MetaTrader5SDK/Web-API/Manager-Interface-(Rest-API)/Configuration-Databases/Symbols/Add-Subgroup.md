[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Add Subgroup

[Previous](Get-by-Group.md) | [Next](Delete-Subgroup.md)

Add a Subgroup

Add a subgroup of symbols.

## Rest API

Request Format
    
    
    POST /api/symbol_group/add
    [ list of names ]

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [ 
       {"Name":"name"},
       {"Name":"name"}, ...
      ]
    }

Examples
    
    
    //--- request to the server
    POST /api/symbol_group/add
    {"Name":"New group"}
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Name" : "New group"
      }
    }

## Raw API

Request Format
    
    
    SYMBOL_GROUP_ADD|\r\n
    List of names in JSON format

Response Format
    
    
    SYMBOL_GROUP_ADD|RETCODE=code description|\r\n
    List of names in JSON format

## Query Parameters

No parameters. The name of one or more subgroups is passed in JSON format as an additional command body.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — list of names of created subgroups.



## Note

The command only works when connected to the main trading server. Otherwise, error [12001](../../../../Return-Codes/API.md) is returned.
