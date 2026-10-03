[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Compact

[Previous](Shutdown.md) | [Next](Assign.md)

# CMTArrayBase::Compact

Reallocate an array in a smaller memory block.
    
    
    void  CMTArrayBase::Compact()

### Note

This method allows to reduce the amount of memory allocated for the array. The condition for the implementation of this method is the availability of free space in the array of no less than the array change step ([CMTArrayBase::Max](Max.md) \- [CMTArrayBase::Total](Total.md) > [CMTArrayBase::Step](Step.md)).
