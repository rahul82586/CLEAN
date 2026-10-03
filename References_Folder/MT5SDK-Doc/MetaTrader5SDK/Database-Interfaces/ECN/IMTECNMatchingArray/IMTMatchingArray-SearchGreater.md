[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatchingArray](../IMTMatchingArray.md) / IMTMatchingArray SearchGreater

[Previous](IMTMatchingArray-SearchGreatOrEq.md) | [Next](IMTMatchingArray-SearchLessOrEq.md)

# IMTECNMatchingArray::SearchGreater

Search in an array for the first element greater than the search key.
    
    
    int  IMTECNMatchingArray::SearchGreater(
       const void*        key,               // sorting key
       MTSortFunctionPtr  sort_function      // a pointer to the search array
       )  const

### Parameters

**key**  
[in] A pointer to the sorting key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of the order object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, an array must first be sorted by calling the [IMTECNMatchingArray::Sort](IMTMatchingArray-Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.
