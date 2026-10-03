[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageDelete

[Previous](LeverageAdd.md) | [Next](LeverageShift.md)

# IMTServerAPI::LeverageDelete

Delete a floating margin configuration by name.
    
    
    MTAPIRES  IMTServerAPI::LeverageDelete(
       LPCWSTR  name      // Configuration name
       )

### Parameters

**name**  
[in] The name of the configuration to delete. TheIMTConLeverage::Namevalue is used for the configuration name.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

A configuration can only be deleted from plugins running on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

# IMTServerAPI::LeverageDelete

Delete a floating margin configuration by index.
    
    
    MTAPIRES  IMTServerAPI::LeverageDelete(
       const UINT  pos      // Configuration position
       )

### Parameters

**pos**  
[in] Configuration position starting from 0.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

A configuration can only be deleted from plugins running on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
