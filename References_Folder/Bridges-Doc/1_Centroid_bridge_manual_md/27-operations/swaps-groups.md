[🏠 Document Start](..\README.md) / [Swaps Symbols](README.md) / Swaps Groups

# Swaps Groups

Overview
The MT4/MT5 Swaps Group Update functionality, can be found within the Bridge Engine UI, under the Operations section. The Swaps
Update functionality is part of a set of operational tools for trading platforms (i.e. MT4, MT5, etc.) that is intended to optimize and minimize
the time needed to manage specific configurations on the trading platforms that need to be performed periodically. Therefore, by having an
optimized way and single system where to manage such tasks (for one or multiple platforms), it can save a lot of time and avoid overhead.
At the Swaps Group screen, the swap values of all or specific symbols, for any specific group within the trading platform, can be updated.
This can be done either via the UI, by adding new config lines for specific group and symbol, or editing existing settings; alternatively, the
Export and Upload can be used to bulk add or update the swap settings across a large number of groups and symbols at the same time.
Swap Group Change
To change the swap for groups:
1. Select the required MT4/5 server.
2. Enter the “New Swap Long/New Swap Short” value on the UI or via upload function.
3. Click “Save” to deploy the changes.
Important Notes
Swap changes will be applied immediately
New value is highlighted in red if it is more or less than 10% of the current swap value.
Swap changes from default to any value or vice versa will always be highlighted red.
Server The specific MT4/5 server to apply the swap operation
Group The group on MT4/5 server
Symbol The symbol for which the swap will be changed
Description Group name - Symbol
Swap Long Current Swap Long value of that group symbol
New Swap Long The new swap long value which will replace the current group symbol swap value
Swap Short Current Swap Short value of that group symbol
New Swap Short The new swap short value which will replace the current group symbol swap value
Field Description

Swap changes can be performed using UI Wizard or upload an excel/csv file.
Deleting a Swap Group
To delete a Swap Group
1. Click the “Delete” icon next to the desired Swap Group.
2. Confirm the “Delete” button in the pop-up window to confirm the deletion.
Exporting a Swap Group
Click “Export” and select “Export to Excel” or “Export to CSV”
Uploading a Swap Group
1. Click on “Upload”
2. Drop the file you want to upload. Alternatively, you can click on “Drop a File”, select the file and click “Open”


3. Click “Upload“ to upload the file or click “Close” to cancel.



