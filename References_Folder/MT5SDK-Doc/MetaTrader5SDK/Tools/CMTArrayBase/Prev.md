[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Prev

[Previous](Next.md) | [Next](At.md)

# CMTArrayBase::Prev

Get a pointer to the previous array element based on the pointer to the element.
    
    
    void*  CMTArrayBase::Prev(
       const void  *elem      // A pointer to the element
       )

### Parameters

***elem**  
[in] A pointer to the element.

### Return Value

A pointer to the previous element before the specified one. If there is no previous element, NULL is returned.
