[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Subscriptions](../Subscriptions.md) / IMTSubscriptionArray

[Previous](IMTSubscription/TimeExpire.md) | [Next](IMTSubscriptionArray/Release.md)

# IMTSubscriptionArray

The interface enables convenient operations with arrays of subscriptions. The class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTSubscriptionArray/Release.md) | Delete the current object.  
[Assign](IMTSubscriptionArray/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTSubscriptionArray/Clear.md) | Clear an object.  
[Add](IMTSubscriptionArray/Add.md) | Add a subscription object or an array of subscription objects to the end of an array.  
[AddCopy](IMTSubscriptionArray/AddCopy.md) | Add a copy of a subscription object or of an array of subscription objects to the end of an array.  
[Delete](IMTSubscriptionArray/Delete.md) | Delete a subscription object by position.  
[Detach](IMTSubscriptionArray/Detach.md) | Detach a subscription object from an array.  
[Update](IMTSubscriptionArray/Update.md) | Change a subscription at the specified position of an array.  
[UpdateCopy](IMTSubscriptionArray/UpdateCopy.md) | Change a subscription at the specified position of an array by copying the parameters of a passed subscription object.  
[Shift](IMTSubscriptionArray/Shift.md) | Change the position of a subscription in an array.  
[Total](IMTSubscriptionArray/Total.md) | Get the number of subscription objects in an array.  
[Next](IMTSubscriptionArray/Next.md) | Get a subscription object by position.  
[Sort](IMTSubscriptionArray/Sort.md) | Sort an array using the passed sort function.  
[Search](IMTSubscriptionArray/Search.md) | Search in an array for an element that matches the search key.  
[SearchGreatOrEq](IMTSubscriptionArray/SearchGreatOrEq.md) | Search in an array for the first element greater than or equal to the search key.  
[SearchGreater](IMTSubscriptionArray/SearchGreater.md) | Search in an array for the first element greater than the search key.  
[SearchLessOrEq](IMTSubscriptionArray/SearchLessOrEq.md) | Search in an array for the first element less than or equal to the search key.  
[SearchLess](IMTSubscriptionArray/SearchLess.md) | Search in an array for the first element less than the search key.  
[SearchLeft](IMTSubscriptionArray/SearchLeft.md) | Search in an array for the first element equal to the search key.  
[SearchRight](IMTSubscriptionArray/SearchRight.md) | Search in an array for the last element equal to the search key.  
  
## Operations with Arrays

There are a number of specific features for operations with arrays:

  * Arrays store pointers to the corresponding interfaces, not the data. This determines some specific features in operations when [adding](IMTSubscriptionArray/Add.md), [updating](IMTSubscriptionArray/Update.md) and [deleting](IMTSubscriptionArray/Delete.md) array elements.
  * Never add a link to one and the same object in an array (when [adding](IMTSubscriptionArray/Add.md) or [deleting](IMTSubscriptionArray/Update.md) elements), because this will lead to a crash during memory release.


