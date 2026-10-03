[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Additional Parameters](../Additional-Parameters.md) / IMTConParamArray

[Previous](IMTConParam/ValueColor.md) | [Next](IMTConParamArray/Release.md)

# IMTConParamArray

The IMTConParamArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTConParamArray/Release.md) | Delete the current object.  
[Assign](IMTConParamArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConParamArray/Clear.md) | Clear an object.  
[Add](IMTConParamArray/Add.md) | Adds an object of a parameter or array of parameters at the end of an array.  
[AddCopy](IMTConParamArray/AddCopy.md) | Adds a copy of a parameter object of an array of copies at the end of an array.  
[Delete](IMTConParamArray/Delete.md) | Deletes an object of a parameter at the specified position.  
[Detach](IMTConParamArray/Detach.md) | Detaches an object of a parameter from an array.  
[Update](IMTConParamArray/Update.md) | Changes a parameter at the specified position of an array.  
[UpdateCopy](IMTConParamArray/UpdateCopy.md) | Changes a parameter at the specified position of an array by copying the passed parameter object.  
[Shift](IMTConParamArray/Shift.md) | Changes the position of a parameter in an array.  
[Total](IMTConParamArray/Total.md) | Gets the number of objects of parameters in an array.  
[Next](IMTConParamArray/Next.md) | Gets an object of a parameter at the specified position.  
[Sort](IMTConParamArray/Sort.md) | Sort an array using the sort function passed.  
[Search](IMTConParamArray/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTConParamArray/SearchGreatOrEq.md) | Search in an array the first element greater than or equal to the search key.  
[SearchGreater](IMTConParamArray/SearchGreater.md) | Search in an array the first element greater than the search key.  
[SearchLessOrEq](IMTConParamArray/SearchLessOrEq.md) | Search in an array the first element less than or equal to the search key.  
[SearchLess](IMTConParamArray/SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTConParamArray/SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTConParamArray/SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTConParamArray/Add.md), [updating](IMTConParamArray/Update.md) and [removing](IMTConParamArray/Delete.md) array elements.
  * Never add a link (when [adding](IMTConParamArray/Add.md) or [updating](IMTConParamArray/Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


