[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Groups](../Groups.md) / IMTConGroupArray

[Previous](IMTConGroupSymbol/BookDepthLimit.md) | [Next](IMTConGroupArray/Release.md)

# IMTConGroupArray

The IMTConGroupArray class contains methods for working with an array of group settings:

Method | Purpose  
---|---  
[Release](IMTConGroupArray/Release.md) | Delete the current object.  
[Assign](IMTConGroupArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConGroupArray/Clear.md) | Clear an object.  
[Add](IMTConGroupArray/Add.md) | Add a group object or a group array object to the array end.  
[AddCopy](IMTConGroupArray/AddCopy.md) | Add a copy of a group object or of a group array object to the array end.  
[Delete](IMTConGroupArray/Delete.md) | Delete a group object by position.  
[Detach](IMTConGroupArray/Detach.md) | Detach a group object from an array.  
[Update](IMTConGroupArray/Update.md) | Update a group at the specified position of an array.  
[UpdateCopy](IMTConGroupArray/UpdateCopy.md) | Update a group at the specified position of an array by copying the parameters of a passed group object.  
[Shift](IMTConGroupArray/Shift.md) | Change the position of a group in an array.  
[Total](IMTConGroupArray/Total.md) | Get the number of group objects in an array.  
[Next](IMTConGroupArray/Next.md) | Get a group object by position.  
[Sort](IMTConGroupArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTConGroupArray/Search.md) | Search an array for an element that matches the search key.  
[SearchGreatOrEq](IMTConGroupArray/SearchGreatOrEq.md) | Search an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTConGroupArray/SearchGreater.md) | Search an array for the first element greater than the search key.  
[SearchLessOrEq](IMTConGroupArray/SearchLessOrEq.md) | Search an array for the first element less than or equal to the search key.  
[SearchLess](IMTConGroupArray/SearchLess.md) | Search an array for the first element less than the search key.  
[SearchLeft](IMTConGroupArray/SearchLeft.md) | Search an array for the first element equal to the search key.  
[SearchRight](IMTConGroupArray/SearchRight.md) | Search an array for the last element equal to the search key.  
  
## Specific Array Operations

There are a number of specific features for operations with arrays:

  * Arrays store pointers to the appropriate interfaces, not the data itself. This requires some specific behavior [adding](IMTConGroupArray/Add.md), [updating](IMTConGroupArray/Update.md) and [deleting](IMTConGroupArray/Delete.md) array elements.
  * Please be sure to never add a link to one and the same object within an array (when [adding](IMTConGroupArray/Add.md) or [updating](IMTConGroupArray/Update.md) an element), as this will lead to a crash during memory release.


