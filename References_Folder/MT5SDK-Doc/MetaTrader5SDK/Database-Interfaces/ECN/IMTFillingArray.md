[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTFillingArray

[Previous](IMTECNFilling/IMTFilling-Comment.md) | [Next](IMTECNFillingArray/IMTFillingArray-Release.md)

# IMTECNFillingArray

The interface enables convenient operations with arrays of filling orders. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTECNFillingArray/IMTFillingArray-Release.md) | Delete the current object.  
[Assign](IMTECNFillingArray/IMTFillingArray-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNFillingArray/IMTFillingArray-Clear.md) | Clear an object.  
[Add](IMTECNFillingArray/IMTFillingArray-Add.md) | Add an object or an array of objects of filling orders to the end of an array.  
[AddCopy](IMTECNFillingArray/IMTFillingArray-AddCopy.md) | Add a copy of an object or of an array of objects of filling orders to the end of an array.  
[Delete](IMTECNFillingArray/IMTFillingArray-Delete.md) | Delete a filling order object by its position.  
[Detach](IMTECNFillingArray/IMTFillingArray-Detach.md) | Detach a filling order object from an array.  
[Update](IMTECNFillingArray/IMTFillingArray-Update.md) | Update a filling order at the specified array position.  
[UpdateCopy](IMTECNFillingArray/IMTFillingArray-UpdateCopy.md) | Update a filling order at the specified array position by copying parameters of the passed order object.  
[Shift](IMTECNFillingArray/IMTFillingArray-Shift.md) | Change the position of a filling order in the array.  
[Total](IMTECNFillingArray/IMTFillingArray-Total.md) | Get the total number of filling orders in the array.  
[Next](IMTECNFillingArray/IMTFillingArray-Next.md) | Get the filling order object by its position.  
[Sort](IMTECNFillingArray/IMTFillingArray-Sort.md) | Sort an array using the passed sort function.  
[Search](IMTECNFillingArray/IMTFillingArray-Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTECNFillingArray/IMTFillingArray-SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTECNFillingArray/IMTFillingArray-SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTECNFillingArray/IMTFillingArray-SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTECNFillingArray/IMTFillingArray-SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTECNFillingArray/IMTFillingArray-SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTECNFillingArray/IMTFillingArray-SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces rather than the data. This sets specific operating features when [adding](IMTECNFillingArray/IMTFillingArray-Add.md), [updating](IMTECNFillingArray/IMTFillingArray-Update.md) and [deleting](IMTECNFillingArray/IMTFillingArray-Delete.md) array elements.
  * Never add a link to one and the same object into an array (when [adding](IMTECNFillingArray/IMTFillingArray-Add.md) or [updating](IMTECNFillingArray/IMTFillingArray-Update.md) an element), because this will lead to a crash during memory release.


