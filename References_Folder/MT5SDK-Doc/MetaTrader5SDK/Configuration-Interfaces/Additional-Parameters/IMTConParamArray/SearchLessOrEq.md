[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / SearchLessOrEq

[Previous](SearchGreater.md) | [Next](SearchLess.md)

# IMTConParamArray::SearchLessOrEq

Search in an array the first element less than or equal to the search key.
    
    
    int  IMTConParamArray::SearchLessOrEq(
       const void         *key,              
       MTSortFunctionPtr  sort_function      
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the position of the parameter object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTConParamArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.
