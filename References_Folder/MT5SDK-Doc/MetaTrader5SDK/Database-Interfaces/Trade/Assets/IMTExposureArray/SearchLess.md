[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / SearchLess

[Previous](SearchLessOrEq.md) | [Next](SearchLeft.md)

# IMTExposureArray::SearchLess

Search in an array the first element less than the search key.
    
    
    int  IMTExposureArray::SearchLess(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Sort function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesort function.

### Return Value

If successful, it returns the position of an asset record object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTExposureArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.
