[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposure](../IMTExposure.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTExposure::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTExposure::Assign(
       const IMTExposure*  exposure      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExposure.Assign(
       CIMTExposure        exposure      // Source object
       )

### Parameters

**exposure**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
