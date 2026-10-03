[🏠 Document Start](..\README.md) / [Guidelines for Configuring and Sending Credentials for FIX Centroid Taker](README.md) / Taker Feeds

# Taker Feeds

Overview
The Taker Feeds component displays all the pricing feeds configured in the Centroid Bridge. The Taker Feed can be assigned to one or
multiple Takers into which quotes will be streamed.
An unlimited number of Taker Feeds can be defined with its dedicated settings and can be configured down to the level of individual
Symbol.
Within this module, you have the capability to:
Create a New Taker Feed: Initiate the setup for a new Taker Feed.
Filter Taker Feeds: Categorize Taker Feeds based on various criteria for easier identification.
Global Enable/Disable: Enable or disable all Taker Feeds globally, applying changes across associated Symbols.
Configure Taker Feed: Customize a specific Taker Feed, toggling its enable/disable status, and adding a description.
Delete Taker Feed: Remove an existing Taker Feed from the system.
Export Taker Feeds: Save the list of Taker Feeds to Excel or CSV for external reference.
Filter and Look up Symbols: Streamline Symbol configuration by searching and filtering within a Taker Feed.
Configure Bulk Symbol Settings: Use the Edit icon to adjust settings for multiple Symbols at once, either for all or a filtered group.
Configure Symbol Settings: Fine-tune settings for a specific Symbol within a Taker Feed.
Export Symbol Settings: Save the configured settings of a particular Taker Feed's Symbol to Excel or CSV.
Upload Modified Settings: After making changes offline, re-upload the modified file to implement the necessary adjustments.
Note: Enabling or disabling a Taker Feed at this level will impact all Symbols within that Taker Feed, meaning prices won’t be streamed for
this specific taker.
Creating a Taker Feed
To create a Taker Feed
1. Click the “Add” button on the top right corner


2. Fill out the Wizard. You may refer to the field descriptions hereafter
3. Click “Submit” to submit the changes
Taker
Feed
Plain_TF, Test_TF,
S_TF
A unique name of the Taker Feed
Taker Centroid_MT4,
Centroid_MT5
The Taker(s) to which the Taker Feed will be assigned. You may select one or multiple Takers
Markup
Model
Markup_Model,
10PTS_MM
The Markup Model which defines the markups to be added on top of the raw prices while
streaming the prices to the taker
Suffix .vip, .test, #, .pro This is mainly relevant to Taker type - MT4/MT5, because here you can have different set of
symbols.
Example: EURUSD, EURUSD.pro, EURUSD.vip
To ensure that the Taker receives prices for suffix symbols such as .pro and .vip, you need to
create a Taker Feed with the specified suffix. Simply input .pro or .vip
Upon adding this information, a Taker Feed will be generated with the designated suffix.
Liquidity
Model
Aggregated_Model When you assign a Liquidity Model to the Taker Feed, you are making sure that this particular feed
is receiving prices from the Maker(s) assigned in that Liquidity Model.
One Maker: If only 1 Maker is assigned to the Liquidity Model, then your Taker Feed is entitled to
receive prices from this Maker only.
Multiple Makers: If there is more then one Maker assigned to the Liquidity Model then your Taker
Feed is entitled to receive prices from both the makers as Aggregated Feed.
Enable Enabled, Disabled Indicates whether the Taker Feed is enabled or disabled
If ticked, the Taker Feed will be enabled for streaming prices upon creation
If unticked, the Taker Feed will be disabled upon creation, meaning no prices will be streamed
for this particular Taker Feed.
Descriptio
n
Plain_Feed,
Test_Feed,
VIP_Feed
A short description for reference purposes
Field Possible Values Description

Note: Settings configured during the creation of the Taker Feed will be applicable across all Symbols. You will be able to modify and
further customize the settings of a Taker Feed on a per Symbol basis as explained hereafter.
Configuring Taker Feed
To Configure/Modify a newly added/existing Taker Feed on a per Symbol basis
1. Select the checkbox adjacent to the taker feed name
2. Configure the settings on a symbol level
3. Click the “Save” button to apply the modifications.
Copy
From
Allows to copy the configuration settings of an existing Taker Feed
Symbol No EURUSD, XAUUSD The name of the Symbol to be configured, as defined under Symbols
Security No FX, CFD, Equity The Security into which the Symbol is grouped
Taker Feed No Retail_Feed,
Plain_Feed
The name of the Taker Feed being configured
Taker Symbol Yes EURUSD.pro,
EURUSD.vb
Taker symbol is the name of the instrument available at the Taker End where
connecting client is expected to subscribe
It is important that the correct Taker symbol is being sent to the bridge during
subscription. Taker symbol can be adjusted if really necessary and not
configurable on the connecting platform
Liquidity Model Yes Aggregated_pool,
ABC_LM
When you assign a Liquidity Model to the Taker Feed, you are making sure
that this particular feed is receiving prices from the Maker(s) assigned in that
Liquidity Model.
One Maker: If only 1 Maker is assigned to the Liquidity Model, then your Taker
Feed is entitled to receive prices from this Maker only.
Multiple Makers: If there is more then one Maker assigned to the Liquidity
Model then your Taker Feed is entitled to receive prices from both the makers
as Aggregated Feed.
Markup Model Yes Retail_markup,
Plain_markup,
By assigning the Markup Model here, all the settings from this Markup Model
will be applied on the Raw prices from the Maker i.e. the Liquidity Model and
Field Editable Possible Values Description

10Points_markup then streamed to your Taker.
Only one Markup Model can be selected for one Taker Feed while creating the
TF however, furthermore ,you can configure symbol wise manually.
Feed Mode Yes Aggregate, Layer The pricing mode to be used by the Feeder/TF.
Aggregate: The Centroid Bridge sends to the Taker the quotes in the
liquidity book, as received from the Maker(s)
Aggregate_IOC: The Centroid Bridge combines all similar quotes in the
liquidity book, sums up the respective liquidity, and streams into clients as
one quote
Layer: The Centroid Bridge constructs an artificial liquidity book based on
the Levels defined in Levels where it fills each Level with the best prices
with sufficient volume to match the volume defined at the respective Level
(layer). Only one quote per Level will be sent.
Layer_IOC: The Centroid Bridge constructs an artificial liquidity book
similar to Layer mode yet the only difference is that in each Level it would
show the VWAP price matching the volume specified at each Level
Volume: when multiple quotes in the liquidity have the same volume, the
Centroid Bridge streams only one quote with the best price
Min Volume Yes 1000 The minimum volume to appear at the TOB.
Note: A multiplier value of 100 should be accounted for in the minimum volume
Example: If Min Volume is set to 25M (250K x 100) and the liquidity book has
the following:
100K @ Level 1
500K @ Level 2
1M @ Level 3
Then the Centroid Bridge will stream the following:
250K @ Level 1
500K @ Level 2
1M @ Level 3
Depth Yes 1,3,5 The number of layers to be streamed to clients.
Example: If Depth is set to 1, only the TOB will be streamed If Depth is set to
5, the Centroid Bridge will stream the first five layers, provided that the liquidity
book has 5 or more layers
Feed Source Yes A_BOOK, B_BOOK The liquidity book that will be used to update clients about book consumption
and available liquidity in the price updates.
The Centroid Bridge maintains two separate books, A and B, and keeps track
of the available liquidity separately. When an A-Book Order is placed the A-
Book liquidity book will be affected and vice versa.
It’s advisable to use the A-Book mode with clients placed on the A-Book and
B-Book for clients placed on the B-Book
Feed TOB Volume Yes It defines a TOB value to be streamed into the Taker irrespective of the actual
Liquidity Book and its TOB value.
Example: If Feed TOB Volume is 10M, Taker would always see 10M at TOB
irrespective of the real Liquidity Book and its TOB

Deleting a Taker Feed
To delete a Taker Feed
1. Click the “Delete” icon next to the desired Taker Feed
2. To confirm deletion, type the name of the Taker Feed in the field.
3. Click on the “Delete” button to confirm the deletion
Feed Mult Yes 1,2,3 A multiplier by which the available liquidity in the book is multiplied, for the
purpose of showing more liquidity. The multiplier is a positive value greater or
equal to 1.
Example: If Feed Mult is set to 3 and available liquidity is as follows:
1M @ Level 1
2M @ Level 2
Then the Centroid Bridge will show:
3M @ Level 1
6M @ Level 2
Price Mode Yes Various, Midpoint Defines whether floating or fixed spreads are used for price streaming.
Various: The Centroid Bridge just adds the markups defined in Markup
Models to the bid and ask price respectively.
Midpoint: The Centroid Bridge streams prices with fixed spreads. The
Centroid Bridge first calculates the mid price (bid price + ask price/2) then
adds the bid and ask markups (defined in the Markup Model) to each side
of the price.
Interval Yes 100, 200, 300 The time interval, measured in milliseconds, specifies the frequency at which
the Taker Feed allows new price updates to the assigned taker. This interval
determines how often the taker receives the most recent prices.
Session Yes MON,00:00-23:59 Defines the time of the day during which the Taker Feed will be streaming All
days of the week should be included and separated by semicolon “;” along
with the time interval during the day. 00:00-00:00 represents a closure during
a particular day
Description No A short description for reference purposes that is copied automatically from
the description defined in Symbols
Enable Yes Enabled, Disabled Indicates whether the Trader Feed is enabled or disabled for the selected
Symbol.
If ticked, quotes will be streamed on that Symbol
If unticked, quotes will be switched off on that Symbol


Exporting a Taker Feed
To export a Taker Feed
1. Select the desired Taker Feed from the list
2. Tick the checkbox to select a Taker Feed
3. Click “Export” and select “Export to Excel” or “Export to CSV”
Uploading a Taker Feed
To upload a Taker Feed symbol settings
1. Click on the “Upload”
2. Click on “Drop File” and select the File or drag the file to this section to upload.


3. To successfully upload the Taker Feed values, click on “Upload”
4. You also have the option to discard the bulk upload by clicking on the “Close” Button


