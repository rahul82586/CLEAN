[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionHistoryArray](../IMTSubscriptionHistoryArray.md) / SearchGreater

[Previous](SearchGreatOrEq.md) | [Next](SearchLessOrEq.md)

# IMTSubscriptionHistoryArray::SearchGreater

Search in an array for the first element greater than the search key.
    
    
    int  IMTSubscriptionHistoryArray::SearchGreater(
       const void*        key,               // Sorting key
       MTSortFunctionPtr  sort_function      // A pointer to the search function
       )  const

### Parameters

**key**  
[in] A pointer to the sorting key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of the subscription object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, an array must first be sorted by calling the [IMTSubscriptionHistoryArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.
