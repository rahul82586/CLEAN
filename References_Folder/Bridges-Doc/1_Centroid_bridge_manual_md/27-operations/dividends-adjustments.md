[🏠 Document Start](..\README.md) / [Operations](README.md) / Dividends Adjustments

# Dividends Adjustments

Overview
The Dividend Adjustment under Operation allows a broker to apply dividends to any MT4/5 login based on their open positions. It offers an
option to fully apply automated dividends according to broker's requirements. With the dividend component, we can select the
corresponding MT4/5 server. The required symbol can be selected together with the base currency which will be used for the conversion
rate. Long/Short dividend value will be used to calculate the final dividend amount and it can be set to apply immediately or scheduled to
be performed at a later time.
Create a Dividend Operation
To create a new dividend task
1. Click “Schedule Dividends Adjustment” to create a new dividend operation.
2. Fill out the wizard with all the required fields, you may refer to the field descriptions hereafter.
3. Click “Preview and Schedule” to submit the changes.


Server The specific MT4/5 server you can choose to apply the dividends adjustment
Symbol The symbol for which the dividends need to be applied
Currency The currency will be treated as the base currency for calculating the conversion rate. Custom button can be
ticked to manually type any desired currency for conversion rate
Collect Symbol Suffixes Dividend will be applied to all the symbol suffixes of the selected symbol
Long Dividends The amount to be (added/deducted) to an account for a long position
Short Dividends The amount to be (added/deducted) from an account for a short position
Conversion Rates The current conversion rate will be used for converting the dividend amount from the selected currency to
the account's group currency. It will apply the conversion rate only if it is enabled
Delayed Allows the dividend task to be scheduled at any date/time
Field Description

Scheduled/Completed Dividend
Scheduled Dividend
1. Scheduled dividend will be shown as blue circle.
2. Clicking on the “pen” icon allows us to edit the dividend fields.
3. Preview of the dividend will be shown after we click “Preview and Schedule”.
Completed Dividend:
1. Completed dividend will be shown as green circle.
2. Clicking on the “eye” icon will display the details of the operation.
3. All the completed tasks can be displayed based on date/time on Monitoring >> “Dividend Completed Jobs” Component.
Applied Date UTC The UTC date and time when the dividends adjustment will be applied
Dividends Deal
Comment
A comment related to the dividend adjustment balance operation. It will be displayed in the MT4/5
Check Margin if enabled, it will check the account margin before applying dividend. Set to disable, the dividend task will
not consider account margin


Dividend Calculation Formula
→ For Long Position:
Amount=Position Volume × Contract Size × Conversion Rate × Long Dividends Value
→ For Short Position:
Amount=Position Volume × Contract Size × Conversion Rate × Short Dividends Value
Important Notes
1. Position Volume Unit: The Position Volume is in lots.
2. Conversion Rate: The conversion rate goes from the chosen base currency to the MT4/MT5 login currency.
3. Conversion Rate of 0: The conversion rate will be zero if the base currency to login currency is not priced in MT4/MT5.
Example:
Base currency (CCY) = GBP
MT4/MT5 login currency (CCY) = USD
To obtain a conversion rate for a dividend, GBPUSD must be priced on MT4/MT5.


