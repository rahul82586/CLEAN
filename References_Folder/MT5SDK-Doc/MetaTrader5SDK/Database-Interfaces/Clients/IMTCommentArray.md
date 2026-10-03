[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Clients](../Clients.md) / IMTCommentArray

[Previous](IMTComment/AttachmentsNext.md) | [Next](IMTCommentArray/Release.md)

# IMTCommentArray

The IMTCommentArray class is designed for operations with comment arrays. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTCommentArray/Release.md) | Delete the current object.  
[Assign](IMTCommentArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTCommentArray/Clear.md) | Clear an object.  
[Add](IMTCommentArray/Add.md) | Add a comment object or an array of comment objects to the end of an array.  
[AddCopy](IMTCommentArray/AddCopy.md) | Add a copy of a comment object or an array of comment objects to the end of an array.  
[Delete](IMTCommentArray/Delete.md) | Delete a comment object by its position.  
[Detach](IMTCommentArray/Detach.md) | Detach a comment object from an array.  
[Update](IMTCommentArray/Update.md) | Change a comment at the specified position of an array.  
[UpdateCopy](IMTCommentArray/UpdateCopy.md) | Change a comment at the specified position of an array by copying the parameters of a passed comment object.  
[Shift](IMTCommentArray/Shift.md) | Change the position of a comment in an array.  
[Total](IMTCommentArray/Total.md) | Get the number of comment objects in an array.  
[Next](IMTCommentArray/Next.md) | Get a comment object by its position.  
[Sort](IMTCommentArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTCommentArray/Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTCommentArray/SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTCommentArray/SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTCommentArray/SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTCommentArray/SearchLess.md) | Search in an array for the first element less than the search key.  
[SearchLeft](IMTCommentArray/SearchLeft.md) | Search in an array for the first element equal to the search key.  
[SearchRight](IMTCommentArray/SearchRight.md) | Search in an array for the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for operations with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This sets some specific features when [adding](IMTCommentArray/Add.md), [updating](IMTCommentArray/Update.md) and [deleting](IMTCommentArray/Delete.md) array elements.
  * Never add a link to one and the same object in an array (when [adding](IMTCommentArray/Add.md) or [updating](IMTCommentArray/Update.md) an element), because this will lead to a crash during memory release.


