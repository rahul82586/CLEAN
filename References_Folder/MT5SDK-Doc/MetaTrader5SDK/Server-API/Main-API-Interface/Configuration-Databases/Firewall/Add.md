[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Add

[Previous](Unsubscribe.md) | [Next](Delete.md)

# IMTServerAPI::FirewallAdd

Add or update a firewall configuration.
    
    
    MTAPIRES  IMTServerAPI::FirewallAdd(
       IMTConFirewall*  config      // Firewall configuration object
       )

### Parameters

**config**  
[in] The firewall configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. The key comparison fields are the beginning and end of the range of addresses -[ IMTConFirewall::From()](../../../../Configuration-Interfaces/Firewall/IMTConFirewall/IMTCon-From.md) and [IMTConFirewall::To()](../../../../Configuration-Interfaces/Firewall/IMTConFirewall/IMTCon-To.md). When you try to add a completely identical record, no changes are made, and therefore the [IMTConFirewallSink::OnFirewallUpdate](../../../../Configuration-Interfaces/Firewall/IMTConFirewallSink/IMTConSink-OnUpdate.md) notification method is not called.
