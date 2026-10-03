[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / SearchLess

[Previous](SearchLessOrEq.md) | [Next](SearchLeft.md)

# IMTConLeverageArray::SearchLess

Search an array for the first element less than the search key.
    
    
    int  IMTConLeverageArray::SearchLess(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] Pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] Pointer to thesearch function.

### Return Value

In case of success, the method returns the position of the configuration object that satisfies the search condition. Otherwise, -1 is returned.

### Note

For successful searching, the array must be pre-sorted by calling the [IMTConLeverageArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.
