[🏠 Document Start](../README.md) / [Structures](README.md) / MTTickShort

[Previous](MTTick.md) | [Next](MTTickRate.md)

<a id="mttickshort"></a>
# MTTickShort (#mttickshort)

This structure describes a summary information about a tick. It differs from the [MTTick](MTTick.md) structure by a reduced number of fields. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTTickShort
      {
       //--- Tick flags
       enum EnTickShortFlags
         {
          TICK_SHORT_FLAG_RAW   =0x00000001,                    // Raw tick
          TICK_SHORT_FLAG_BID   =0x00000002,                    // Tick changes bid price value
          TICK_SHORT_FLAG_ASK   =0x00000004,                    // Tick changes ask price value
          TICK_SHORT_FLAG_LAST  =0x00000008,                    // Tick changes last price value
          TICK_SHORT_FLAG_VOLUME=0x00000010,                    // Tick changes volume value
          TICK_SHORT_FLAG_BUY   =0x00000020,                    // Tick created due to a buy operation
          TICK_SHORT_FLAG_SELL  =0x00000040,                    // Tick created due to a sell operation
          //--- Enumeration borders
          TICK_SHORT_FLAG_NONE  =0x00000000,                    // none
         };
       INT64             datetime;                              // Date and time
       double            bid;                                   // The bid price
       double            ask;                                   // The ask price
       double            last;                                  // The last price
       UINT64            volume;                                // The tick volume
       INT64             datetime_msc;                          // Date and time in milliseconds
       UINT64            flags;                                 // Flags
       UINT64            volume_ext;                            // Last deal volume with extended accuracy
       UINT              reserved[26];                          // Reserved field
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTManagerAPI::TickLast](../Manager-API/Manager-Interface/Tick-Data/TickLast.md)
  * [IMTManagerAPI::TickHistoryRequest](../Manager-API/Manager-Interface/Tick-Data/TickHistoryRequest.md)
  * [IMTAdminAPI::TickRequest](../Manager-API/Administrator-Interface/Tick-Data/TickRequest.md)
  * [IMTAdminAPI::TickRequestRaw](../Manager-API/Administrator-Interface/Tick-Data/TickRequestRaw.md)
  * [IMTAdminAPI::TickAdd](../Manager-API/Administrator-Interface/Tick-Data/TickAdd.md)
  * [IMTAdminAPI::TickReplace](../Manager-API/Administrator-Interface/Tick-Data/TickReplace.md)
  * [IMTTickSink::OnTick](../Database-Interfaces/Price-Data/IMTTickSink/OnTick.md)
  * [IMTReportAPI::TickHistoryGet](../Report-API/Main-Interface-of-Reports/Price-Data/TickHistoryGet.md)
  * [IMTReportAPI::TickHistoryGetRaw](../Report-API/Main-Interface-of-Reports/Price-Data/TickHistoryGetRaw.md)
  * [IMTServerAPI::TickLast](../Server-API/Main-API-Interface/Tick-Data/TickLast.md)
  * [IMTServerAPI::TickGet](../Server-API/Main-API-Interface/Tick-Data/TickGet.md)
  * [IMTServerAPI::TickGetRaw](../Server-API/Main-API-Interface/Tick-Data/TickHistoryGetRaw.md)



The structure contains the following parameters:

Field | Type | Description  
datetime | INT64 | Date and time of the tick in seconds passed since 01.01.1970. This fields is not filled in by default (equal to 0) - the history server inserts the server's current trading time when receiving the data. If necessary, the gateway developer can set this date on their own. Using this feature implies 100% correctness of the transferred data time. Therefore, it should be used only when necessary.

  * datetime_msc has a higher priority than datetime. The server will use this value if it it specified.
  * If datetime_msc is specified only, datetime value will be filled automatically on its basis (without milliseconds).
  * If datetime is specified only, datetime_msc value will be filled automatically on its basis (with zero value for milliseconds).

If you specify the time yourself, consider the time zone of the trade server ([IMTConTime::TimeZone](../Configuration-Interfaces/Time/IMTConTime/IMTCon-Zone.md)). For example, if the data feed passes the UNIX time (GMT 0), while the trading server works in GMT+2 time zone, the value should be increased by 60*60*2 (2 hours in seconds).  
bid | double | The Bid price.  
ask | double | The Ask price.  
last | double | The price of the last committed transaction.  
volume | UINT64 | Volume. The volume is recorded in the same form as it is passed by a data provider. A data provider may pass volumes as amounts of contracts (in lots) or as amounts of money. On the trading platform side, this value is interpreted depending on the type of calculation of profit and margin set for a symbol ([IMTConSymbol::CalcMode](../Configuration-Interfaces/Symbols/IMTConSymbol/CalcMode.md)):

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
flags | UINT64 | Tick flags passed using the EnTickShortFlags enumeration. The flags reveal additional information about the tick and the data it has changed.  
volume_ext | UINT64 | Last deal volume with [extended accuracy (#volume)](../Development-Features/README.md#volume). It is similar to the 'volume' field, but the value is passed with the fixed number of decimal places (8).

  * The 'volume_ext' value has a higher priority than 'volume'. The server will use this value if specified.
  * When returning volume values, the server fills both fields: with standard and extended accuracy.

  
reserved | UINT | A reserved field for future use.  
  
<a id="entickshortflags"></a>
## EnTickShortFlags (#entickshortflags)

EnTickShortFlags contains the tick flags.

ID | Value | Description  
TICK_SHORT_FLAG_RAW | 0x00000001 | Initial tick obtained from a data source/gateway. The tick has not been transformed (for example, according to the symbol spread balance — [IMTConSymbol::SpreadBalance](../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadBalance.md)).  
TICK_SHORT_FLAG_BID | 0x00000002 | Tick has changed the Bid price.  
TICK_SHORT_FLAG_ASK | 0x00000004 | Tick has changed the Ask price.  
TICK_SHORT_FLAG_LAST | 0x00000008 | Tick has changed the Last price.  
TICK_SHORT_FLAG_VOLUME | 0x00000010 | Tick has changed the volume.  
TICK_FLAG_BUY | 0x00000020 | Tick has been created as a result of a buy operation.  
TICK_FLAG_SELL | 0x00000040 | Tick has been created as a result of a sell operation.  
TICK_FLAG_NONE | 0x00000000 | No flags.
