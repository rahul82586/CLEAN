[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTSearch](../SMTSearch.md) / Insert

[Previous](Sort-Function.md) | [Next](QuickSort.md)

# SMTSearch::Insert

Insert an element in a pre-sorted array without disturbing the sort order.
    
    
    static char*  SMTSearch::Insert(
       void             *base,       // Array
       const void       *elem,       // An element to insert
       size_t           total,       // Array size
       const size_t     width,       // Size of the array element
       SortFunctionPtr  compare      // Sort function
       )

### Parameters

***base**  
[in] A pointer to an array in which you want to insert an element.

***elem**  
[in] A pointer to an element, which you want to insert into an array.

**total**  
[in] The current size of the array in elements.

**width**  
[in] The size of one array element in bytes.

**compare**  
[in] A pointer to thesort function. A pointer to the inserted elem element is passed as the first parameter in the sort function.

### Return Value

A pointer to a new element of the array. If inserting an element fails, or the inserted element already exists in the array, it returns NULL.

### Note

After successful insertion the size of the array increases by one element. Memory for the new element should always be pre-allocated by the programmer.

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
    //| Example of the Insert method                                     |
    //+------------------------------------------------------------------+
    int Example()
      {
       int arr_a[6]={2,1,5,7,2,2};
       int arr_b[7]={0};
       int c=3;
       //--- Sort
       SMTSearch::QuickSort(arr_a,6,SortInts);
       //--- Now arr_a = 1,2,2,2,5,7
       //--- Copy arr_a into a larger array arr_b
       memcpy(arr_b,arr_a,sizeof(arr_a));
       SMTSearch::Insert(arr_b,&c,6,sizeof(int),SortInts); // arr_b = { 1,2,2,2,3,5,7 }
    //---
       return(0);
      }
