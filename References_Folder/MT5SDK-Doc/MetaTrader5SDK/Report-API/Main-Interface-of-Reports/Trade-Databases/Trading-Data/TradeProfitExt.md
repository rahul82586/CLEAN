[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Trading Data](../Trading-Data.md) / TradeProfitExt

[Previous](TradeProfit.md) | [Next](TradeRateBuy.md)

# IMTReportAPI::TradeProfitExt

Calculates profit for the specified trading conditions using extended volume accuracy.
    
    
    MTAPIRES  IMTReportAPI::TradeProfitExt(
       LPCWSTR       group,           // Group name
       LPCWSTR       symbol,          // Symbol name
       const UINT    type,            // Operation type
       const UINT64  volume,          // Volume
       const double  price_open,      // Open price
       const double  price_close,     // Close price
       double&       profit,          // Profit
       double&       profit_rate      // Profit conversion rate
       )

### Program Parameters

**group**  
[in] The name of the group of clients, for which the calculations are performed.

**symbol**  
[in] The name of the trading instrument, for which the calculations are performed.

**type**  
[in] Position direction: buying -IMTPosition::POSITION_BUY, selling -IMTPosition::POSITION_SELL.

**volume**  
[in] Position volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

**price_open**  
[in] Position open price.

**price_close**  
[in] Position close price.

**profit**  
[out] Position profit in thedeposit currencyof the specified group.

**profit_rate**  
[out] Conversion rate for the profit of the position from theprofit currencyof a trading instrument to the group deposit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

Profit is converted from the profit currency of a trading instrument to the group deposit currency using the current market prices for the group.
