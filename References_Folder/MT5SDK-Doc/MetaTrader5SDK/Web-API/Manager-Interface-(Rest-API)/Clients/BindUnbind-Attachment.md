[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / BindUnbind Attachment

[Previous](Get-Attachment.md) | [Next](../Mail.md)

# Bind/Unbind Attachment

The request allows attaching a file or removing an attached files from a comment or a document.

## Rest API

Request Format
    
    
    GET /api/attachment/attach?id=attachments&entity=destination&entity_id=identifier&action=action
    POST /api/attachment/attach?id=attachments&entity=destination&entity_id=identifier&action=action

Response Format
    
    
    {
     "retcode" : "code description",
    }

The example
    
    
    //--- request to the server
    GET /api/attachment/attach?id=731&entity=document&entity_id=41084&action=attach
    //--- server response
    {
      "retcode" : "0 Done",
    }

## Raw API

Request Format
    
    
    ATTACHMENT_ATTACH|ID=attachment|ENTITY=destination|ENTITY_ID=identifier|ACTION=action|\r\n

Response Format
    
    
    ATTACHMENT_ATTACH|RETCODE=code description|\r\n\r\n

## Request Parameters

  * id — attachment identifier. Can be received using [/api/attachment/add](Add-Attachment.md) and [/api/attachment/get](Get-Attachment.md) requests.
  * entity — the entity to which the file is attached (or from which the attachment is removed): document or comment.
  * entity_id — document or comment identifier.
  * action — the action to be performed: attach or detach.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.


