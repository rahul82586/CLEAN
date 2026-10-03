[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Get Comment

[Previous](Delete-Comment.md) | [Next](Add-Attachment.md)

# Get a Comment on a Document or Client

The request allows receiving a comment added to a document or to a client record.

## Rest API

Request Format
    
    
    GET /api/comment/get?id=list of IDs
    GET /api/comment/get?client=list of identifiers&position=position&total=number
    GET /api/comment/get?document=list of identifiers&position=position&total=number
    POST /api/comment/get?id=list of IDs
    POST /api/comment/get?client=list of identifiers&position=position&total=number
    POST /api/comment/get?document=list of identifiers&position=position&total=number

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [
        {
        comment description
        },
        {
        comment description
        },
        ...
      ]
    }

The example
    
    
    //--- request to the server
    GET /api/comment/get?client=1032&position=0&total=2
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        {
          "RecordID" : "1278",
          "RelatedClient" : "1032",    
          "Flags" : "0",
          "Text" : "<font face=\"Tahoma\">Called client, no answer<\/font>",
          "CommentType" : "2"
          ...
        },
        {
          "RecordID" : "1279",
          "RelatedClient" : "1032",    
          "Flags" : "0",
          "Text" : "<font face=\"Tahoma\">Called client, ready to proceed with registration<\/font>",
          "CommentType" : "2"
          ...
        }
      ]
    }

## Raw API

Request Format
    
    
    COMMENT_GET|ID=identifiers|\r\n
    COMMENT_GET|ID=identifiers|POSITION=position|TOTAL=number|\r\n

Response Format
    
    
    COMMENT_GET|RETCODE=code description|\r\n
    An array of document descriptions in JSON format

## Request Parameters

  * id — IDs of comments, data on which you wish to obtain. Specified as a comma separated list.
  * client — IDs of clients, for whom you wish to obtain comments. With this parameter, comments can be additionally filtered using parameters "position" and "total".
  * document — identifiers of documents for which you wish to receive comments. With this parameter, comments can be additionally filtered using parameters "position" and "total".
  * position — position in the list of client or document comments, starting with which comments should be obtained. An optional parameter which can be used together with the "client" or "document" parameter. It is equal to 0 by default (the first position in the list).
  * total — the number of comments which should be obtained. An optional parameter which can be used together with the "client" or "document" parameter. All comments are requested by default.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — an array of comment descriptions in JSON format. The complete description of passed parameters is available under the ["Data structure" (#comment)](Data-Structure.md#comment) section.


