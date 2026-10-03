[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Get Identifiers

[Previous](Get-Change-History.md) | [Next](Bind-Account.md)

# Get the List of Client Identifiers

The request allows receiving the list of identifiers of all client available to the manager.

## Rest API

Request Format
    
    
    GET /api/client/get_ids?group=groups
    POST /api/client/get_ids?group=groups

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ list of identifiers ]
    }

The example
    
    
    //--- request to the server
    GET /api/client/get_ids
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [ 1032, 1033, 1040, 1045 ]
    }

## Raw API

Request Format
    
    
    CLIENT_IDS|GROUP=groups|\r\n

Response Format
    
    
    CLIENT_IDS|RETCODE=code description|\r\n
    List of identifiers

## Request Parameters

  * group — an optional parameter for filtering results by the preferred group ([TradingGroup](Data-Structure.md)) specified for the client. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex. The following clients are returned when filter by groups is used:


  * Clients for whom TradingGroup is specified and this group corresponds to the request mask
  * Clients for whom TradingGroup is not specified, but there is at least one [bound account](Bind-Account.md) from the requested group
  * Clients for whom TradingGroup is not specified and there are no bound accounts (to prevent the clients from being lost)



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — list of client identifiers.



## Note

The request returns the list of client IDs available to the manager account, which is used for [connection](../../Authentication.md). A client record is available to the manager if one of the following conditions is met:

  * The client is created by this manager
  * The client is explicitly assigned to the manager ([AssignedManager](Data-Structure.md))
  * The preferred trading group ([TradingGroup](Data-Structure.md)) set for the client is available to the manager (the manager has [permissions for the group](../../../Configuration-Interfaces/Managers/IMTConManager/GroupAdd.md))
  * Any of the [trading accounts bound to the client](Bind-Account.md) is available to the manager (the manager has [permissions for the group](../../../Configuration-Interfaces/Managers/IMTConManager/GroupAdd.md) in which the account is located)


