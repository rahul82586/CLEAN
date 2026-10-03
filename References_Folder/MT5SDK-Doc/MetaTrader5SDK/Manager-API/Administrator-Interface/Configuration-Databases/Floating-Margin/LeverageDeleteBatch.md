[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageDeleteBatch

[Previous](LeverageDelete.md) | [Next](LeverageShift.md)

# IMTAdminAPI::LeverageDeleteBatch

Delete a batch of floating margin configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::LeverageDeleteBatch(
       IMTConLeverage**  configs,        // Array of settings
       const UINT          config_total, // Number of settings in the array
       MTAPIRES*           results       // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LeverageDeleteBatch(
       CIMTConLeverage[] configs,        // Array of settings
       MTRetCode[]         results       // Array of results
       )

Python
    
    
    AdminAPI.LeverageDeleteBatch(
       list[MTConLeverage] configs       # Array of settings
       )

### Parameters

**configs**  
[in] Pointer to an array of configurations which should be deleted.

**config_total**  
[in] Number of configurations in the 'configs' array.

**results**  
[out] Array with the results of deleting each configuration on the server.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned. The response code [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) indicates successful submission of changes to the server. The result of applying these changes are passed in the 'results' parameter.

### Note

Configurations can only be deleted when connected to the main trade server. In all other cases, the [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) response code is returned. If the object is not found, the [MT_RET_ERR_PARAMS](../../../../Return-Codes/Common-errors.md) error code is added to the 'results' array of this object.
