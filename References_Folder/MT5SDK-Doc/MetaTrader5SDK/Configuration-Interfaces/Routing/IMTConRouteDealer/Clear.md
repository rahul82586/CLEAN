[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConRouteDealer](../IMTConRouteDealer.md) / Clear

[Previous](Assign.md) | [Next](Login.md)

# IMTConRouteDealer::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConRouteDealer::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConRouteDealer.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
