[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Update

[Previous](Remove.md) | [Next](Shift.md)

# CMTArrayBase::Update

Update the element at the specified position in the array.
    
    
    bool  CMTArrayBase::Update(
       const UINT  pos,       // Position
       const void  *elem      // New element
       )

### Parameters

**pos**  
[in] The position at which you want to update the element. Numbering starts from 0.

***elem**  
[in] A pointer to the element that you want to use instead the specified one.

### Return Value

If successful, returns true, otherwise returns false.

### Note

The size of the new element must match the size of the array elements [CMTArrayBase::Width](Width.md).
