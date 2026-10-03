[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / DeleteBatch

[Previous](Delete.md) | [Next](Shift.md)

# IMTAdminAPI::KYCDeleteBatch

Delete a batch of KYC provider configurations.

C++
    
    
    MTAPIRES  IMTAdminAPI::KYCDeleteBatch(
       IMTConKYC**  configs,      // Array of settings
       const UINT         config_total, // Number of settings in the platform
       MTAPIRES*          results       // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.KYCDeleteBatch(
       CIMTConKYC[] configs,      // Array of settings
       MTRetCode[]        results       // Array of results
       )

### Parameters

**configs**  
[in] A pointer to an array of configurations which you want to delete.

**config_total**  
[in] The number of configurations in the 'configs' array.

**results**  
[out] An array with the results of each configuration deletion on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code is an indication of successful change sending to a server; the results of applying changes are passed in the 'results' parameter.

### Note

Configurations can only be deleted when connected to the main trade server. In all other cases, the [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) response code is returned. If the object is not found, the [MT_RET_ERR_PARAMS](../../../../Return-Codes/Common-errors.md) error code is added to the 'results' array of this object.
