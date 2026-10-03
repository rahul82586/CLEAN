[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / RouteShift

[Previous](RouteDeleteBatch.md) | [Next](RouteTotal.md)

# IMTAdminAPI::RouteShift

Move a routing rule in the list.

C++
    
    
    MTAPIRES  IMTAdminAPI::RouteShift(
       const UINT  pos,       // Position of a rule
       const int   shift      // Shift
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.RouteShift(
       uint        pos,       // Position of a rule
       int         shift      // Shift
       )

Python
    
    
    AdminAPI.RouteShift(
       pos,        # Position of a rule
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of a routing rule, starting with 0.

**shift**  
[in] Shift of a rule relative to its current position. A negative value means the shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Rules are executed from top downwards. If a received request corresponds to the conditions of the top rule, it is handled under this rule, otherwise conditions of the second rule are checked, and so on. A request is handled in accordance with the rules until it is executed or passed to a dealer.
