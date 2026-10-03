[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Add Comment

[Previous](Get-Document-History.md) | [Next](Update-Comment.md)

# Add a Comment to a Document or Client

The request allows adding a comment to a client record or to a document.

## Rest API

Request Format
    
    
    POST /api/comment/add
    [ One or more comment descriptions in JSON format ]

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
    POST /api/comment/add
    [
      {
        "RelatedClient" : "1032",    
        "Flags" : "0",
        "Text" : "<font face=\"Tahoma\">Called client, no answer<\/font>",
        "CommentType" : "2"
      },
      {
        "RelatedClient" : "1032",    
        "Flags" : "0",
        "Text" : "<font face=\"Tahoma\">Called client, ready to proceed with registration<\/font>",
        "CommentType" : "2"
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
    
    
    COMMENT_ADD|\r\n
    Comment description in JSON format

Response Format
    
    
    COMMENT_ADD|\r\n
    Comment IDs and response codes

## Request Parameters

The request has no parameters. The description of the comment to be created is passed in the JSON body of the request.

The mandatory field is "RelatedClient" or "RelatedDocument", based on which the comment is bound to a client record or to a document. The complete description of the possible user parameters is provided in the ["Data structure" (#comment)](Data-Structure.md#comment) section.

The JSON description of the document passed when creating is the same as the description returned by the server. For example;
    
    
    {
      "RelatedClient" : "1032",    
      "Flags" : "0",
      "Text" : "<font face=\"Tahoma\">Called client, no answer<\/font>",
      "CommentType" : "2"
      ...
    }

## Response Parameters

  * id — created comment identifier.
  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

A comment can only be added from the applications connected to the trading server on which the client was created. For all other applications, the response code [12001](../../../Return-Codes/API.md) is returned. If the client is not found, the response code [13](../../../Return-Codes/Common-errors.md) is returned.
