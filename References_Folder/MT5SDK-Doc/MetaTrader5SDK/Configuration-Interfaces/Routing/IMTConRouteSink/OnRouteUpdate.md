[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRouteSink](../IMTConRouteSink.md) / OnRouteUpdate

[Previous](OnRouteAdd.md) | [Next](OnRouteDelete.md)

# IMTConRouteSink::OnRouteUpdate

A handler of the event of updating a routing rule.

C++
    
    
    virtual void  IMTConRouteSink::OnRouteUpdate(
       const IMTConRoute*  config      // A pointer to the rule object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConRouteSink.OnRouteUpdate(
       CIMTConRoute        config      // The rule object
       )

### Parameters

**config**  
[in] A pointer to the object of the modified rule.

### Note

This method is called by the API to notify of change of a routing rule.
