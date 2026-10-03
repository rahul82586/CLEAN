[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Clients](../Clients.md) / IMTAttachmentArray

[Previous](IMTAttachment/FileFlags.md) | [Next](IMTAttachmentArray/Release.md)

# IMTAttachmentArray

The IMTAttachmentArray class is designed for working with arrays of [document](IMTDocument.md) files and [attachments to comments](IMTComment.md). The interface contains the following methods:

Method | Purpose  
---|---  
[Release](IMTAttachmentArray/Release.md) | Delete the current object.  
[Assign](IMTAttachmentArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTAttachmentArray/Clear.md) | Clear an object.  
[Add](IMTAttachmentArray/Add.md) | Add an attachment object or an array of attachment objects to the end of an array.  
[AddCopy](IMTAttachmentArray/AddCopy.md) | Add a copy of an attachment object or of an array of attachment objects to the end of an array.  
[Delete](IMTAttachmentArray/Delete.md) | Delete an attachment object by its position.  
[Detach](IMTAttachmentArray/Detach.md) | Detach an attachment object from an array.  
[Update](IMTAttachmentArray/Update.md) | Change an attachment at the specified position of the array.  
[UpdateCopy](IMTAttachmentArray/UpdateCopy.md) | Change an attachment at the specified position of an array by copying the parameters of a passed attachment object.  
[Shift](IMTAttachmentArray/Shift.md) | Change the attachment position in an array.  
[Total](IMTAttachmentArray/Total.md) | Get the number of attachment objects in an array.  
[Next](IMTAttachmentArray/Next.md) | Get an attachment object by its position.  
[Sort](IMTAttachmentArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTAttachmentArray/Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTAttachmentArray/SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTAttachmentArray/SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTAttachmentArray/SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTAttachmentArray/SearchLess.md) | Search in an array for the first element less than the search key.  
[SearchLeft](IMTAttachmentArray/SearchLeft.md) | Search in an array for the first element equal to the search key.  
[SearchRight](IMTAttachmentArray/SearchRight.md) | Search in an array for the last element equal to the search key.  
  
## Working with Arrays

Please note the following specific features when working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This causes some specific features when [adding](IMTAttachmentArray/Add.md), [updating](IMTAttachmentArray/Update.md) and [deleting](IMTAttachmentArray/Delete.md) array elements.
  * Never add a link to one and the same object in an array (when [adding](IMTAttachmentArray/Add.md) or [updating](IMTAttachmentArray/Update.md) elements), because this will lead to a crash during memory release.


