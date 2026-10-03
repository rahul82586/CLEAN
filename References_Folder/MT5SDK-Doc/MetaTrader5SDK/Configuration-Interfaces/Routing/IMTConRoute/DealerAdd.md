[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / DealerAdd

[Previous](ConditionNext.md) | [Next](DealerUpdate.md)

# IMTConRoute::DealerAdd

Add a dealer to whom requests under the conditions of this rule will be sent for processing.

C++
    
    
    MTAPIRES  IMTConRoute::DealerAdd(
       IMTConRouteDealer*  dealer      // An object of a dealer entry
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.DealerAdd(
       CIMTConRouteDealer  dealer      // An object of a dealer entry
       )

Python (Manager API)
    
    
    MTConRoute.DealerAdd(
       dealer              # An object of a dealer entry
       )

### Parameters

**dealer**  
[in] An object of a dealer entry.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
