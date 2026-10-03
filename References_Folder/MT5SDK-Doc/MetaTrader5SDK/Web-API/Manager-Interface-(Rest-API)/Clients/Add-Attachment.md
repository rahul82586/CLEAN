[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Add Attachment

[Previous](Get-Comment.md) | [Next](Get-Attachment.md)

# Add Attachment to Database

This request allows adding an attached file to the file database.

## Rest API

Request Format
    
    
    POST /api/attachment/add
    [ One or more attachment descriptions in JSON format ]

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
    POST /api/attachment/add
    [
      {
        "RelatedClient" : "1032",
        "FileType" : "4",
        "FileName" : "image 2020-03-12 09-53.jpg",
      },
      {
        "RelatedClient" : "1032",
        "FileType" : "2",
        "FileName" : "image 2020-03-12 09-54.jpg
      }
    ]
    //--- server response
    [
      {
        "id" : "730",
        "retcode" : "0 Done",
      },
      {
        "id" : "731",
        "retcode" : "0 Done",
      },
      ...
    ]

## Raw API

Request Format
    
    
    ATTACHMENT_ADD|\r\n
    Description of attachments in JSON format

Response Format
    
    
    ATTACHMENT_ADD|\r\n
    Attachment IDs and response codes

## Request Parameters

The request has no parameters. The description of the attachment to be created is passed in the JSON body of the request.

RelatedClient field is mandatory. The complete description of the possible user parameters is provided in the ["Data structure" (#attachment)](Data-Structure.md#attachment) section.

The JSON description of the document passed when creating is the same as the description returned by the server. For example;
    
    
    {
      "RelatedClient" : "1032",
      "FileType" : "2",
      "FileName" : "image 2020-03-12 09-54.jpg
      ...
    }

## Response Parameters

  * id — identifier of the created attachment.
  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

Once the attachment identifier is received, you can add the attachment to a document or a request using the [/api/attachment/attach](BindUnbind-Attachment.md) request.
