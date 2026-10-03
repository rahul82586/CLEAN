[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Add

[Previous](Data-Structure.md) | [Next](Add-Multiple.md)

# Adding a group

Using this request you can create or change a group of clients on a server.

## Rest API

Request format
    
    
    POST /api/group/add
    { Description of the group being created in JSON format }

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the group created in JSON format }
    }

Example
    
    
    //--- request to the server
    POST /api/group/add
    {
      "Group" : "demo\\forex",
      "Server" : "0",
      "PermissionsFlags" : "2",
      "AuthMode" : "0",
      "AuthPasswordMin" : "5",
    ...
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Group" : "demo\\forex",
        "Server" : "0",
        "PermissionsFlags" : "2",
        "AuthMode" : "0",
        "AuthPasswordMin" : "5",
    ...
      }
    }

## Raw API

Request format
    
    
    GROUP_ADD|\r\n
    Description of the group being created in JSON format

Response format
    
    
    GROUP_ADD|RETCODE=code description|\r\n
    The body of the created group in JSON format

## Request Parameters

This request has no parameters. Description of the group is passed in the JSON format as an additional command body. When adding a group, all its [parameters (#group)](Data-Structure.md#group) must be set.

The JSON description of the group passed when creating is the same as the description returned by the server.

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — description of the group created in JSON format. The description of the passed parameters is given in the "[Data structure](Data-Structure.md)" section



## Notes

  * This command works only when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * When the command is run the presence of the group you are adding is checked. The key field for comparison is the name of the group (including the path). If such a group already exists, its settings are updated.
  * When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged.
  * Before adding, the correctness of the record is checked. If the entry is incorrect, it returns the error code [3](../../../../Return-Codes/Common-errors.md).
  * To enable a newly added group, [restart the main trade server](../Network/Restart-Server.md).



Groups can be edited in two modes, depending on the permissions of the manager account which is used for the [Web API client connection](../../Text-Protocol-(Raw-API)/Authentication.md#client-start). An administrator account with the group editing permission allows adding groups and editing the parameters of existing groups to which the account has access. A manager account with the RIGHT_GRP_DETAILS_MARGIN and RIGHT_GRP_DETAILS_COMMISSION rights allows changing a limited set of parameters of existing groups:

  * MarginCall
  * MarginStopOut
  * MarginSOMode
  * EnTradeFlags::TRADEFLAGS_SO_COMPENSATION
  * Commission parameters
  * Group symbol parameters:


  * Path
  * SpreadDiff
  * SpreadDiffBalance
  * MarginInitial
  * MaringMaintenance
  * MarginHedged
  * MarginHedged
  * MarginFlags
  * MarginRateInitial
  * MarginRateMaintenance
  * MarginRateLiquidity
  * MarginRateCurrency
  * SwapMode
  * SwapLong
  * SwapShort
  * Swap3Day


