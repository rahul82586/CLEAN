[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / OnTradeSplit

[Previous](OnTradeExecution.md) | [Next](HookTradeRequestAdd.md)

# IMTTradeSink::OnTradeSplit

A handler of the [trading position split](../Main-API-Interface/Trade/Positions/PositionSplit.md) event.
    
    
    virtual void  IMTTradeSink::OnTradeSplit(
       const UINT           shares_new,   // Number of new shares
       const UINT           shares_old,   // Number of old shares
       const UINT           round_prices, // Price rounding rule
       const UINT           round_volumes,// Volume rounding rule
       const UINT           flags,        // Additional split options
       const double         adjustment,   // Adjustments
       const IMTConGroup*   group,        // A pointer to the group configuration object
       const IMTConSymbol*  symbol,       // A pointer to the symbol configuration object
       const IMTPosition*   position_old, // A pointer to the position object
       const IMTPosition*   position_new, // A pointer to the position object
       )

### Parameters

**shares_new**  
[in] Number of new shares.

**shares_old**  
[in] Number of old shares.

**round_prices**  
[in] The price rounding rule in case the number of digital places of a new price exceeds the value set in the symbol's Digits parameter (IMTConSymbol::Digits). The following three options are available:

**round_volumes**  
[in] The volume rounding rule in case the client will have a fractional number of shares after the split. The following three options are available:

**flags**  
[in] Additional split options in the form of flags:

**adjustment**  
[in] The size of the adjustment (passed by the user at split start or calculated by the server).

**group**  
[in] A pointer to thegroup configurationobject of the client for whose position the split is performed.

**symbol**  
[in] A pointer to thetrading symbol configurationobject for the position of which the split is performed.

**position_old**  
[in] A pointer to the object describing thetrading positionstate before the split.

**position_new**  
[in] A pointer to the object describing thetrading positionstate after the split. New prices and new volumes are set for this position in accordance with the split parameters.

  * 0 — standard rounding
  * 1 — round down
  * 2 — round up


  * 0 — standard rounding
  * 1 — round down
  * 2 — round up


  * 1 — clear trading position stop levels to avoid triggering after split.
  * 2 — if the split operation would cause the position volume to become less than one contract, the split operation is not performed. If this flag is set, such positions will be automatically closed.



### Note

The event is called separately for each position after split.
