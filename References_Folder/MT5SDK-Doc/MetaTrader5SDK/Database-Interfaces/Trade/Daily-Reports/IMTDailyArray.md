[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Daily Reports](../Daily-Reports.md) / IMTDailyArray

[Previous](IMTDaily/OrderGet.md) | [Next](IMTDailyArray/Release.md)

# IMTDailyArray

The IMTConDailyArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTDailyArray/Release.md) | Delete the current object.  
[Assign](IMTDailyArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTDailyArray/Clear.md) | Clear an object.  
[Add](IMTDailyArray/Add.md) | Add an object of a daily report or of an array of daily reports at the end of an array.  
[AddCopy](IMTDailyArray/AddCopy.md) | Add a copy of an object of a daily report or an array of copies at the end of an array.  
[Delete](IMTDailyArray/Delete.md) | Delete an object of a daily report by its position.  
[Detach](IMTDailyArray/Detach.md) | Detach an object of a daily report from an array.  
[Update](IMTDailyArray/Update.md) | Change a daily report at the specified position of an array.  
[UpdateCopy](IMTDailyArray/UpdateCopy.md) | Change a daily report at the specified position of an array by copying the parameters of a passed object of a daily report.  
[Shift](IMTDailyArray/Shift.md) | Change the position of a daily report in an array.  
[Total](IMTDailyArray/Total.md) | Get the number of objects of daily reports in an array.  
[Next](IMTDailyArray/Next.md) | Get an object of a daily report by its position.  
[Sort](IMTDailyArray/Sort.md) | Sort an array using the sort function passed.  
[Search](IMTDailyArray/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTDailyArray/SearchGreatOrEq.md) | Search in an array the first element greater than or equal to the search key.  
[SearchGreater](IMTDailyArray/SearchGreater.md) | Search in an array the first element greater than the search key.  
[SearchLessOrEq](IMTDailyArray/SearchLessOrEq.md) | Search in an array the first element less than or equal to the search key.  
[SearchLess](IMTDailyArray/SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTDailyArray/SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTDailyArray/SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTDailyArray/Add.md), [updating](IMTDailyArray/Update.md) and [removing](IMTDailyArray/Delete.md) array elements.
  * Never add a link (when [adding](IMTDailyArray/Add.md) or [updating](IMTDailyArray/Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


