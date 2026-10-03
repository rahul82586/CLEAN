[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / AddRange

[Previous](Add.md) | [Next](AddEmpty.md)

# CMTArrayBase::AddRange

Add a range of elements from the specified array object to the current array object.
    
    
    bool  CMTArrayBase::AddRange(
       const CMTArrayBase&  array,     // Array object
       const UINT           from,      // Start of range
       const UINT           to         // End of range
       )

### Parameters

**array**  
[in] An array objectCMTArrayBase, from which a range of elements should be added.

**from**  
[in] The index of the first element in the range. Numbering starts from 0.

**to**  
[in] The index of the last element in the range. Numbering starts from 0.

### Return Value

If successful, returns true, otherwise returns false.

### Note

Sizes of elements of the arrays ([CMTArrayBase::Width](Width.md)) must be the same.
