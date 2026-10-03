[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / DealerDelete

[Previous](DealerUpdate.md) | [Next](DealerClear.md)

# IMTConRoute::DealerDelete

Delete an entry of a dealer to whom requests under the conditions of this rule will be sent for processing.

C++
    
    
    MTAPIRES  IMTConRoute::DealerDelete(
       const UINT  pos      // Position of a dealer entry
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.DealerDelete(
       uint        pos      // Position of a dealer entry
       )

Python (Manager API)
    
    
    MTConRoute.DealerDelete(
       pos         # Position of a dealer entry
       )

### Parameters

**pos**  
[in] Position of a dealer entry in the list, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
