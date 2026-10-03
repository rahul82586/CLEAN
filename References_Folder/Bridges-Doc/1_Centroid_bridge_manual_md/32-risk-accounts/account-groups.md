[🏠 Document Start](..\README.md) / [Limit Symbol Groups](README.md) / Account Groups

# Account Groups

Overview
In this component, you can create Risk Accounts and account Groups (under which Risk Accounts are grouped) and configure Risk
Accounts on a Account Group and Risk Account basis.
Account Group Level Configuration
Configuration at the Account Group Level is applied across all Risk Accounts underneath. Limit Symbol Group is the parameter that is
being configured at the Group Level which is applied to all Risk Accounts underneath. The Limit Symbol Group parameter will be explained
in more detail in the respective section hereafter.
You can make the following configurations at the Account Group Level:
Filter Account Groups: Narrow down Account Groups based on desired fields to simplify configuration.
Select Account Groups: Choose one or multiple Account Groups to display the Risk Accounts underneath.
Enable/Disable all Account Groups: Manage the active status of all Account Groups.
Configure Limit Symbol Group: Set configurations across all available Account Groups, impacting all linked Risk Accounts.
Enable/Disable a particular Account Group: Affect all Risk Accounts within the selected Account Group.
Configure Limit Symbol Group of an Account Group: Apply settings across all Risk Accounts within the chosen Account Group.
Delete an Account Group: Remove an existing Account Group.
Export Account Groups: Save the list of Account Groups to an Excel file or CSV file.
Creating an Account Group
To create an Account Group
1. Click on the “Add” button
2. Fill out the Wizard, as explained below


3. Click on “Submit” to submit the changes
Deleting an Account Group
To delete an Account Group
1. Click the “Delete” icon next to the desired Account Group
2. To confirm the deletion, type the name of the Account Group in the field.
3. Click on the “Delete” button to confirm.

Exporting an Account Group
To Export an Account Group
Account Group The name of the Account Group to be created
Limit Symbol
Group
Assign the limit symbol group that you created for this particular Risk Account.
Enable Indicates whether the Account Group is enabled or disabled
* If ticked, the Account Group is enabled upon creation
* If unticked, the Account Group is disabled upon creation
Description A short description for reference purposes
Field Description


1. Select the desired Account Group from the list
2. Tick the checkbox to select an Account Group
3. Click “Export” and select “Export to Excel” or “Export to CSV”
Account Level Configuration
Other parameters can be configured at the level of Risk Account which applies solely to that particular Risk Account, unlike the ones
configured at the level of Account Group which are enforced across all Risk Accounts within.
You can configure the following parameters at the level of Risk Account under a selected Account Group:
Filter by Desired Fields: Narrow down options based on desired fields to simplify configuration.
Enable/Disable Risk Accounts: Manage the active status of Risk Accounts.
Configure Bulk Parameters: Adjust parameters across multiple Risk Accounts within the Account Group.
Configure Parameters of a Risk Account: Set desired parameters for a specific Risk Account.
Delete a Risk Account: Remove a specific Risk Account.
Export Risk Accounts: Save the list of Risk Accounts within an Account Group to an Excel File or CSV File.
Creating a Risk Account
To create a Risk Account
1. Click the “Add” to create a new Risk Account that is under the desired account group.
2. Fill out the Wizard as explained below.
3. Click on “Submit” to submit the changes.


Risk Account Preferred Risk Account Name
Group The Account Group the Risk Account belongs to
Currency USD The currency of the Risk Account into which all transactions are translated.
Note: Default value is always USD
Category Taker,
Maker
Defines whether the Risk Account is of type Taker or Maker.
Taker: If the Risk Account is linked to one or multiple Takers and/or Taker Execution Models
Maker: If the Risk Account is linked to one or multiple Makers
Note: If the Risk Account is linked to a Taker the name of the Taker will appear followed by @*. E.g:
FIX_CLIENT@*. IF the Risk Account is linked to a certain Taker Execution Model within the Taker, the
name of the Taker will appear followed by @ and the name of the Taker Execution Model. Example:
FIX_CLIENT@Account1
Taker/Maker Indicates whether the Risk Account is defined as a Taker or a Maker upon creating the Risk Account,
as explained hereafter in Create a Risk Account section
Taker: If the Risk Account is defined as a Taker, this parameter allows to link the Risk Account to
one or multiple Takers and/or Taker Execution Models
Maker: If the Risk Account is defined as a Maker, this parameter allows to link the Risk Account to
one or multiple Makers to check exposure as well as controlling what is being sent to the Maker
Type Margin,
NOP, Risk
The Type of the Risk Account which defines its purpose:
Margin: keeps track of all orders under a Risk Account and rejects any order that would increase
the exposure above the Margin Call Level threshold
Field Possible
Values
Description

Deleting a Risk Account
To delete a Risk Account
1. Click the “Delete” icon next to the desired Risk Account.
NOP: Similar to Margin with one additional feature that allows to define an exposure on a per
Symbol basis as explained in Limit Symbol Currency hereafter (Exposure Limit field)
Risk: This option is only available if the Risk Account is “Taker Type”, This applies to B Book
execution only and works in conjunction with the NOP Limits defined at the level of the Symbol.
When the threshold is breached, the Centroid Bridge would automatically start routing any position
that would further increase the exposure to the Maker. For orders of opposite side that would
decrease the exposure, the Centroid Bridge would send them to the Maker as well to offset
overflow until the exposure is flattened out.
Stop Out
Level
50 The margin percentage level at which point the Risk Account will get stopped out and positions will get
closed automatically
Stop Out
Mode

A_PERCEN
T
A_HIGH_L
OSS
A_HIGH_M
ARGIN
Dictates how the Risk Account gets liquidated when the Stop out level is reached:
AB_HIGH_LOSS: Closes the highest losing Position first irrespective of execution (A or B Book)
AB_HIGH_MARGIN: Closes the Position with the highest Blocked Margin first irrespective of
execution (A or B Book)
A_HIGH_LOSS: Closes the highest losing A Book Position
A_HIGH_MARGIN: Closes the A Book Position with the highest Blocked Margin first
B_HIGH_LOSS: Closes the highest losing B Book Position
B_HIGH_MARGIN: Closes the B Book Position with the highest Blocked Margin first
Disabled: Stop out is not active thus Account does not get liquidated
Note: When the Centroid Bridge closes the first Position it checks whether the Stop out level is still
above the defined one, if not it will close the next Position depending on the Square Off Mode utilized
Note: If the Position is made up of Orders accumulated from different Taker Execution Models, the
Centroid Bridge will close the Position by sending each Order separately through its respective Taker
Execution Model
Enable Enabled,
Disabled
Indicates whether the Risk Account is enabled or disabled
If ticked, the Risk Account is enabled
If unticked, the Risk Account is disabled which means that the Risk Account would still track the
positions but would not apply margin or risk settings
Exposure
Limit
1,000,000,0
00
This is only relevant to Risk Accounts of type NOP where a Limit in USD notional value can be set at
which point no Orders that would increase the exposure above that limit would be allowed.
Note: Default value is -1 which indicates that no Exposure Limit set
Warn Level 50,70,90 Margin percentage levels of the Risk Account at which point a notification alert will be sent by the
Centroid Bridge via email to the registered email address(es).
You can add as many values as you want provided that the total number of characters does not
exceed 40
Margin Call
Level
100 The Margin percentage level at which point no Orders that would further increase the exposure would
be allowed
Description A short description for reference purposes

2. To confirm the deletion, type the name of the Risk Account in the field.
3. Click on the “Delete” button to confirm.
Exporting a Risk Account
To Export a Risk Account
1. Select the desired Risk Account from the list
2. Tick the checkbox to select a Risk Account
3. Click “Export” and select “Export to Excel” or “Export to CSV”



