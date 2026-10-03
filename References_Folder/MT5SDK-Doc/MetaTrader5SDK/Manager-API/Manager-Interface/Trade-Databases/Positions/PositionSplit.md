[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionSplit

[Previous](PositionDeleteBatch.md) | [Next](../../History-Data.md)

# IMTManagerAPI::PositionSplit

Split trading positions. For details please read the [MetaTrader 5 Manager Help](https://support.metaquotes.net/en/docs/mt5/manager/position_split).

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionSplit(
       UINT64*            tickets,           // Tickets of positions
       const UINT         tickets_total,     // Number of tickets
       const double*      adjustments,       // Balance adjustments
       const UINT         new_shares,        // Number of new shares
       const UINT         old_shares,        // Number of old shares
       const UINT         round_rule_price,  // Price rounding rule
       const UINT         round_rule_volume, // Volume rounding rule
       const UINT         flags,             // Additional split options
       MTAPIRES*          results            // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionSplit(
       ulong[]            tickets,           // Tickets of positions
       ulong[]            adjustments,       // Balance adjustments
       uint               new_shares,        // Number of new shares
       uint               old_shares,        // Number of old shares
       uint               round_rule_price,  // Price rounding rule
       uint               round_rule_volume, // Volume rounding rule
       uint               flags,             // Additional split options
       MTRetCode[]        results            // Array of results
       )

Python
    
    
    ManagerAPI.PositionSplit(
       tickets,           # Tickets of positions
       adjustments,       # Balance adjustments
       new_shares,        # Number of new shares
       old_shares,        # Number of old shares
       round_rule_price,  # Price rounding rule
       round_rule_volume, # Volume rounding rule
       flags              # Additional split options
       )

### Parameters

**tickets**  
[in] An array of tickets of the positions for which you want to perform the split operation.

**ticket_total**  
[in] The number of tickets in the 'tickets' array.

**adjustments**  
[in] Adjustment calculation mode:

**new_shares**  
[in] Number of new shares. Shares are split/consolidated in a certain ratio, while their prices are also converted accordingly.

**old_shares**  
[in] Number of old shares. Shares are split/consolidated in a certain ratio, while their prices are also converted accordingly.

**round_rule_price**  
[in] The price rounding rule in case the number of digital places of a new price exceeds the value set in the symbol's Digits parameter (IMTConSymbol::Digits). The following three options are available:

**round_rule_volume**  
[in] The volume rounding rule in case the client will have a fractional number of shares after the split. The following three options are available:

**flags**  
[in] Additional split options as flags:

**results**  
[in] An array of each position split results.

  * To delegate adjustment calculation to the server, pass nullptr.
  * To use custom adjustment values, pass the filled 'double' array. the array must be filled in accordance with the passed array of position tickets.
  * If no adjustment should be calculated, pass an array of zeros.


  * 0 — standard rounding
  * 1 — round down
  * 2 — round up


  * 0 — standard rounding
  * 1 — round down
  * 2 — round up


  * 1 — it is recommended to clear trading positions' stop levels to avoid their activation after a split. This can be done by setting flag 1.
  * 2 — if the split operation will cause a position volume to become less than one contract, the split operation will be not performed. You can close such positions automatically by using this flag.



### Return Value

An indication of successful command setting is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.
