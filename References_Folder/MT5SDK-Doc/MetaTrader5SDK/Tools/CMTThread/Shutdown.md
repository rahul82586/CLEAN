[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTThread](../CMTThread.md) / Shutdown

[Previous](Start.md) | [Next](Terminate.md)

# CMTThread::Shutdown

Wait for the completion of thread operation during the specified time period.
    
    
    bool  CMTThread::Shutdown(
       const UINT  timeout=INFINITE      // Time to wait
       )

### Parameters

**timeout=INFINITE**  
[in] Time to wait for the completion of thread operation in milliseconds.

### Return Value

If the thread completes operation after the specified time period, true is returned. If the thread continues to work, it returns false.
