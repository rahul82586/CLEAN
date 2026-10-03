[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTSync](../CMTSync.md) / Unlock

[Previous](Lock.md) | [Next](TryLock.md)

# CMTSync::Unlock

The function is used to release a critical section after it has been captured by the [CMTSync::Lock](Lock.md) method. After calling this method, the object can be used by other threads.
    
    
    void  CMTSync::Unlock()
