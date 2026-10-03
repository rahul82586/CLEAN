[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Trade](../../Trade.md) / [General Principles](../General-Principles.md) / Fill Policy

[Previous](State-of-Orders.md) | [Next](Position-Accounting-System.md)

# Fill Policy

In addition to the general rules of execution set separately for each [symbol](../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExecMode.md), the additional "Filling" condition can be specified in an order:

  * Fill or Kill (FOK)  
This fill policy means that an order can be filled only in the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. In the Market and Exchange execution modes, the required volume can be filled by several offers available on the market at the moment.
  * Immediate or Cancel (IOC)  
In this case a trader agrees to execute a deal with the volume maximally available in the market within that indicated in the order. In case the order cannot be filled completely, the available volume of the order will be filled, and the remaining volume will be canceled. The permission to use IOC orders is determined at the trade server.
  * Book or Cancel (BOC)  
The BOC policy indicates that the order can only be placed in the Depth of Market (order book). If the order can be filled immediately when placed, this order is canceled. This policy guarantees that the price of the placed order will be worse than the current market. BOC is used to implement passive trading: it is guaranteed that the order cannot be executed immediately when placed and thus it does not affect current liquidity. This fill policy is only supported for limit and stop limit orders.
  * Return  
This policy is only used for market (Buy and Sell), [limit and stop limit orders (#pending-order)](Types-of-Orders.md#pending-order). If filled partially, an order with the remaining volume is not canceled, and is processed further. For market orders, the Return policy is used only in the Exchange Execution [mode](Types-of-Execution.md), while for limit and stop limit ones, it is applied in the Market Execution and Exchange Execution modes.



Use of fill policies depending on the execution type can be shown as the following table:

Type of Execution\Fill Policy | Fill or Kill | Immediate or Cancel | Book or Cancel | Return  
---|---|---|---|---  
Instant Execution | + | — | — | —  
Request Execution | + | — | — | —  
Market Execution | + | + | — | +  
Exchange Execution | + | + | + | +  
  
> Possible types of filling are listed in [IMTOrder::EnOrderFilling (#enorderfilling)](../Orders/IMTOrder/Enumerations.md#enorderfilling).
