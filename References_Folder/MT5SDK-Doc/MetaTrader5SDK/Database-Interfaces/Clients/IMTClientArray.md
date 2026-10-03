[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Clients](../Clients.md) / IMTClientArray

[Previous](IMTClient/ClientExternalID.md) | [Next](IMTClientArray/Release.md)

# IMTClientArray

The IMTClientArray class is designed for operations with arrays of client records. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTClientArray/Release.md) | Delete the current object.  
[Assign](IMTClientArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTClientArray/Clear.md) | Clear an object.  
[Add](IMTClientArray/Add.md) | Add a client object or an array of client objects to the end of an array.  
[AddCopy](IMTClientArray/AddCopy.md) | Add a copy of a client object or an array of client objects to the end of an array.  
[Delete](IMTClientArray/Delete.md) | Delete a client object by its position.  
[Detach](IMTClientArray/Detach.md) | Detach a client object from an array.  
[Update](IMTClientArray/Update.md) | Change a client at the specified position of an array.  
[UpdateCopy](IMTClientArray/UpdateCopy.md) | Change a client at the specified position of an array by copying the parameters of a passed client object.  
[Shift](IMTClientArray/Shift.md) | Change the position of a client in an array.  
[Total](IMTClientArray/Total.md) | Get the number of client objects in an array.  
[Next](IMTClientArray/Next.md) | Get a client object by its position.  
[Sort](IMTClientArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTClientArray/Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTClientArray/SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTClientArray/SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTClientArray/SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTClientArray/SearchLess.md) | Search in an array for the first element less than the search key.  
[SearchLeft](IMTClientArray/SearchLeft.md) | Search in an array for the first element equal to the search key.  
[SearchRight](IMTClientArray/SearchRight.md) | Search in an array for the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for operations with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This sets some specific features when [adding](IMTClientArray/Add.md), [updating](IMTClientArray/Update.md) and [deleting](IMTClientArray/Delete.md) array elements.
  * Never add a link to one and the same object in an array (when [adding](IMTClientArray/Add.md) or [updating](IMTClientArray/Update.md) an element), because this will lead to a crash during memory release.


