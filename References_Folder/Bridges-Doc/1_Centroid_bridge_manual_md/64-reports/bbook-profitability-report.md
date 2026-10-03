[🏠 Document Start](..\README.md) / [Trade Transactions](README.md) / BBook Profitability Report

# BBook Profitability Report

Overview
The BBook Profitability Report offers a comprehensive examination of orders within the Aggregator, whether partially or fully directed to the
B Book. It provides a detailed breakdown of how B Book legs are executed, simulating an authentic STP setup. Moreover, the report
enables brokers to contrast the execution on MT4/MT5 platforms with that on the Centroid Aggregator.
Beyond mere numerical data, this report serves as a valuable tool for brokers to assess the financial impact of price improvement. By
comparing Centroid Aggregator execution to retaining orders in MT4/MT5, brokers can gauge whether they would achieve better or lesser
returns. This analytical approach helps brokers identify scenarios where price improvement proves advantageous for them or their clients,
facilitating more informed decision-making.
Note: Brokers have the capability to fine-tune the allocation of price improvement in favor of the client through the Gain Percentage field
within the Taker Execution Model, specified on a per Symbol basis. For instance, configuring the Gain Percentage to 100 allows the broker
to retain the entire price improvement when it favors the client, without passing on any percentage. Conversely, a Gain Percentage setting
of 0 ensures that the client receives the complete benefit of the price improvement.
Request BBook Profitability Report
To request a BBook Profitability Report
1. Click on the "Toggle here to search" button.
2. Complete the Wizard as detailed below.
3. Pre-set the columns necessary for the report in the Grid Columns.
4. Click "View Results" to execute the report or directly "Export to CSV or Excel" file.
Note: Use the Reset button to clear the pre-defined filters
Note: In the above fields, any field that is left empty, apart from dates, implies that all values are included in the search
Start Date The Start Date of your desired search interval
End Date The End Date of your desired search interval
Ext Client
Group
MT4/MT5 Group number for Takers of type MT4/MT5
Ext Client
Login
MT4/MT5 Login number for Takers of type MT4/MT5
Field Description

After generating the BBook Profitability Report, you can perform the following actions
1. Arrange columns in ascending or descending order.
2. Apply filters to columns using various arithmetic and logical conditions.
3. Navigate through pages using options for first, last, previous, and next pages.
4. Optimize the report layout to fit the entire content on the page.
5. Automatically adjust column sizes based on the data within each column.
BBook Profitability Details
Ext Order
ID
MT4/MT5 Ticket Number for Takers of type MT4/MT5
Cen Ord Id Centroid Order ID
Symbol Select one or multiple Symbols from the list of Symbols
Taker The Taker(s) configured in the Centroid Bridge such as FIX, MT4, MT5 and Centroid’s Trading Platform
TEM Taker Execution Model(s) through which the Order was executed
Risk
Account
Risk Account through which the Order was executed, if any
Ext Bid/Ask Indicates whether we are comparing the Filled Price to the Price that was initiated from the Taker (MT4 or MT5) or not.
If ticked, Aggregator calculates the Slippage based on the difference between Fill Price and Price initiated by Taker
If unticked, Aggregator calculates the Slippage based on the difference between Fill Price and the Price initiated by
the Aggregator based on the first scan of the Liquidity Book when the Order was received
Grid
Columns
Columns or data fields that will be available in the report
Cen Ord ID Centroid unique Order ID recorded in the Aggregator
Ext Client Login Login number of the MT4/MT5 Taker if the order is originated from a Taker of type MT4 or MT5. Otherwise,
value will be 0
Ext Order ID Order ID number of the MT4/MT5 Taker if the order is originated from a Taker of type MT4 or MT5. Otherwise,
value will be 0
Field Description

To Export the BBook Profitability Report
Click on “Export to CSV” or “Export to Excel” to export the report
Recv Time The Time at which the Oder was received in the Aggregator
Taker Execution
Model
The Taker Execution Model through which the Order was processed
Symbol The traded Symbol
Party Symbol The Party Symbol as defined in the corresponding Maker Session
Side The side of the Order; Buy or Sell
Ord Type The category of the executed Order, whether it is Market or Limit.
Volume The requested Volume of the Order
Fill Volume The total Filled Volume in Base Currency
BFill Volume The B Book Filled Volume of the Order is determined as follows:
If the Order is 100% B Book, BFill Volume is equivalent to the Fill Volume.
If the Order is partially B Booked, this value represents the percentage of the Order that has been directed
to the B Book.
BFill Price The Aggregator's execution price for the B Book Order.
Exit Price The price at which the client's Order would have been executed in the front-end platform (MT4/MT5) without
utilizing the Centroid B Book (Depth of Market).
Notional B The notional value of the B Book-filled Order in USD.
Price Improvement
(USD)
The Price Improvement in USD is calculated as the difference between the Exit Price and BFill Price, multiplied
by the Volume.
If the result is positive, it indicates a profit for the Broker.
If the result is negative, it signifies a loss for the Broker and a profit for the Client.
CS Cost (USD) The cost of executing the Order through Centroid Aggregator in USD.
Price Improvement
Net of CS Cost
(USD)
The net Profit/Loss attributable to Price Improvement, considering the CS Cost resulting from executing the
trade via the Centroid Aggregator, is calculated as follows:
Price Improvement Net=Price Improvement USD−CS Cost USD
This metric reflects the overall financial impact of price improvement, accounting for the associated cost
incurred through the Centroid Aggregator.



