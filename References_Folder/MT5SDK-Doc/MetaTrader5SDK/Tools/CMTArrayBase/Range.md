[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Range

[Previous](Position.md) | [Next](Sort.md)

# CMTArrayBase::Range

Get the range of elements from the array.
    
    
    bool  CMTArrayBase::Range(
       const UINT  from,     // Start of range
       const UINT  to,       // End of range
       void*       data      // The range of elements
       )

### Parameters

**from**  
[in] The position of the first element in the range. Numbering starts from 0.

**to**  
[in] The position of the last element in the range. Numbering starts from 0.

**data**  
[out] A pointer to the received range of elements.

### Return Value

If successful, returns true, otherwise returns false.

### Note

The received elements of size (from - to) * [CMTArrayBase::Width](Width.md), are copied into data.
