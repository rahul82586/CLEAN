[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Resize

[Previous](Reserve.md) | [Next](Add.md)

# CMTArrayBase::Resize

Change the size of the array to the specified number of elements.
    
    
    bool  CMTArrayBase::Resize(
       const UINT  size      // New size
       )

### Parameters

**size**  
[in] The target size of the array. It is specified as the number of elements.

### Return Value

If successful, returns true, otherwise returns false.

### Note

If the new size size is less than the current one, the number of elements in the array ([CMTArrayBase::Total](Total.md)) becomes equal to size. If the new size is greater than the current one, then (size - CMTArrayBase::Total) elements are added to the array. The value of newly added elements will be undefined.
