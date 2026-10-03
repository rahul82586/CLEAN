[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / LeverageDelete

[Previous](LeverageUpdateBatch.md) | [Next](LeverageDeleteBatch.md)

# IMTAdminAPI::LeverageDelete

Delete a floating margin configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::LeverageDelete(
       LPCWSTR  name      // Configuration name
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LeverageDelete(
       string   name      // Configuration name
       )

Python
    
    
    AdminAPI.LeverageDelete(
       str      name      # Configuration name
       )

### Parameters

**name**  
[in] The name of the configuration to delete. TheIMTConLeverage::Namevalue is used for the configuration name.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

A configuration can only be deleted from the applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

# IMTAdminAPI::LeverageDelete

Delete a floating margin configuration by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::LeverageDelete(
       const UINT  pos      // Configuration position
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.LeverageDelete(
       uint        pos      // Configuration position
       )

Python
    
    
    AdminAPI.LeverageDelete(
       int         pos      # Configuration position
       )

### Parameters

**pos**  
[in] Configuration position starting from 0.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

A configuration can only be deleted from the applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
