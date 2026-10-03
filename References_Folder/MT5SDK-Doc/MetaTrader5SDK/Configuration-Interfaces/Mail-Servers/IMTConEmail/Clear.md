[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Mail Servers](../../Mail-Servers.md) / [IMTConEmail](../IMTConEmail.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConEmail::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConEmail::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConEmail.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method clears all fields ​​and removes nested objects.
