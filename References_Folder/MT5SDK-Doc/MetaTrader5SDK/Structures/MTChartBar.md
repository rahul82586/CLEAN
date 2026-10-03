[🏠 Document Start](../README.md) / [Structures](README.md) / MTChartBar

[Previous](MTLogRecord.md) | [Next](MTBookItem.md)

# MTChartBar

The MTChartBar structure describes the bar of a chart. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTChartBar
      {
       INT64             datetime;                               // Date and time
       //--- prices
       double            open;                                   // The Open price
       double            high;                                   // The High price
       double            low;                                    // The Low price
       double            close;                                  // The Close price
       //--- volume
       UINT64            tick_volume;                            // Tick volume
       INT32             spread;                                 // Spread
       UINT64            volume;                                 // Volume
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTAdminAPI::ChartRequest](../Manager-API/Administrator-Interface/History-Data/ChartRequest.md)
  * [IMTAdminAPI::ChartDelete](../Manager-API/Administrator-Interface/History-Data/ChartDelete.md)
  * [IMTAdminAPI::ChartUpdate](../Manager-API/Administrator-Interface/History-Data/ChartUpdate.md)
  * [IMTGatewayAPI::ChartRequest](../Gateway-API/Main-Interface/History-Data/ChartRequest.md)
  * [IMT](../Gateway-API/Main-Interface/History-Data/ChartDelete.md)[Gateway](../Gateway-API/Main-Interface/History-Data/ChartRequest.md)[API::ChartDelete](../Gateway-API/Main-Interface/History-Data/ChartDelete.md)
  * [IMT](../Gateway-API/Main-Interface/History-Data/ChartUpdate.md)[Gateway](../Gateway-API/Main-Interface/History-Data/ChartRequest.md)[API::ChartUpdate](../Gateway-API/Main-Interface/History-Data/ChartUpdate.md)
  * [IMTReportAPI::ChartHistoryGet](../Report-API/Main-Interface-of-Reports/Price-Data/ChartHistoryGet.md)
  * [IMTServerAPI::ChartGet](../Server-API/Main-API-Interface/History-Data/ChartGet.md)
  * [IMTServerAPI::ChartDelete](../Server-API/Main-API-Interface/History-Data/ChartDelete.md)
  * [IMTServerAPI::ChartUpdate](../Server-API/Main-API-Interface/History-Data/ChartUpdate.md)



The structure contains the following parameters:

Field | Type | Description  
datetime | INT64 | Date and time of a bar in seconds that have elapsed since 01.01.1970.  
open | double | Bar open price — price at the beginning of bar formation (beginning of a minute).  
high | double | The highest price inside the bar.  
low | double | The lowest price inside the bar.  
close | double | Bar close price — price at the end of bar formation (end of the minute).  
tick_volume | UINT64 | Tick volume — number of ticks received during bar formation. The variable only counts the ticks that change the price based on which the bar is constructed (Bid or Last, depending on symbol settings). Several ticks in a row with the same price will be counted as one.  
spread | INT32 | The lowest symbol spread recorded during the bar formation time.  
volume | UINT64 | The real volume of trades executed during bar formation.  
  
For more information about working with price data in the platform, please see the [Price Data](https://support.metaquotes.net/en/docs/mt5/platform/administration/common_info/price_data) and [Charts](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_charts) sections.
