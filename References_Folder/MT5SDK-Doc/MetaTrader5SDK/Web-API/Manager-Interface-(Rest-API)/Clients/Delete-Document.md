[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Delete Document

[Previous](Update-Document.md) | [Next](Get-Document.md)

# Delete Client Document

The request allows deleting a document from a client record.

## Rest API

Request Format
    
    
    GET /api/document/delete?id=list of IDs
    POST /api/document/delete?id=list of IDs

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
    GET /api/document/delete?id=1278,1279
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
    
    
    DOCUMENT_DELETE|ID=identifiers|\r\n

Response Format
    
    
    DOCUMENT_DELETE|\r\n
    Client IDs and response codes

## Request Parameters

  * id — identifiers of documents to be deleted. Specified as a comma separated list.



## Response Parameters

  * id — identifier of a deleted document.
  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

A document can only be deleted from the applications connected to the trade server, on which the document was created. For all other applications, the response code [12001](../../../Return-Codes/API.md) is returned. If the object is not found, the response code [13](../../../Return-Codes/Common-errors.md) is returned.
