[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewall](../IMTCon.md) / IMTCon Clear

[Previous](IMTCon-Assign.md) | [Next](IMTCon-Action.md)

# IMTConFirewall::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConFirewall::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFirewall.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
