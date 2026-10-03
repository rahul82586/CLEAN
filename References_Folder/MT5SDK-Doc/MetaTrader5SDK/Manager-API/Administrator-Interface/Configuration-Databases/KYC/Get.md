[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Get

[Previous](Next.md) | [Next](Start.md)

# IMTAdminAPI::KYCGet

Get a KYC provider configuration by name.

C++
    
    
    MTAPIRES  IMTAdminAPI::KYCGet(
       LPCWSTR           name,      // Configuration name
       IMTConKYC*        kyc        // KYC provider configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.KYCGet(
       string            name,      // Configuration name
       CIMTConKYC        kyc        // KYC provider configuration object
       )

### Parameters

**name**  
[in] The name of the configuration.

**kyc**  
[out] KYC provider configuration object. The 'kyc' object must be created in advance using theIMTServerAPI::KYCCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConKYC::Name](../../../../Configuration-Interfaces/KYC/IMTConKYC/IMTCon-Name.md) value is used as the configuration name.
