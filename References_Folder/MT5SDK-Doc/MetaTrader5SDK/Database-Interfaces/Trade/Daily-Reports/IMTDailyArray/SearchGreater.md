[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / SearchGreater

[Previous](SearchGreatOrEq.md) | [Next](SearchLessOrEq.md)

# IMTDailyArray::SearchGreater

Search in an array the first element greater than the search key.
    
    
    int  IMTDailyArray::SearchGreater(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the position of a daily report object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTDailyArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.
