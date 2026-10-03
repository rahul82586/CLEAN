[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / AddEmpty

[Previous](AddRange.md) | [Next](Append.md)

# CMTArrayBase::AddEmpty

Add empty elements to an array.
    
    
    bool  CMTArrayBase::AddEmpty(
       const UINT  total      // Number of elements
       )

### Parameters

**total**  
[in] The number of empty elements to be added.

### Return Value

If successful, returns true, otherwise returns false.

### Note

After executing this method, the number of elements in the current array ([CMTArrayBase::Total](Total.md)) will be increased by total elements. The value of newly added elements will be undefined.
