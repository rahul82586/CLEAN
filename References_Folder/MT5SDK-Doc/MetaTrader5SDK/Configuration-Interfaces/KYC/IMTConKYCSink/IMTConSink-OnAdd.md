[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCSink](../IMTConSink.md) / IMTConSink OnAdd

[Previous](../IMTConSink.md) | [Next](IMTConSink-OnUpdate.md)

# IMTConKYCSink::OnKYCAdd

The event handler for adding a new KYC provider configuration.

C++
    
    
    virtual void  IMTConKYCSink::OnKYCAdd(
       const IMTConKYC*  config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConKYCSink.OnKYCAdd(
       CIMTConKYC        config  // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the object of the added configuration.

### Note

This method is called by the API to notify that a new KYC provider configuration has been added.
