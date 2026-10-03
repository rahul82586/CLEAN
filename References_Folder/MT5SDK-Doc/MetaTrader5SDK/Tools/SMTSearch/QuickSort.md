[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTSearch](../SMTSearch.md) / QuickSort

[Previous](Insert.md) | [Next](Search.md)

# SMTSearch::QuickSort

Sort the specified array using the sort function passed.
    
    
    static void  SMTSearch::QuickSort(
       T                *base,     // Array
       UINT             num,       // Number of elements
       SortFunctionPtr  comp       // Sort function
       )

### Parameters

***base**  
[in] A pointer to an array of type "T". This type means that the type of the array will be determined at the compilation stage.

**num**  
[in] The number of elements in the base array.

**comp**  
[in] A pointer to thesort function.

Example:
    
    
    //+------------------------------------------------------------------+
    //| Sort Function                                               |
    //+------------------------------------------------------------------+
    int SortInts(const void *left,const void *right)
      {
       const int lft=*(const int *)left;
       const int rgh=*(const int *)right;
    //---
       if(lft<rgh) return(-1);
       if(lft>rgh) return(1);
    //--- 
       return(0);
      }
    //+------------------------------------------------------------------+
    //| Example of the QuickSort method                                  |
    //+------------------------------------------------------------------+
    int Example()
      {
       int arr_a[6]={2,1,5,7,2,2};
       //--- Sort
       SMTSearch::QuickSort(arr_a,6,SortInts);
       //--- Now arr_a = 1,2,2,2,5,7
       return(0);
      }
