[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / DeleteRange

[Previous](Delete.md) | [Next](Remove.md)

# CMTArrayBase::DeleteRange

Delete the range of elements from the array.
    
    
    bool  CMTArrayBase::DeleteRange(
       const UINT  from,     // Start of range
       const UINT  to        // End of range
       )

### Parameters

**from**  
[in] Position of the first element in the range of elements to delete. Numbering starts from 0.

**to**  
[in] The position of the last element in the range of elements to remove. Numbering starts from 0.

### Return Value

If successful, returns true, otherwise returns false.
