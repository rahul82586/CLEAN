[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon Clear

[Previous](IMTCon-Assign.md) | [Next](IMTCon-Flags.md)

# IMTConVPS::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConVPS::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.Clear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method cleans all fields ​​and removes embedded objects.
