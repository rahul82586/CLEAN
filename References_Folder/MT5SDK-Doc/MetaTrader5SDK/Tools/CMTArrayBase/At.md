[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / At

[Previous](Prev.md) | [Next](Position.md)

# CMTArrayBase::At

Get a pointer to the array element at the specified position.
    
    
    void*  CMTArrayBase::At(
       const UINT  pos      // Position of the element
       )

### Parameters

**pos**  
[in] The position of the element, a pointer to which you want to get. Numbering starts from 0.

### Return Value

A pointer to the array element. If there is no element, NULL is returned.

# CMTArrayBase::At

Get a constant pointer to the array element at the specified position.
    
    
    const void*  CMTArrayBase::At(
       const UINT  pos      // Position of the element
       )

### Parameters

**pos**  
[in] The position of the element, a pointer to which you want to get. Numbering starts from 0.

### Return Value

A constant pointer to the array element. If there is no element, NULL is returned.
