[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Price Data](../../Price-Data.md) / [IMTTickSink](../IMTTickSink.md) / OnTick

[Previous](../IMTTickSink.md) | [Next](OnTickStat.md)

# IMTTickSink::OnTick

A handler of the event of new quote arrival.

C++
    
    
    virtual void  IMTTickSink::OnTick(
       LPCWSTR             symbol,     // Symbol
       const MTTickShort&  tick        // A reference to the quote structure
       )

.NET (Manager API)
    
    
    virtual void  CIMTTickSink.OnTick(
       string              symbol,     // Symbol
       MTTickShort         tick        // Quote structure
       )

### Parameters

**news**  
[in] The name of the symbol a quote for which has arrived.

**tick**  
[in] A reference to the structure describing the quote (MTTickShort).

### Note

The event is called after a quote is saved in the database for this symbol. This means that the quote has been received from the current data feed used for the symbol in accordance with the priority (as determined by the position of the data source (gateway/data feed) in the configuration list) and has passed all checks for correctness and compliance with the [filtering](../../../Configuration-Interfaces/Symbols/IMTConSymbol/FilterSoft.md) criteria.

# IMTTickSink::OnTick

A handler of the event of new quote arrival with the specification of the data source.

C++
    
    
    virtual void  IMTTickSink::OnTick(
       const int           feeder,     // The index of the data feed
       const MTTick&       tick        // A reference to the structure of the quote
       )

.NET (Manager API)
    
    
    virtual void  CIMTTickSink.OnTick(
       int                 feeder,     // The index of the data feed
       MTTick              tick        // Quote structure
       )

### Parameters

**feeder**  
[in] The index of the data source, from which a quote is received.

**tick**  
[in] A reference to the structure that described the quote (MTTick).

### Note

This method is used only in the MetaTrader 5 Server API.

## Identifying the data source based on the feeder index

The type of the data source from which the quote has been received is determined in accordance with the constants defined in the [EnMTFeederConstants (#enmtfeederconstants)](../../../Structures/MTTick.md#enmtfeederconstants) enumeration:

  * The MT_FEEDER_DEALER (-1) value means that the quote was added manually through a manager terminal or API.
  * A value from 0 to 63 (MT_FEEDER_OFFSET - 1) means that the quote was received from a gateway.
  * A value of 64 (MT_FEEDER_OFFSET) or greater means that the quote was received from a data feed.



After determining the type of data source ([gateway](../../../Configuration-Interfaces/Gateways.md) or [data feed](../../../Configuration-Interfaces/Data-Feeds.md)), we can analyze a certain value. The index corresponds to the position of the data feed/gateway, from which the quote was received, in the list of configurations at the time of tick arrival. For example, index 0 means that the quote came from the first gateway in the list of gateway configurations. Value of 65 means that the quote came from the second data feed in the list of data feed configurations.
