[🏠 Document Start](../README.md) / [Structures](README.md) / MTTick

[Previous](MTLicenseCheck.md) | [Next](MTTickShort.md)

<a id="mttick"></a>
# MTTick (#mttick)

This structure describes the full information about a tick. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTTick
      {
       //--- Tick flags
       enum EnTickFlags
         {
          TICK_FLAG_BUY  =1,                                    // Created as a result of buy operation
          TICK_FLAG_SELL =2,                                    // Created as a result of sell operation
          //--- Enumeration borders
          TYPE_FIRST     =0,                                    // No flags
          TYPE_LAST      =TICK_FLAG_BUY|TICK_FLAG_SELL          // All flags
         };
       //---
       wchar_t           symbol[32];                            // Symbol
       wchar_t           bank[32];                              // Source
       INT64             datetime;                              // Date and time
       double            bid;                                   // The bid price
       double            ask;                                   // The ask price
       double            last;                                  // The last price
       UINT64            volume;                                // The last deal volume
       INT64             datetime_msc;                          // Date and time in milliseconds
       UINT64            flags;                                 // Flags
       UINT64            volume_ext;                            // Last deal volume with extended accuracy
       UINT              reserved[26];                          // Reserved field
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTManagerAPI::TickAdd](../Manager-API/Manager-Interface/Tick-Data/TickAdd.md)
  * [IMTGatewayAPI::SendTicks](../Gateway-API/Main-Interface/Quote-and-News-Feeds/SendTicks.md)
  * [IMTServerAPI::TickAdd](../Server-API/Main-API-Interface/Tick-Data/TickAdd.md)
  * [IMTTickSink::HookTick](../Database-Interfaces/Price-Data/IMTTickSink/HookTick.md)



The structure contains the following parameters:

Field | Type | Description  
symbol | wchar_t | Symbol name.  
bank | wchar_t | The price source (Liquidity provider).  
datetime | INT64 | Date and time of the tick in seconds passed since 01.01.1970. This fields is not filled in by default (equal to 0) - the history server inserts the server's current trading time when receiving the data. If necessary, the gateway developer can set this date on their own. Using this feature implies 100% correctness of the transferred data time. Therefore, it should be used only when necessary.

  * datetime_msc has a higher priority than datetime. The server will use this value if it it specified.
  * If datetime_msc is specified only, datetime value will be filled automatically on its basis (without milliseconds).
  * If datetime is specified only, datetime_msc value will be filled automatically on its basis (with zero value for milliseconds).

If you specify the time yourself, consider the time zone of the trade server ([IMTConTime::TimeZone](../Configuration-Interfaces/Time/IMTConTime/IMTCon-Zone.md)). For example, if the data feed passes the UNIX time (GMT 0), while the trading server works in GMT+2 time zone, the value should be increased by 60*60*2 (2 hours in seconds).  
bid | double | The Bid price.  
ask | double | The Ask price.  
last | double | The price of the last committed transaction.  
volume | UINT64 | Volume of a last deal. The volume is recorded in the same form as it is passed by a data provider. A data provider may pass volumes as amounts of contracts (in lots) or as amounts of money. On the trading platform side, this value is interpreted depending on the type of calculation of profit and margin set for a symbol ([IMTConSymbol::CalcMode](../Configuration-Interfaces/Symbols/IMTConSymbol/CalcMode.md)):

  * For the [IMTConSymbol::TRADE_MODE_FOREX (#encalcmode)](../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#encalcmode) type, the volumes are interpreted as amounts of money.
  * For all the other type, the volumes are interpreted as amounts of contracts (lots).

For operations with [extended volume accuracy (#volume)](../Development-Features/README.md#volume), use the 'volume_ext' field.

  * The 'volume_ext' value has a higher priority than 'volume'. The server will use this value if specified.
  * When returning volume values, the server fills both fields: with standard and extended accuracy.

  
datetime_msc | INT64 | Date and time of the tick in milliseconds passed since 01.01.1970. This fields is not filled in by default (equal to 0) - the history server inserts the server's current trading time when receiving the data. If necessary, the gateway developer can set this date on their own. Using this feature implies 100% correctness of the transferred data time. Therefore, it should be used only when necessary.

  * datetime_msc has a higher priority than datetime. The server will use this value if it it specified.
  * If datetime_msc is specified only, datetime value will be filled automatically on its basis (without milliseconds).
  * If datetime is specified only, datetime_msc value will be filled automatically on its basis (with zero value for milliseconds).

If you specify the time yourself, consider the time zone of the trade server ([IMTConTime::TimeZone](../Configuration-Interfaces/Time/IMTConTime/IMTCon-Zone.md)). For example, if the data feed passes the UNIX time (GMT 0), while the trading server works in GMT+2 time zone, the value should be increased by 60*60*1000*2 (2 hours in milliseconds).  
flags | UINT64 | Tick flats passed using the EnTickFlags enumeration.  
volume_ext | UINT64 | Last deal volume with [extended accuracy (#volume)](../Development-Features/README.md#volume). It is similar to the 'volume' field, but the value is passed with the fixed number of decimal places (8).

  * The 'volume_ext' value has a higher priority than 'volume'. The server will use this value if specified.
  * When returning volume values, the server fills both fields: with standard and extended accuracy.

  
reserved | UINT | A reserved field for future use.  
  
<a id="enmtfeederconstants"></a>
## EnMTFeederConstants (#enmtfeederconstants)

Indexes are used for specifying the data source, from which the price was received. The type of the data source, from which the information has been received, is determined in accordance with the constants described in the EnMTFeederConstants enumeration.

ID | Value | Description  
MT_FEEDER_DEALER | -1 | Information added manually from a manager terminal or API.  
MT_FEEDER_OFFSET | 64 | This value defines the start of the range of [data feed](../Configuration-Interfaces/Data-Feeds.md) indexes. Values ​​from 0 to 63 mean that the information was received from a [gateway](../Configuration-Interfaces/Gateways.md). Values ​​of 64 or greater indicate that the information was received from a data feed.  
  
The enumeration is used in the following methods:

  * [IMTTickSink::OnTick](../Database-Interfaces/Price-Data/IMTTickSink/OnTick.md)
  * [IMTTickSink::OnTickStat](../Database-Interfaces/Price-Data/IMTTickSink/OnTickStat.md)



<a id="entickflags"></a>
## EnTickFlags (#entickflags)

Tick flags are described in EnTickFlags.

ID | Value | Description  
TICK_FLAG_BUY | 1 | Tick created as a result of a buy operation.  
TICK_FLAG_SELL | 2 | Tick created as a result of a sell operation.  
TICK_FLAG_NONE | 0 | Beginning of enumeration. It corresponds to the absence of flags.  
TICK_FLAG_ALL |  | End of enumeration. All flags are enabled.  
  
Data on direction is generally filled by the source of ticks, i.e. a gateway or a data feed. If the data source does not provide such information, the history server fills the direction automatically using the following algorithm:

  * If the Last deal price is greater than or equal to the last Ask price, the price is considered to be the result of a buy deal (TICK_FLAG_BUY).
  * If the Last deal price is less than or equal to the last Bid price, the price is considered to be the result of a sell deal (TICK_FLAG_SELL).
  * In other cases, it is considered that the direction cannot be determined, and both flags are set for a tick (TICK_FLAG_BUY | TICK_FLAG_SELL).


