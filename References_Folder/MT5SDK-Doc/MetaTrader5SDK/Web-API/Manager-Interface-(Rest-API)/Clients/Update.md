[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Update

[Previous](Add.md) | [Next](Delete.md)

# Client Update

The request allows updating client data on the server.

## Rest API

Request Format
    
    
    POST /api/client/update
    [ One or more client descriptions in JSON format ]

Response Format
    
    
    [
      {
       "id" : "identifier",
       "retcode" : "code description",
      },
      {
       "id" : "identifier",
       "retcode" : "code description",
      },
      ...
    ]

The example
    
    
    //--- request to the server
    POST /api/client/update
    [
      {
        "RecordID" : "1278",
        "PersonName" : "John",
        "PersonLastName" : "Smith"
        "ClientType" : "1",
        "ClientStatus" : "700",
        "AssignedManager" : "1000"
      },
      {
        "RecordID" : "1279",
        "PersonName" : "Mary",
        "PersonLastName" : "Anne"
        "ClientType" : "1",
        "ClientStatus" : "700",
        "AssignedManager" : "1200"
      }
    ]
    //--- server response
    [
      {
        "id" : "1278",
        "retcode" : "0 Done",
      },
      {
        "id" : "1279",
        "retcode" : "0 Done",
      },
      ...
    ]

## Raw API

Request Format
    
    
    CLIENT_UPDATE|\r\n
    Description of clients in JSON format

Response Format
    
    
    CLIENT_UPDATE|\r\n
    Client IDs and response codes

## Request Parameters

The request has no parameters. The description of the client data to be updated is passed in the JSON body of the request.

The RecordID field is mandatory. The client record is determined by this field. The set of fields to be updated can be any. The complete description of the possible user parameters is provided in the ["Data structure"](Data-Structure.md) section.

The JSON description of the client record passed when updating is the same as the description returned by the server. For example;
    
    
    {
      "ClientType" : "1",
      "ClientStatus" : "700",
      "ClientExternalID" : "",
      "AssignedManager" : "0",
      "Comment" : "automatically generated on startup",
      ...
    }

## Response Parameters

  * id — updated client ID.
  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

A client can only be updated from the applications connected to the trade server, on which the client was created. For all other applications, the response code [12001](../../../Return-Codes/API.md) is returned. If the object is not found, the response code [13](../../../Return-Codes/Common-errors.md) is returned.
