[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Position

[Previous](ContractSize.md) | [Next](ExternalID.md)

# IMTPosition::Position

Gets the ticket (a unique number) of a trade position in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTPosition::Position()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTPosition.Position()

### Return Value

The ticket of a position in the MetaTrader 5 platform.

### Note

Usually, a position ticket matches the ticket of the order ([IMTOrder::Order](../../Orders/IMTOrder/Order.md)) used to open the position, except when the position is reversed in a single . The ticket may be different for positions with the following opening reasons ([IMTPosition::EnPositionReason (#enpositionreason)](Enumerations.md#enpositionreason)):

  * POSITION_REASON_ROLLOVER — charging swaps with position re-opening
  * POSITION_REASON_SPLIT — re-opening a position after a split
  * POSITION_REASON_VMARGIN — re-opening a position after charging a variation margin
  * POSITION_REASON_SYNC — opening a position when synchronizing with an external system (without a previous order)
  * POSITION_REASON_TRANSFER — relocating a position with a calculated price to a new symbol with the same underlying asset



Tickets of positions having other opening reasons match initial orders.
