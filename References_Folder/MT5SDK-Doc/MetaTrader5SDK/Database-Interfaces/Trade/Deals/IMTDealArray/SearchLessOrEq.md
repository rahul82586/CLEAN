[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / SearchLessOrEq

[Previous](SearchGreater.md) | [Next](SearchLess.md)

# IMTDealArray::SearchLessOrEq

Search in an array the first element less than or equal to the search key.
    
    
    int  IMTDealArray::SearchLessOrEq(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the position of a deal object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTDealArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.
