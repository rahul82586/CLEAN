[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Symbols](../Symbols.md) / IMTConSymbolArray

[Previous](IMTConSymbolSession/CloseMinutes.md) | [Next](IMTConSymbolArray/Release.md)

# IMTConSymbolArray

The IMTConSymbolArray class contains methods for working with an array of symbol settings:

Method | Purpose  
---|---  
[Release](IMTConSymbolArray/Release.md) | Delete the current object.  
[Assign](IMTConSymbolArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConSymbolArray/Clear.md) | Clear an object.  
[Add](IMTConSymbolArray/Add.md) | Add a symbol object or a symbol array object to the end of an array.  
[AddCopy](IMTConSymbolArray/AddCopy.md) | Add a copy of a symbol object or of a symbol array object to the array end.  
[Delete](IMTConSymbolArray/Delete.md) | Delete a symbol object by position.  
[Detach](IMTConSymbolArray/Detach.md) | Detach a symbol object from an array.  
[Update](IMTConSymbolArray/Update.md) | Update a symbol at the specified position of an array.  
[UpdateCopy](IMTConSymbolArray/UpdateCopy.md) | Update a symbol at the specified position of an array by copying the parameters of a passed symbol object.  
[Shift](IMTConSymbolArray/Shift.md) | Change the position of a symbol in an array.  
[Total](IMTConSymbolArray/Total.md) | Get the number of symbol objects in an array.  
[Next](IMTConSymbolArray/Next.md) | Get a symbol object by position.  
[Sort](IMTConSymbolArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTConSymbolArray/Search.md) | Search an array for an element that matches the search key.  
[SearchGreatOrEq](IMTConSymbolArray/SearchGreatOrEq.md) | Search an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTConSymbolArray/SearchGreater.md) | Search an array for the first element greater than the search key.  
[SearchLessOrEq](IMTConSymbolArray/SearchLessOrEq.md) | Search an array for the first element less than or equal to the search key.  
[SearchLess](IMTConSymbolArray/SearchLess.md) | Search an array for the first element less than the search key.  
[SearchLeft](IMTConSymbolArray/SearchLeft.md) | Search an array for the first element equal to the search key.  
[SearchRight](IMTConSymbolArray/SearchRight.md) | Search an array for the last element equal to the search key.  
  
## Specific Array Operations

There are a number of specific features for operations with arrays:

  * Arrays store pointers to the appropriate interfaces, not the data itself. This requires some specific behavior [adding](IMTConSymbolArray/Add.md), [updating](IMTConSymbolArray/Update.md) and [deleting](IMTConSymbolArray/Delete.md) array elements.
  * Please be sure to never add a link to one and the same object within an array (when [adding](IMTConSymbolArray/Add.md) or [updating](IMTConSymbolArray/Update.md) an element), as this will lead to a crash during memory release.


