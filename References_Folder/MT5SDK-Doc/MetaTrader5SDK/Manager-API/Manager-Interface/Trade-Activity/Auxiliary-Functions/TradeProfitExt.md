[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Auxiliary Functions](../Auxiliary-Functions.md) / TradeProfitExt

[Previous](TradeProfit.md) | [Next](TradeRateBuy.md)

# IMTManagerAPI::TradeProfitExt

Calculates profit for the specified trading conditions using extended volume accuracy.

C++
    
    
    MTAPIRES  IMTManagerAPI::TradeProfitExt(
       LPCWSTR       group,           // Group name
       LPCWSTR       symbol,          // Symbol name
       const UINT    type,            // Operation type
       const UINT64  volume,          // Volume
       const double  price_open,      // Open price
       const double  price_close,     // Close price
       double&       profit,          // Profit
       double&       profit_rate      // Profit conversion rate
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TradeProfitExt(
       string                 group,       // Group name
       string                 symbol,      // Symbol name
       CIMTOrder.EnOrderType  type,        // Operation type
       ulong                  volume,      // Volume
       double                 price_open,  // Open price
       double                 price_close, // Close price
       out double             profit,      // Profit
       out double             profit_rate  // Profit conversion rate
       )

Python
    
    
    ManagerAPI.TradeProfitExt(
       group,                 # Group name
       symbol,                # Symbol name
       type,                  # Type of operation
       volume,                # Volume
       price_open,            # Open price
       price_close            # Close price
       )

### Program Parameters

**group**  
[in] The name of the group of clients, for which the calculations are performed.

**symbol**  
[in] The name of the trading instrument, for which the calculations are performed.

**type**  
[in] Position direction: buying -IMTPosition::POSITION_BUY, selling -IMTPosition::POSITION_SELL.

**volume**  
[in] Position volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

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
