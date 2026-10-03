[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Clients](../Clients.md) / IMTAttachment

[Previous](IMTDocumentSink/OnDocumentDelete.md) | [Next](IMTAttachment/Enumerations.md)

# IMTAttachment

The IMTAttachment class is designed for working with [document](IMTDocument.md) files and [attachments in comments](IMTComment.md). The interface contains the following methods:

Method | Purpose  
---|---  
[Release](IMTAttachment/Release.md) | Delete the current object.  
[Assign](IMTAttachment/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTAttachment/Clear.md) | Clear an object.  
[RecordID](IMTAttachment/RecordID.md) | Get and set the attachment identifier.  
[RelatedClient](IMTAttachment/RelatedClient.md) | Get and set the client ID with which the attachment is associated.  
[FileType](IMTAttachment/FileType.md) | Get and set the file type.  
[FileName](IMTAttachment/FileName.md) | Get and set the file name.  
[FileContent](IMTAttachment/FileContent.md) | Get and set the attached file contents.  
[FileSize](IMTAttachment/FileSize.md) | Get and set the attached file size.  
[FileFlags](IMTAttachment/FileFlags.md) | Get and set file flags.  
  
The IMTAttachment class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnFileType (#enfiletype)](IMTAttachment/Enumerations.md#enfiletype) | File types.  
[EnFileFlags (#enfileflags)](IMTAttachment/Enumerations.md#enfileflags) | File flags.
