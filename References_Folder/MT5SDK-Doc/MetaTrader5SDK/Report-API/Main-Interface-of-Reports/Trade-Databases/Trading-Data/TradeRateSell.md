[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Trading Data](../Trading-Data.md) / TradeRateSell

[Previous](TradeRateBuy.md) | [Next](../../Daily-Reports.md)

# IMTReportAPI::TradeRateSell

Calculate the conversion rate for a Sell trade.
    
    
    MTAPIRES  IMTReportAPI::TradeRateSell(
       LPCWSTR       base,            // Name of the sold currency
       LPCWSTR       currency,        // Name of the calculation currency
       double&       rate,            // Conversion rate
       LPCWSTR       group=NULL,      // Group name
       LPCWSTR       symbol=NULL,     // Symbol name
       const double  price=0          // Price
       )

### Parameters

**base**  
[in] Name of the base (sold) currency. Three-letter abbreviation for the currency, for example, EUR.

**currency**  
[in] The name of the currency that is used to pay for the sold currency. Three-letter abbreviation for the currency, for example, USD.

**rate**  
[out] The calculated conversion rate of selling the 'base' currency for the 'currency' currency.

**group=NULL**  
[in] The name of the group of clients, for which the calculations are performed. If the group is specified, then the conversion rate is calculated using the market prices, taking into account spreadadjustmentfor this group. If a group is not specified, market prices are used.

**symbol=NULL**  
[in] The name of the symbol that should be taken into account when calculating the conversion rate. If a trading symbol with the name specified in the symbol parameter is used for calculating the conversion rate, then the 'price' price will be used as the price of this symbol.

**price=0**  
[in] The price of the symbol specified in the symbol parameter, which will be used for conversion instead of the current market price. This parameter is ignored for the symbols with theIMTConSymbol::TRADE_FLAGS_PROFIT_BY_MARKETflag enabled. The market price is always used for such symbols.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code is returned.

### Note

This method calculates the rate of selling the 'base' currency for the 'currency' currency.
