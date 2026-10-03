[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTHistoryFillingArray

[Previous](IMTECNHistoryFilling/IMTHistoryFilling-Comment.md) | [Next](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Release.md)

# IMTECNHistoryFillingArray

The interface enables convenient operations with arrays of filling orders in history. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Release.md) | Delete the current object.  
[Assign](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Clear.md) | Clear an object.  
[Add](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Add.md) | Add an object or an array of objects of filling orders to the end of an array.  
[AddCopy](IMTECNHistoryFillingArray/IMTHistoryFillingArray-AddCopy.md) | Add a copy of an object or of an array of objects of filling orders to the end of an array.  
[Delete](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Delete.md) | Delete a filling order object by its position.  
[Detach](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Detach.md) | Detach a filling order object from an array.  
[Update](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Update.md) | Update a filling order at the specified array position.  
[UpdateCopy](IMTECNHistoryFillingArray/IMTHistoryFillingArray-UpdateCopy.md) | Update a filling order at the specified array position by copying parameters of the passed order object.  
[Shift](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Shift.md) | Change the position of a filling order in the array.  
[Total](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Total.md) | Get the total number of filling orders in the array.  
[Next](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Next.md) | Get the filling order object by its position.  
[Sort](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Sort.md) | Sort an array using the passed sort function.  
[Search](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTECNHistoryFillingArray/IMTHistoryFillingArray-SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTECNHistoryFillingArray/IMTHistoryFillingArray-SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTECNHistoryFillingArray/IMTHistoryFillingArray-SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTECNHistoryFillingArray/IMTHistoryFillingArray-SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTECNHistoryFillingArray/IMTHistoryFillingArray-SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTECNHistoryFillingArray/IMTHistoryFillingArray-SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces rather than the data. This sets specific operating features when [adding](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Add.md), [updating](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Update.md) and [deleting](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Delete.md) array elements.
  * Never add a link to one and the same object into an array (when [adding](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Add.md) or [updating](IMTECNHistoryFillingArray/IMTHistoryFillingArray-Update.md) an element), because this will lead to a crash during memory release.


