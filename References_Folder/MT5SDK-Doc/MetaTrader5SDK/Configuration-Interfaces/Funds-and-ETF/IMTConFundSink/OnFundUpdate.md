[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundSink](../IMTConFundSink.md) / OnFundUpdate

[Previous](OnFundAdd.md) | [Next](OnFundDelete.md)

# IMTConFundSink::OnFundUpdate

Event handler for fund configuration update.

C++
    
    
    virtual void  IMTConFundSink::OnFundUpdate(
       const IMTConFund*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFundSink.OnFundUpdate(
       CIMTConFund         config  // Configuration object
       )

### Parameters

**config**  
[in] A pointer to the updated configuration objectIMTConFund.

### Note

The API calls this method to notify that a fund configuration has changed.
