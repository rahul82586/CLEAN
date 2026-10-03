[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [History Data](../History-Data.md) / ChartSplit

[Previous](ChartReplace.md) | [Next](../Tick-Data.md)

# IMTAdminAPI::ChartSplit

Split of the symbol's bar history. For details please read the [MetaTrader 5 Administrator Help files](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_charts/split_charts).

C++
    
    
    MTAPIRES  IMTAdminAPI::ChartSplit(
       LPCWSTR            symbol,         // Symbol
       const UINT         new_shares,     // Number of new shares
       const UINT         old_shares,     // Number of old shares
       const UINT         rounding_rule,  // Rounding rule
       const INT64        datetime_from,  // Beginning of interval for split
       const INT64        datetime_to     // End of interval for split
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.ChartSplit(
       string             symbol,         // Symbol
       uint               new_shares,     // Number of new shares
       uint               old_shares,     // Number of old shares
       uint               rounding_rule,  // Rounding rule
       long               datetime_from,  // Beginning of interval for split
       long               datetime_to     // End of interval for split
       )

### Parameters

**symbol**  
[in] The symbol for which you want to run split.

**new_shares**  
[in] Number of new shares. Shares are split/consolidated in a certain ratio, while their prices are also converted accordingly.

**old_shares**  
[in] Number of old shares. Shares are split/consolidated in a certain ratio, while their prices are also converted accordingly.

**rounding_rule**  
[in] The rounding rule in case the number of digital places of a new price exceeds the value set in the symbol's Digits parameter (IMTConSymbol::Digits). The following three options are available:

**datetime_from**  
[in] The beginning date of the time interval in which split will be performed. If the parameter is not set, the split will be performed for the entire symbol price history.

**datetime_to**  
[in] The end date of the time interval in which split will be performed. If the parameter is not set, the split will be performed for the entire symbol price history.

  * 0 — standard rounding
  * 1 — round down
  * 2 — round up



### Return Value

An indication of successful command setting is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is asynchronous and receiving of the MT_RET_OK response does not mean that the split has completed. The operation can take a long time.
