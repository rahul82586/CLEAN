[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageShift

[Previous](LeverageDelete.md) | [Next](LeverageTotal.md)

# IMTServerAPI::LeverageShift

Change the position of a floating margin configuration in the list.
    
    
    MTAPIRES  IMTServerAPI::LeverageShift(
       const UINT  pos,       // Configuration position
       const int   shift      // Shift
       )

### Parameters

**pos**  
[in] Configuration position starting from 0.

**shift**  
[in] Configuration shift relative to its current position. A negative value means shift towards the top of the list, while a positive value shifts the item towards the end.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

The position of a configuration can only be changed from the plugins running on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.
