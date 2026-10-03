[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Get Attachment

[Previous](Add-Attachment.md) | [Next](BindUnbind-Attachment.md)

# Get Attachment

This request allows receiving attachments from the database by a list of identifiers.

## Rest API

Request Format
    
    
    GET /api/attachment/get?id=list of identifiers
    POST /api/attachment/get?id=list of IDs

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [
        {
        attachment description
        },
        {
        attachment description
        },
        ...
      ]
    }

The example
    
    
    //--- request to the server
    GET /atachment_get?id=1278,1279
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        {
          "RecordID" : "1278",
          "RelatedClient" : "1032",
          "FileType" : "4",
          "FileName" : "image 2020-03-12 09-53.jpg",
          ...
        },
        {
          "RecordID" : "1279",
          "RelatedClient" : "1032",
          "FileType" : "2",
          "FileName" : "image 2020-03-12 09-54.jpg
          ...
        }
      ]
    }

## Raw API

Request Format
    
    
    ATTACHMENT_GET|ID=identifiers|\r\n

Response Format
    
    
    ATTACHMENT_GET|RETCODE=code description|\r\n
    An array of attachment descriptions in JSON format

## Request Parameters

  * id — IDs of attachments, data on which you wish to obtain. Specified as a comma separated list.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — array of attachment descriptions in JSON format. The complete description of passed parameters is available under the ["Data structure" (#attachment)](Data-Structure.md#attachment) section.


