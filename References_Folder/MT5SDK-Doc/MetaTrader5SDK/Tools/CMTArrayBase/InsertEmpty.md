[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / InsertEmpty

[Previous](Insert.md) | [Next](Delete.md)

# CMTArrayBase::InsertEmpty

insert empty elements at the specified array position.
    
    
    bool  CMTArrayBase::InsertEmpty(
       const UINT  pos,       // Position
       const UINT  total      // Number of elements
       )

### Parameters

**pos**  
[in] The position at which you want to insert the elements. Numbering starts from 0.

**total**  
[in] The number of empty elements to be inserted.

### Return Value

If successful, returns true, otherwise returns false.

### Note

After executing this method, the number of elements in the current array ([CMTArrayBase::Total](Total.md)) will be increased by total elements. The value of new elements will be undefined.
