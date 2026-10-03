[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConAccountAllocation::Assign

Assign the passed object to the current one.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::Assign(
       const IMTConAccountAllocation*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAgreement.Assign(
       CIMTConAccountAllocation        obj        // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
