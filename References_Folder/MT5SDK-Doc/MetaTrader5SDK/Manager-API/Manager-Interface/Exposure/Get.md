[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Exposure](../Exposure.md) / Get

[Previous](Next.md) | [Next](GetAll.md)

# IMTManagerAPI::ExposureGet

Get a record from an exposure table by a symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::ExposureGet(
       LPCWSTR       symbol,       // Symbol
       IMTExposure*  exposure      // Exposure object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ExposureGet(
       string        symbol,       // Symbol
       CIMTExposure  exposure      // Exposure object
       )

Python
    
    
    ManagerAPI.ExposureGet(
       str           symbol        # Symbol
       )

### Parameters

**symbol**  
[in] Symbol.

**exposure**  
[out] An object of the exposure record. The exposure object must first be created using theIMTManagerAPI::ExposureCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To receive information about exposure, it is necessary to subscribe to events of its changes using the [IMTManagerAPI::ExposureSubscribe](Subscribe.md) method.
