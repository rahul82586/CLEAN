[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / SearchRight

[Previous](SearchLeft.md) | [Next](../IMTDealSink.md)

# IMTDealArray::SearchRight

Search in an array the last element equal to the search key.
    
    
    int  IMTDealArray::SearchRight(
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
