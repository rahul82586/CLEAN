[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Position

[Previous](At.md) | [Next](Range.md)

# CMTArrayBase::Position

Get the position of an element in the array based on the pointer to the element.
    
    
    int  CMTArrayBase::Position(
       const void*  ptr      // A pointer to the element
       )

### Parameters

**ptr**  
[in] A pointer to the element.

### Return Value

The position of the element in the array. Numbering starts from 0.
