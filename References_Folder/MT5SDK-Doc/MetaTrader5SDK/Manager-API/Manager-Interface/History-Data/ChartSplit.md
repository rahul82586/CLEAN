[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [History Data](../History-Data.md) / ChartSplit

[Previous](ChartReplace.md) | [Next](../Tick-Data.md)

# IMTManagerAPI::ChartSplit

Split of the symbol's price history. For details please read the [MetaTrader 5 Administrator Help](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_charts/split_charts).

C++
    
    
    MTAPIRES  IMTManagerAPI::ChartSplit(
       LPCWSTR            symbol,         // Symbol
       const UINT         new_shares,     // Number of new shares
       const UINT         old_shares,     // Number of old shares
       const UINT         rounding_rule,  // Rounding rule
       const INT64        datetime_from,  // Beginning of interval for split
       const INT64        datetime_to     // End of interval for split
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ChartSplit(
       string             symbol,         // Symbol
       uint               new_shares,     // Number of new shares
       uint               old_shares,     // Number of old shares
       uint               rounding_rule,  // Rounding rule
       long               datetime_from,  // Beginning of interval for split
       long               datetime_to     // End of interval for split
       )

Python
    
    
    ManagerAPI.ChartSplit(
       symbol,            # Symbol
       new_shares,        # Number of new shares
       old_shares,        # Number of old shares
       rounding_rule,     # Rounding rule
       datetime_from,     # Beginning of interval for split
       datetime_to        # End of interval for split
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

An indication of successful command sending is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method is asynchronous and receiving of the MT_RET_OK response does not mean that the split has completed. The operation can take a long time.
