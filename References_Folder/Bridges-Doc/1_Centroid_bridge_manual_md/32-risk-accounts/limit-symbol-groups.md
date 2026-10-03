[🏠 Document Start](..\README.md) / [Risk Accounts](README.md) / Limit Symbol Groups

# Limit Symbol Groups

Overview
In straightforward terms, the Limit Symbol Group allows you to set different parameters for various Risk Accounts, such as Margin,
Exposure Limit, Commission, Swaps, and more.
Here's how you assign the Limit Symbol Group to a Risk Account:
In this component, you can view all the Limit Symbol Groups defined in the portal in addition to doing the following:
Create a Limit Symbol Group: Establish a new Limit Symbol Group.
Filter and Look Up a Limit Symbol Group: Search for and identify a particular Limit Symbol Group.
Delete a Limit Symbol Group: Remove a specific Limit Symbol Group.
Export Limit Symbol Groups: Save the list of Limit Symbol Groups to an Excel file or CSV file.
Filter a Symbol within a Limit Symbol Group: Narrow down options for Symbols within a Limit Symbol Group to simplify
configuration.
Configure Bulk Symbol Settings: Adjust settings for multiple Symbols by clicking the edit button next to the desired column.
Configure a Limit Symbol Group: Fine-tune settings down to the level of each individual Symbol within a Limit Symbol Group.
Export Symbol Configuration of a Limit Symbol Group: Save the configured Symbol settings of a specific Limit Symbol Group to an
Excel file or CSV file.
Upload New Configuration: Implement new configurations for a specific Limit Symbol Group by uploading the changes.


Create a Limit Symbol Group
To create a Limit Symbol Group:
1. Click on “Add” to create a new Limit Symbol Group.
2. Fill out the Wizard as explained below
3. Click “Submit” to submit the changes
Once the new Limit Symbol Group has been created, you can assign it to the desired Account Group which in turn would deploy across all
Risk Account underneath.
Limit Symbol Group Test_LSG, Plain_LSG,
TakerName_LSG
A unique name of the Limit Symbol Group
Description A short description for reference purposes
Copy From Allows to copy the configuration settings of an existing Limit Symbol Group
Field Possible Values Description

Configure Limit Symbol Group
To configure a Limit Symbol Group on a per Symbol basis
1. Select the Limit Symbol Group you want to configure by ticking the box before the Limit Symbol Group Name.
2. Locate and make the changes to the desired Symbol(s). The changes are highlighted in orange
3. Click the “Save” button on top to deploy the changes
Symbol No EURUSD The Symbol to be configured
Limit Symbol
Group
No Test_LSG
ABC_LSG
The Limit Symbol Group being configured
Security No FX, CFD,
Equity
The Security into which the underlying Symbol is grouped
Limit Yes 10,000,000 Exposure Limit in notional value at which point no more Orders that would increase the
Symbol exposure above that limit would be permitted.
[Note: This will only work with Risk Account type NOP and Risk]
Margin
Percentage
Yes 0.5,1,2 The Margin % to be blocked when the client is opening a new position.
The resulting value will be added to the overall margin blocked of the Risk Account.
Example:
Symbol: EURUSD
Margin %: 0.5
Open Order: 100000
Price: 1.11550
The Margin Blocked will be calculated as = Open Order Value * Margin % * Price
= 100000 * 0.5% * 1.11550 = USD 557.75 [Margin will be blocked]
Margin Percentage is also related to Leverage and the formula is 1/Leverage * 100.
For example, if the symbol has a leverage of 5 then the Margin Percentage will be 20 (
1 / 5 * 100)
Field Editabl
e
Possible
Values
Description

Commission Yes 1.5, 10, 15 The commission column allows you to input the amount you wish to charge clients for
opening or closing positions in a trading platform.
Commission
Type
Yes Fixed, Fixed
Per Lot, Per
Mil
We have three type of Commission available for Risk Accounts, and they are as follows
Fixed
This will be calculated as Trade Entry i.e. One trade entry the commission will
applied as whole
Calculation: Trade Entry * Commission = Commission Value
This value will be deducted as soon as the trade is placed (in/out)
Fixed Per Lot
Calculation: Volume / Contract Size * Commission = Commission Value
This value will be deducted as soon as the trade is placed (in/out)
Per Mil
Calculation: Trade Volume / Per Million * Commission * Price = Commission Value.
This value will be deducted as soon as the trade is placed (in/out)
Swaps Type Yes Fixed Money
Per Lot,
Point, Price
Percentage
Swap calculation refers to the process of determining the interest or overnight financing
charges associated with holding a trading position overnight. It is commonly applied in
the context of forex trading. The swap amount is calculated as follows:
Fixed Money per Lot: This method involves dividing the trading volume by the
contract size and then multiplying by the swap value (in the Quote Currency) for
short or long positions.
For instance, if the swap long value for EURUSD is -7 and the contract size is
100,000, the overnight swap for a volume of 200,000 long EURUSD would be
calculated as (200,000/100,000) x -7 = USD -14.
Point: Similar to pip calculation, a point value in the Quote Currency considers the
number of decimals in the Symbol and Contract Size. The swap point is calculated
as (swap value) x (net volume) x (1/10^digits) x (conversion quote to deposit
currency).
For example, if the short value of EURGBP is 5 and the traded volume is 100,000,
the swap value would be 5 x 100,000 x 0.00001 x conv GBP to USD = GBP 5. This
value is then converted into the Risk Account currency by multiplying 5 x conv GBP
to USD.
Price Percentage: This method calculates swaps based on a percentage or
interest rate of the traded instrument. The formula is given by Price Percentage =
(current market price) x (net volume) x (swap value / 100.0) x (1 / 360) x (conversion
quote to deposit currency).
Note: Swap is subtracted from the Balance solely upon the partial or complete closure
of a position, contingent on the volume closed. While open positions persist, Swap
remains unrealized, akin to floating Profit/Loss (PL), and exclusively influences Equity.
Contract Size Yes 100,000 The Contract Size of the Symbol. This is mainly used for margin, commission and swap
calculations
Long Value Yes -2, 0.5, 3 The Swap value to be charged for long (buy) overnight positions.
If negative, the value will be deducted from the Risk Account Balance
If positive, the value will be added to the Risk Account Balance
Short Value Yes -2, 0.5, 3 The Swap value to be charged for short (sell) overnight positions.
If negative, the value will be deducted from the Risk Account Balance
If positive, the value will be added to the Risk Account Balance

Delete a Limit Symbol Group
To delete a Limit Symbol Group
1. Click on the “Delete” button next to the desired Limit Symbol Group.
2. To confirm the deletion, type the name of the Limit Symbol Group in the field.
2. Click on the “Delete” button to confirm.
Exporting a Limit Symbol Group
To Export a Limit Symbol Group
1. Select the Limit Symbol Group from the list you wish to export.
2. Click “Export” and select “Export to Excel” or “Export to CSV”
PL Multiplier Yes 0.5, 2 This parameter is only used to adjust the Profit and Loss (PL) in the event of different
PL calculations on the Maker’s side in terms of tick size and tick value.
For instance, if on our side the tick value for one tick size is equivalent to $1 whereas
on the Maker’s side it is equivalent to $2, we could simply put in 2 as PL Multiplier to
ensure that PLs are matching on both ends
Three Day
Swap
Yes WED, FRI The Day of the week on which a three day swap value will be charged for positions
held overnight on that day.
If the value is set to None, then no 3 day swap would be charged, instead the Bridge
would charge Swaps on Saturday and Sunday as well for any position held over the
weekend
Settlement
Time
Yes The Settlement Time of the contract, if any
Description No Symbol description for reference purposes


Uploading a Limit Symbol Group
To Upload a Limit Symbol Group
1. Click on “Upload”
2. Drop the file you want to upload. Alternatively, you can click on “Drop a File”, select the file and click “Open”
3. Click “Upload“ to upload the file or click “Close” to cancel.



