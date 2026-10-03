[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTProviderArray

[Previous](IMTECNProvider/IMTProvider-Version.md) | [Next](IMTECNProviderArray/IMTProviderArray-Release.md)

# IMTECNProviderArray

The interface enables convenient operations with arrays of providers. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTECNProviderArray/IMTProviderArray-Release.md) | Delete the current object.  
[Assign](IMTECNProviderArray/IMTProviderArray-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNProviderArray/IMTProviderArray-Clear.md) | Clear an object.  
[Add](IMTECNProviderArray/IMTProviderArray-Add.md) | Add a provider object or an array of provider objects to the end of an array.  
[AddCopy](IMTECNProviderArray/IMTProviderArray-AddCopy.md) | Add a copy of a provider object or of an array of provider objects to the end of an array.  
[Delete](IMTECNProviderArray/IMTProviderArray-Delete.md) | Delete a provider object by its position.  
[Detach](IMTECNProviderArray/IMTProviderArray-Detach.md) | Detach a provider object from an array.  
[Update](IMTECNProviderArray/IMTProviderArray-Update.md) | Update a provider at the specified position of an array.  
[UpdateCopy](IMTECNProviderArray/IMTProviderArray-UpdateCopy.md) | Update a provider at the specified position of an array by copying the parameters of a passed provider object.  
[Shift](IMTECNProviderArray/IMTProviderArray-Shift.md) | Change the position of a provider in an array.  
[Total](IMTECNProviderArray/IMTProviderArray-Total.md) | Get the number of provider objects in an array.  
[Next](IMTECNProviderArray/IMTProviderArray-Next.md) | Get a provider object by its position.  
[Sort](IMTECNProviderArray/IMTProviderArray-Sort.md) | Sort an array using the passed sort function.  
[Search](IMTECNProviderArray/IMTProviderArray-Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTECNProviderArray/IMTProviderArray-SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTECNProviderArray/IMTProviderArray-SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTECNProviderArray/IMTProviderArray-SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTECNProviderArray/IMTProviderArray-SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTECNProviderArray/IMTProviderArray-SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTECNProviderArray/IMTProviderArray-SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces rather than the data. This sets specific operating features when [adding](IMTECNProviderArray/IMTProviderArray-Add.md), [updating](IMTECNProviderArray/IMTProviderArray-Update.md) and [deleting](IMTECNProviderArray/IMTProviderArray-Delete.md) array elements.
  * Never add a link to one and the same object into an array (when [adding](IMTECNProviderArray/IMTProviderArray-Add.md) or [updating](IMTECNProviderArray/IMTProviderArray-Update.md) an element), because this will lead to a crash during memory release.


