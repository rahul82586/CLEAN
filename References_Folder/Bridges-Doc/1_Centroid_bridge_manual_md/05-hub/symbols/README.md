[🏠 Document Start](..\..\README.md) / [Securities](..\README.md) / Symbols

# Symbols

Overview
In this component, you can include symbols for trading on the Centroid Bridge which is explained as the top level here. Any modification
made to the symbol at this main level will impact the symbol at all the other levels or components.
All Symbols defined in the Centroid Bridge and their respective configuration settings are displayed in this component.
Within this module, you have the capability to:
Add a New Symbol: Use the new Symbol wizard to add a new Symbol.
Add or Update Symbols: Upload a bulk of Symbols from an Excel file or CSV file.
Filter and Look Up Symbols: Search for specific Symbols by different lookup criteria to ease configuration.
Configure Bulk Symbols: Edit a bulk of Symbols by clicking the Edit icon for all or a group of filtered Symbols.
Sort Columns: Arrange certain columns in ascending or descending order by clicking the field name.
Enable/Disable Symbols: Manage the active status of particular Symbol(s) in the Centroid Bridge.
Configure Per Symbol: Edit and configure specific fields on a per Symbol basis.
Delete a Symbol: Remove a Symbol from the system.
Multi-delete Symbols: Select multiple symbols and delete them simultaneously.
Export Symbols: Save the list of Symbols to an Excel file or CSV file.
Symbol No EURUSD,
XAUUSD,
AAPL,
BTCUSD
The name of the Symbol to be added and used.
Note: You may have multiple suffixes on your Taker/MT4/MT5. However, while creating a
symbol, the only focus is to create the base symbols. So you will only be adding Plain
Symbols in this window. Suffix can be added later with the help of Taker Feed component.
Security No FX, CFD,
EQUITIES
The Security into which the underlying Symbol is grouped.
Base Yes EUR, GBP,
DAX
The base currency of the Symbol.
For FX, it’s the first currency of the pair.
For non-FX such as CFDs, it’s the full name of the Symbol.
Field Editable Possible
Values
Description

Adding a Symbol
To add a New Symbol from the UI
You can add a new Symbol any time you wish to introduce a new product to be traded via the Centroid Bridge. There are two ways of
creating a Symbol, either by creating one Symbol at a time from the UI or by bulk creation i.e. uploading a list of Symbols from an Excel file
or CSV format.
1. Click the “Add” button to create a symbol.
Quote Yes USD, EUR,
GBP
The quote currency by which the Symbol is denominated.
For FX, it’s the second currency of the pair.
For CFDs, it’s the currency in which the Symbol is quoted. (e.g., FTSE is quoted in
GBP)
Category Yes Spot, Futures Represents another level of categorization to further categorize a Symbol.
ISIN Yes US0378331005 The ISIN code of the underlying instrument. For reference purposes only and is not
mandatory.
(e.g., Symbol: AAPL, ISIN: US0378331005)
Digits Yes 5 The number of decimals in the quoted price of the underlying Symbol.
Vol Digits Yes 2 The number of decimals allowed to be traded of the underlying Symbol.
Default value is 2. This allows up to 0.01 volume of trade. To allow 0.00000001 volume of
trades for Crypto symbols, Vol Digits must be updated to 8 and all the min size and step
settings must also be adjusted on Taker Execution Model and Maker Symbol settings with
consideration to allowed ABook and BBook minimum volume.
Note: Vol Digits setting can only be changed by Centroid Support Team.
Sessions Yes MON,00:00-
23:59
Defines the time when the symbol is Active i.e. sending prices to the Taker and receiving
the trades from the Taker.

All days of the week should be included and separated by a semicolon “;” along with the
time interval during the day. 00:00-00:00 represents a closure during a particular day.
Descripti
on
Yes A short description for reference. This will also be used as the default description values
for all the other components such as Liquidity Models, Markup Models, Makers, Taker
Feeds, and Taker Execution Models.
The description column can also be utilized to write rules whenever creating Synthetic
Symbols.
Enable Yes Enabled,
Disabled
Indicates whether the Symbol is enabled or disabled.
Note: Disabling a Symbol at this level implies that the Symbol will be disabled at all levels
throughout the Centroid Bridge, hence no quoting or trading on that Symbol.

2. Fill out the Wizard with all relevant information and click the “Submit” button.
Uploading Symbols
To upload Symbols from an Excel Sheet or CSV
An alternative method of creating Symbols from the UI is available which allows creating a bulk of Symbols all at once by uploading
multiple Symbols from an Excel or CSV file format.
Note: Please make sure to export the file first. Once you have the format, you will work on the same file and upload it with the same format
to avoid errors. Kindly also avoid utilizing special characters.
1. To get the correct format of the file or export your symbol settings list (via Excel or CSV), click the “Export” button and proceed to make
the changes.
2. Click the “Upload” button if you want to upload multiple new symbols or to update existing symbols.
3. Click the “Drop A File” to browse and select the file or you can just easily drop the Excel or CSV file into the designated area.


4. Click the “Upload” button to submit and upload the file.
5. You also have the option to discard the bulk upload by clicking the “Close” Button.
Note: When using the bulk operation to upload all the symbols, you can perform the following or possible scenarios:
Case 1: Uploading a file to only add new symbols
* Export the Symbol file
* Remove all the existing symbols
* Add new symbols then upload the file
Case 2: Uploading a file to add new symbols and not modifying any existing symbols
* Export the Symbol file
* Do not remove the existing symbols
* Add the new symbols then upload the file
Case 3: Uploading a file to only modify existing symbols
* Export the file
* Modify the values then upload the file
Case 4: Uploading a file to add new symbols and modify existing symbols
* Export the Symbol file
* Modify the existing symbols
* Add new symbols then upload the file


Modifying a Symbol
To configure or modify an existing Symbol’s configuration
1. Double-click the editable field next to the desired Symbol. The rows configured are flagged by a brown-highlighted check box on the left
and the edited field(s) are also highlighted in brown.
2. Click the “Save” button on the top left to deploy the changes or “Revert All” to discard the changes.
3. Another option to modify the Symbol(s) is mentioned on Uploading Symbols.
Deleting a Symbol
To delete an existing Symbol
1. Click the “Delete” icon next to the desired Symbol or you may also tick the check box beside the symbol and click the “Delete” button
on the top left.
To delete an existing Symbol in bulk
1. Tick the check box next to the specific symbol(s) you wish to delete and it will be highlighted. Multi-selecting symbols can also be done
by ticking the check box on the top left of the Symbol column.
2. Click the “Delete” button to bulk delete.
3. Enter “delete” in the text field on the confirmation pop-up message and click the “Delete” button to confirm the deletion.




