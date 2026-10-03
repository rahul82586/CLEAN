[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Add

[Previous](Resize.md) | [Next](AddRange.md)

# CMTArrayBase::Add

Add an element to an array.
    
    
    bool  CMTArrayBase::Add(
       const void  *elem      // An element to be added
       )

### Parameters

***elem**  
[in] A pointer to the element to be added.

### Return Value

If successful, returns true, otherwise returns false.

### Note

The size of the elements to be added must match the size of the array elements [CMTArrayBase::Width](Width.md).

# CMTArrayBase::Add

Add an array of elements to an array.
    
    
    bool  CMTArrayBase::Add(
       const void  *elem,     // Array of elements
       const UINT  total      // Number of elements
       )

### Parameters

***elem**  
[in] The array of elements that you want to add.

**total**  
[in] The number of elements in the array to be added.

### Return Value

If successful, returns true, otherwise returns false.

### Note

The size of all elements to be added must match the size of the array elements [CMTArrayBase::Width](Width.md).

# CMTArrayBase::Add

Add an array object to the current array object.
    
    
    bool  CMTArrayBase::Add(
       const CMTArrayBase&  array      // Array object
       )

### Parameters

**array**  
[in] An object of the arrayCMTArrayBasethat you want to add.

### Return Value

If successful, returns true, otherwise returns false.

### Note

Sizes of elements of the arrays ([CMTArrayBase::Width](Width.md)) must be the same.
