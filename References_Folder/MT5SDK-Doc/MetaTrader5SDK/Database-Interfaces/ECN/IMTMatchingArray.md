[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTMatchingArray

[Previous](IMTECNMatching/IMTMatching-VolumeCurrentClientExt.md) | [Next](IMTECNMatchingArray/IMTMatchingArray-Release.md)

# IMTECNMatchingArray

The interface enables convenient operations with arrays of matching orders. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTECNMatchingArray/IMTMatchingArray-Release.md) | Delete the current object.  
[Assign](IMTECNMatchingArray/IMTMatchingArray-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNMatchingArray/IMTMatchingArray-Clear.md) | Clear an object.  
[Add](IMTECNMatchingArray/IMTMatchingArray-Add.md) | Add an object or an array of objects of matching orders to the end of an array.  
[AddCopy](IMTECNMatchingArray/IMTMatchingArray-AddCopy.md) | Add a copy of an object or an array of objects of matching orders to the end of an array.  
[Delete](IMTECNMatchingArray/IMTMatchingArray-Delete.md) | Delete a matching order object by its position.  
[Detach](IMTECNMatchingArray/IMTMatchingArray-Detach.md) | Detach a matching order object from an array.  
[Update](IMTECNMatchingArray/IMTMatchingArray-Update.md) | Update a matching order at the specified array position.  
[UpdateCopy](IMTECNMatchingArray/IMTMatchingArray-UpdateCopy.md) | Update a matching order at the specified array position by copying the parameters of a passed order object.  
[Shift](IMTECNMatchingArray/IMTMatchingArray-Shift.md) | Change the position of a matching order in the array.  
[Total](IMTECNMatchingArray/IMTMatchingArray-Total.md) | Get the number of matching order objects in the array.  
[Next](IMTECNMatchingArray/IMTMatchingArray-Next.md) | Get a matching order object by its position.  
[Sort](IMTECNMatchingArray/IMTMatchingArray-Sort.md) | Sort an array using the passed sort function.  
[Search](IMTECNMatchingArray/IMTMatchingArray-Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTECNMatchingArray/IMTMatchingArray-SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTECNMatchingArray/IMTMatchingArray-SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTECNMatchingArray/IMTMatchingArray-SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTECNMatchingArray/IMTMatchingArray-SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTECNMatchingArray/IMTMatchingArray-SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTECNMatchingArray/IMTMatchingArray-SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces rather than the data. This sets specific operating features when [adding](IMTECNMatchingArray/IMTMatchingArray-Add.md), [updating](IMTECNMatchingArray/IMTMatchingArray-Update.md) and [deleting](IMTECNMatchingArray/IMTMatchingArray-Delete.md) array elements.
  * Never add a link to one and the same object into an array (when [adding](IMTECNMatchingArray/IMTMatchingArray-Add.md) or [updating](IMTECNMatchingArray/IMTMatchingArray-Update.md) an element), because this will lead to a crash during memory release.


