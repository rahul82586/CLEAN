[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewallSink](../IMTConSink.md) / IMTConSink OnUpdate

[Previous](IMTConSink-OnAdd.md) | [Next](IMTConSink-OnDelete.md)

# IMTConFirewallSink::OnFirewallUpdate

A handler of the event of update of a firewall rule.

C++
    
    
    virtual void  IMTConFirewallSink::OnFirewallUpdate(
       const IMTConFirewall*  config      // A pointer to the rule object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFirewallSink.OnFirewallUpdate(
       CIMTConFirewall        config      // An object of the rule
       )

### Parameters

**config**  
[in] A pointer to the updated rule object.

### Note

This method is called by the API to notify that firewall rule has been updated.
