[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCSink](../IMTConSink.md) / IMTConSink OnSync

[Previous](IMTConSink-OnDelete.md) | [Next](../../Subscriptions.md)

# IMTConKYCSink::OnKYCSync

The event handler for synchronizing KYC provider configurations.

C++
    
    
    virtual void  IMTConKYCSink::OnKYCSync()

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConKYCSink.OnKYCSync()

### Note

This method is called by the API to notify that KYC provider configurations have been synchronized.
