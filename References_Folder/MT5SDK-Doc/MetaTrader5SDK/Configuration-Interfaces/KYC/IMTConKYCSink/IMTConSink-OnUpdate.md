[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCSink](../IMTConSink.md) / IMTConSink OnUpdate

[Previous](IMTConSink-OnAdd.md) | [Next](IMTConSink-OnDelete.md)

# IMTConKYCSink::OnKYCUpdate

The event handler for updating a KYC provider configuration.

C++
    
    
    virtual void  IMTConKYCSink::OnKYCUpdate(
       const IMTConKYC*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConKYCSink.OnKYCUpdate(
       CIMTConKYC         config  // Configuration object
       )

### Parameters

**config**  
[in] The pointer to the updated configuration object.

### Note

This method is called by the API to notify that a KYC provider configuration has been modified.
