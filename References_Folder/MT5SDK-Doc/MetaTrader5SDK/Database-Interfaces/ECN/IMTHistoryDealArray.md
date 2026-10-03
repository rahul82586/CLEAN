[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [ECN](../ECN.md) / IMTHistoryDealArray

[Previous](IMTECNHistoryDeal/IMTHistoryDeal-Provider.md) | [Next](IMTECNHistoryDealArray/IMTHistoryDealArray-Release.md)

# IMTECNHistoryDealArray

This interface enables convenient operations with the arrays of [deals (#deals)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#deals) performed as a result of order execution at gateways. The interface contains the following methods:

Method | Purpose  
---|---  
[Release](IMTECNHistoryDealArray/IMTHistoryDealArray-Release.md) | Delete the current object.  
[Assign](IMTECNHistoryDealArray/IMTHistoryDealArray-Assign.md) | Assign a passed object to the current one.  
[Clear](IMTECNHistoryDealArray/IMTHistoryDealArray-Clear.md) | Clear an object.  
[Add](IMTECNHistoryDealArray/IMTHistoryDealArray-Add.md) | Add a deal object or an array of deal objects to the end of an array.  
[AddCopy](IMTECNHistoryDealArray/IMTHistoryDealArray-AddCopy.md) | Add a copy of a deal object or of an array of deal objects to the end of an array.  
[Delete](IMTECNHistoryDealArray/IMTHistoryDealArray-Delete.md) | Delete a deal object by its position.  
[Detach](IMTECNHistoryDealArray/IMTHistoryDealArray-Detach.md) | Detach a deal object from an array.  
[Update](IMTECNHistoryDealArray/IMTHistoryDealArray-Update.md) | Change a deal at the specified position of an array.  
[UpdateCopy](IMTECNHistoryDealArray/IMTHistoryDealArray-UpdateCopy.md) | Change a deal at the specified position of an array by copying the parameters of a passed deal object.  
[Shift](IMTECNHistoryDealArray/IMTHistoryDealArray-Shift.md) | Change the position of a deal in an array.  
[Total](IMTECNHistoryDealArray/IMTHistoryDealArray-Total.md) | Get the number of deal objects in an array.  
[Next](IMTECNHistoryDealArray/IMTHistoryDealArray-Next.md) | Get a deal object by its position.  
[Sort](IMTECNHistoryDealArray/IMTHistoryDealArray-Sort.md) | Sort an array using the passed sort function.  
[Search](IMTECNHistoryDealArray/IMTHistoryDealArray-Search.md) | Search in an array for the array element matching the search key.  
[SearchGreatOrEq](IMTECNHistoryDealArray/IMTHistoryDealArray-SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTECNHistoryDealArray/IMTHistoryDealArray-SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTECNHistoryDealArray/IMTHistoryDealArray-SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTECNHistoryDealArray/IMTHistoryDealArray-SearchLess.md) | Search in an array the first element less than the search key.  
[SearchLeft](IMTECNHistoryDealArray/IMTHistoryDealArray-SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](IMTECNHistoryDealArray/IMTHistoryDealArray-SearchRight.md) | Search in an array the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for working with arrays:

  * Arrays store pointers to the appropriate interfaces rather than the data. This sets specific operating features when [adding](IMTECNHistoryDealArray/IMTHistoryDealArray-Add.md), [updating](IMTECNHistoryDealArray/IMTHistoryDealArray-Update.md) and [deleting](IMTECNHistoryDealArray/IMTHistoryDealArray-Delete.md) array elements.
  * Never add a link to one and the same object into an array (when [adding](IMTECNHistoryDealArray/IMTHistoryDealArray-Add.md) or [updating](IMTECNHistoryDealArray/IMTHistoryDealArray-Update.md) an element), because this will lead to a crash during memory release.


