[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / IMTPositionArray

[Previous](IMTPosition/ReasonSet.md) | [Next](IMTPositionArray/Release.md)

# IMTPositionArray

The IMTPositionArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTPositionArray/Release.md) | Delete the current object.  
[Assign](IMTPositionArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTPositionArray/Clear.md) | Clear an object.  
[Add](IMTPositionArray/Add.md) | Add an object of a position or array of positions at the end of an array.  
[AddCopy](IMTPositionArray/AddCopy.md) | Add a copy of an object of a position or array of positions at the end of an array.  
[Delete](IMTPositionArray/Delete.md) | Delete the object of a trade position by the index.  
[Detach](IMTPositionArray/Detach.md) | Detach an object of a trade position from an array.  
[Update](IMTPositionArray/Update.md) | Change a trade position at the specified index of an array.  
[UpdateCopy](IMTPositionArray/UpdateCopy.md) | Change a trade position at the specified position of an array by copying the parameters of a passed object of a trade position.  
[Shift](IMTPositionArray/Shift.md) | Shift a trade position in an array.  
[Total](IMTPositionArray/Total.md) | Get the number of objects of trade positions in an array.  
[Next](IMTPositionArray/Next.md) | Get an object of a trade position by the index.  
[Sort](IMTPositionArray/Sort.md) | Sort an array using the sort function passed.  
[Search](IMTPositionArray/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTPositionArray/SearchGreatOrEq.md) | Search in an array the first element greater than or equal to the search key.  
[SearchGreater](IMTPositionArray/SearchGreater.md) | Search in an array the first element greater than the search key.  
[SearchLessOrEq](IMTPositionArray/SearchLessOrEq.md) | Search in an array the first element less than or equal to the search key.  
[SearchLess](IMTPositionArray/SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTPositionArray/SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTPositionArray/SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTPositionArray/Add.md), [updating](IMTPositionArray/Update.md) and [removing](IMTPositionArray/Delete.md) array elements.
  * Never add a link (when [adding](IMTPositionArray/Add.md) or [updating](IMTPositionArray/Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


