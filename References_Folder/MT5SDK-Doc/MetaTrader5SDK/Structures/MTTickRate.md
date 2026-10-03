[🏠 Document Start](../README.md) / [Structures](README.md) / MTTickRate

[Previous](MTTickShort.md) | [Next](MTTickStat.md)

<a id="mttickrate"></a>
# MTTickRate (#mttickrate)

This structure describes brief information about a tick. It differs from the [MTTick](MTTick.md) abd [MTTickShort](MTTickShort.md) structures by a reduced number of fields. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTTickRate
      {
       //--- tick flags
       enum EnTickShortFlags
         {
          TICK_SHORT_FLAG_RAW   =0x00000001,                    // source ticks
          TICK_SHORT_FLAG_BID   =0x00000002,                    // the tick changed the bid price
          TICK_SHORT_FLAG_ASK   =0x00000004,                    // the tick changed the ask price
          TICK_SHORT_FLAG_LAST  =0x00000008,                    // the tick changed the last price
          TICK_SHORT_FLAG_VOLUME=0x00000010,                    // the tick changed the volume
          TICK_SHORT_FLAG_BUY   =0x00000020,                    // the tick appeared as a result of a buy operation
          TICK_SHORT_FLAG_SELL  =0x00000040,                    // the tick appeared as a result of a sell operation
          //--- enumeration borders
          TICK_SHORT_FLAG_NONE  =0x00000000,                    // no flags
         };
       INT64             datetime_msc;                          // date and time in milliseconds
       double            bid;                                   // bid price
       double            ask;                                   // ask price
       double            last;                                  // last price
       UINT64            flags;                                 // flags
       UINT64            volume_ext;                            // last deal volume
       UINT              reserved[2];                           // reserved field
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTGatewayAPI::TickHistoryRequest](../Gateway-API/Main-Interface/Tick-Data/TickHistoryRequest.md)
  * [IMTGatewayAPI::TickHistoryRequestRaw](../Gateway-API/Main-Interface/Tick-Data/TickHistoryRequestRaw.md)
  * [IMTGatewayAPI::TickHistoryAdd](../Gateway-API/Main-Interface/Tick-Data/TickHistoryAdd.md)
  * [IMTGatewayAPI::TickHistoryReplace](../Gateway-API/Main-Interface/Tick-Data/TickHistoryReplace.md)



The structure contains the following parameters:

Field | Type | Description  
datetime_msc | INT64 | The date and time of a tick as a number of milliseconds since 01.01.1970. This field is empty by default (the value is 0), while the historical server adds the current server trading time when receiving data. If necessary, the gateway developer can set this parameter on his own. Using this feature implies 100% correctness of the transferred data time. Therefore, it should be used only when necessary. If you specify the time yourself, consider the time zone of the trade server ([IMTConTime::TimeZone](../Configuration-Interfaces/Time/IMTConTime/IMTCon-Zone.md)). For example, if the data feed passes the UNIX time (GMT 0), while the trading server works in GMT+2 time zone, the value should be increased by 60*60*1000*2 (2 hours in milliseconds).  
bid | double | The Bid price.  
ask | double | The Ask price.  
last | double | The price of the last committed transaction.  
flags | UINT64 | Tick flags specified using the EnTickShortFlags enumeration. The flags reveal additional information about the tick and the data it has changed.  
volume_ext | UINT64 | Last deal volume. The value is passed with a fixed number of decimal places (8). The volume is recorded in the same form, in which it is passed by the data provider. The data provider can broadcast it both in the form of the number of lots (contracts) and as a monetary amount. On the trading platform side, this value is interpreted depending on the profit calculation and margin calculation type, which is specified for the symbol ([IMTConSymbol :: CalcMode](../Configuration-Interfaces/Symbols/IMTConSymbol/CalcMode.md)):

  * For the [IMTConSymbol::TRADE_MODE_FOREX (#encalcmode)](../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#encalcmode) type, the volume is interpreted as a monetary amount.
  * For all other types the volume is interpreted as the number of contracts (lots).

  
reserved | UINT | A reserved field for future use.  
  
<a id="entickshortflags"></a>
## EnTickShortFlags (#entickshortflags)

EnTickShortFlags contains the tick flags.

Identifier | Value | Description  
TICK_SHORT_FLAG_RAW | 0x00000001 | Initial tick obtained from a data source/gateway. The tick was not transformed (for example, according to the symbol spread balance — [IMTConSymbol::SpreadBalance](../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadBalance.md)).  
TICK_SHORT_FLAG_BID | 0x00000002 | The tick changed the Bid price.  
TICK_SHORT_FLAG_ASK | 0x00000004 | The tick changed the Ask price.  
TICK_SHORT_FLAG_LAST | 0x00000008 | The tick changed the Last price.  
TICK_SHORT_FLAG_VOLUME | 0x00000010 | The tick changed the volume.  
TICK_FLAG_BUY | 0x00000020 | The tick was created as a result of a buy operation.  
TICK_FLAG_SELL | 0x00000040 | The tick was created as a result of a sell operation.  
TICK_FLAG_NONE | 0x00000000 | No flags.
