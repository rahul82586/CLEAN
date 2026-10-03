[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewallSink](../IMTConSink.md) / IMTConSink OnSync

[Previous](IMTConSink-OnDelete.md) | [Next](../../Symbols.md)

# IMTConFirewallSink::OnFirewallSync

A handler of the firewall rules synchronization event.

C++
    
    
    virtual void  IMTConFirewallSink::OnFirewallSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFirewallSink.OnFirewallSync()

### Note

This method is called by the API to notify that firewall rules have been synchronized.
