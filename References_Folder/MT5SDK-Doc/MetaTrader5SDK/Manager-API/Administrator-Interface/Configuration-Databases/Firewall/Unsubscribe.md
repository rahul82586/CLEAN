[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Unsubscribe

[Previous](Subscribe.md) | [Next](Update.md)

# IMTAdminAPI::FirewallUnsubscribe

Unsubscribe from events associated with the firewall configuration.

C++
    
    
    MTAPIRES  IMTAdminAPI::FirewallUnsubscribe(
       IMTConFirewallSink*  sink      // A pointer to the IMTConFirewallSink object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.FirewallUnsubscribe(
       CIMTConFirewallSink  sink      // CIMTConFirewallSink object
       )

Python
    
    
    AdminAPI.FirewallUnsubscribe(
       sink                 # IMTConFirewallSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTConFirewallSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTAdminAPI::FirewallSubscribe](Subscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
