[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_deals

[Previous](mt5-positions/Enumerations.md) | [Next](mt5-deals/Enumerations.md)

# mt5_deals

Data on [deals](../../../Platform-Setup/Deals.md) is exported to the table. If ["Export history orders and deals into separate tables by years" (#sql-settings)](../../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#sql-settings) option is enabled in settings, deals for each year are exported to a separate table. A year is specified in the table heading, for example, mt5_deals_2012. If the option is disabled, all deals are exported to a single mt5_deals table.

The table contains the following fields:

Name | Type | Description  
Deal | Integer | Primary key. The ticket of a deal.  
Timestamp | Integer | Unique record within the table. It is used for internal purposes of MetaTrader 5 servers. If the timestamp is changed for a record, it means that the record has been changed.  
Login | Integer | The login of the client, to whom the deal belongs.  
Dealer | Integer | The login of a dealer, who has processed a deal.  
Order | Integer | The ticket of the order, as a result of which a deal was executed.  
Action | Integer | Type of action performed with a deal. Passed in a value of the [EnDealAction (#endealaction)](mt5-deals/Enumerations.md#endealaction) enumeration.  
Entry | Integer | Deal direction. Passed in a value of the [EnEntryFlags (#enentryflags)](mt5-deals/Enumerations.md#enentryflags) enumeration.  
Digits | Integer | The number of decimal places in the price of a deal.  
DigitsCurrency | Integer | The number of decimal places the deposit currency of the client who has executed the deal.  
ContractSize | Float | The contract size of the symbol, for which a deal was executed.  
Time | DateTime | Trade execution time in the YYYY-MM-DD HH:MM:SS format.  
Symbol | String | The symbol, for which a deal is executed.  
Price | Float | The price of the deal.  
PriceSL | Float | The Stop Loss level of a deal. Stop Loss values for entry and reversal deals are set in accordance with the Stop Loss of orders, which initiated these deals. The Stop Loss values ​​of appropriate positions as of the time of position closing are used for exit deals.  
PriceTP | Float | Take Profit values for entry and reversal deals are set in accordance with the Take Profit of orders, which initiated these deals. The Take Profit values ​​of appropriate positions as of the time of position closing are used for exit deals.   
Volume | Integer | The deal volume. One unit corresponds to 1/10000 lot.  
VolumeExt | Integer | The deal volume with an extended accuracy. One unit corresponds to 1/100000000 lot.  
VolumeClosed | Integer | The position volume that was closed by the deal. One unit corresponds to 1/10000 lot.  
VolumeClosedExt | Integer | The extended accuracy volume of a position that was closed by this deal. One unit corresponds to 1/100000000 lot.  
Profit | Float | Profit from a deal.  
Value | Float | The deal value in client deposit currency.  
Storage | Float | The swap size for a deal.  
Commission | Float | The amount of [commission](../../../Platform-Setup/Groups/Commission-Settings.md) charged for a deal.  
Fee | Float | [Fee](../../../Platform-Setup/Groups/Commission-Settings.md) per deal.  
RateProfit | Float | The exchange rate of the profit currency of a deal to the deposit currency of a client group.  
RateMargin | Float | The exchange rate of the margin currency of a deal to the client's deposit currency.  
ExpertID | Integer | The ID of the Expert Advisor that has executed a deal.  
PositionID | Integer | The position identifier (ticket) for a deal.  
Comment | String | Comment to a deal.  
ProfitRaw | Float | The amount of return resulting from a deal. Return is specified in the profit currency of the symbol, for which the deal is executed.  
PricePosition | Float | The price of the position closed with this deal.  
TickValue | Float | The tick value price for a deal.  
TickSize | Float | The tick size for a deal.  
Flags | Integer | The common flags of a deal. This parameter is reserved for future use.  
Reason | Integer | The reason for performing a deal. Passed in a value of the [EnDealReason (#endealreason)](mt5-deals/Enumerations.md#endealreason) enumeration.  
Gateway | String | The ID of a gateway, using which a deal was performed.  
PriceGateway | Float | The price that was actually used for performing a deal through a gateway in an external trading system without taking in consideration its price transformation settings of the gateway.  
MarketBid | Float | The market Bid price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.  
MarketAsk | Float | The market Ask price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.  
MarketLast | Float | The market Last price as at the time of deal execution by the server. The field is only filled for the deals which were created after the platform was updated to build 2890 or higher. For earlier deals, the value will be zero.  
TimeMsc | DateTime | Trade execution time in the YYYY-MM-DD HH:MM:SS.MS format.  
ApiData | String | User data which can be added via MetaTrader 5 API. Sample user data entry: [{"pos":0,"app_id":1,"valInt":500,"valUInt":500,"valDbl":0.00000000}]. It specifies the user data index, the ID of the application that added it, as well as the data of three types: Int, UInt and double. The string may contain up to 16 such entries.
