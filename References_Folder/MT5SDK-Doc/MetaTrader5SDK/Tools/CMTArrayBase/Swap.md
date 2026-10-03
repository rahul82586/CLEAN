[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Swap

[Previous](Assign.md) | [Next](Reserve.md)

# CMTArrayBase::Swap

Swap the contents of the current array and the contents of the passed array object.
    
    
    void  CMTArrayBase::Swap(
       CMTArrayBase  &arr      // An array for exchanging contents
       )

### Parameters

**& arr**  
[in] The array, with which you want to swap contents.

### Note

After executing this method, the current array will contain data from the passed array, and the passed array will contain data from the current one.
