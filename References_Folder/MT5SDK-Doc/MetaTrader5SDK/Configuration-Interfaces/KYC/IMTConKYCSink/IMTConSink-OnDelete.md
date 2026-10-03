[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYCSink](../IMTConSink.md) / IMTConSink OnDelete

[Previous](IMTConSink-OnUpdate.md) | [Next](IMTConSink-OnSync.md)

# IMTConKYCSink:OnKYCDelete

The event handler for deleting a KYC provider configuration.

C++
    
    
    virtual void  IMTConKYCSink::OnKYCDelete(
       const IMTConKYC*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConKYCSink.OnKYCDelete(
       CIMTConKYC         config  // Configuration object
       )

### Parameters

**config**  
A pointer to the object of the deleted configuration.

### Note

This method is called by the API to notify that a KYC provider configuration has been deleted.
