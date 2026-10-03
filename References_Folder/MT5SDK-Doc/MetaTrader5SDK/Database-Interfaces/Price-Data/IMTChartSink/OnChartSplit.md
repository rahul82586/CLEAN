[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Price Data](../../Price-Data.md) / [IMTChartSink](../IMTChartSink.md) / OnChartSplit

[Previous](Enumerations.md) | [Next](HookChartSplit.md)

# IMTChartSink::OnChartSplit

Price data split event handler For further details about the split operation please refer to [MetaTrader 5 Administrator Help](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_charts/split_charts).
    
    
    virtual void  IMTChartSink::OnChartSplit(
       LPCWSTR            symbol,         // Symbol
       const double       new_shares,     // Number of new shares
       const double       old_shares,     // Number of old shares
       const UINT         rounding_rule,  // Rounding rule
       const INT64        datetime_from,  // Beginning of split range
       const INT64        datetime_to     // End of split range
       )

### Parameters

**news**  
[in] The symbol for which the split is performed.

**new_shares**  
[in] Number of new shares. Shares are split/consolidated in a certain ratio, and their prices are also converted accordingly.

**old_shares**  
[in] Number of old shares. Shares are split/consolidated in a certain ratio, and their prices are also converted accordingly.

**rounding_rule**  
[in] The rounding rule in case the number of decimal places of a new price after conversion exceeds the value set in the symbol's Digits parameter (IMTConSymbol::Digits). Specified by a value from theIMTChartSink::EnSplitRoundingenumeration.

**datetime_from**  
[in] The beginning date of the time interval in which split will be performed. If the parameter is not set, the split will be performed for the entire symbol price history.

**datetime_to**  
[in] The end date of the time interval in which split will be performed. If the parameter is not set, the split will be performed for the entire symbol price history.

### Note

The method is only used in the MetaTrader 5 Server API.
