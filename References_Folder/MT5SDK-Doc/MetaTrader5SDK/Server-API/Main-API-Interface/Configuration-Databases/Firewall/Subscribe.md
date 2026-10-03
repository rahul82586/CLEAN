[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Subscribe

[Previous](Create.md) | [Next](Unsubscribe.md)

# IMTServerAPI::FirewallSubscribe

Subscribe to events and hooks associated with the firewall configuration.
    
    
    MTAPIRES  IMTServerAPI::FirewallSubscribe(
       IMTConFirewallSink*  sink      // A pointer to the IMTConFirewallSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConFirewallSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTConFirewallSink](../../../../Configuration-Interfaces/Firewall/IMTConSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
