[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / SearchRight

[Previous](SearchLeft.md) | [Next](../CMTStr.md)

# CMTArrayBase::SearchRight

Search in an array the last element equal to the search key.
    
    
    static void*  CMTArrayBase::SearchRight(
       const void                  *key,          // Search key
       SMTSearch::SortFunctionPtr  sort_function  // Sort function
       )

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter.

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns a pointer to the found item. Otherwise, it returns NULL.

### Note

For a successful search, an array must be sorted first by calling the [CMTArrayBase::Sort](Sort.md) method. The sort function in the sort and search methods must match.
