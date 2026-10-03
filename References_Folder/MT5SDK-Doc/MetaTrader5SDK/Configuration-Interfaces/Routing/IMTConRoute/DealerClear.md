[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / DealerClear

[Previous](DealerDelete.md) | [Next](DealerShift.md)

# IMTConRoute::DealerClear

Clear the list of dealers to whom requests under the conditions of this rule will be sent for processing.

C++
    
    
    MTAPIRES  IMTConRoute::DealerClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRoute.DealerClear()

Python (Manager API)
    
    
    MTConRoute.DealerClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears the entire list of dealers in a rule.
