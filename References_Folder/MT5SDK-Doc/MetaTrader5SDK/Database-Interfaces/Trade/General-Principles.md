[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Trade](../Trade.md) / General Principles

[Previous](../Trade.md) | [Next](General-Principles/Types-of-Orders.md)

# General Principles

Before you begin to study trading functions of the Server API, you must have a clear understanding of the basic terms: [order](Orders.md), [deal](Deals.md) and [position](Positions.md).

  * Order  
An order is an instruction for a broker to buy or sell a financial instrument. There are two main [types of orders](General-Principles/Types-of-Orders.md): market and pending. In addition, there are special Take Profit and Stop Loss orders.
  * Deal  
A Deal is a fact of buying or selling a symbol. Buying is executed at the demand price (Ask), and Sell is performed at the supply price (Bid). A deal can be opened as a result of execution of a market order or triggering of a pending order. Keep in mind that in some cases, execution of an order can result in several deals.
  * Position  
A position is a market obligation, i.e. the number of bought or sold contracts of a financial instrument. A long position is financial security bought expecting the security price go higher. A short position is an obligation to supply a security expecting the price will fall in future.



## Interrelation of orders, deals and positions

The platform allows you to easily track how a position was opened or how a deal was performed. Each trading operation has its unique ID called a "ticket". Each order and deal receive a ticket relating to their relevant position. Each deal receives a ticket of an order, by which it was concluded.

If a position was affected by multiple deals, for example in the case of a partial closing or increasing volumes, each of the deals feature the position's ticket. This makes it easy to track the entire history of the position as a whole.

If trading operations are sent to an exchange or a liquidity provider, they additionally feature an ID from an external system. This allows additional tracking of the interrelation of operations away from the platform.

![The history of opening a position can be tracked by tickets](images/operation_connnection.png)

## General Scheme of Trade Operations

  * From the client terminal, an order is sent to a broker to execute a deal with the specified parameters.
  * On the server, correctness of an order is checked (correctness of prices, availability of funds on the account, etc.).
  * Orders that have passed the check wait to be processed on the trade server. Then the order can be:


  * executed (in one of automatic [execution](General-Principles/Types-of-Execution.md) modes or by a dealer)
  * canceled upon expiry
  * rejected (e.g. when money is not enough or there is no suiting offer in the market; or rejected by the dealer)
  * canceled by a trader;
  * Execution of a market order or triggering of a pending order results in a deal;
  * If there are no positions for a symbol, conclusion of a deal results in opening of a position. If there is a position for the symbol, the deal will lead to increase or reduction of the position volume, its closure or reversal.



![Scheme of trade operations](images/trading_scheme.png)

Scheme of trade operations
