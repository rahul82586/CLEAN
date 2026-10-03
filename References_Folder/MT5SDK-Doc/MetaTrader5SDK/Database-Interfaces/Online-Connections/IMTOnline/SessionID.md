[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnline](../IMTOnline.md) / SessionID

[Previous](Clear.md) | [Next](Login.md)

# IMTOnline::SessionID

Get a unique ID of a user connection session.

C++
    
    
    UINT64  IMTOnline::SessionID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTOnline.SessionID()

### Return Value

Unique ID of a user connection session.

### Notes

The ID is unique within the current session of the trading server (before restart).
