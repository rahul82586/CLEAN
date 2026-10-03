[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Deals](../Deals.md) / Data Structure

[Previous](../Deals.md) | [Next](Get-by-Ticket.md)

# Data Structure

Data on deals is passed in JSON format as a response to the [/api/deal/get](Get-by-Ticket.md) and [/api/deal/get_page](Get-Paged.md) requests. Deal information includes the following parameters:

Option Field | Type | Description  
Deal | Integer | Deal ticket.  
ExternalID | String | The deal ID in external trading systems.  
Login | Integer | The login of the client, to whom the deal belongs.  
Dealer | Integer | The login of a dealer, who has processed a deal.  
Order | Integer | The ticket of the order, as a result of which a deal was executed.  
Action | Integer | Type of action performed with a deal. Passed in a value of the [EnDealAction (#endealaction)](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) enumeration.  
Entry | Integer | Deal direction. Passed in a value of the [EnDealEntry (#endealentry)](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealentry) enumeration.  
Digits | Integer | The number of decimal places in the price of a deal.  
DigitsCurrency | Integer | The number of decimal places the deposit currency of the client who has executed the deal.  
ContractSize | Float | The contract size of the symbol, for which a deal was executed.  
Time | Integer | The time of a deal execution in seconds that have elapsed since 01.01.1970.  
Symbol | String | The symbol, for which a deal is executed.  
Price | Float | The price of the deal.  
PriceSL | Float | The Stop Loss level of a deal. The Stop Loss values for entry and reversal deals are set in accordance with the Stop Loss of the orders, which initiated appropriate deals. The Stop Loss values ​​of appropriate positions as of the time of position closure are used for exit deals.  
PriceTP | Float | The Take Profit level of a deal. The Take Profit values for entry and reversal deals are set in accordance with the Take Profit of orders, which initiated these deals. The Take Profit values ​​of appropriate positions as of the time of position closure are used for exit deals.  
Volume | Integer | Volume of a deal. One unit corresponds to 1/10000 lot.  
VolumeExt | Integer | Volume of a deal with an extended accuracy. One unit corresponds to 1/100000000 lot.  
Profit | Float | Profit from a deal.  
Value | Float | The deal value in client deposit currency.  
Storage | Float | The swap size for a deal.  
Commission | Float | The amount of commission charged for a deal.  
RateProfit | Float | The exchange rate of the profit currency of a deal to the deposit currency of a client group.  
RateMargin | Float | The exchange rate of the margin currency of a deal to the client's deposit currency.  
ExpertID | Integer | The ID of the Expert Advisor that has executed a deal.  
PositionID | Integer | The position identifier (ticket) for a deal.  
Comment | String | Comment to a deal.  
ProfitRaw | Float | Return is specified in the profit currency of the symbol, for which the deal is executed. The profit/loss is expressed in the profit currency of the symbol, for which a deal is executed.  
PricePosition | Float | The price of the position closed with this deal.  
VolumeClosed | Integer | The position volume that was closed by the deal.  
TickValue | Float | The tick price for a deal.  
TickSize | Float | The tick size for a deal.  
Flags | Integer | The common flags of a deal. This parameter is reserved for future use.  
TimeMsc | Integer | The time of a deal in milliseconds.  
Reason | Integer | The reason for performing a deal. Passed in a value of the [EnDealReason (#endealreason)](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealreason) enumeration.  
Gateway | String | The ID of a gateway, using which a deal was performed.  
PriceGateway | Float | The price that was actually used for performing a deal through a gateway in an external trading system without taking in consideration its price transformation settings of the gateway.  
MarketBid | Float | The market Bid price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.  
MarketAsk | Float | The market Ask price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.  
MarketLast | Float | The market Last price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.  
ModificationFlags | Integer | The deal modification flags. Passed in a value of the [EnTradeModifyFlags (#entrademodifyflags)](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#entrademodifyflags) enumeration (sum of values of appropriate flags). Deals that close a position or part of it inherit its modification flags. After closing, no separate entry about the position remains in the database. To prevent the information about modification from being lost, flags are copied to the deal that closes his position. At the same time, the additional EnTradeModifyFlags::MODIFY_FLAGS_POSITION modification flag is set for the deal meaning that the flags were inherited from the position.
