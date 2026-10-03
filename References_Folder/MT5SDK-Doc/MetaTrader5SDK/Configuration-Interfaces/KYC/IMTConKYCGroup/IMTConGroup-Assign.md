[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCGroup](../IMTConGroup.md) / IMTConGroup Assign

[Previous](IMTConGroup-Release.md) | [Next](IMTConGroup-Clear.md)

# IMTConMessengerGroup::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConKYCGroup::Assign(
       const IMTConKYCGroup*  group  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYCGroup.Assign(
       CIMTConKYCGroup        group  // Source object
       )

### Parameters

**group**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
