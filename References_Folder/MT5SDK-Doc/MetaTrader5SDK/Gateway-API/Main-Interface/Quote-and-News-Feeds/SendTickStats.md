[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Quote and News Feeds](../Quote-and-News-Feeds.md) / SendTickStats

[Previous](../Quote-and-News-Feeds.md) | [Next](SendTicks.md)

# IMTGatewayAPI::SendTickStats

Sending statistical information about a financial instrument.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SendTickStats(
       MTTickStat*  stats,           // Statistical data array
       const UINT   stats_total      // Number of the elements in the array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendTickStats(
       MTTickStat[] stats           // Statistical data array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SendTickStat(
       MTTickStat   stats           // A single description of statistical data
       )

### Parameters

**stats**  
[in] A pointer to the statistical data array described by theMTTickStatstructure.

**stats_total**  
[in] Number of the elements in the stats array.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This method sends the filled [MTTickStat](../../../Structures/MTTickStat.md) structures array to the trading platform.

  * bid_high
  * bid_low
  * ask_high
  * ask_low


  * last_high
  * last_low
  * vol_high, vol_high_ext
  * vol_low, vol_low_ext


