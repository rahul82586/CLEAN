[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTSync](../CMTSync.md) / Lock

[Previous](../CMTSync.md) | [Next](Unlock.md)

# CMTSync::Lock

The function is used to capture a critical section. After being called, the method waits until all other threads that use the section release it using the [CMTSync::Unlock](Unlock.md) method and then captures it. This ensures that after the call of CMTSync::Lock, a synchronization object will be used only by one thread.
    
    
    void  CMTSync::Lock()
