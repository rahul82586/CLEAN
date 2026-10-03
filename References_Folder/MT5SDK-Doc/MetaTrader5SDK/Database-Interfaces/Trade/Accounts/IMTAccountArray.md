[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Accounts](../Accounts.md) / IMTAccountArray

[Previous](IMTAccount/Liabilities.md) | [Next](IMTAccountArray/Release.md)

# IMTAccountArray

The IMTAccountArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTAccountArray/Release.md) | Delete the current object.  
[Assign](IMTAccountArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTAccountArray/Clear.md) | Clear an object.  
[Add](IMTAccountArray/Add.md) | Adds an object or an array of objects of trading accounts at the end of the array.  
[AddCopy](IMTAccountArray/AddCopy.md) | Adds a copy of an object or an array of objects of trading accounts at the end of an array.  
[Delete](IMTAccountArray/Delete.md) | Deletes an object of a trading account by position.  
[Detach](IMTAccountArray/Detach.md) | Detaches an object of a trading account from an array.  
[Update](IMTAccountArray/Update.md) | Changes a trading account at the specified position of an array.  
[UpdateCopy](IMTAccountArray/UpdateCopy.md) | Changes a trading account at the specified position of an array by copying the parameters of a passed object of the trading account.  
[Shift](IMTAccountArray/Shift.md) | Changes the position of a trading account in an array.  
[Total](IMTAccountArray/Total.md) | Gets the number of objects of trading accounts in an array.  
[Next](IMTAccountArray/Next.md) | Gets an object of a trading account by position.  
[Sort](IMTAccountArray/Sort.md) | Sort an array using the sort function passed.  
[Search](IMTAccountArray/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTAccountArray/SearchGreatOrEq.md) | Search in an array the first element greater than or equal to the search key.  
[SearchGreater](IMTAccountArray/SearchGreater.md) | Search in an array the first element greater than the search key.  
[SearchLessOrEq](IMTAccountArray/SearchLessOrEq.md) | Search in an array the first element less than or equal to the search key.  
[SearchLess](IMTAccountArray/SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTAccountArray/SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTAccountArray/SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTAccountArray/Add.md), [updating](IMTAccountArray/Update.md) and [removing](IMTAccountArray/Delete.md) array elements.
  * Never add a link (when [adding](IMTAccountArray/Add.md) or [updating](IMTAccountArray/Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


