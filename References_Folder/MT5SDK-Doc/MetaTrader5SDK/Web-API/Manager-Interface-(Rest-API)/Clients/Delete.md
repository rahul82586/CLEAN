[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Delete

[Previous](Update.md) | [Next](Get.md)

# Delete Client

The request allows deleting a client from the server.

## Rest API

Request Format
    
    
    GET /api/client/delete?id=list of IDs
    POST /api/client/delete?id=list of IDs

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
    GET /api/client/delete?id=1278,1279
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
    
    
    CLIENT_DELETE|ID=identifiers|\r\n

Response Format
    
    
    CLIENT_DELETE|\r\n
    Client IDs and response codes

## Request Parameters

  * id — IDs of clients to be deleted. Specified as a comma separated list.



## Response Parameters

  * id — deleted client ID.
  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

A client can only be deleted from the applications connected to the trade server, on which the client was created. For all other applications, the response code [12001](../../../Return-Codes/API.md) is returned. If the object is not found, the response code [13](../../../Return-Codes/Common-errors.md) is returned.
