[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Delete Multiple

[Previous](Delete.md) | [Next](Shift.md)

# Delete Multiple Groups

The request allows deleting multiple groups.

## Rest API

Request format
    
    
    GET /api/group/delete_batch?group=list of names
    GET /api/group/delete_batch?name=list of names
    GET /api/group/delete_batch?index=list of indexes
     
    POST /api/group/delete_batch?group=list of names
    POST /api/group/delete_batch?name=list of names
    POST /api/group/delete_batch?index=list of indexes
    POST
    [list of indexes]

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [ response codes ]
    }

Example
    
    
    //--- request to the server
    GET /api/group/delete_batch?group=demoforex-usd,demoforex-eur
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [ 0, 13, 0 
      ]
    }

## Raw API

Request format
    
    
    GROUP_DELETE_BATCH|GROUP=list of names|\r\n
    GROUP_DELETE_BATCH|NAME=list of names|\r\n
    GROUP_DELETE_BATCH|INDEX=list of indexes|\r\n

Response format
    
    
    GROUP_DELETE_BATCH|RETCODE=code description|\r\n

## Request Parameters

  * group — names of groups to be deleted, separated by commas. The names are specified together with the path.
  * name — names of groups to be deleted, separated by commas. The names are specified together with the path.
  * index — indexes of groups to be deleted, separated by commas. Group numbering starts with 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of response codes regarding deletion of each of the specified groups.



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit group configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.
  * A group which contains at least one account cannot be deleted. At an attempt to delete such a group, the error [2003](../../../../Return-Codes/Configuration-Management.md) will be returned.
  * The last manager group on the server cannot be deleted. At an attempt to delete such a group, the error [2001](../../../../Return-Codes/Configuration-Management.md) will be returned.
  * Only one of the parameters can be used in the request. Multiple lists are not allowed.
  * The 'name' and 'group' parameters are equivalent. They are supported for unification and backward compatibility of requests.


