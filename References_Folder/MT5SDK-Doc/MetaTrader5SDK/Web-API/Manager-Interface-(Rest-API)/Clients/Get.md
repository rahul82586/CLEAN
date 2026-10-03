[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Get

[Previous](Delete.md) | [Next](Get-Change-History.md)

# Get Client Information

The request allows receiving client information by ID.

## Rest API

Request Format
    
    
    GET /api/client/get?id=list of IDs&group=groups
    POST /api/client/get?id=list of IDs&group=groups

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [
        {
        client description
        },
        {
        client description
        },
        ...
      ]
    }

The example
    
    
    //--- request to the server
    GET /api/client/get?id=1278,1279
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        {
          "RecordID" : "1278",
          "PersonName" : "John",
          "PersonLastName" : "Smith"
          "ClientType" : "1",
          "ClientStatus" : "700",
          "AssignedManager" : "1000"
          ...
        },
        {
          "RecordID" : "1279",
          "PersonName" : "Mary",
          "PersonLastName" : "Anne"
          "ClientType" : "1",
          "ClientStatus" : "700",
          "AssignedManager" : "1200"
        },
        ...
      ]
    }

## Raw API

Request Format
    
    
    CLIENT_GET|ID=identifiers|GROUP=groups|\r\n

Response Format
    
    
    CLIENT_GET|RETCODE=code description|\r\n
    An array of client descriptions in JSON format

## Request Parameters

  * id — IDs of clients, data on which you wish to obtain. Specified as a comma separated list.
  * group — an optional parameter for filtering results by the preferred group ([TradingGroup](Data-Structure.md)) specified for the client. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using "*" (any value) and "!" (exception). For example: "demo*,!demoforex" - all groups with the names beginning with 'demo', except for the group demoforex. The following clients are returned when filter by groups is used:


  * Clients for whom TradingGroup is specified and this group corresponds to the request mask
  * Clients for whom TradingGroup is not specified, but there is at least one [bound account](Bind-Account.md) from the requested group
  * Clients for whom TradingGroup is not specified and there are no bound accounts (to prevent the clients from being lost)



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of client descriptions in JSON format. The complete description of passed parameters is available under the ["Data structure"](Data-Structure.md) section.


