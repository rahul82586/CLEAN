[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Update Comment

[Previous](Add-Comment.md) | [Next](Delete-Comment.md)

# Update a Document or Client Comment

The request allows changing a comment to a client record or to a document.

## Rest API

Request Format
    
    
    POST /api/comment/update
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
    POST /api/comment/update
    [
      {
        "RecordID" : "1278",
        "RelatedClient" : "1032",    
        "Flags" : "0",
        "Text" : "<font face=\"Tahoma\">Called client, no answer<\/font>",
        "CommentType" : "2"
      },
      {
        "RecordID" : "1279",
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
    
    
    COMMENT_UPDATE|\r\n
    Comment description in JSON format

Response Format
    
    
    COMMENT_UPDATE|\r\n
    Comment IDs and response codes

## Request Parameters

The request has no parameters. The description of comment changes is passed in the JSON body of the request.

The RecordID field is mandatory. The comment to be edited is determined by this field. The complete description of the possible user parameters is provided in the ["Data structure" (#comment)](Data-Structure.md#comment) section.

The JSON description of the document passed when updating is the same as the description returned by the server. For example;
    
    
    {
      "RelatedClient" : "1032",    
      "Flags" : "0",
      "Text" : "<font face=\"Tahoma\">Called client, no answer<\/font>",
      "CommentType" : "2"
      ...
    }

## Response Parameters

  * id — identifier of the updated comment.
  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

A comment can only be updated from the applications connected to the trade server, on which the comment was created. For all other applications, the response code [12001](../../../Return-Codes/API.md) is returned. If the client is not found, the response code [13](../../../Return-Codes/Common-errors.md) is returned.
