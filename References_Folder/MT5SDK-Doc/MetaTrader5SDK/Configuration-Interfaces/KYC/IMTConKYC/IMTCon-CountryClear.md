[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon CountryClear

[Previous](IMTCon-CountryDelete.md) | [Next](IMTCon-CountryShift.md)

# IMTConKYC::CountryClear

Clear the list of countries for which the KYC provider is used.

C++
    
    
    MTAPIRES  IMTConKYC::CountryClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.CountryClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

This method removes from the list all countries for which the KYC provider is used.
