[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFundSink](../IMTConFundSink.md) / OnFundDelete

[Previous](OnFundUpdate.md) | [Next](OnFundSync.md)

# IMTConFundSink:OnFundDelete

Event handler for fund configuration deletion.

C++
    
    
    virtual void  IMTConFundSink::OnFundDelete(
       const IMTConFund*   config  // A pointer to the configuration object
       )

.NET (Gateway/Manager API)
    
    
    virtual void  CIMTConFundSink.OnFundDelete(
       CIMTConFund         config  // Configuration object
       )

### Parameters

**config**  
A pointer to the deletedIMTConFundconfiguration object.

### Note

The API calls this method to notify that a fund configuration has been deleted.
