[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests Profit

[Previous](Requests-Request.md) | [Next](Requests-ProfitExt.md)

# IMTServerAPI::TradeProfit

Calculates profit for the specified trading conditions.
    
    
    MTAPIRES  IMTServerAPI::TradeProfit(
       LPCWSTR       group,           // Group name
       LPCWSTR       symbol,          // Symbol name
       const UINT    type,            // Type of operation
       const UINT64  volume,          // Volume
       const double  price_open,      // Open price
       const double  price_close,     // Close price
       double&       profit,          // Profit
       double&       profit_rate      // Profit conversion rate
       )

### Parameters

**group**  
[in] The name of the group of clients, for which the calculations are performed.

**symbol**  
[in] The name of the trading instrument, for which the calculations are performed.

**type**  
[in] Position direction: Buy -IMTPosition::POSITION_BUY, Sell -IMTPosition::POSITION_SELL.

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

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Profit is converted from the profit currency of a trading instrument to the group deposit currency using the current market prices for the group.
