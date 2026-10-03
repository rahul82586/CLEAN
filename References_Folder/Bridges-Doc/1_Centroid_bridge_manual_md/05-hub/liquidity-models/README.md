[🏠 Document Start](..\..\README.md) / [Synthetic Symbols](..\README.md) / Liquidity Models

# Liquidity Models

Overview
We can picture the Liquidity Model as pools where one or more Liquidity Providers (Makers) come together. The Makers are the
participants in this liquidity pool which we call the Liquidity Model and are responsible for sending prices and executing the orders.
The Liquidity Model can be a standalone model if it only contains one Maker (LP) or can be aggregated in case it contains more than one
Maker (LP). In the case of aggregation, Centroid Bridge will advertise the top of the book or the best price and target the Maker that offers
it during the execution. The selection of Liquidity Provider(s) or Maker(s) within the model can be configured on a per symbol basis offering
a great degree of flexibility.
Within this module, you have the capability to:
Add a Liquidity Model: Incorporate a new Liquidity Model.
Filter Liquidity Models: Categorize Liquidity Models based on different criteria.
Enable/Disable Liquidity Models: Manage the active status of the Liquidity Models in the Centroid Bridge.
Configure Global Liquidity Model: Adjust the settings at a global level by enabling/disabling or adding a description.
Delete a Liquidity Model: Remove an existing Liquidity Model.
Export a Liquidity Model: Save the list of Liquidity Models to an Excel or CSV file.
Filter and Lookup Symbol Settings: Search for Symbol settings by different lookup criteria to ease configuration.
Configure Bulk Symbols: Click the “Edit” icon to modify bulk Symbols may it be all Symbols or a group of filtered Symbols.
Configure Symbol Settings (Pricing and Trading): Fine-tune the settings of a Symbol within a Liquidity Model at the level of each
Symbol.
Export Symbol Settings of a Particular Liquidity Model: Save the configured Symbol settings of a specific Liquidity Model to an
Excel or CSV file.
Upload Excel or CSV File: Update or change bulk configurations of an existing Liquidity Model by uploading an Excel or CSV file.
Creating a Liquidity Model
To create a Liquidity Model
1. Click the “Hub” module.
2. Click the “Liquidity Models” component.
3. Click the “Add” button to create a new Liquidity Model.
4. Fill out the wizard with all relevant information. You may refer to the field descriptions hereafter.
5. Click the “Submit” button to submit the changes.


Configuring a Liquidity Model
To configure or modify a newly added or existing Liquidity Model on a per symbol basis
1. Click the little arrow on the Symbol column to have it sorted in an alphabetical order.
2. Configure the Liquidity Model by modifying the editable fields. All editable fields are represented by a “Pen” icon.
3. Click the “Save” button on the top left to apply the changes.
4. Click the “Revert All” button if you want to revert to the previous values.
Enabled This will determine whether the newly created Liquidity Model should be activated or
deactivated upon creation.
Name MakerName_LM This is intended to recognize the Liquidity Model and determine the particular Maker being
utilized in this Liquidity Model.
Description A short description for reference purposes only.
Makers Liquidity_Provider
-1
In this process, you will designate a specific Maker for the newly created Liquidity Model.
Essentially, this Liquidity Model will be responsible for interacting with the assigned Maker.
Field Possible Values Description

Symbol No EURUSD,
XAUUSD
The name of the Symbol to be configured as defined in Symbols.
Security No FX, CFD,
EQUITIES
The Security into which the Symbol is grouped.
Liquidity Model No Aggregated_LM The current Liquidity Model being configured.
Primary Maker Yes PB1, Maker_1 The Primary Maker or Liquidity Provider to source liquidity from by streaming
quotes into the Liquidity Model and executing any flow routed through that Liquidity
Model.
You can select multiple Makers in case you wish to aggregate prices from different
Makers to construct an aggregated liquidity book. The book is ordered by best
prices on top. As for Orders, it will be routed to the Maker providing the best price
at the time of execution.
Failover Makers Yes Maker_2 The Failover Makers to source liquidity in case of the Primary Maker stopped
pricing. This column will only work if stated in Symbols Profile and Stale Rules.
Sessions Yes MON,00:00-23:59 Defines the time of the day during which the Liquidity Model will be available for
trading.
All days of the week should be included and separated by a semicolon “;” along
with the time interval during the day. 00:00-00:00 represents a closure during a
particular day.
Exec Mode Yes SWEEP,
SINGLE_IOC,
SINGLE_FOK
Defines the execution modes of the Symbol for all Orders routed via Liquidity
Model.
SWEEP: the Orders will be executed by sweeping the book of quotes
constructed by the Maker(s) making up that Liquidity Model (unless indicated
otherwise in the Exec Boost parameter).
SINGLE_IOC: only one quote of the book will be targeted for execution even if
it does not satisfy the full amount, hence may result in a partial fill.
SINGLE_FOK only one quote of the book will be targeted for execution
provided that this quote can fill the requested volume entirely, hence no partial
fills.
Field Editab
le
Possible Values Description

Adding a Failover Maker
To add a Failover Maker
1. Click the “Hub” module.
2. Click the “Liquidity Models” component.
3. Select the desired “Liquidity Model” you wish to add a Failover Maker to it.
4. Add one or more Makers on the “Failover Makers“ column
Exec Boost Yes Enabled, Disabled Allows to boost the Order by sending the full requested amount at the TOB, rather
than splitting it into Legs based on the available Liquidity Book.
If Enabled, the Order will be sent in full to the Maker at the TOB, irrespective of
the available volume.
If Disabled, the Order will be executed by splitting it into different Legs if
needed based on the available Liquidity Book.
Note: For B Book Orders, the Order will be fully filled at TOB price if Exec Boost is
enabled.
Filter Factor Yes -2, -1, 10 Indicates whether a filtration is applied to prices coming into the Liquidity Model or
not.
If filtration is enabled, it dictates how the filtration is applied as explained below:
(-2) means that no price filtration is applied to the Liquidity Model, hence all
prices are allowed in.
(-1) means that filtration is being applied using the default parameters applied
in the relevant Filtration Pool.
(Other positive value) means that this value is used as a Factor which would
override the one defined in the Filtration Pool.
Book
Construction
Yes Allows to construct multi-layer books at the level of each Symbol and set markups
at each layer.
Note: Refer to the sub-section hereafter wherein construction of books at the level
of each Symbol are discussed in-depth.
Description Yes A short description for reference purposes that is copied automatically from the
description defined in Symbols.
Enable Yes Enabled, Disabled Indicates whether the Liquidity Model is enabled or disabled.

Deleting a Liquidity Model
To delete a Liquidity Model
1. Click the “Delete” icon next to the desired Liquidity Model.
2. Enter the Liquidity Model name in the text field on the confirmation pop-up window and click the “Delete” button to confirm the deletion.
Exporting a Liquidity Model
To export a Liquidity Model
1. Select the desired liquidity model from the list.
2. Tick the checkbox to select a Liquidity Model.
3. Click the “Export” button and select “Export to Excel” or “Export to CSV”.


Uploading a Liquidity Model
To upload a Liquidity Model symbol settings
1. To get the correct format, you need to use and follow the Exporting a Liquidity Model
2. Click the “Upload” button.
3. Click the “Drop A File” to browse and select the file or you can just easily drop the Excel or CSV file into the designated area.
4. To successfully upload the Liquidity Model values, click the “Upload” button.
5. You also have the option to discard the bulk upload by clicking the “Close” button.
Book Construction
The Book Construction is a feature within the Liquidity Model module that is configured at the level of individual Symbol through the Book
Construction field. It allows the construction of a virtual liquidity book and customizes a multi-layered Liquidity Book based on own


preferences in addition to adding markups at the different levels of the constructed Liquidity Book.
Note: If you are creating a virtual book of 3 layers without any markup then it will be merged and streamed as one layer only. So
to achieve a multi-layered virtual book, you need to add markups on each layer along with the volume.
When constructing a Book, the Centroid Bridge always takes the Top of the Book that is available to the Centroid Bridge whenever a new
price update comes in. The Book is constructed using the artificial Volumes specified at each level in addition to the Top of the Book price
to which the markup specified at each level is added. Volume can be randomized (using a range), fixed, or derived from the real Volume at
the Top of the Book.
When it comes to execution, we have to differentiate A Book from B Book as follows:
A Book: For A Book execution, the entire Order will be sent to the Makers at the Top of the Book irrespective of the Volumes at the
constructed Book.
B Book: For B Book execution, Orders will be filled based on the constructed Book by sweeping the Book from top to bottom until the
Order is fully or partially filled. It’s the same way the Centroid Bridge would execute any Order based on a real Liquidity Book.

Adding a Book Construction
1. Double-click the Book Construction field next to your desired Symbol.
2. Select whether you like to create the Book through a List or Text.
3. Select your preferred book construction mode as follows:
“Normal”: If you want to construct the Book based on the Bid and Ask.
“Midpoint”: if you want to construct the Book based on the midpoint price.
4. Click the “Add” button to start creating the Book Construction.


5. Fill out the wizard. Please note that the Markup shall be defined in points.


6. Click the “Submit” button once you have finalized the Book.
Note: The above steps will be repeated depending on the number of levels the Book will be made of.
7. Click the “Save” button to save the changes and finalize the Book Construction.
8. Click the “Revert All” button if you want to discard the changes made.


