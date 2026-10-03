[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Shift

[Previous](DeleteBatch.md) | [Next](Total.md)

# IMTAdminAPI::KYCShift

Change the position of a KYC provider configuration in the list.

C++
    
    
    MTAPIRES  IMTAdminAPI::KYCShift(
       const UINT  pos,       // Configuration position
       const int   shift      // Shift
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.KYCShift(
       uint        pos,       // Configuration position
       int         shift      // Shift
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**shift**  
[in] The shift of the configuration relative to its current position. A negative value means shift towards the top of the list; a positive value shifts the item towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The position of a configuration can only be changed from the applications running on the main server. For all other plugins, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned.
