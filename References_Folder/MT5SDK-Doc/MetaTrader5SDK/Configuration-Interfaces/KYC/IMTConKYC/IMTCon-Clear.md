[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon Clear

[Previous](IMTCon-Assign.md) | [Next](IMTCon-Name.md)

# IMTConKYC::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConKYC::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

This method cleans all fields ​​and removes embedded objects.
