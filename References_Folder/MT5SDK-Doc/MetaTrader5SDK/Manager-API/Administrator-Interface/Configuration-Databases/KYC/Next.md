[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Next

[Previous](Total.md) | [Next](Get.md)

# IMTAdminAPI::KYCNext

Get a KYC provider configuration by index.

C++
    
    
    MTAPIRES  IMTAdminAPI::KYCNext(
       const UINT        pos,       // Position of configuration
       IMTConKYC*        kyc        // KYC provider configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.KYCNext(
       uing              pos,       // Position configuration
       CIMTConKYC        kyc        // KYC provider configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**kyc**  
[out] KYC provider configuration object. The 'kyc' object must be created in advance using theIMTServerAPI::KYCCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of the KYC provider with a specified index to the 'kyc' object.
