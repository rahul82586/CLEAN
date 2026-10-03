[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRouteSink](../IMTConRouteSink.md) / OnRouteAdd

[Previous](../IMTConRouteSink.md) | [Next](OnRouteUpdate.md)

# IMTConRouteSink::OnRouteAdd

A handler of the event of adding a new routing rule.

C++
    
    
    virtual void  IMTConRouteSink::OnRouteAdd(
       const IMTConRoute*  config      // A pointer to the rule object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConRouteSink.OnRouteAdd(
       CIMTConRoute        config      // The rule object
       )

### Parameters

**config**  
[in] A pointer to the object of the added rule.

### Note

This method is called by the API to notify that a new routing rule has been added.
