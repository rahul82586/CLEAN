[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Append

[Previous](AddEmpty.md) | [Next](Insert.md)

# CMTArrayBase::Append

Add an empty element to an array.
    
    
    void*  CMTArrayBase::Append()

### Return Value

A pointer to the newly added element. If element adding failed, NULL is returned.

### Note

After executing this method, the size of the current array object ([CMTArrayBase::Total](Total.md)) is increased by 1 element. The value of newly added element will be undefined.
