[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Clients](../Clients.md) / IMTDocumentArray

[Previous](IMTDocument/AttachmentsNext.md) | [Next](IMTDocumentArray/Release.md)

# IMTDocumentArray

The IMTDocumentArray class is designed for working with arrays of client documents. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDocumentArray/Release.md) | Delete the current object.  
[Assign](IMTDocumentArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDocumentArray/Clear.md) | Clear an object.  
[Add](IMTDocumentArray/Add.md) | Add a document object or an array of document objects to the end of an array.  
[AddCopy](IMTDocumentArray/AddCopy.md) | Add a copy of a document object or of an array of document objects to the end of an array.  
[Delete](IMTDocumentArray/Delete.md) | Delete a document object by its position.  
[Detach](IMTDocumentArray/Detach.md) | Detach a document object from an array.  
[Update](IMTDocumentArray/Update.md) | Change a document at the specified position of an array.  
[UpdateCopy](IMTDocumentArray/UpdateCopy.md) | Change a document at the specified position of an array by copying the parameters of a passed document object.  
[Shift](IMTDocumentArray/Shift.md) | Change the position of a document in an array.  
[Total](IMTDocumentArray/Total.md) | Get the number of document objects in an array.  
[Next](IMTDocumentArray/Next.md) | Get a document object by its position.  
[Sort](IMTDocumentArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTDocumentArray/Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTDocumentArray/SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTDocumentArray/SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTDocumentArray/SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTDocumentArray/SearchLess.md) | Search in an array for the first element less than the search key.  
[SearchLeft](IMTDocumentArray/SearchLeft.md) | Search in an array for the first element equal to the search key.  
[SearchRight](IMTDocumentArray/SearchRight.md) | Search in an array for the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for operations with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This sets some specific features when [adding](IMTDocumentArray/Add.md), [updating](IMTDocumentArray/Update.md) and [deleting](IMTDocumentArray/Delete.md) array elements.
  * Never add a link to one and the same object in an array (when [adding](IMTDocumentArray/Add.md) or [updating](IMTDocumentArray/Update.md) an element), because this will lead to a crash during memory release.


