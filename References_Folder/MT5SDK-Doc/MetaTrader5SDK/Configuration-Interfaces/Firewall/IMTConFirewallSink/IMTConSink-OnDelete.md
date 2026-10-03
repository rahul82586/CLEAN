[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewallSink](../IMTConSink.md) / IMTConSink OnDelete

[Previous](IMTConSink-OnUpdate.md) | [Next](IMTConSink-OnSync.md)

# IMTConFirewallSink::OnFirewallDelete

A handler of the event of deletion of a firewall rule.

C++
    
    
    virtual void  IMTConFirewallSink::OnFirewallDelete(
       const IMTConFirewall*  config      // A pointer to the rule object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFirewallSink.OnFirewallDelete(
       CIMTConFirewall        config      // An object of the rule
       )

### Parameters

**config**  
[in] A pointer to the object of the deleted rule.

### Note

This method is called by the API to notify that firewall rule has been deleted.
