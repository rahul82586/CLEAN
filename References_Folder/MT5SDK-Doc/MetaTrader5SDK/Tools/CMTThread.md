[🏠 Document Start](../README.md) / [Tools](README.md) / CMTThread

[Previous](CMTSync/TryLock.md) | [Next](CMTThread/Start.md)

# CMTThread

This class is a wrapper of WinAPI thread. It allows running parallel computing in a separate thread.

The class contains the following methods:

Method | Purpose  
---|---  
[Start](CMTThread/Start.md) | Start the thread. After calling this method, the function thread_func starts.  
[Shutdown](CMTThread/Shutdown.md) | Wait for the completion of thread operation during the specified time period.  
[Terminate](CMTThread/Terminate.md) | Forced completion of a thread.  
[IsBusy](CMTThread/IsBusy.md) | Check the thread activity.  
[Handle](CMTThread/Handle.md) | Get a thread handle (WinAPI-descriptor).  
[Priority](CMTThread/Priority.md) | Set a thread priority.
