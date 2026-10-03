[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests IMTRequestArray

[Previous](IMTRequest/Requests-ApiDataClearAll.md) | [Next](IMTRequestArray/Requests-Release.md)

# IMTRequestArray

The IMTRequestArray class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTRequestArray/Requests-Release.md) | Delete the current object.  
[Assign](IMTRequestArray/Requests-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTRequestArray/Requests-Clear.md) | Clear an object.  
[Add](IMTRequestArray/Requests-Add.md) | Add an object of a trade request or array of requests at the end of an array.  
[AddCopy](IMTRequestArray/Requests-AddCopy.md) | Add a copy of an object of a trade request or array of requests at the end of an array.  
[Delete](IMTRequestArray/Requests-Delete.md) | Delete a trade request by its index.  
[Detach](IMTRequestArray/Requests-Detach.md) | Detach an object of a trade request from an array.  
[Update](IMTRequestArray/Requests-Update.md) | Change a trade request at the specified position of an array.  
[UpdateCopy](IMTRequestArray/Requests-UpdateCopy.md) | Change a trade request at the specified position of an array by copying the parameters of a passed object of a trade request.  
[Shift](IMTRequestArray/Requests-Shift.md) | Change the position of a trade request in an array.  
[Total](IMTRequestArray/Requests-Total.md) | Get the number of objects of trade requests in an array.  
[Next](IMTRequestArray/Requests-Next.md) | Get a trade request by its index.  
[Sort](IMTRequestArray/Requests-Sort.md) | Sort an array using the sort function passed.  
[Search](IMTRequestArray/Requests-Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](IMTRequestArray/Requests-SearchGreatOrEq.md) | Search in an array the first element greater than or equal to the search key.  
[SearchGreat](IMTRequestArray/Requests-SearchGreater.md) | Search in an array the first element greater than the search key.  
[SearchLessOrEq](IMTRequestArray/Requests-SearchLessOrEq.md) | Search in an array the first element less than or equal to the search key.  
[SearchLess](IMTRequestArray/Requests-SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTRequestArray/Requests-SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTRequestArray/Requests-SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Working with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces, and not the data. This leads to some operation peculiarities when [adding](IMTRequestArray/Requests-Add.md), [updating](IMTRequestArray/Requests-Update.md) and [removing](IMTRequestArray/Requests-Delete.md) array elements.
  * Never add a link (when [adding](IMTRequestArray/Requests-Add.md) or [updating](IMTRequestArray/Requests-Update.md) an element) to one and the same object in an array, because this will lead to a crash during memory release.


