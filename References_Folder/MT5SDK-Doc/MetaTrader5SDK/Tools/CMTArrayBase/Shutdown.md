[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Shutdown

[Previous](Zero.md) | [Next](Compact.md)

# CMTArrayBase::Shutdown

Free the memory allocated for the array.
    
    
    void  CMTArrayBase::Shutdown()

### Note

After executing this method, the number of elements in the array ([CMTArrayBase::Total](Total.md)) and the maximum allowed number of elements ([CMTArrayBase::Max](Max.md)) will be equal to zero.
