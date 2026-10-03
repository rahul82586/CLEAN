[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Online Connections](../Online-Connections.md) / IMTOnlineArray

[Previous](IMTOnline/ComputerID.md) | [Next](IMTOnlineArray/Release.md)

# IMTOnlineArray

The IMTOnlineArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTOnlineArray/Release.md) | Delete the current object.  
[Assign](IMTOnlineArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTOnlineArray/Clear.md) | Clear an object.  
[Add](IMTOnlineArray/Add.md) | Add an object or an array of objects of client records at the end of an array.  
[AddCopy](IMTOnlineArray/AddCopy.md) | Add a copy of an object or an array of objects of client records at the end of an array.  
[Delete](IMTOnlineArray/Delete.md) | Delete a client record object by its position.  
[Detach](IMTOnlineArray/Detach.md) | Detach a client record object from an array.  
[Update](IMTOnlineArray/Update.md) | Change a client record at the specified position of an array.  
[UpdateCopy](IMTOnlineArray/UpdateCopy.md) | Change a client record at the specified position of an array by copying the parameters of a passed object of a client record.  
[Shift](IMTOnlineArray/Shift.md) | Change the position of a client record in an array.  
[Total](IMTOnlineArray/Total.md) | Get the number of client record objects in an array.  
[Next](IMTOnlineArray/Next.md) | Get a client record object by its position.  
[Sort](IMTOnlineArray/Sort.md) | Sort an array using the sort function passed.  
[Search](IMTOnlineArray/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTOnlineArray/SearchGreatOrEq.md) | Searches in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTOnlineArray/SearchGreater.md) | Searches in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTOnlineArray/SearchLessOrEq.md) | Searches in an array for the first element less than or equal to the search key.  
[SearchLess](IMTOnlineArray/SearchLess.md) | Searches in an array for the first element less than the search key.  
[SearchLeft](IMTOnlineArray/SearchLeft.md) | Searches in an array for the first element equal to the search key.  
[SearchRight](IMTOnlineArray/SearchRight.md) | Searches in an array for the last element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTOnlineArray/Add.md), [updating](IMTOnlineArray/Update.md) and [removing](IMTOnlineArray/Delete.md) array elements.
  * Never add a link (when [adding](IMTOnlineArray/Add.md) or [updating](IMTOnlineArray/Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


