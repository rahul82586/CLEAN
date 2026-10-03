[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRouteSink](../IMTConRouteSink.md) / OnRouteDelete

[Previous](OnRouteUpdate.md) | [Next](OnRouteSync.md)

# IMTConRouteSink::OnRouteDelete

A handler of the event of deletion of a routing rule.

C++
    
    
    virtual void  IMTConRouteSink::OnRouteDelete(
       const IMTConRoute*  config      // A pointer to the rule object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConRouteSink.OnRouteDelete(
       CIMTConRoute        config      // The rule object
       )

### Parameters

**config**  
[in] A pointer to the object of the deleted rule.

### Note

This method is called by the API to notify that a routing rule has been deleted.
