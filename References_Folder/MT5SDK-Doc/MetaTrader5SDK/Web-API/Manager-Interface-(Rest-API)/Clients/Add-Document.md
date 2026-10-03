[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Add Document

[Previous](Get-Accounts.md) | [Next](Update-Document.md)

# Add a Document to a Client

The request allows adding a document to a client record.

## Rest API

Request Format
    
    
    POST /api/document/add
    [ One or more document descriptions in JSON format ]

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
    POST /api/document/add
    [
      {
        "RelatedClient" : "1032",
        "DocumentType" : "1",
        "DocumentSubtype" : "2",
        "DocumentName" : "Passport"
      },
      {
        "RelatedClient" : "1032",
        "DocumentType" : "2",
        "DocumentSubtype" : "5",
        "DocumentName" : "Utility bill"
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
    
    
    DOCUMENT_ADD|\r\n
    An array of document descriptions in JSON format

Response Format
    
    
    DOCUMENT_ADD|\r\n
    Document IDs and response codes

## Request Parameters

The request has no parameters. The description of the document to be created is passed in the JSON body of the request.

The mandatory field is "RelatedClient", based on which the document is bound to a client record. The complete description of the possible user parameters is provided in the ["Data structure" (#document)](Data-Structure.md#document) section.

The JSON description of the document passed when creating is the same as the description returned by the server. For example;
    
    
    {
        "RelatedClient" : "1032",
        "DocumentType" : "2",
        "DocumentSubtype" : "5",
        "DocumentName" : "Utility bill",
      ...
    }

## Response Parameters

  * id — created document identifier.
  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * A document can only be added from the applications connected to the trading server on which the client was created. For all other applications, the response code [12001](../../../Return-Codes/API.md) is returned. If the client is not found, the response code [13](../../../Return-Codes/Common-errors.md) is returned.
  * If a document is added with the zero identifier ([RecordID (#document)](Data-Structure.md#document)), the ID will be automatically assigned by the server.


