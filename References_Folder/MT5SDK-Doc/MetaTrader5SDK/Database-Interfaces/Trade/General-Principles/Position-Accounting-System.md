[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [General Principles](../General-Principles.md) / Position Accounting System

[Previous](Fill-Policy.md) | [Next](../Orders.md)

<a id="position-accounting-system"></a>
# Position Accounting System (#position-accounting-system)

Two position accounting systems are supported in the trading platform: Netting and Hedging. The system used depends on the [group settings](../../../Configuration-Interfaces/Groups/IMTConGroup.md):

![Margin Settings](images/group_margin.png)

Different accounting systems are only supported for the OTC market. Exchange markets only support the netting system.

<a id="netting"></a>
## Netting System (#netting)

With this system, you can have only one common position for a symbol at the same time:

  * If there is an open position for a symbol, executing a deal in the same direction increases the volume of this position.
  * If a deal is executed in the opposite direction, the volume of the existing position can be decreased, the position can be closed (when the deal volume is equal to the position volume) or reversed (if the volume of the opposite deal is greater than the current position).



It does not matter, what has caused the opposite deal — an executed market order or a triggered pending order.

The below example shows execution of two EURUSD Buy deal 0.5 lots each:

![Execution of the two Buy deals resulted in one net position.](images/netting_positions.png)

<a id="hedging"></a>
## Hedging System (#hedging)

With this system, you can have multiple open positions of one and the same symbol, including opposite positions.

If you have an open position for a symbol, and execute a new deal (or a pending order triggers), a new position is additionally opened. Your current position does not change.

The below example shows execution of two EURUSD Buy deal 0.5 lots each:

![Execution of the two Buy deals resulted in two trading positions.](images/hedging_positions.png)

<a id="impact-of-the-system-selected"></a>
## Impact of the System Selected (#impact-of-the-system-selected)

Depending on the position accounting system, some of the platform functions may have different behavior:

  * Stop Loss and Take Profit inheritance rules may differ. More details are provided in the client terminal user guide.
  * If you need to close a position in the netting system, you should perform an opposite trading operation for the same symbol and the same volume. In order to close a position in the hedging system, explicitly select the "Close Position" command in the context menu of the position.
  * A position cannot be reversed in the hedging system. In this case, the current position is closed and a new one with the remaining volume is opened.
  * In the hedging system, a new condition for margin calculation is available — [Hedged margin](../../../Configuration-Interfaces/Symbols/IMTConSymbol.md).


