[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray SearchGreatOrEq

[Previous](IMTFillingArray-Search.md) | [Next](IMTFillingArray-SearchGreater.md)

# IMTECNFillingArray::SearchGreatOrEq

Search in an array for the first element greater than or equal to the search key.
    
    
    int  IMTECNFillingArray::SearchGreatOrEq(
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

For a successful search, an array must first be sorted by calling the [IMTECNFillingArray::Sort](IMTFillingArray-Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.
