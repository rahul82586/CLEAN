[🏠 Document Start](../README.md) / [Structures](README.md) / MTTickStat

[Previous](MTTickRate.md) | [Next](MTMailRange.md)

<a id="mttickstat"></a>
# MTTickStat (#mttickstat)

This structure describes the statistical information about a symbol. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTTickStat
      {
       wchar_t           symbol[32];                            // Symbol
       INT64             datetime;                              // Date and time
       //--- bid
       double            bid_high;                              // max. bid
       double            bid_low;                               // min. bid
       //--- ask
       double            ask_high;                              // max. ask
       double            ask_low;                               // min. ask
       //--- last price
       double            last_high;                             // max. last
       double            last_low;                              // min. last
       //--- trade volume
       UINT64            vol_high;                              // max. volume
       UINT64            vol_low;                               // min. volume
       //--- Trade session statistics
       UINT64            trade_deals;                           // The number of deals during a session
       UINT64            trade_volume;                          // The volume of deals during a session
       UINT64            trade_turnover;                        // Turnover for a session
       UINT64            trade_interest;                        // The volume of effective contracts
       UINT64            trade_buy_orders;                      // The number of buy orders
       UINT64            trade_buy_volume;                      // The volume of buy orders
       UINT64            trade_sell_orders;                     // The number of sell orders
       UINT64            trade_sell_volume;                     // The volume of sell orders
       UINT64            trade_volume_ext;                      // The volume of deals within the session, with extended accuracy
       UINT64            trade_buy_volume_ext;                  // The volume of buy requests with extended accuracy
       UINT64            trade_sell_volume_ext;                 // The volume of sell requests with extended accuracy
       UINT64            vol_high_ext;                          // Max volume with extended accuracy
       UINT64            vol_low_ext;                           // Min volume with extended accuracy
       int               trade_reserved[20];                    // Reserved field
       //--- Date and time
       INT64             datetime_msc;                          // Date and time in milliseconds
       //--- Quotation session statistics
       double            price_open;                            // Session open price
       double            price_close;                           // Session close price
       double            price_aw;                              // Average weighted price
       double            price_obsolete;                        // Obsolete field
       double            price_volatility;                      // Price volatility
       double            price_theortical;                      // Theoretical price of an option
       double            price_greeks_delta;                    // Option delta
       double            price_greeks_theta;                    // Option theta
       double            price_greeks_gamma;                    // Option gamma
       double            price_greeks_vega;                     // Option vega
       double            price_greeks_rho;                      // Option rho
       double            price_greeks_omega;                    // Option omega
       double            price_sensitivity;                     // Option sensitivity
       int               price_reserved[14];                    // Reserved field
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTManagerAPI::TickAddStat](../Manager-API/Manager-Interface/Tick-Data/TickAddStat.md)
  * [IMTManagerAPI::TickStat](../Manager-API/Manager-Interface/Tick-Data/TickStat.md)
  * [IMTTickSink::OnTickStat](../Database-Interfaces/Price-Data/IMTTickSink/OnTickStat.md)
  * [IMTTickSink::HookTickStat](../Database-Interfaces/Price-Data/IMTTickSink/HookTickStat.md)
  * [IMTGatewayAPI::SendTickStats](../Gateway-API/Main-Interface/Quote-and-News-Feeds/SendTickStats.md)
  * [IMTServerAPI::TickAddStat](../Server-API/Main-API-Interface/Tick-Data/TickAddStat.md)
  * [IMTServerAPI::TickStat](../Server-API/Main-API-Interface/Tick-Data/TickStat.md)



The structure contains the following parameters:

Field | Type | Description  
news | wchar_t | Symbol name.  
datetime | INT64 | Date and time of the tick in seconds passed since 01.01.1970. This fields is not filled in by default (equal to 0) - the history server inserts the server's current trading time when receiving the data. If necessary, the gateway developer can set this date on their own. Using this feature implies 100% correctness of the transferred data time. Therefore, it should be used only when necessary.

  * datetime_msc has a higher priority than datetime. The server will use this value if it it specified.
  * If datetime_msc is specified only, datetime value will be filled automatically on its basis (without milliseconds).
  * If datetime is specified only, datetime_msc value will be filled automatically on its basis (with zero value for milliseconds).

If you specify the time yourself, consider the time zone of the trade server ([IMTConTime::TimeZone](../Configuration-Interfaces/Time/IMTConTime/IMTCon-Zone.md)). For example, if the data feed passes the UNIX time (GMT 0), while the trading server works in GMT+2 time zone, the value should be increased by 60*60*2 (2 hours in seconds).  
bid_high | double | The highest bid price for the current day.  
bid_low | double | The lowest bid price for the current day.  
ask_high | double | The highest ask price for the current day.  
ask_low | double | The highest and lowest ask prices for the current day.  
last_high | double | The highest price at which a deal has been conducted for the current day.  
last_low | double | The lowest price at which a deal has been conducted for the current day.  
vol_high | UINT64 | The maximum volume of a deal for the current day. When specifying a value pay attention to the peculiarities of working with volume. For operations with [extended volume accuracy (#volume)](../Development-Features/README.md#volume), use the vol_high_ext field.  
vol_low | UINT64 | The minimum volume of a deal for the current day. When specifying a value pay attention to the peculiarities of working with volume. For operations with [extended volume accuracy (#volume)](../Development-Features/README.md#volume), use the vol_low_ext field.  
trade_deals | UINT64 | The total number of deals executed for the current session.  
trade_volume | UINT64 | The total volume of deals executed for the current session. When specifying a value pay attention to the peculiarities of working with volume. For operations with [extended volume accuracy (#volume)](../Development-Features/README.md#volume), use the trade_volume_ext field.  
trade_turnover | UINT64 | Money turnover for a symbol for the current session.  
trade_interest | UINT64 | The total volume of effective contracts (futures, options) for which there have been no calculations yet.  
trade_buy_orders | UINT64 | The total number of buy requests.  
trade_buy_volume | UINT64 | The total volume of buy requests. When specifying a value pay attention to the peculiarities of working with volume. For operations with [extended volume accuracy (#volume)](../Development-Features/README.md#volume), use the trade_buy_volume_ext field.  
trade_sell_orders | UINT64 | The total number of sell requests.  
trade_sell_volume | UINT64 | The total volume of buy sell requests. When specifying a value pay attention to the peculiarities of working with volume. For operations with [extended volume accuracy (#volume)](../Development-Features/README.md#volume), use the trade_sell_volume_ext field.  
trade_volume_ext | UINT64 | The total volume of deals within a session, with [extended accuracy (#volume)](../Development-Features/README.md#volume). It is similar to the 'trade_volume' field, but the value is passed with the fixed number of decimal places (8). The 'trade_volume_ext' value has a higher priority than 'trade_volume'.  
trade_buy_volume_ext | UINT64 | The total volume of buy requests with [extended accuracy (#volume)](../Development-Features/README.md#volume). It is similar to the 'trade_buy_volume' field, but the value is passed with the fixed number of decimal places (8). The 'trade_buy_volume_ext' value has a higher priority than 'trade_buy_volume'.  
trade_sell_volume_ext | UINT64 | The total volume of sell requests with [extended accuracy (#volume)](../Development-Features/README.md#volume). It is similar to the 'trade_sell_volume' field, but the value is passed with the fixed number of decimal places (8). The 'trade_sell_volume_ext' value has a higher priority than 'trade_sell_volume'.  
vol_high_ext | UINT64 | The maximum deal volume doe a day, with [extended accuracy (#volume)](../Development-Features/README.md#volume). It is similar to the 'vol_high' field, but the value is passed with the fixed number of decimal places (8). The 'vol_high_ext' value has a higher priority than 'vol_high'.  
vol_low_ext | UINT64 | The minimum deal volume doe a day, with [extended accuracy (#volume)](../Development-Features/README.md#volume). It is similar to the 'vol_low' field, but the value is passed with the fixed number of decimal places (8). The 'vol_low_ext' value has a higher priority than 'vol_low'.  
trade_reserved | int | A reserved field for future use.  
datetime_msc | INT64 | Date and time of the tick in milliseconds passed since 01.01.1970. This fields is not filled in by default (equal to 0) - the history server inserts the server's current trading time when receiving the data. If necessary, the gateway developer can set this date on their own. Using this feature implies 100% correctness of the transferred data time. Therefore, it should be used only when necessary.

  * datetime_msc has a higher priority than datetime. The server will use this value if it it specified.
  * If datetime_msc is specified only, datetime value will be filled automatically on its basis (without milliseconds).
  * If datetime is specified only, datetime_msc value will be filled automatically on its basis (with zero value for milliseconds).

If you specify the time yourself, consider the time zone of the trade server ([IMTConTime::TimeZone](../Configuration-Interfaces/Time/IMTConTime/IMTCon-Zone.md)). For example, if the data feed passes the UNIX time (GMT 0), while the trading server works in GMT+2 time zone, the value should be increased by 60*60*1000*2 (2 hours in milliseconds).  
price_open | double | The Open price of the current (last active) session.  
price_close | double | The Close price of the previous session (of the last session of the previous trading day).  
price_aw | double | The weighted average price for a session.  
price_obsolete | double | This is a deprecated field which was previously used to pass the price change in percentage terms (price_change). The server no longer accepts the value of this field.  
price_volatility | double | The implied volatility. It is specified as a percentage, and characterizes the expectations of market participants about the value of the underlying asset of the option.  
price_theoretical | double | The theoretical (fair) price of an option calculated for the specified strike based on historical data.  
price_greeks_delta | double | Option delta. "[The Greeks (#greeks)](https://www.metatrader5.com/ru/terminal/help/trading/options_board#greeks)", which include Delta, Theta, Gamma, Vega, Po and Omega, are quantities representing the sensitivity of the option price to changes in various parameters: strike prices, volatility, etc.  
price_greeks_theta | double | Option theta.  
price_greeks_gamma | double | Option gamma.  
price_greeks_vega | double | Option vega.  
price_greeks_rho | double | Option rho.  
price_greeks_omega | double | Option omega.  
price_sensitivity | double | Option sensitivity. It shows by how many points the price of the option's underlying asset should change so that the price of the option changes by one point.  
price_reserved | int | A reserved field for future use.  
  
<a id="volume"></a>
## Peculiarities of working with volume (#volume)

Volume (for example, in the parameters like trade_sell_volume, trade_buy_volume etc.) is recorded in the same form as it is passed by a data provider. A data provider may pass volumes as amounts of contracts (in lots) or as amounts of money. On the trading platform side, this value is interpreted depending on the type of calculation of profit and margin set for a symbol ([IMTConSymbol::CalcMode](../Configuration-Interfaces/Symbols/IMTConSymbol/CalcMode.md)):

  * For the [IMTConSymbol::TRADE_MODE_FOREX (#encalcmode)](../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#encalcmode) type, the volumes are interpreted as amounts of money.
  * For all the other type, the volumes are interpreted as amounts of contracts (lots).



Notes on extended volume accuracy operations:

  * The *_volume_ext value always has a higher priority than *_volume. The server will use this value if specified.
  * If only the '*_volume_ext' value is specified, the '*_volume' field will be filled automatically based on the extended accuracy value (without milliseconds).
  * If only '*_volume' is specified, the '*_volume_ext' field will be filled automatically on the bases of the standard accuracy value (with zero milliseconds).


