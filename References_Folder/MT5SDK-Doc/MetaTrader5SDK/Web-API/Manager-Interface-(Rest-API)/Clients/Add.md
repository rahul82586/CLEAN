[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Add

[Previous](Data-Structure.md) | [Next](Update.md)

# Add Client

The request allows creating a client on the server.

## Rest API

Request Format
    
    
    POST /api/client/add
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
    POST /api/client/add
    [
      {
        "PersonName" : "John",
        "PersonLastName" : "Smith"
        "ClientType" : "1",
        "ClientStatus" : "700",
        "AssignedManager" : "1000"
      },
      {
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
    
    
    CLIENT_ADD|\r\n
    Description of clients in JSON format

Response Format
    
    
    CLIENT_ADD|\r\n
    Client IDs and response codes

## Request Parameters

The request has no parameters. The description of the client to be created is passed in the JSON body of the request.

There are no mandatory fields, any data set can be passed. The complete description of the possible user parameters is provided in the ["Data structure"](Data-Structure.md) section.

The JSON description of the client record passed when creating is the same as the description returned by the server. For example;
    
    
    {
      "ClientType" : "1",
      "ClientStatus" : "700",
      "ClientExternalID" : "",
      "AssignedManager" : "0",
      "Comment" : "automatically generated on startup",
      ...
    }

> When creating a client, a check is performed to make sure that the PersonName or ContactEmail parameters are unique for the client database on the server.

## Response Parameters

  * id — created client identifier.
  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * A client can only be added to the database on the server, to which the API application is connected.
  * When creating a client, the sever automatically assigns a unique identifier to this client ([RecordID](Data-Structure.md)). The identifier cannot be set manually.


