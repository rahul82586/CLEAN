[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Price Data](../../Price-Data.md) / [IMTTickSink](../IMTTickSink.md) / OnTickStat

[Previous](OnTick.md) | [Next](HookTick.md)

# IMTTickSink::OnTickStat

A handler of the event of update of the statistical information about a price.

C++
    
    
    virtual void  IMTTickSink::OnTickStat(
       const MTTickStat&   tstat      // A reference to a structure of the description of statical information
       )

.NET (Manager API)
    
    
    virtual void  CIMTTickSink.OnTickStat(
       MTTickStat          tstat      // A structure of the description of statical information
       )

### Parameters

**tstat**  
[in] A reference to the structure that describes statistical price information (MTTickStat).

### Note

The event is called after information is saved in the database for this symbol. This means that the statistical information has been received from the current data feed used for the symbol in accordance with the priority (as determined by the position of the data source (gateway/data feed) in the configuration list) and has passed all checks for correctness.

# IMTTickSink::OnTickStat

A handler of the event of update of the statistical price information with the specification of a data source.

C++
    
    
    virtual void  IMTTickSink::OnTickStat(
       const int           feeder,    // The index of the data feed
       const MTTickStat&   tstat      // A reference to a structure of the description of statical information
       )

.NET (Manager API)
    
    
    virtual void  CIMTTickSink.OnTickStat(
       int                 feeder,    // The index of the data feed
       MTTickStat          tstat      // A structure of the description of statical information
       )

### Parameters

**feeder**  
[in] The index of the data source, from which statical information is received.

**tstat**  
[in] A reference to the structure that describes statistical price information (MTTickStat).

### Note

This method is used only in the MetaTrader 5 Server API.

## Identifying the data source based on the feeder index

The type of the data source, from which the information has been received, is determined in accordance with the constants defined in the [EnMTFeederConstants (#enmtfeederconstants)](../../../Structures/MTTick.md#enmtfeederconstants) enumeration:

  * The MT_FEEDER_DEALER (-1) value means that the information was added manually through a manager terminal or API.
  * A value from 0 to 63 (MT_FEEDER_OFFSET - 1) means that the information was received from a gateway.
  * A value of 64 (MT_FEEDER_OFFSET) or greater means that the information was received from a data feed.



After determining the type of data source ([gateway](../../../Configuration-Interfaces/Gateways.md) or [data feed](../../../Configuration-Interfaces/Data-Feeds.md)), we can analyze a certain value. The index corresponds to the position of the data feed/gateway, from which the information was received, in the list of configurations at the time of tick arrival. For example, index 0 means that the information was received from the first gateway in the list of gateway configurations. Value of 65 means that the information was received from the second data feed in the list of data feed configurations.
