[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Setup](../../Platform-Setup.md) / [Ultency](../Ultency.md) / Deals

[Previous](Liquidity-Orders.md) | [Next](Ticks.md)

<a id="deals"></a>
# Deals (#deals)

Ultency maintains its own database of trading operations. When a client on the platform side places an order that is routed for execution to Ultency, a corresponding operation is created in Ultency. This is referred to as a [matching order](Matching-Orders.md). Based on routing rules, Ultency generates one or more requests for execution  these are called [liquidity orders](Liquidity-Orders.md). Depending on the execution type, these orders may be routed to liquidity providers (A-Book) or executed internally (B-Book). Deals that execute the liquidity order either by liquidity providers or internally are transmitted to Ultency and can be viewed in this section.

In this section, you can view all liquidity orders: which provider they originated from, their volume, price, and other parameters.

![Ultency Deals](images/ultency_deals.png)

<a id="request"></a>
## Requesting Deals (#request)

To view deals, request them using one of the following methods:

  * By Groups  
Select a group from the dropdown list.
  * By Logins  
Enter one or more account numbers separated by commas.
  * By Symbols  
Specify one or more instruments separated by commas.



Additional query parameters may include:

  * One of the predefined date ranges: "Today", "Last 3 days", "Last week", "Last 3 months", "Last 6 months" or "All history". To specify a custom request period, use the fields to the right. Orders are requested by execution time. Open orders do not have this parameter, so they will be included in all queries.
  * Exact time range. Specify the start or end time manually or use the calendar popup, opened via the button ![Calendar](images/calendar_button.png).



After entering the required parameters, click "Request".

<a id="view"></a>
## Viewing a Deal (#view)

To view a deal, double-click on it in the list. The trade dialog is a full-featured tool that offers many useful functions: displaying the structure of the operation, visualizations, tick and order book history, and the operation log.

![Deal in Ultency](images/ultency_deal_view.png)

<a id="account-details"></a>
### Account Details (#account-details)

At the top of the dialog, a summary of the account on which the operation was performed is displayed: name, login, group, and leverage. Click this line to open [detailed account information](../Accounts/Editing-Account.md).

<a id="connected-transactions"></a>
### Overview and Related Operations (#connected-transactions)

All related trading operations are shown in this block: deals executed as a result of order execution and the resulting position. Thus you can easily access the entire chain of related actions. Select an operation from the tree and all relevant parameters will be instantly displayed in the bottom part.

![Viewing Related Operations](images/ultency_operation_tree.png)

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

  * Ultency deal â ticket number of the deal created in Ultency as a result of a liquidity order execution.
  * Liquidity order â ticket number of the [liquidity order](Liquidity-Orders.md) created in Ultency to fill the client's order.


  * Ultency matching order â ticket number of the [matching order](Matching-Orders.md) created in Ultency based on the client's trade request.


  * Type â deal type: buy or sell.


  * Size/volume â deal volume on the Ultency side, in contracts and lots.
  * Provider size/volume â deal volume executed on the liquidity provider side. Specified in the number of contracts and lots.


  * Symbol â [aggregated symbol](Aggregated-Symbols.md) in Ultency, for which the operation is performed.
  * Provider symbol â name of the [trading instrument](Provider-Symbols.md) on the liquidity provider side.


  * Liquidity provider â name of the [liquidity provider (#liquidity-providers)](Connection.md#liquidity-providers) that executed the deal.
  * External ID â deal ticket on the liquidity provider side. 


  * Time â deal execution time.


  * Contract size â contract size of the [aggregated symbol (#execution)](Aggregated-Symbols.md#execution) in Ultency used in the operation.
  * Provider contract â contract size of the [trading instrument](Provider-Symbols.md) on the liquidity provider side.
  * Provider price â price at which the trade was executed on the provider side.
  * Provider markup â markup size as defined in the [provider symbol settings (#quotes)](Provider-Symbols.md#quotes). Specified in points.
  * Provider commission â commission charged by the liquidity provider for the deal.
  * MT5 price â price at which the deal was executed on the Ultency side, inclusive of all markups.
  * Aggregated symbol markup â markup size as defined in the [aggregated symbol settings (#markup)](Aggregated-Symbols.md#markup). Specified in points.
  * Provider time â time taken to register the deal with the liquidity provider. Specified in microseconds.
  * Ultency time â time taken to create the corresponding deal in Ultency. Specified in microseconds.



<a id="visualization"></a>
### Visualization (#visualization)

In this section, execution of a trading operation is visualized on the tick chart of the appropriate aggregated symbol.

![Trading visualization](images/ultency_matching_order_visualization.png)

<a id="ticks"></a>
### Closest Ticks Before and After the Operation (#ticks)

When analyzing disputable situations with traders, it is often necessary to analyze quotes that existed at the time of the trading operation. This information can be retrieved in just two clicks. Open the deal details and go to the "Ticks" or "Ultency Ticks" tab. The terminal will automatically request the full day's tick history for the date of the trade. The tick closest to the trade execution time will be automatically highlighted in the list.

  * Ticks â ticks actually shown to traders on the MetaTrader 5 side. These represent the platform-side symbol, which receives tick data from the aggregated symbol in Ultency according to [translation settings](Translations-of-Symbols-and-Quotes.md). As a result, markup settings from the translation rules and standard price adjustment parameters set for the [symbol (#spread)](../Symbols/Symbol-Settings/Common.md#spread) or [group](../Groups/Group-Symbol-Settings/Common.md) may apply.
  * Ultency ticks â ticks of the [aggregated symbol (#quotes)](Aggregated-Symbols.md#quotes) in Ultency.



![Closest Ticks Before and After the Operation](images/ultency_matching_order_ticks.png)

<a id="book"></a>
### Ultency Book (#book)

Every time deals are matched, Ultency records the current state of the aggregated order book. This feature provides better understanding of how the system operates and helps resolve potential disputes. For more details, see the [Execution Books](Execution-Books.md) section.

![Order book state at the order execution time](images/ultency_matching_order_book.png)

<a id="journal"></a>
### Trading Operation Journal (#journal)

This is another tool to assist during the follow-up operation examination. There is no need to manually query [logs from the server](../Network-cluster/Journal.md) or to filter entries. Open the trading operation details, navigate to the "Journal" tab, and the terminal will automatically request the relevant records from the server, filtered by ticket and from the operation date to the current day.

![Trading Operation Journal](images/ultency_matching_order_journal.png)

<a id="report"></a>
### Trading Operation Report (#report)

All data from the trading operation dialog can be saved as a report. The report includes the full operation chain from order to position, a visual tick chart, log excerpts, and overall account status.

To generate the file, right-click in the "[Overview and related operations (#connected-transactions)](Deals.md#connected-transactions)" section and select "Report" from the context menu. Then choose which data to include: account status, trading results, log, tick chart, etc.

![Trading Operation Report](images/ultency_matching_order_report.png)

<a id="context"></a>
## Context Menu (#context)

The context menu of this section includes the following commands:

  * ![Edit](images/edit_button.png) Edit â open the selected deal.
  * ![Delete](images/delete_button.png) Delete â delete the selected deal
  * ![Request](images/request_button_1.png) Request â execute a [request (#request)](../Orders.md#request).
  * Copy As â copy the deals selected in the list:
    * ![Copy as lines](images/copy_button.png) Lines â copy all selected information.
    * List Of Logins â copy only the list of logins.
    * List Of Tickets â copy only the list of tickets.
  * ![Journal](images/journal_icon.png) Journal By â query [journal](../Network-cluster/Journal.md) entries for the selected deal.
  * ![Export](images/export_button.png) Export â [export](../General-Information/Data-Export.md) the requested deals to an *.HTM, *.HTML, or *.CSV file.
  * ![Search](images/find_button.png) Find â open the [search](../../MetaTrader-5-Administrator/User-Interface/Search.md) window.
  * Auto Arrange â if this option is enabled, the size of columns is selected automatically.
  * Grid â show/hide grid to separate fields in the deals table.
  * Columns â use this submenu to select which [deal data (#view)](Deals.md#view) fields are displayed in the list.


