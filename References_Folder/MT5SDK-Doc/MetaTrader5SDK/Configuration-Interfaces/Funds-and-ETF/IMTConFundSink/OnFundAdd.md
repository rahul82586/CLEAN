[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundSink](../IMTConFundSink.md) / OnFundAdd

[Previous](../IMTConFundSink.md) | [Next](OnFundUpdate.md)

# IMTConFundSink::OnFundAdd

Event handler for adding of a new fund configuration.

C++
    
    
    virtual void  IMTConFundSink::OnFundAdd(
       const IMTConFund*  config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFundSink.OnFundAdd(
       CIMTConFund        config  // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the added configuration objectIMTConFund.

### Note

The API calls this method to notify that a new fund configuration has been added.
