[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Trim

[Previous](Shift.md) | [Next](Next.md)

# CMTArrayBase::Trim

Delete elements from the beginning of the array.
    
    
    bool  CMTArrayBase::Trim(
       const UINT  size      // Number of elements
       )

### Parameters

**size**  
[in] The number of elements that you need to delete from the beginning of the array.

### Return Value

If successful, returns true, otherwise returns false.

### Note

The method deletes size elements from the beginning of the array.
