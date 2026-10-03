[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / IMTDealArray

[Previous](IMTDeal/ModificationFlags.md) | [Next](IMTDealArray/Release.md)

# IMTDealArray

The IMTDealArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDealArray/Release.md) | Delete the current object.  
[Assign](IMTDealArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDealArray/Clear.md) | Clear an object.  
[Add](IMTDealArray/Add.md) | Add an object of a deal or array of deals at the end of an array.  
[AddCopy](IMTDealArray/AddCopy.md) | Add a copy of an object of a deal or array of deals at the end of an array.  
[Delete](IMTDealArray/Delete.md) | Delete an object of a deal by its position.  
[Detach](IMTDealArray/Detach.md) | Detach an object of a deal from an array.  
[Update](IMTDealArray/Update.md) | Changes a deal at the specified position of an array.  
[UpdateCopy](IMTDealArray/UpdateCopy.md) | Change a deal at the specified position of an array by copying the parameters of a passed object of a deal.  
[Shift](IMTDealArray/Shift.md) | Change the position of a deal in an array.  
[Total](IMTDealArray/Total.md) | Get the number of objects of deals in an array.  
[Next](IMTDealArray/Next.md) | Get an object of a deal by its position.  
[Sort](IMTDealArray/Sort.md) | Sort an array using the sort function passed.  
[Search](IMTDealArray/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTDealArray/SearchGreatOrEq.md) | Search in an array the first element greater than or equal to the search key.  
[SearchGreater](IMTDealArray/SearchGreater.md) | Search in an array the first element greater than the search key.  
[SearchLessOrEq](IMTDealArray/SearchLessOrEq.md) | Search in an array the first element less than or equal to the search key.  
[SearchLess](IMTDealArray/SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTDealArray/SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTDealArray/SearchRight.md) | Search in an array the first element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTDealArray/Add.md), [updating](IMTDealArray/Update.md) and [removing](IMTDealArray/Delete.md) array elements.
  * Never add a link (when [adding](IMTDealArray/Add.md) or [updating](IMTDealArray/Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


