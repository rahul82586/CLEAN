[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Insert

[Previous](Append.md) | [Next](InsertEmpty.md)

# CMTArrayBase::Insert

Insert an element at the specified position of the array.
    
    
    bool  CMTArrayBase::Insert(
       const UINT  pos,       // Position
       const void  *elem      // The element to be inserted
       )

### Parameters

**pos**  
[in] The position at which you want to insert an element. Numbering starts from 0.

***elem**  
[in] A pointer to the element.

### Return Value

If successful, returns true, otherwise returns false.

### Note

The size of the element to be inserted must match the size of the array elements [CMTArrayBase::Width](Width.md).

# CMTArrayBase::Insert

Insert array elements at the specified position in the array.
    
    
    bool  CMTArrayBase::Insert(
       const UINT  pos,       // Position
       const void  *elem,     // Array of elements
       const UINT  total      // Number of elements
       )

### Parameters

**pos**  
[in] The position at which you want to insert the elements. Numbering starts from 0.

***elem**  
[in] A pointer to the array of elements.

### Return Value

If successful, returns true, otherwise returns false.

### Note

The size of the elements to be inserted must match the size of the array elements [CMTArrayBase::Width](Width.md).

# CMTArrayBase::Insert

Insert an element in a pre-sorted array without disturbing the sort order.
    
    
    void*  CMTArrayBase::Insert(
       const void                  *elem,             // The element to be inserted
       SMTSearch::SortFunctionPtr  sort_function      // Sort function
       )

### Parameters

***elem**  
[in] A pointer to an element, which you want to insert into an array.

**sort_function**  
[in] A pointer to thesort function. A pointer to the inserted elem element is passed as the first parameter in the sort function.

### Return Value

A pointer to a new element of the array. If inserting an element fails, or the inserted element already exists in the array, it returns NULL.

### Note

After successful insertion the size of the array increases by one element.
