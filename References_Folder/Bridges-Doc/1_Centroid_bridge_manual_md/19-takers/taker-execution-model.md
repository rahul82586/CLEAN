[🏠 Document Start](..\README.md) / [Taker Feeds](README.md) / Taker Execution Model

# Taker Execution Model

Overview
A Taker Execution Model can be thought of as a Trading or Execution Account in the Centroid Bridge defined for one or multiple Takers
with execution settings configured on a per Symbol basis. Takers can target different Taker Execution Models defined in the Centroid
Bridge for the purpose of routing Orders based on different execution settings pertaining to different types of clients. The Taker Execution
Model can be configured down to the level of individual Symbols.
Within this module, you have the capability to:
Create a New Taker Execution Model: Initiate the setup for a new Taker Execution Model.
Enable/Disable Global Settings: Enable or disable a Taker Execution Model at a global level, applying changes across all available
models and Symbols.
Filter Taker Execution Models: Categorize Taker Execution Models based on various criteria for easier identification.
Configure Specific Model: Enable/Disable a particular Taker Execution Model and configure its parameters, affecting all associated
Symbols.
Delete Taker Execution Model: Remove an existing Taker Execution Model from the system.
Export Taker Execution Models: Save the list of Taker Execution Models to Excel or CSV for external reference.
Filter and Look up Symbol Settings: Streamline Symbol configuration by searching and filtering within a Taker Execution Model.
Configure Bulk Symbol Settings: Use the Edit icon to adjust settings for multiple Symbols at once, either for all or a filtered group.
Configure Model Symbol Settings: Fine-tune settings for a specific Symbol within a Taker Execution Model.
Export Symbol Settings: Save the configured settings of a particular Taker Execution Model's Symbol to Excel or CSV.
Upload Modified Settings: After making changes offline, re-upload the modified file to implement the necessary adjustments.
Creating a Taker Execution Model
To create a Taker Execution Model
1. Click the “Add” button to create a new Taker Execution Model


2. Fill out the Wizard. You may refer to the field descriptions hereafter
3. Click “Submit” to submit the changes
Taker Execution
Model
TEM-1, Test_TEM, A-
Book_TEM
A unique name of the Taker Execution Model
Taker Centroid_MT4,
Centroid_MT5
The Taker(s) to which the Taker Execution Model is assigned. You may select one or
multiple Takers.
Assigning the Taker means this Taker will be targeting this TEM.
Currency USD The Currency of the Taker Execution Model into which all calculations will be
converted.
USD is the default and only available option
Trade Limit 500, 700 The maximum number of Order requests the Centroid Bridge will process, within a
specified period of time, defined in Trade Span hereafter
Markup Model Markup_Model,
10PTS_MM
The Markup Model defines the markups to be added on top of the raw prices at the
Time of Execution.
Liquidity Model Liquidity_Model The Liquidity Model that will be assigned to the Taker Execution model indicates the
Maker(s) the Orders will be sent to.
Depending on the BBook% settings if the TEM is A Book or B Book. If A Book, please
check the below conditions
If the Liquidity Model comprises One Maker only, Orders will be routed to that one
Maker.
If the Liquidity Model comprises more than one Maker, Orders will be routed to
different Makers and executed with the Maker depending on the factor that which
Maker is advertising the best price during the time of execution.
Trade Span 1000ms, 1200ms,
1500ms
A time interval, in milliseconds, associated with Trade Limit which specifies the period
of time during which the Trade Limit will be applicable
Trade Reject
Delay
200ms, 400ms A time delay in milliseconds, by which the rejection replies occurring from Trade Limit
will be delayed, in the event of breaching the maximum number of allowed trade
Field Possible Values Description

modify and customize the settings of particular Symbols individually as explained hereafter.
Configuring Taker Execution Model
To Configure or modify a Taker Execution Model
1. Click on the checkbox next to the Taker Execution Model name to select it
2. Configure the settings on a symbol level
3. Click the “Save" button to apply the modifications.
4. Click the “Revert All” button to undo the changes that have been made
requests, specified in the Trade Limit
Enable Enabled, Disabled Indicates whether the Taker Execution Model is enabled or disabled
If ticked, the Taker Execution Model will be enabled for trading upon creation
If unticked, the Taker Execution Model will be fully switched off upon creation,
hence no Orders will be executed through this Taker Execution Model
Description A short description for reference purposes
Copy From It allows to copy all the settings from an existing Taker Execution Model
Symbol No EURUSD,
XAUUSD
The name of the Symbol to be configured, as defined in Symbols
Security No FX, Crypto The Security into which the Symbol is grouped, Default settings copied from the
Symbol from the Hub Module.
Taker Execution
Model
No TEM_A, TEM_B The name of the Taker Execution Model being configured
Liquidity Model Yes Aggregated_Mo
del
The Liquidity Model that will be assigned to the Taker Execution model indicates the
Maker(s) the Orders will be sent to.
Depending on the BBook% settings if the TEM is A Book or B Book. If A Book,
please check the below conditions
Field Editable Possible
Values
Description

If the Liquidity Model comprises One Maker only, Orders will be routed to that
one Maker.
If the Liquidity Model comprises more than one Maker, Orders will be routed to
different Makers and executed with the Maker depending on the factor that
which Maker is advertising the best price during the time of execution.
Markup Model Yes Plain_Markup
5Points_Markup
The Markup Model defines the Markups to be added on top of the Raw Prices when
Orders are executed on the Taker level.
Note: The Markup assigned here is not sent to the LP while execution which means
LP execution is on the Raw Price, but the Markup is only added on top of the Raw
Price when sending the confirmation from the Bridge to the Taker/Client.
Exec Mode Yes Sweep
Single_FOK
Single_IOC
The execution mode to be used when executing an Order.
Sweep: The Centroid Bridge sweeps the available liquidity book from top to
bottom (best to worse) until the Order is fully or partially filled
Single_IOC: The Centroid Bridge targets one quote (layer) of the liquidity book
that has enough volume and the best price to fill the Order entirely or partially. In
case no quote is available to fully fill the Order, it will be sent to the one that has
the largest volume from the available Book, also partial filling is allowed when
executing orders with Single_IOC.
Single_FOK: The Centroid Bridge targets one quote (layer) of the liquidity book
that can fill the entire size of the Order. If no quote with sufficient volume is
found, the Centroid Bridge reports a rejection after the TTL has expired which
means No Partial Filling is allowed when executing orders with Single_FOK.
Min Volume Yes 1000 The minimum order size, in notional volume, is to be processed by this Taker
Execution Model. Any volume below the specified amount will be rejected.
Example:
Taker: MT5/MT4/cTrader
Symbol: EURUSD
Contract Size: 100000
Min Lot on Application level: 0.01
Minimum Volume to be set on the bridge level: 0.01*100000 = 1000
Formula: Min Volume = Platform Min Lot x Contract Size
Max Volume Yes 100000000 The maximum Order size, in notional volume, to be processed by this Taker
Execution Model. Any volume beyond the specified amount will be rejected as
“above max vol”
Formula: Max Volume = Platform Max Lot x Contract Size
TTL Yes 300 ms This settings is in milliseconds, this component means, it will re-attempt to fill the
rejected orders if it is within the TTL time.
AMin Yes 1000 This component is same as the Min Volume, but as the name suggests this
component is strictly restricted for A book orders. Which means as a client you can
set a Minimum volume that you wish to send to your LP. If this condition is not
satisfied then the order will be booked as B Book irrespective of the BBook %
defined on the TEM level.
AStep Yes 1000
The value is in
Volume.
The step value in notional volume that represents the increment of the Order
Anything that does not comply, the remainder will be b booked
Example: If AStep is 3000, an Order of 5000 will be split as follows:

3000 sent to STP
2000 executed as B Book
Note: By default, this will also be used as Order Step validation unless configure
otherwise in description.
B Book Percent
(0-100)
Yes 0, 50, 100 The percentage of Order to be internalized (bbooked) in the Centroid Bridge. The
remainder is sent to the Maker as STP.
The percentage is a number between 0 and 100, where 0 represents a full A-Book
Order whereas 100 represents a full B-Book Order.
Example: If Book Percent is set to 80 then 80% of the Order will be b-booked while
the remaining 20% will be sent as STP.
BFix Yes 5000
10000
If you enter a value of 5000 under BFix, the centroid bridge will compare the TOB
from the Maker, if the advertised volume from the Maker is less than 5000, then the
BFix value will be New Available TOB for BBook.
BBoost Yes 1,2,3 This is only relevant to B-Book execution where the value defined in here is a
multiplier by which each layer of the liquidity book is multiplied. The BBoost value is
always equal or greater than 1.
Example: If liquidity book is made up of 3 layers:
Layer 1: 500K
Layer 2: 1M
Layer 3: 3M
Applying a BBoost factor of 3, the liquidity book would become as follows:
Layer 1: 1.5M
Layer 2: 3M
Layer 3: 9M
BDelay From Yes 100,200,300 This is only relevant to B-Book execution. It represents the first interval of a random
time delay applicable to execution in order to simulate the A-Book execution
BDelay To Yes 120,220,320 It represents the second interval of a random time delay applicable to execution in
order to simulate the A-Book execution.
The Order gets executed at the market price, after the delay has elapsed.
The below formula is used to calculate the final outcome of the delay that will be
enforced on the execution:
Delay = Random (BDelay From, BDelay To)
Example: If BDelay From is 100 ms and BDelay To is 120 ms, Delay would be
Random (100 and 120)
Gain Perc Yes 0,50,100 In the event of encountering a price improvement or positive slippage, the
percentage of improvement that will be reported to clients i.e. the difference
between Requested Price and Execution Price
100 means the Broker would keep all the improvement without passing on any
percentage to the client
0 means the Broker would pass all the improvement on to the Client
Multiplier Yes 0.5,2,10 A multiplier by which the order size will be multiplied prior to sending the order
request to the Maker.
Example: If Multiplier is set to 2 and client trades 100,000 EURUSD, an order
request of 200,000 EURUSD will be sent to the Maker.

LL Variation Yes 10, 20, 30 LL Variation is only relevant for B Book Execution and works along with the other
parameters such as BDelay From, BDelay To, Gain Perc and the action depends on
the parameters selected under LL Action.
This can be configured in points, where the Centroid Bridge will scan the book then
compare the previous price and new price. If the difference between the two price is
above or below the LL Variation then LL action will be triggered
1. If the difference between the new price after delay and the old price is within the
LL Variation: - If the new price is worse, the client gets the worse price
2. If the new price is better, the client gets a percentage of the price difference
depending on the percentage specified in the Gain Perc parameter
3. If the difference between the new price after delay and the old price is outside
the LL Variation, the Centroid Bridge would execute based on the selection in LL
Action as explained hereafter
Note: -1 means that this parameter is not enabled
LL Action Yes Indicates how to handle Orders if the difference between new price after delay and
old price is greater than the LL Variation on one side, or could be used to override
the normal execution in terms of request price.
Price Difference after delay:
Reject: The Centroid Bridge would reject the Order if the difference of the new
price after delay and old price is outside the LL Variation
Accept: Checks if the new price is in client’s favor or not
1- If new price is in broker’s favor (against client), client gets the new price
2- If new price is in client’s favor, the client gets a percentage of the price
difference depending on the percentage specified in Gain Perc parameter
Execution Parameters:
CONFIRM_BY_REQ_PRICE: Confirms order by request price as B Book
irrespective of the B Book Percentage Parameter, without even processing the
Order via the normal execution flow
PROC_CONFIRM_BY_REQ_PRICE: Processes the Order and returns the
requested price to the client irrespective of the actual execution price, for both A
and B Book Orders
PROC_CONFIRM_BY_REQ_PRICE_B: Processes the Order and returns the
requested price to client only for B Book execution whereas returning the actual
execution price to client for A Book execution
Note: For PROC_CONFIRM_BY_REQ_PRICE, clients may incur losses on A Book
trades in the event of order slippage
B Slip
Threshold
Yes 1, 2, 5 Configurable in points, it will absorb negative slippage according to the configured
value, provided it does not exceed the B Slip Max Accept value or if the B Slip Max
Accept is configured as 0
This feature is specifically intended for scenarios involving negative slippage. It is
applicable only to B Book trades, including of a 50% allocation for A Book and 50%
for B Book. The calculation of negative slippage will be based on the raw price,
excluding any markups.
You can use B Slip Threshold and B Slip Percentage independently or together.

To delete a Taker Execution Model
1. Click the “Delete” icon next to the desired Taker Execution Model
2. To confirm deletion, type the name of the Taker Execution Model in the field.
3. Click on the "Delete" button to confirm deletion.
The calculation of the threshold will take place prior to the percentage.
B Slip
Percentage
Yes 5%, 10%, 50% Configurable in percentage, this will additionally absorb any remaining negative
slippage after the B Slip Threshold, or it can function independently in determining
the extent of negative slippage absorption, as long as it does not surpass the B Slip
Max Accept
This feature is specifically intended for scenarios involving negative slippage. It is
applicable only to B Book trades, consisting of a 50% allocation for A Book and 50%
for B Book. The calculation of negative slippage will be based on the raw price,
excluding any markups.
You can use Threshold and Percentage independently or together.
When using Percentage Absorption, if it yields a value of 0.5, the absorbed slippage
will consistently be rounded in favor of the broker. For instance, if the negative
slippage is 7, the percentage is 50, resulting in 3.5 points, the absorption will be
3points.
B Slip Max
Accept
Yes 25, 50, 65 [in
points]
Configurable in points, it sets the maximum negative slippage that the broker can
absorb after applying the B Slip Threshold and B Slip Percentage settings.
This feature is specifically intended for scenarios involving negative slippage. It is
applicable only to B Book trades, consisting of a 50% allocation for A Book and 50%
for B Book. The calculation of negative slippage will be based on the raw price,
excluding any markups.
B Slip Max Accept will always prevail or take precedence over the total negative
slippage resulting from B Slip Threshold, B Slip Percentage, or a combination of B
Slip Threshold and B Slip Percentage.
Session Yes MON,00:00-
23:59
Defines the time of the day during which the Taker Execution Model will be
available for trading. All days of the week should be included and separated by
semicolon “;” along with the time interval during the day. 00:00-00:00 represents a
closure during a particular day
Description No A short description for reference purposes that is copied automatically from the
description defined in Symbols
Enable Yes Enabled,
Disabled
Indicates whether the Symbol is enabled or disabled for the selected Taker
Execution Model
If ticked, order requests of the particular Symbol will be processed via the Taker
Execution Model
If unticked, no order requests will go through

To Export the listed Taker Execution Model
1. Click on the “Taker Execution Models” Tab.
2. Click “Export” and select “Export to Excel” or “Export to CSV”
Exporting a Taker Execution Model Symbol Setting
To Export Takers Execution Model Symbol Settings
1. Select the desired Taker Execution Model from the list
2. Click Export → Export to Excel / Export to CSV
Uploading a Taker Execution Model
To Upload Takers Execution Model Symbol Settings
1. Click on “Upload”


2. Click on “Drop File” and select the File or drag the file to this section to upload.
3. To successfully upload the values, click on “Upload”.



