[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Add

[Previous](Unsubscribe.md) | [Next](Delete.md)

# IMTServerAPI::KYCAdd

Add or update a KYC provider configuration.
    
    
    MTAPIRES  IMTServerAPI::KYCAdd(
       IMTConKYC*  config  // KYC provider configuration object
       )

### Parameters

**config**  
[in] KYC provider configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the record exists. If the record already exists, it is updated; otherwise, a new entry is added. A key field for comparison is the configuration name [IMTConKYC::Name()](../../../../Configuration-Interfaces/KYC/IMTConKYC/IMTCon-Name.md). If you try to add a completely identical record, no changes are made, and therefore the [IMTConKYCSink::OnKYCUpdate](../../../../Configuration-Interfaces/KYC/IMTConKYCSink/IMTConSink-OnUpdate.md) notification method is not called.
