[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [KYC](../KYC.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Add.md)

# IMTServerAPI::KYCUnsubscribe

Unsubscribe from events and hooks associated with KYC provider configurations.
    
    
    MTAPIRES  IMTServerAPI::KYCUnsubscribe(
       IMTConKYCSink*  sink   // A pointer to the IMTConKYCSink object
       )

### Parameters

**sink**  
[in] A pointer to the object implementing theIMTConKYCSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method is paired with [IMTServerAPI::KYCSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface which has not been previously subscribed to, the [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
