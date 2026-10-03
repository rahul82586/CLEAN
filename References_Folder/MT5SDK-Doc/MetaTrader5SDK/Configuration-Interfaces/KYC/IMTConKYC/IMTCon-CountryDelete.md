[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon CountryDelete

[Previous](IMTCon-CountryUpdate.md) | [Next](IMTCon-CountryClear.md)

# IMTConKYC::CountryDelete

Delete the country for which the KYC provider is used.

C++
    
    
    MTAPIRES  IMTConKYC::CountryDelete(
       const UINT  pos      // Country position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.CountryDelete(
       uint        pos      // Country position
       )

### Parameters

**pos**  
[in] The position of the country in the list, starting from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.
