[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Get Document

[Previous](Delete-Document.md) | [Next](Get-Document-History.md)

# Get Client Document

The request allows receiving a document from a client record.

## Rest API

Request Format
    
    
    GET /api/document/get?id=list of IDs
    GET /api/document/get?client=list of identifiers&position=position&total=number
    POST /api/document/get?id=list of IDs
    POST /api/document/get?client=list of identifiers&position=position&total=number

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [
        {
        document description
        },
        {
        document description
        },
        ...
      ]
    }

The example
    
    
    //--- request to the server
    GET /api/document/get?client=1032&position=0&total=2
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        {
          "RelatedClient" : "1032",
          "DocumentType" : "1",
          "DocumentSubtype" : "2",
          "DocumentName" : "Passport",
          ...
        },
        {
          "RecordID" : "1279",
          "RelatedClient" : "1032",
          "DocumentType" : "2",
          "DocumentSubtype" : "5",
          "DocumentName" : "Utility bill"
          ...
        }
      ]
    }

## Raw API

Request Format
    
    
    DOCUMENT_GET|ID=identifiers|\r\n
    DOCUMENT_GET|ID=identifiers|POSITION=position|TOTAL=number|\r\n

Response Format
    
    
    DOCUMENT_GET|RETCODE=code description|\r\n
    An array of document descriptions in JSON format

## Request Parameters

  * id — IDs of documents, data on which you wish to obtain. Specified as a comma separated list.
  * client — IDs of clients, whose documents should be received. With this parameter, document can be additionally filtered using parameters "position" and "total".
  * position — position in the list of client documents, starting with which documents should be obtained. An optional parameter which can be used together with the "client"parameter. It is equal to 0 by default (the first position in the list).
  * total — the number of client documents which should be obtained. An optional parameter which can be used together with the "client"parameter. All documents are requested by default.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — an array of document descriptions in JSON format. The complete description of passed parameters is available under the ["Data structure" (#document)](Data-Structure.md#document) section.


