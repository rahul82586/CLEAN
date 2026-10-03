[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTThread](../CMTThread.md) / Priority

[Previous](Handle.md) | [Next](../SMTTime.md)

# CMTThread::Priority

Set a thread priority.
    
    
    bool  CMTThread::Priority(
       int  priority      // Priority
       )

### Parameters

**priority**  
[in] Thread priority. The following values can be used to specify priority:

ID | Value | Description  
THREAD_MODE_BACKGROUND_BEGIN | 0x00010000 | Start processing in the background mode.  
THREAD_MODE_BACKGROUND_END | 0x00020000 | Finish processing in the background.  
THREAD_PRIORITY_ABOVE_NORMAL | 1 | Assign a priority a point above the priority class of the process.  
THREAD_PRIORITY_BELOW_NORMAL | -1 | Assign a priority a point lower than the priority class of the process.  
THREAD_PRIORITY_HIGHEST | 2 | Assign a priority two points above the priority class of the process.  
THREAD_PRIORITY_IDLE | -15 | Assign a base priority equal to 1 to the processes IDLE_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, ABOVE_NORMAL_PRIORITY_CLASS and HIGH_PRIORITY_CLASS or equal to 16 to the REALTIME_PRIORITY_CLASS processes.  
THREAD_PRIORITY_LOWEST | -2 | Assign a priority two points lower than the priority class of the process.  
THREAD_PRIORITY_NORMAL | 0 | Assign a normal priority for the priority class of the process.  
THREAD_PRIORITY_TIME_CRITICAL | 15 | Assign a base priority equal to 15 to the processes IDLE_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, ABOVE_NORMAL_PRIORITY_CLASS and HIGH_PRIORITY_CLASS or equal to 31 to the REALTIME_PRIORITY_CLASS processes.  
  
### Return Value

If successful, returns true, otherwise returns false.
