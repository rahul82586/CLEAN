[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Next

[Previous](Trim.md) | [Next](Prev.md)

# CMTArrayBase::Next

Get an array element at the position.
    
    
    bool  CMTArrayBase::Next(
       const UINT  pos,       // Position of the element
       void        *elem      // The resulting element
       )

### Parameters

**pos**  
The position of the element to get. Numbering starts from 0.

***elem**  
[out] A pointer to the resulting element.

### Return Value

If successful, returns true, otherwise returns false.

### Note

The specified element of size [CMTArrayBase::Width](Width.md) is copied into elem.

# CMTArrayBase::Next

Get a pointer to the next array element based on the pointer to the element.
    
    
    void*  CMTArrayBase::Next(
       const void  *elem      // A pointer to the element
       )

### Parameters

***elem**  
[in] A pointer to the element.

### Return Value

A pointer to the next element after the specified one. If there is no next element, NULL is returned.
