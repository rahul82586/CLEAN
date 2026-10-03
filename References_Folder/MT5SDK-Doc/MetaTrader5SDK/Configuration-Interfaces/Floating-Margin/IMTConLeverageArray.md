[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Floating Margin](../Floating-Margin.md) / IMTConLeverageArray

[Previous](IMTConLeverage/RuleGet.md) | [Next](IMTConLeverageArray/Release.md)

# IMTConLeverageArray

The IMTConLeverageArray class contains methods for working with an array of floating margin configurations:

Method | Purpose  
---|---  
[Release](IMTConLeverageArray/Release.md) | Delete the current object.  
[Assign](IMTConLeverageArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConLeverageArray/Clear.md) | Clear an object.  
[Add](IMTConLeverageArray/Add.md) | Add an object of a floating margin configuration or an array of configurations to the end the array.  
[AddCopy](IMTConLeverageArray/AddCopy.md) | Add a copy of the floating margin configuration object or an array of copies to the end of the array.  
[Delete](IMTConLeverageArray/Delete.md) | Delete a floating margin configuration object by position.  
[Detach](IMTConLeverageArray/Detach.md) | Detach a floating margin configuration object from the array.  
[Update](IMTConLeverageArray/Update.md) | Update the floating margin configuration at the specified array position.  
[UpdateCopy](IMTConLeverageArray/UpdateCopy.md) | Update the floating margin configuration at the specified array position by copying the passed configuration object.  
[Shift](IMTConLeverageArray/Shift.md) | Change the position of a floating margin configuration in the array.  
[Total](IMTConLeverageArray/Total.md) | Get the number of floating margin configuration objects in the array.  
[Next](IMTConLeverageArray/Next.md) | Get a floating margin configuration object by position.  
[Sort](IMTConLeverageArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTConLeverageArray/Search.md) | Search an array for an element that matches the search key.  
[SearchGreatOrEq](IMTConLeverageArray/SearchGreatOrEq.md) | Search an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTConLeverageArray/SearchGreater.md) | Search an array for the first element greater than the search key.  
[SearchLessOrEq](IMTConLeverageArray/SearchLessOrEq.md) | Search an array for the first element less than or equal to the search key.  
[SearchLess](IMTConLeverageArray/SearchLess.md) | Search an array for the first element less than the search key.  
[SearchLeft](IMTConLeverageArray/SearchLeft.md) | Search an array for the first element equal to the search key.  
[SearchRight](IMTConLeverageArray/SearchRight.md) | Search an array for the last element equal to the search key.  
  
## Specifics of Array Operations

Please mind the following points while working with arrays:

  * Arrays store pointers to the appropriate interfaces, not the data. This determines specific operation features when [adding](IMTConLeverageArray/Add.md), [update](IMTConLeverageArray/Update.md), and [deleting](IMTConLeverageArray/Delete.md) array elements.
  * Never add a reference to the same object into an array (when [adding](IMTConLeverageArray/Add.md) or [updating](IMTConLeverageArray/Update.md) an element), as this will lead to a crash when freeing the memory.


