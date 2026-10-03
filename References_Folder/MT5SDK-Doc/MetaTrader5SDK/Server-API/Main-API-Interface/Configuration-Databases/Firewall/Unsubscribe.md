[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Add.md)

# IMTServerAPI::FirewallUnsubscribe

Unsubscribe from events and hooks associated with the firewall configuration.
    
    
    MTAPIRES  IMTServerAPI::FirewallUnsubscribe(
       IMTConFirewallSink*  sink      // A pointer to the IMTConFirewallSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConFirewallSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTServerAPI::FirewallSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
