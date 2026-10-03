[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAgreement](../IMTConAccountAgreement.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConAccountAgreement::Assign

Assign the passed object to the current one.

C++
    
    
    MTAPIRES  IMTConAccountAgreement::Assign(
       const IMTConAccountAgreement*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAgreement.Assign(
       CIMTConAccountAgreement        obj        // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
