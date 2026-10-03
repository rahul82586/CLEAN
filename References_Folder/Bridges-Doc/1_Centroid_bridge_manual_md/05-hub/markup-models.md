[🏠 Document Start](..\README.md) / [Book Construction](README.md) / Markup Models

# Markup Models

Overview
A Markup Model goes together with the Liquidity Model and consists of additional Markups to be added on top of the quotes coming
through the Liquidity Model i.e. the Maker.
In this component, you can define a variety of Markup Models for the purpose of adding additional Markups on top of the prices coming
from your Liquidity Providers (Makers) for both streaming and execution. The additional Markups defined in this component represents the
profit the Broker will be earning on all the flow sent to the Liquidity Providers (Makers).
Within this module, you have the capability to:
Add a Markup Model: Introduce a new Markup Model.
Filter Markup Models: Categorize Markup Models based on different criteria to simplify configuration.
Configure Global Markup Model: Adjust bid and ask markups, configure markup multipliers, manage enabling/disabling setting, and
adding a description for a specific Markup Model at a global level.
Delete a Markup Model: Remove an existing Markup Model.
Export a Markup Model: Save the list of Markup Models to an Excel or CSV file.
Filter and Lookup Configuration Settings: Search for configuration settings by different lookup criteria to ease configuration.
Configure Bulk Symbols: Click the “Edit” icon to modify bulk Symbols may it be all Symbols or a group of filtered Symbols.
Configure Markup Model Symbol: Fine-tune the settings of a Symbol within a Markup Model at the level of each Symbol.
Export Symbol Settings of a Particular Markup Model: Save the configured Symbol settings of a specific Markup Model to an Excel
or CSV file.
Upload Excel or CSV File: Update or change bulk configurations of an existing Markup Model by uploading an Excel or CSV file.
Note: Multipliers are coefficients by which the entire Markup Model will be multiplied. You may set up three different Multipliers and
alternate between them at any point in time. Multipliers are useful when it comes to increasing markups during news or market volatility in
one click without going through each Symbol individually.
Creating a Markup Model
To create a Markup Model
1. Click on Hub > Markup Models > Add


2. Fill out the Wizard with all relevant information. You may refer to the field descriptions hereafter.
3. Click the “Submit” button to apply the changes.
Enabled Indicates whether the Markup Model is enabled or disabled.
If ticked, the Markup Model is enabled upon creation.
If unticked, the Markup Model is disabled upon creation.
Note: Disabling a Markup Model at this level means that Markup and other relevant settings defined
here will not be taken into account for all Takers to which this Markup Model is assigned.
Note: Enabling/Disabling State at this level will apply across all Symbols and can be later changed
separately for each Symbol
Name Markup_Mo
del
A unique name of the Markup Model.
Description A short description for reference purposes only.
Bid Points 1, 2, 5 Bid Markup to be added on top of the bid price. Markups are specified in points which are added to
the last digit of the symbol. The Markups defined here are applicable across all Symbols within this
Markup Model. However, you may have to change the Markups separately on a per symbol basis for
securities other than FX at a later stage.
Field Possible
Values
Description

Configuring a Markup Model
To configure or modify a newly added or existing Markup Model on a per symbol basis
1. Click the little arrow on the Symbol column to have it sorted in an alphabetical order.
2. Configure the Markup Model by modifying the editable fields.
a. Select “Points” if you want to put a Markup as points. Example: BTCUSD is a 2-digit symbol. If you put a 5 points Markup Bid and
Ask, it will correspond to 0.05 on Bid/Ask respectively.
b. Select “Price” if you want to put a Markup as a whole number. Example: EURUSD is a 5-digit symbol. If you put a 5 number
Markup Bid and Ask, it will correspond to 5.00000 on Bid/Ask respectively.
3. All editable fields are represented by a “Pen” icon. You may utilize it to bulk edit.
4. Click the “Save” button on the top left to apply the changes.
5. Click the “Revert All” button if you want to revert to the previous values.
Note: A negative value would represent a markdown whereby Broker would be giving a price better
than the raw price for the client.
Example: 1 point Markup for the symbol having digits of 5 would correspond to 0.00001.
Ask Points 1, 2, 5 Ask Markup to be added on top of the ask price. Markups are specified in points which are added to
the last digit of the symbol. The Markups defined here are applicable across all Symbols within this
Markup Model. However, you may have to change the markups separately on a per symbol basis for
securities other than FX at a later stage.
Note: A negative value would represent a markdown whereby Broker would be giving a price better
than the raw price for the client.
Example: 1 point Markup for the symbol having digits of 5 would correspond to 0.00001.
Multiplier Mode Select one of the three available Multipliers. If no Multiplier is selected, the default value will be the
First Multiplier.
Multipliers
(1,2,3)
0.5, 1, 2 A coefficient by which the entire Markup Model will be multiplied across all Symbols. Bid and Ask
Markups for each Symbol will be multiplied by the value defined in the selected Multiplier.
Copy From Allows to copy all settings from an existing Markup Model.
Symbol EURUSD,
XAUUSD
The name of the Symbol to be configured as defined in Symbols.
Security FX, CFD,
EQUITIES
The Security into which the Symbol is grouped.
Field Possible
Values
Description

Model
plain_markup The current Markup Model being configured.
Digits 2 The number of digits defined for the Symbol upon creation.
Sessions MON,00:00-
23:59
Defines the time of the day during which the Markup Model will be functional.
All days of the week should be included and separated by a semicolon “;” along with the time interval
during the day. 00:00-00:00 represents a closure during a particular day.
Markup Bid 0.00002, 0.02,
0.003
The Markup or additional spread to be added on top of the bid price. Markups are defined in decimal
points.
Note: A negative value would be highlighted in red and represent a markdown whereby Broker would
be giving a price better than the raw price for the client.
Example: 2 points Markup for the symbol having digit of 5 would correspond to 0.00002.
Markup Ask 0.02, 0.00002,
0.003
The Markup or additional spread to be added on top of the ask price. Markups are defined in decimal
points.
Note: A negative value would be highlighted in red and represent a markdown whereby Broker would
be giving a price better than the raw price for the client.
Example: 5 points Markup for the symbol having digits of 5 would correspond to 0.00005.
Example: 10 points Markup for the symbol having digit of 5 would correspond to 0.00010.
Markup Bid
Var
0.00003 Defines a random additional bid Markup to be added on top of the Markup Bid to randomize the
behavior. The client in this case will see the spread as “Any value between Markup Bid + Markup Bid
Var”.
Example: Let’s say Markup Bid is 0.00010 (10 points) and the Markup Bid Var is 0.00003 (3 points).
So, the Markup Bid will be any value between 10-13 points.
10 points [Fixed] + 3 points [Var] = 10-13 points
Markup Ask
Var
0.00005 Defines a random additional ask Markup to be added on top of the Markup Ask to randomize the
behavior. The client in this case will see the spread as “Any value between Markup Ask + Markup
Ask Var”.
Example: Let’s say Markup Ask is 0.00010 (10 points) and the Markup Ask Var is 0.00005 (5 points).
So, the Markup Ask will be any value between 10-15 points.
10 points [Fixed] + 5 points [Var] = 10-15 points
Spread Min 0.00003 Defines a minimum spread of the final price shown to client after the bid and ask Markups have been
applied.
If the price is lower than the defined Spread Min, the Centroid Bridge will enforce the Spread Min by
adjusting the Bid and Ask Prices accordingly.
If Spread Min = -1, this indicates that Spread Min is disabled, meaning no spread min to be
enforced. (Note: In case of inverted spread from the Maker, the bridge will accept and advertise
the prices to the Takers.)
If Spread Min = Spread Max, this results in a FIXED SPREAD.
If Spread Min = 0, the bridge will adjust the inverted spread to become 0.
Midpoint Price – (Spread Min/2) and Midpoint Price + (Spread Min/2)
Spread Max 0.00008 Defines a maximum spread of the final price shown to client after the bid and ask Markups have
been applied in the event of price widening.

If the price is greater than the defined Spread Max, the Centroid Bridge will enforce the Spread Max
by adjusting the Bid and Ask Prices accordingly.
If Spread Max = -1, this indicates that Spread Max is disabled.
If Spread Min = Spread Max, this results in a FIXED SPREAD.
If Spread Max = 0, the spread would become 0 using the midpoint price which would be shown
on both ends, bid and ask respectively.
Midpoint Price – (Spread Max/2) and Midpoint Price + (Spread Max/2)
Spread Min
Exec
ABSORB,
PASS,
INVALIDATE,
REJECT,
INVALIDATE_A
ND_REJECT,
PASS_A_ABS
ORB_B
This works with coordination of Spread Min if defined. It dictates the execution behavior in case the
Price exceeds the Spread Min. The execution will be subject to the following options:
ABSORB: The difference between the Actual Price and the Spread Min will be absorbed by the
Broker. So, the client will get executed at the adjusted price that was advertised upon placing the
order.
PASS: The difference between the Actual Price and Spread Min will be passed on to the client
which will theoretically execute the client against the real market price.
INVALIDATE: If the Price is higher than the Spread Min defined, the tick will not be advertised
to client but order may still come through if same Markup Model is used for TF and TEM.
REJECT: If the Price is higher than the Spread Min defined, then the Centroid Bridge will reject
all the trades, hence no execution will take place. However, the price is still advertised to the
Taker.
INVALIDATE_AND_REJECT: If the Price is higher than the Spread Min defined, Prices will be
invalidated (not updating) and trades will be rejected.
PASS_A_ABSORB_B: If the Price is higher than the Spread Min defined, the slippage or the
difference between the Actual Price and Spread Min for A Book orders will be passed on the to
the client, while for B Book Orders, the Broker will absorb the slippage.
Spread Max
Exec
ABSORB,
PASS,
INVALIDATE,
REJECT,
INVALIDATE_A
ND_REJECT,
PASS_A_ABS
ORB_B
This works with coordination of Spread Max if defined. It dictates the execution behavior in case the
Price exceeds the Spread Max. The execution will be subject to the following options:
PASS: The difference between the Actual Price and Spread Max will be passed on to the client
which will theoretically execute the client against the real market price.
ABSORB: The difference between the Actual Price and the Spread Max will be absorbed by the
Broker. So, the client will get executed at the adjusted price that was advertised upon placing the
order.
REJECT: If the Price is higher than the Spread Max defined, then the Centroid Bridge will reject
all the trades, hence no execution will take place. However, the price is still advertised to the
Taker.
INVALIDATE: If the Price is higher than the Spread Max defined, the tick will not be advertised
to client but order may still come through if same Markup Model is used for TF and TEM.
INVALIDATE_AND_REJECT: If the Price is higher than the Spread Max defined, Prices will be
invalidated (not updating) and trades will be rejected.
PASS_A_ABSORB_B: If the Price is higher than the Spread Max defined, this is how it will work
for A Book and B Book clients:
For A Book Clients: Execution Price will be sent as the confirmation i.e. the difference will be
passed to the client resulting to Slippage.
For B Book Clients: Requested Price will be sent as the confirmation i.e. the difference will be
absorbed by the Broker.
Extra Digits 1, 2, 3 This adds a decimal digit to the price for all clients to where this Markup Model will be assigned.

Deleting a Markup Model
To delete a Markup Model
1. Click the “Delete” icon next to the desired Markup Model
2. To confirm the deletion, type the name of the Markup Model in the field.
3. Confirm the “Delete” button in the pop-up window to confirm the deletion
Exporting a Markup Model
To export a Markup Model
Example: EURUSD 5-digit symbol. Let’s say you are adding 1 decimal, then EURUSD will start
pricing with 6 digits and you can confirm this by checking from the Market Watch.
Level 0, 2, 5 If the Maker is pricing with 5 layers and the Markup Model is having a Level of 1, then only 1 layer
(that is first layers only) will have the effect of Markup Model while the rest of the 4 layers from the
Maker will be streamed as raw to your clients.
0 = It covers all layers.
1, 2, 3 = Any other number configured here means it would be restricted to these many layers
only.
WL Bid
Points
(White-
Label)
0, 10, 50 Here you can define a value in points as a share of the markup you are giving to your White-Label
Client that will be available in the markup report.
Example: If the digit for a particular symbol is 5 and you have configured 5 (points) then the WL
client will get 5 points out of the Bid Markup configured here.
WL Ask
Points
(White-
Label)
0, 10, 50 Here you can define a value in points as a share of the markup you are giving to your White-Label
Client that will be available in the markup report
Example: If the digit for a particular symbol is 5 and you have configured 5 (points) then the WL
client will get 5 points out of the Ask Markup configured here.
Description A short description for reference purposes that is copied automatically from the description defined in
Symbols.
Enable Enabled,
Disabled
Defines whether the Markup settings are enabled or disabled for that particular symbol.
If ticked, the Markup settings are Enabled.
If unticked, the Markup settings are Disabled.


1. Select the markup model from the list you wish to export.
2. Click “Export” and select “Export to Excel” or “Export to CSV”
Uploading a Markup Model
To upload a Markup Model symbol settings
1. Click on “Upload”
2. Drop the file you want to upload. Alternatively, you can click on “Drop a File”, select the file and click “Open”
3. Click “Upload“ to upload the file or click “Close” to cancel.


Note: The best way to avoid any errors would be creating a plain markup model or exporting the existing one, and updating all the details
along with the Markup Model Name, so a new one is created and nothing is changed for the old one.

