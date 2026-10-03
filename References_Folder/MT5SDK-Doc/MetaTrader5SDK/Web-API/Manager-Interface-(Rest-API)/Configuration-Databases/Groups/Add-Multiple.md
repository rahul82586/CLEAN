[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Add Multiple

[Previous](Add.md) | [Next](Delete.md)

# Add Multiple Groups

Using the request you can create or update multiple groups of clients on a server.

## Rest API

Request format
    
    
    POST /api/group/add_batch
    [ Description of groups to be created, in JSON format ]

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [ Description of created groups, in JSON format ]
    }

Example
    
    
    //--- request to the server
    POST /api/group/add_batch
    [
      {
       "Group" : "demo\\forex-usd",
       "Server" : "0",
       "PermissionsFlags" : "2",
       "AuthMode" : "0",
       "AuthPasswordMin" : "5",
       ...
      },
      {
       "Group" : "demo\\forex-eur",
       "Server" : "0",
       "PermissionsFlags" : "2",
       "AuthMode" : "0",
       "AuthPasswordMin" : "5",
       ...
      }
    ]
    //--- server response
    [
      {
       "retcode" : "0 Done",
       "answer" : {
          "Group" : "demo\\forex-usd",
          "Server" : "0",
          "PermissionsFlags" : "2",
          "AuthMode" : "0",
          "AuthPasswordMin" : "5",
          ...
      },
      {
      "retcode" : "0 Done",
      "answer" : {
        "Group" : "demo\\forex-eur",
        "Server" : "0",
        "PermissionsFlags" : "2",
        "AuthMode" : "0",
        "AuthPasswordMin" : "5",
        ...
      }
    ]

## Raw API

Request format
    
    
    GROUP_ADD|\r\n
    Description of groups to be created, in JSON format

Response format
    
    
    GROUP_ADD|RETCODE=code description|\r\n
    Description of created groups in JSON format

## Request Parameters

The request has no parameters. Description of the groups is passed in JSON format as an additional body. When adding a group, all its [parameters (#group)](Data-Structure.md#group) must be specified.

The JSON description of the group passed when creating is the same as the description returned by the server.

## Response parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — the description of the created groups in JSON format. The description of passed parameters is provided under the "[Data structure](Data-Structure.md)" section



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * During request execution, the presence of the group you are adding is checked. The key field for comparison is the name of the group (including the path). If such a group already exists, its settings are updated.
  * When you update the configuration, only those group parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged. Parameters passed as arrays will be updated completely. For example, if you only specify part of the symbol settings in the symbols array, all unspecified settings will be erased, as the new description will completely replace the existing one.
  * The record correctness is checked before the configuration is added. If the record is incorrect, the error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To enable the newly added groups, [restart the main trade server](../Network/Restart-Server.md).



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


