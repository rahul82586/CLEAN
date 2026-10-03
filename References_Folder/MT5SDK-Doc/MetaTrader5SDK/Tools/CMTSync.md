[🏠 Document Start](../README.md) / [Tools](README.md) / CMTSync

[Previous](CMTStr/FindRChar.md) | [Next](CMTSync/Lock.md)

# CMTSync

This class is a wrapper for a standard implementation of a critical section (synchronization object) in WinAPI. It allows to implement a synchronized access to a resource.

The class contains the following methods:

Method | Purpose  
---|---  
[Lock](CMTSync/Lock.md) | Capture a critical section.  
[Unlock](CMTSync/Unlock.md) | Release the critical section after it has been captured.  
[TryLock](CMTSync/TryLock.md) | Check if capturing a critical section is possible.
