[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [VPS](../VPS.md) / Subscribe

[Previous](CreateGroup.md) | [Next](Unsubscribe.md)

# IMTServerAPI::VPSSubscribe

Subscribe to events and hooks associated with changes in the VPS sponsorship settings.
    
    
    MTAPIRES  IMTServerAPI::VPSSubscribe(
       IMTConVPSSink*  sink   // the pointer to the IMTConVPSSink object
       )

### Parameters

**sink**  
[in] The pointer to the object that implements theIMTConVPSSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. The same [IMTConVPSSink](../../../../Configuration-Interfaces/VPS/IMTConSink.md) interface cannot subscribe to an event twice. The [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) response code is returned in this case.
