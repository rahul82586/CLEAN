[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Ultency](../Ultency.md) / Matching Orders

[Previous](Routing/Conditions.md) | [Next](Liquidity-Orders.md)

<a id="matching-orders"></a>
# Matching Orders (#matching-orders)

Ultency maintains its own database of trading operations. When a client on the platform side places an order that is routed for execution to Ultency, a corresponding operation is created in Ultency. This is referred to as a matching order. Based on routing rules, Ultency generates one or more requests for execution  these are called [liquidity orders](Liquidity-Orders.md). Depending on the execution type, these orders may be routed to liquidity providers (A-Book) or executed internally (B-Book). Deals that execute the liquidity order either by liquidity providers or internally are transmitted to Ultency and can be viewed in the [relevant section](Deals.md).

In this section, you can view all the orders that are being matched: when and by whom they were created, as well as how they were forwarded and executed in Ultency.

![Matching Orders](images/ultency_matching_orders.png)

<a id="request"></a>
## Request Orders (#request)

To view orders, request them using one of the following methods:

  * By Groups  
Select a group from the dropdown list.
  * By Logins  
Enter one or more account numbers separated by commas.
  * By Symbols  
Specify one or more instruments separated by commas.



Additional query parameters may include:

  * "Open Only" â display orders that have not yet been executed.
  * One of the predefined date ranges: "Today", "Last 3 days", "Last week", "Last 3 months", "Last 6 months" or "All history". To specify a custom request period, use the fields to the right. Orders are requested by execution time. Open orders do not have this parameter, so they will be included in all queries.
  * Exact time range. Specify the start or end time manually or use the calendar popup, opened via the button ![Calendar](images/calendar_button_2.png).



After entering the required parameters, click "Request".

<a id="view"></a>
## Viewing an Order (#view)

To view an order, double-click on it in the list. The trade dialog is a full-featured tool that offers many useful functions: displaying the structure of the operation, visualizations, tick and order book history, and the operation log.

![Сводимый ордер](images/ultency_matching_order_view.png)

<a id="account-details"></a>
### Account Details (#account-details)

At the top of the dialog, a summary of the account on which the operation was performed is displayed: name, login, group, and leverage. Click this line to open [detailed account information](../Accounts/Editing-Account.md).

<a id="connected-transactions"></a>
### Overview and Related Operations (#connected-transactions)

All related trading operations are shown in this block: deals executed as a result of order execution and the resulting position. Thus you can easily access the entire chain of related actions. Select an operation from the tree, and all relevant parameters will be instantly displayed in the bottom part.

![Viewing Related Operations](images/ultency_operation_tree_2.png)

In the example above:

  1. Final position opened on the MetaTrader 5 side as a result of the order executed in Ultency.
  2. Original pending order placed from MetaTrader 5.
  3. Matching order created in Ultency to execute the client's original market order.
  4. Corresponding liquidity order created to fill the matching order.
  5. First deal that partially filled the matching order. Since the volume of the best available ask at that time was smaller (0.04) than the original request (0.1), Ultency filled the order using two price levels.
  6. Second deal that partially filled the matching order. Next after the best ask in the order book.
  7. Final deal created on the MetaTrader 5 side.



<a id="details"></a>
### Trading Operation Details (#details)

For each order, the following parameters are shown:

  * Ultency matching order â ticket number of the order created in Ultency.
  * Order type â type of the order created in Ultency.
  * MT5 order type â type of the original order created on the MetaTrader 5 side.
  * MT5 order â ticket number of the original order created on the MetaTrader 5 side.
  * MT5 server â name of the [trading server](../Network-cluster/Configuring-Servers/Trade-Server.md), on which the original order was created.
  * MT5 group â name of the [group](../Groups.md) associated with the account from which the original order originated.
  * МТ5 action â trading action that triggered the original order: 'market' â placement of a market order, 'activate' â activation of a pending order.
  * Symbol â [aggregated symbol](Aggregated-Symbols.md) in Ultency for which the matching order was created.
  * MT5 symbol â symbol of the original order on the MetaTrader 5 side.


  * State â current status of the matching order (e.g., filled, rejected, partially filled, expired, etc.).


  * Expiration type â [expiration type (#expiration)](../Symbols/Symbol-Settings/Trade.md#expiration) of the matching order: "GTC" (Good Till Canceled), "Day" or "Specified".
  * MT5 expiration type â expiration type of the original order on the MetaTrader 5 side: "GTC" (Good Till Canceled), "Day" or "Specified".
  * Expiration time â if the matching order expired, this field shows the expiration date and time.
  * MT5 expiration time â if the original order on the MetaTrader 5 expired, this field shows its expiration date and time.
  * Filling type â additional [fill policy rules (#fill-policy)](../General-Information/Trading-System.md#fill-policy) for the matching order: "Fill or kill", "Cancel remainder", "Passive", or "Return remainder".
  * MT5 filling type â additional [fill policy rules (#fill-policy)](../General-Information/Trading-System.md#fill-policy) for the original order on the MetaTrader 5 side: "Fill or kill", "Cancel remainder", "Passive", or "Return remainder".
  * Matching flags â additional execution settings applied to the matching order. For example, 'merge deals' means [execution deal merging (#merge-deals)](Aggregated-Symbols.md#merge-deals) was enabled.
  * Create time â matching order creation time.


  * Done time â matching order execution time in Ultency.
  * Coverage â percentage of the order volume routed through A-Book.
  * Price â price at which the matching order was routed for execution in either A-Book or B-Book.
  * МТ5 price â price at which the original order was submitted on the MetaTrader 5 side.
  * MT5 contract size â contract size of the [trading instrument (#contract-size)](../Symbols/Symbol-Settings/Trade.md#contract-size) on the MetaTrader 5 side.
  * MT5 size/volume â volume requested in the original order on the MetaTrader 5 side. Specified in contracts and lots.
  * MT5 size/volume executed â volume from the MT5 side that was executed as a result of order matching in Ultency. Specified in contracts and lots.
  * MT5 VWAP executed â final price at which the original order was executed. Calculated as the volume-weighted average price across all deals that executed the order on the Ultency side, including all markups.
  * Aggregated symbol markup â markup size as defined in the [aggregated symbol settings (#markup)](Aggregated-Symbols.md#markup). Specified in points.
  * A-Book size â initial volume intended to be routed through A-Book according to the [routing rules (#coverage)](Routing.md#coverage).
  * B-Book size â initial volume intended to be routed through B-Book according to the routing rules.
  * A-Book size taken â A-Book volume that was sent to the liquidity provider but not yet executed. A value in this field indicates the order is still in the process of being filled.
  * A-Book size executed â volume that was actually executed through A-Book (on the liquidity provider side).
  * A-Book VWAP executed â volume-weighted average price of all deals that filled the A-Book portion of the order.
  * B-Book size executed â volume that was actually executed through B-Book (on the platform side).
  * B-Book VWAP executed â volume-weighted average price of all deals that filled the B-Book portion of the order.



Additional information that may be displayed in the list of matching orders:

  * Coverage â portion of the matching order volume executed through A-Book.
  * Book link â identifier of the order book snapshot captured at the moment of execution. This can be used to request corresponding data in the "[Execution Books](Execution-Books.md)" section.



<a id="visualization"></a>
### Visualization (#visualization)

In this section, execution of a trading operation is visualized on the tick chart of the appropriate aggregated symbol.

![Trading visualization](images/ultency_matching_order_visualization_2.png)

<a id="ticks"></a>
### Closest Ticks Before and After the Operation (#ticks)

When analyzing disputable situations with traders, it is often necessary to analyze quotes that existed at the time of the trading operation. This information can be retrieved in just two clicks. Open the deal details and go to the "Ticks" or "Ultency Ticks" tab. The terminal will automatically request the full day's tick history for the date of the trade. The tick closest to the trade execution time will be automatically highlighted in the list.

  * Ticks â ticks actually shown to traders on the MetaTrader 5 side. These represent the platform-side symbol, which receives tick data from the aggregated symbol in Ultency according to [translation settings](Translations-of-Symbols-and-Quotes.md). As a result, markup settings from the translation rules and standard price adjustment parameters set for the [symbol (#spread)](../Symbols/Symbol-Settings/Common.md#spread) or [group](../Groups/Group-Symbol-Settings/Common.md) may apply.
  * Ultency ticks â ticks of the [aggregated symbol (#quotes)](Aggregated-Symbols.md#quotes) in Ultency.



![Closest Ticks Before and After the Operation](images/ultency_matching_order_ticks_2.png)

<a id="book"></a>
### Ultency Book (#book)

Every time deals are matched, Ultency records the current state of the aggregated order book. This feature provides a better understanding of how the system operates and helps resolve potential disputes. For more details, see the [Execution Books](Execution-Books.md) section.

![Order book state at the order execution time](images/ultency_matching_order_book_2.png)

<a id="journal"></a>
### Trading Operation Journal (#journal)

This is another tool to assist during the follow-up operation examination. There is no need to manually query [logs from the server](../Network-cluster/Journal.md) or to filter entries. Open the trading operation details, navigate to the "Journal" tab, and the terminal will automatically request the relevant records from the server, filtered by ticket and from the operation date to the current day.

![Trading Operation Journal](images/ultency_matching_order_journal_2.png)

<a id="report"></a>
### Trading Operation Report (#report)

All data from the trading operation dialog can be saved as a report. The report includes the full operation chain from order to position, a visual tick chart, log excerpts, and overall account status.

To generate the file, right-click in the "[Overview and related operations (#connected-transactions)](Matching-Orders.md#connected-transactions)" section and select "Report" from the context menu. Then choose which data to include: account status, trading results, log, tick chart, etc.

![Trading Operation Report](images/ultency_matching_order_report_2.png)

<a id="context"></a>
## Context Menu (#context)

The context menu of this section includes the following commands:

  * ![Edit](images/edit_button_2.png) Edit â open the selected order.
  * ![Delete](images/delete_button_2.png) Delete â delete the selected order.
  * ![Request](images/request_button_3.png) Request â execute a [request (#request)](../Orders.md#request).
  * Copy As â copy the orders selected in the list:
    * ![Copy as lines](images/copy_button_2.png) Lines â copy all selected information.
    * List Of Logins â copy only the list of logins.
    * List Of Tickets â copy only the list of tickets.
  * ![Journal](images/journal_icon_2.png) Journal By â query [journal](../Network-cluster/Journal.md) entries for the selected order.
  * ![Export](images/export_button_2.png) Export â [export](../General-Information/Data-Export.md) the requested orders to an *.HTM, *.HTML, or *.CSV file.
  * ![Search](images/find_button_2.png) Find â open the [search](../../MetaTrader-5-Administrator/User-Interface/Search.md) window.
  * Auto Arrange â if this option is enabled, the size of columns is selected automatically.
  * Grid â show/hide grid to separate fields in the orders table.
  * Columns â use this submenu to select which [order data (#view)](Matching-Orders.md#view) fields are displayed in the list.


