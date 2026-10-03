[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTSearch](../SMTSearch.md) / Sort Function

[Previous](../SMTSearch.md) | [Next](Insert.md)

# Sort Function

The sort function is used in the sort and search methods of the SMTSearch class. It is defined by the programmer. In the methods of the SMTSearch class, a pointer to this function is passed, where the two values, at which its left and right parameters point, are compared. This function is similar to CRT sort functions "qsort" and "bsearch".
    
    
    typedef int (__cdecl *SortFunctionPtr)(const void *, const void *);

Depending on the comparison results, the following values are returned:

  * <0 — if the left parameter is less than the right one
  * 0 — if the left parameter is equal to the right one
  * >0 — if the left parameter is greater than the right one


