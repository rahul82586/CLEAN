[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / SearchLeft

[Previous](SearchLess.md) | [Next](SearchRight.md)

# IMTConGroupArray::SearchLeft

Search an array for the first element equal to the search key.
    
    
    int  IMTConGroupArray::SearchLeft(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of the object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, the array must be previously sorted by calling the [IMTConGroupArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.
