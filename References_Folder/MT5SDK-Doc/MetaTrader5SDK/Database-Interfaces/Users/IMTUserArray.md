[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Users](../Users.md) / IMTUserArray

[Previous](IMTUser/ExternalAccountGet.md) | [Next](IMTUserArray/Release.md)

# IMTUserArray

The IMTUserArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTUserArray/Release.md) | Delete the current object.  
[Assign](IMTUserArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTUserArray/Clear.md) | Clear an object.  
[Add](IMTUserArray/Add.md) | Add an object or an array of objects of client records at the end of an array.  
[AddCopy](IMTUserArray/AddCopy.md) | Add a copy of an object or an array of objects of client records at the end of an array.  
[Delete](IMTUserArray/Delete.md) | Delete a client record object by its position.  
[Detach](IMTUserArray/Detach.md) | Detach a client record object from an array.  
[Update](IMTUserArray/Update.md) | Change a client record at the specified position of an array.  
[UpdateCopy](IMTUserArray/UpdateCopy.md) | Change a client record at the specified position of an array by copying the parameters of a passed object of a client record.  
[Shift](IMTUserArray/Shift.md) | Change the position of a client record in an array.  
[Total](IMTUserArray/Total.md) | Get the number of client record objects in an array.  
[Next](IMTUserArray/Next.md) | Get a client record object by its position.  
[Sort](IMTUserArray/Sort.md) | Sort an array using the sort function passed.  
[Search](IMTUserArray/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTUserArray/SearchGreatOrEq.md) | Search in an array the first element greater than or equal to the search key.  
[SearchGreater](IMTUserArray/SearchGreater.md) | Search in an array the first element greater than the search key.  
[SearchLessOrEq](IMTUserArray/SearchLessOrEq.md) | Search in an array the first element less than or equal to the search key.  
[SearchLess](IMTUserArray/SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTUserArray/SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTUserArray/SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTUserArray/Add.md), [updating](IMTUserArray/Update.md) and [removing](IMTUserArray/Delete.md) array elements.
  * Never add a link (when [adding](IMTUserArray/Add.md) or [updating](IMTUserArray/Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


