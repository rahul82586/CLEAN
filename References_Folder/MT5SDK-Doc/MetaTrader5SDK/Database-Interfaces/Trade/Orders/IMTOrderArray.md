[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / IMTOrderArray

[Previous](IMTOrder/ModificationFlags.md) | [Next](IMTOrderArray/Release.md)

# IMTOrderArray

The IMTOrderArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTOrderArray/Release.md) | Delete the current object.  
[Assign](IMTOrderArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTOrderArray/Clear.md) | Clear an object.  
[Add](IMTOrderArray/Add.md) | Adds an object or an array of objects of trade orders at the end of an array.  
[AddCopy](IMTOrderArray/AddCopy.md) | Add a copy of an object or an array of objects of trade orders at the end of an array.  
[Delete](IMTOrderArray/Delete.md) | Delete an object of a trade order by its position.  
[Detach](IMTOrderArray/Detach.md) | Detach an object of a trade order from an array.  
[Update](IMTOrderArray/Update.md) | Changes an order at the specified position of an array.  
[UpdateCopy](IMTOrderArray/UpdateCopy.md) | Change an order at the specified position of an array by copying the parameters of a passed object of an order.  
[Shift](IMTOrderArray/Shift.md) | Change the position of an order in an array.  
[Total](IMTOrderArray/Total.md) | Get the number of objects of trade orders in an array.  
[Next](IMTOrderArray/Next.md) | Get an object of a trade order by its position.  
[Sort](IMTOrderArray/Sort.md) | Sort an array using the sort function passed.  
[Search](IMTOrderArray/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTOrderArray/SearchGreatOrEq.md) | Search in an array the first element greater than or equal to the search key.  
[SearchGreater](IMTOrderArray/SearchGreater.md) | Search in an array the first element greater than the search key.  
[SearchLessOrEq](IMTOrderArray/SearchLessOrEq.md) | Search in an array the first element less than or equal to the search key.  
[SearchLess](IMTOrderArray/SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTOrderArray/SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTOrderArray/SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTOrderArray/Add.md), [updating](IMTOrderArray/Update.md) and [removing](IMTOrderArray/Delete.md) array elements.
  * Never add a link (when [adding](IMTOrderArray/Add.md) or [updating](IMTOrderArray/Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


