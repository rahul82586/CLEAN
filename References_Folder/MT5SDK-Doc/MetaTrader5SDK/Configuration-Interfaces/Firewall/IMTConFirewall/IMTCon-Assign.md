[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewall](../IMTCon.md) / IMTCon Assign

[Previous](IMTCon-Release.md) | [Next](IMTCon-Clear.md)

# IMTConFirewall::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConFirewall::Assign(
       const IMTConFirewall*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFirewall.Assign(
       CIMTConFirewall        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
