[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Clients](../Clients.md) / IMTComment

[Previous](IMTClientSink/OnClientDelete.md) | [Next](IMTComment/Enumerations.md)

# IMTComment

The IMTComment class is designed for working with comments on [clients](IMTClient.md) and their [documents](IMTDocument.md). The interface contains the following methods:

Method | Purpose  
---|---  
[Release](IMTComment/Release.md) | Delete the current object.  
[Assign](IMTComment/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTComment/Clear.md) | Clear an object.  
[RecordID](IMTComment/RecordID.md) | Get the comment identifier.  
[RelatedClient](IMTComment/RelatedClient.md) | Get the ID of the client with which the comment is associated.  
[RelatedDocument](IMTComment/RelatedDocument.md) | Get the ID of the document with which the comment is associated.  
[Flags](IMTComment/Flags.md) | Get comment flags.  
[Extra](IMTComment/Extra.md) | Get additional information about the comment.  
[Text](IMTComment/Text.md) | Get the comment text.  
[CommentType](IMTComment/CommentType.md) | Get the comment type.  
[CommentResult](IMTComment/CommentResult.md) | Get a call result from a comment.  
[AttachmentsAdd](IMTComment/AttachmentsAdd.md) | Add an attachment to a comment.  
[AttachmentsClear](IMTComment/AttachmentsClear.md) | Clear the list of comment attachments.  
[AttachmentsTotal](IMTComment/AttachmentsTotal.md) | Get the number of attachments in a comment.  
[AttachmentsNext](IMTComment/AttachmentsNext.md) | Get the comment attachment identifier by index.  
  
The IMTComment class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnCommentFlags (#encommentflags)](IMTComment/Enumerations.md#encommentflags) | Comment flags.  
[EnCommentType (#encommenttype)](IMTComment/Enumerations.md#encommenttype) | Comment types.  
[EnCommentResult (#encommentresult)](IMTComment/Enumerations.md#encommentresult) | Call results.
