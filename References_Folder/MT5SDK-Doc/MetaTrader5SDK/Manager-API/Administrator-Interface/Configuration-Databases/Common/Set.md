[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Set

[Previous](Get.md) | [Next](../Network.md)

# IMTAdminAPI::CommonSet

Sets the common platform configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::CommonSet(
       const IMTConCommon*  common      // IMTConCommon object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.CommonSet(
       CIMTConCommon        common      // CIMTConCommon object
       )

Python
    
    
    AdminAPI.CommonSet(
       common         # IMTConCommon object
       )

### Parameters

**common**  
[in] An object of the common configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
