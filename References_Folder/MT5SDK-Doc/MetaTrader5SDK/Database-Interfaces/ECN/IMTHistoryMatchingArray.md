[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTHistoryMatchingArray

[Previous](IMTECNHistoryMatching/IMTHistoryMatching-VolumeCurrentClientExt.md) | [Next](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Release.md)

# IMTECNHistoryMatchingArray

The interface enables convenient operations with arrays of matching orders from the history. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Release.md) | Delete the current object.  
[Assign](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Clear.md) | Clear an object.  
[Add](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Add.md) | Add an object or an array of objects of matching orders to the end of an array.  
[AddCopy](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-AddCopy.md) | Add a copy of an object or an array of objects of matching orders to the end of an array.  
[Delete](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Delete.md) | Delete a matching order object by its position.  
[Detach](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Detach.md) | Detach a matching order object from an array.  
[Update](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Update.md) | Update a matching order at the specified array position.  
[UpdateCopy](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-UpdateCopy.md) | Update a matching order at the specified array position by copying the parameters of a passed order object.  
[Shift](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Shift.md) | Change the position of a matching order in the array.  
[Total](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Total.md) | Get the number of matching order objects in the array.  
[Next](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Next.md) | Get a matching order object by its position.  
[Sort](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Sort.md) | Sort an array using the passed sort function.  
[Search](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces rather than the data. This sets specific operating features when [adding](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Add.md), [updating](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Update.md) and [deleting](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Delete.md) array elements.
  * Never add a link to one and the same object into an array (when [adding](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Add.md) or [updating](IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Update.md) an element), because this will lead to a crash during memory release.


