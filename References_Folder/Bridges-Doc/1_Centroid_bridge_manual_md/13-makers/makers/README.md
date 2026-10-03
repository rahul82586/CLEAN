[🏠 Document Start](..\..\README.md) / [Makers](..\README.md) / Makers

# Makers

Overview
A Maker represents the Liquidity Provider in the Bridge. It consists of a 2-way connection between the Centroid Bridge and the Maker
whereby the Bridge receives price updates from the Maker and sends Order requests for execution to the Maker based on a variety of
routing rules.
In this Component, you can view the list of Makers that are defined in the Centroid Bridge and its symbol settings. The makers can be
configured down to the level of individual Symbols as explained below.
In this component, you will be able to do the following:
Create a New Maker Session: Add a new Maker Session to the Centroid Bridge.
Filter Maker Sessions: Filter by different search criteria.
Edit Maker Configurations: View and edit Maker configuration settings for both trading and pricing sessions.
Export List: Export the list of Makers to an Excel File or CSV file.
Configure Bulk Symbol Settings: Configure a bulk of Symbol settings by clicking the Edit icon, for all Symbols at once or a group of
filtered Symbols.
Export Symbol Settings: Export the list of Symbol Settings of a particular Maker to an Excel file or CSV file.
Upload Modified Settings: Upload an Excel or CSV file to update or change a bulk of configurations on existing Makers.
Viewing / Editing Maker Connection Settings
To view the Maker Connection Settings, click on the button right next to the desired Maker and a pop-up window that contains the Maker
Settings will appear as shown below:
The settings are divided into the following three tabs:
Feeding: The Maker Connection Settings of the pricing session.
Trading: The Maker Connection Settings of the trading session.


Both: The Maker Connection Settings of the Maker in case the connection to the Maker is made via one session that combines both
feeding and trading.
Note: If the connection to the Maker is made through separate sessions, Feeding and Trading, both tabs will have values, whereas if the
connection is made through one session, both Feeding and Trading tabs will show empty values.
Note: For some Makers, you may find the Account number of the Trading Account with the Maker within the configuration settings.
In some cases, editing the session is required from the Broker’s end if the LP, for instance, changed some settings such as the account
(tag 1) credentials of the Trading Session.
To edit the Maker Connection Settings
1. Click on the desired tab, Trading in the below example.
2. Edit the desired values to the right, Username, and Password in the below example.
3. Click the Save button.


Configuring the Maker and its Symbols
To configure or modify a Maker on a per Symbol basis:
1. Click the check box at the start of the row next to the desired Maker.
2. Configure the desired field for the desired Symbol, which is highlighted.
3. Click the “Save” button on the top left to deploy the changes.
Symbol No EURUSD,
XAUUSD
The Symbol to be configured
Maker Symbol Yes EUR/USD,
XAUUSD.c
The name of the instrument you are subscribing to on the Maker’s end. This
allows to map Symbols in your Centroid Bridge to Maker’s Symbols. Here we can
configure the Maker Symbol, which will be provided by the Maker itself
Example:
Symbol: EURUSD
Maker Symbol: EUR/USD
Security No FX, CFD,
EQUITIES
The Security into which the Symbol is grouped.
Base Yes EUR, USD,
GER30
The base currency of the Symbol. For FX, it is by default the first currency of the
pair whereas for CFDs, it is the full name of the Symbol.
Example:
EURUSD, Base is EUR
UK100, Base is UK100
Quote Yes EUR, USD, GBP The quote currency of the Symbol. For FX, it is by default the second currency of
the pair whereas for CFDs, it is the currency by which the Symbol is
denominated.
Example:
GBPUSD, Quote is USD
Digits Yes 5 Defines the decimal points in the price of the underlying Symbol to be received
from the Maker.
Session Yes MON,00:00-23:59 Defines the time of the day during which the Maker Symbol will be available for
trading.
Field Editable Possible Values Description

All days of the week should be included and separated by semicolon “;” along
with the time interval during the day. 00:00-00:00 represents a closure during a
particular day.
Markup Bid Yes 0.00005, 0.1, 1 Pre-Aggregation Markup, i.e. This will have the Markup on the Raw Price from
the Maker, and if you have any Additional Markup Model then, Raw Price +
Markup [Maker] + Markup Model = Client’s Final Price / Spread.
Example: Same as Markup Model, In Points, 1 point markup for the symbol
having digit as 5 would be 0.00001.
Note: A negative value would represent a markdown whereby the broker would
be giving a price better than the raw price for the client.
Markup Ask Yes 0.003, 0.5 Pre-Aggregation Markup, i.e. This will have the Markup on the Raw Price from
the Maker, and if you have any Additional Markup Model then, Raw Price +
Markup [Maker] + Markup Model = Client’s Final Price / Spread.
Example: Same as Markup Model, In Points, 5 point markup for the symbol
having digit as 5 would be 0.00005.
Note: A negative value would represent a markdown whereby the broker would
be giving a price better than the raw price for the client.
Depth Yes 0,1,3,5,10 Depth, the number of layers you are subscribing to from a specific Maker.
Example: Depth configured as 5, then the bridge is expecting to receive and
process up to a maximum of 5 layers from the Maker, now it depends on the
maker if it will send 5 layers.
Min Size Yes 1000
[In Volume]
The Minimum size of order allowed, executed, and to be sent to the Maker, any
order below this value will be rejected by the Bridge.
Example: EURUSD Min Size configured as 10000, client is placing an order for
1000, this order will be rejected as “below min volume”
A Step Yes 5000 The increment in the size from the minimum.
Orders sent to the Maker should be a multiple of A Step.
Example: If A Step is 2,000 and an order of 9,000 is received, then the
Aggregator will execute 8,000 and the remaining 1,000 will expire.
Note: It is advisable to keep the A Step similar to Min Size.
Consume A Vol Yes Enabled, Disabled Order requests will lead to a reduction in the total/available liquidity from the
maker.
Enabled: The available liquidity book will be 800k from that Maker for
EURUSD.
Disabled: It won’t have any effect of the order request it will still stream with
1M as available liquidity from the Maker for EURUSD.
Example: If Maker is advertising 1M on a certain symbol, if consume is enabled,
an Order request of 100K will reduce the available liquidity advertised by the
Maker to 900k.
Allow Sweep Yes Enabled, Disabled Indicates whether the price updates received from the Maker are sweepable or
not.
Enabled: The Aggregator targets more than one quote by sweeping the book
until the order is filled (fully or partially).

Disabled: The Aggregator targets one quote of the book per Maker only, that
can best fill the order.
Multi Req Trade Yes 0, 1 This defines how orders pertaining to different levels of the liquidity book are sent
to the Maker.
If set to 1, the Aggregator breaks the order into multiple legs based on the
number of levels swept in the book and sends multiple order requests to the
Maker(s).
If set to 0, the Aggregator sends one Order in full to the Maker at TOB Price
Example: If you have the following liquidity book.
Level 1: 100K – Maker 1
Level 2: 100K – Maker 2
Level 3: 200k – Maker 1
Level 4: 500K – Maker 2
If an Order of 500K comes in:
If Multi Req Trade is 1, 2 order requests will be sent to each LP as follows:
100K and 200K to Maker 1
100K and 100K to Maker 2
If Multi Req Trade is 0, 1 order request will be sent to each LP as follows:
300K to Maker 1
200K to Maker 2
Expiry Date Yes 20220131 This is only relevant to Symbols of type Futures which could be mandated by
some Makers and defines the Expiry Date of the Symbol.
Note: Each Maker may have a different format of Expiry Date to be sent
alongside the Order request.
Sub Volumes Yes 100, 500, 1000 This is only relevant to certain Makers which allow to subscribe to different
volumes of the liquidity book.
Timeout Warn Yes 30,000 ms Default Value is 30000 millisecond, at which, if no reply is received from the
maker for a specific order request then the Centroid Bridge will start generating
Warning Messages.
Timeout Error Yes 180,000 ms Default Value is 180000 millisecond, at which, if no reply is received from the
maker for a specific order request the Centroid Bridge will consider the Order
Expired and Rejects It.
Disclaimer: It is ideal that Timeout Error value is higher than the Timeout Warn
value.
Timeout Kill Yes 10, 20, 30 Default value is 10, meaning after 10 Timeout Errors the Centroid Bridge will
Disable that specific symbol.
Prices Timeout Yes 35000 ms Default value is 35000, meaning if there is no price updates within this time frame
from the maker, trades on Bbook will be rejected.
Feed Side Yes BID,ASK,BID_AS
K
You can define which side of prices you would like to receive from the specific
Maker.
ASK: Only Ask price will be processed after receiving it from the Maker.
ASK_TRADE: Both Ask and Trade prices will be processed after receiving
from the Maker.
BID: Only the Bid price will be processed after receiving it from the Maker.

Re-subscribing Maker Session / Symbol
To re-subscribe or refresh a session at the maker level, you will need to do the following:
1. Click on the configuration option located at the right end of the respective maker session.
2. Access the relevant session, such as Feeding or Trading.
3. Modify the value of the "Enabled" key to 'N' and save the changes.
4. Subsequently, update the value back to 'Y' and save the changes.
This action initiates the resubscription process at the maker session-level.
To re-subscribe or refresh a maker symbol(s), you will need to do the following:
1. Select the relevant maker session.
2. Find the symbol you want to re-subscribe to and deactivate it.
3. Apply the modifications on the Maker Symbol (not just the symbol) and save.
BID_ASK: Both Bid and Ask prices will be processed after receiving them
from the Maker.
BID_ASK_TRADE: Bid, Ask, and Trade prices will be processed after
receiving them from the Maker.
BID_TRADE: Both Bid and Trade prices will be processed after receiving from
the Maker.
TRADE: Only the Trade price will be processed after receiving it from the
Maker.
Accepted Price
Delay
Yes 400 ms Delay in milliseconds after which the price coming from the Maker into the Bridge
will be rejected. In other words, if the travel time it takes for the price to be
streamed from the Maker into the Bridge is greater than the defined Accepted
Price Delay, the price will be discarded hence won’t be allowed into the Bridge.
Ignore Prices for
B exec
Yes Enabled, Disabled This works with the Prices Timeout Component.
Enabled: If there are no price updates from the maker for the defined value [ms]
in Prices Timeout, no execution will take place for the B Book orders.
Disabled: Here the Centroid Bridge will ignore the Prices Timeout settings and
will process/execute the B Book orders based on the last received price.
Description No Euro Vs. US
Dollar
Default values from the Symbol.
MS Description Yes SPOT Symbols An additional description field which could be used for the Maker itself. The most
common approach is to copy tick prices from one Maker to another which does
not have a working Pricing Session. To do so, it suffices to list the name of the
Maker which you wish to price on a per Symbol basis. The Maker Name should
be exactly as appears in Maker Session in the format #mask=Maker_Name#.
Enable Yes Enabled, Disabled Indicates whether the Symbol is enabled or disabled on the Maker Session .
If ticked, the Symbol is enabled.
If unticked, the Symbol is disabled.
Disclaimer: Disabling a Symbol at this level means that the Symbol will be
disabled for a particular Maker, hence the symbol is not subscribed and no
quoting or trading on that Symbol will be allowed.

4. Reactivate the symbol after the changes have been made.
This action initiates the resubscription process at the maker symbol level.
To apply the same action to multiple symbols, you can utilize the Bulk Edit function.
Exporting Maker Symbol Settings
To Export Maker Symbol Settings
1. You will need to click on the “Makers” module.
2. Click on the required “Maker”.
3. Click “Export” and select “Export to Excel” or “Export to CSV”.
Importing Maker Symbol Settings
To Import Maker Symbol Settings:
1. Click on “Upload”
2. Click on “Drop File”


3. To successfully upload the Maker Symbols values, click on “Upload”
4. You also have the option to discard the bulk upload by clicking on the “Close” Button.



