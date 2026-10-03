[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatchingArray](../IMTHistoryMatchingArray.md) / IMTHistoryMatchingArray SearchLess

[Previous](IMTHistoryMatchingArray-SearchLessOrEq.md) | [Next](IMTHistoryMatchingArray-SearchLeft.md)

# IMTECNHistoryMatchingArray::SearchLess

Search in an array the first element less than the search key.
    
    
    int  IMTECNHistoryMatchingArray::SearchLess(
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

For a successful search, an array must first be sorted by calling the [IMTECNHistoryMatchingArray::Sort](IMTHistoryMatchingArray-Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.
