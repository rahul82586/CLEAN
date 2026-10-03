[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / BindingsShift

[Previous](BindingsUpdate.md) | [Next](BindingsDelete.md)

# IMTConServer::BindingsShift

Move a binding in the list.

C++
    
    
    MTAPIRES  IMTConServer::BindingsShift(
       const UINT  pos,       // Position of the binding
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.BindingsShift(
       uint        pos,       // Position of the binding
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConServer.BindingsShift(
       pos,        # Position of the binding
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the binding in the list, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Address for listening (binding) is the address and port to be listened to by the access server for the availability of external connections.
