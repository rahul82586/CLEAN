[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Summary Positions](../../Summary-Positions.md) / [IMTSummaryArray](../IMTSummaryArray.md) / SearchLess

[Previous](SearchLessOrEq.md) | [Next](SearchLeft.md)

# IMTSummaryArray::SearchLess

Search in an array the first element less than the search key.
    
    
    int  IMTSummaryArray::SearchLess(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Sort function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesort function.

### Return Value

If successful, it returns the position of a summary position record object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTSummaryArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.
