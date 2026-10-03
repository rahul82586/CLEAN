[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRouteDealer](../IMTConRouteDealer.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConRouteDealer::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConRouteDealer::Assign(
       const IMTConRouteDealer*  config      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRouteDealer.Assign(
       CIMTConRouteDealer        config      // Source object
       )

### Parameters

**config**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
