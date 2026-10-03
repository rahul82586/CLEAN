[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Subscriptions](../Subscriptions.md) / IMTSubscriptionHistoryArray

[Previous](IMTSubscriptionHistory/AmountDeal.md) | [Next](IMTSubscriptionHistoryArray/Release.md)

# IMTSubscriptionHistoryArray

The interface enables convenient operations with arrays of subscription actions. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTSubscriptionHistoryArray/Release.md) | Delete the current object.  
[Assign](IMTSubscriptionHistoryArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTSubscriptionHistoryArray/Clear.md) | Clear an object.  
[Add](IMTSubscriptionHistoryArray/Add.md) | Add an object or an array of objects of subscription actions to the end of an array.  
[AddCopy](IMTSubscriptionHistoryArray/AddCopy.md) | Add a copy of an object or an array of objects of subscription actions to the end of an array.  
[Delete](IMTSubscriptionHistoryArray/Delete.md) | Delete a subscription action object by position.  
[Detach](IMTSubscriptionHistoryArray/Detach.md) | Detach a subscription action object from an array.  
[Update](IMTSubscriptionHistoryArray/Update.md) | Change a subscription action at the specified position of an array.  
[UpdateCopy](IMTSubscriptionHistoryArray/UpdateCopy.md) | Change a subscription action at the specified position of an array by copying the parameters of a passed action object.  
[Shift](IMTSubscriptionHistoryArray/Shift.md) | Change the position of a subscription action in an array.  
[Total](IMTSubscriptionHistoryArray/Total.md) | Get the number of subscription actions in an array.  
[Next](IMTSubscriptionHistoryArray/Next.md) | Get a subscription action object by position.  
[Sort](IMTSubscriptionHistoryArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTSubscriptionHistoryArray/Search.md) | Search in an array for an element that matches the search key.  
[SearchGreatOrEq](IMTSubscriptionHistoryArray/SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTSubscriptionHistoryArray/SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTSubscriptionHistoryArray/SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTSubscriptionHistoryArray/SearchLess.md) | Search in an array for the first element less than the search key.  
[SearchLeft](IMTSubscriptionHistoryArray/SearchLeft.md) | Search in an array for the first element equal to the search key.  
[SearchRight](IMTSubscriptionHistoryArray/SearchRight.md) | Search in an array for the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for operations with arrays:

  * Arrays store pointers to the corresponding interfaces, not the data. This determines some specific features in operations when [adding](IMTSubscriptionHistoryArray/Add.md), [updating](IMTSubscriptionHistoryArray/Update.md) and [deleting](IMTSubscriptionHistoryArray/Delete.md) array elements.
  * Never add a link to one and the same object in an array (when [adding](IMTSubscriptionHistoryArray/Add.md) or [deleting](IMTSubscriptionHistoryArray/Update.md) elements), because this will lead to a crash during memory release.


