[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTSync](../CMTSync.md) / TryLock

[Previous](Unlock.md) | [Next](../CMTThread.md)

# CMTSync::Trylock

Check if capturing a critical section is possible.
    
    
    bool  CMTSync::Trylock()

### Return Value

If a critical section is not captured by other threads, it returns false. If captured - true.

### Note

It is not guaranteed that in the next moment of time (for example, if [CMTSync::Lock](Lock.md) is immediately called), the object of the critical section will have the same status (captured or free).
