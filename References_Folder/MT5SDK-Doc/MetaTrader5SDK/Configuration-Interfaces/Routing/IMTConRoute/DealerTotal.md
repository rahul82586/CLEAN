[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRoute](../IMTConRoute.md) / DealerTotal

[Previous](DealerShift.md) | [Next](DealerNext.md)

# IMTConRoute::DealerTotal

Get the total number of entries of dealers to whom requests under the conditions of this rule will be sent for processing.

C++
    
    
    UINT  IMTConRoute::DealerTotal()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConRoute.DealerTotal()

Python (Manager API)
    
    
    MTConRoute.DealerTotal()

### Return Value

The number of dealer entries in a rule.
