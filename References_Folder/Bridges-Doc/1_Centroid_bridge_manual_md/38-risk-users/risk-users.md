[🏠 Document Start](..\README.md) / [Risk Users](README.md) / Risk Users

# Risk Users

Overview
The Risk Users module complements the Risk Accounts module, enabling the creation of client users linked to specific Risk Accounts. This
facilitates granting clients access to a specialized trading interface for reviewing account balances, open and closed positions, and
conducting various balance operations. Additionally, clients can directly execute trades from the Trading Platform. Detailed coverage of
these features will follow in the Trading and Reports components, specifically within the Trader view.
A key scenario involves creating a Risk User for a specific Risk Account tied to a FIX Taker client. The FIX client accesses a personalized
interface for monitoring positions, balances, and direct trading. Risk Users can access one or multiple Risk Accounts. Users can be linked
to risk accounts, acting as a read-only pool to monitor and aggregate trades and balances from multiple accounts.
Users
Within this module, you have the capability to:
Create Risk User: Establish a new Risk User.
Filter Risk Users: Sort and identify Risk Users from the available list.
Edit Risk User Info and Configuration: Modify details and settings for a Risk User.
Delete Existing Risk User: Remove a currently defined Risk User.
Export Risk User List (Excel/CSV): Save the list of Risk Users to an Excel or CSV file.
Creating a Risk User
To create a new Risk User
1. Click “Add” to create a new Risk User.
2. Fill out User Information
3. Click “Add Risk Account” to link the Risk User to a Risk Account. You need to repeat this step for an additional Risk Account to be
linked to the Risk User
4. Configure Risk Account based on Risk User preference
5. Click “Submit” to submit the changes
New User


Assigning the Risk Account: Click on Add Risk Account
Username Yes The username of the Risk User to be used to access the User interface.
Email Yes Email of Risk User.
Password Yes The password for the Risk User is utilized for accessing the user interface.
Confirm Password Yes Please verify the password entered in the preceding field.
First Name Yes The First Name of the User which will be displayed on top upon logging in.
Last Name Yes The User's Last Name, which will appear at the top upon logging in.
Phone No Contact number of the Risk User.
Emails Notify (csv) No List the emails eligible to receive the Daily Statement when the Daily Statement option is
selected.
Field Required Description
Alias USD_RA, TakerName_RA,
MakerName_RA
An acronym to tell apart different Risk Accounts when several are chosen. This
helps switch between them easily in the user interface.
Risk Account Connect the Risk Account created previously to the Risk User.
Taker Centroid_MT4, Centroid_MT5 Specify the specific Taker for the Risk Account if it's linked to multiple Takers or
TEMs across different Takers.
TEM Tem-1, Test-TEM, TEM-2 Indicate the specific Taker Execution Model (TEM) for the Risk Account to pull
data from. Incase of 2 or more TEM’s kindly on Add Risk Account for second row.
Taker Feed Plain_TF, 10Points_TF,
Retail_Feed
Specify the Taker Feed, indicating the assigned suffixes used by your Taker
Client.
Read Only Indicates whether the Risk User is a Read Only User
If ticked, User read-only access limited to viewing the Account and statement
without the ability to trade
If unticked, User has full access, view and trade
Daily Statement Specifies whether the Risk User receives End-of-Day (EOD) Statements
dispatched by the Centroid Bridge.
Ext Order Info Indicates whether the Risk User can view Orders coming from external Takers
(platforms) or only the one placed via the GUI
If ticked, User views Orders coming from external Takers.
If unticked, User does not view Orders coming from external Takers it only
views the ones placed from the Use GUI
Default Sets the selected Risk Account to default when Risk User logs in, this is incase of
having multiple Risk Accounts.
Field Possible Values Description

Editing a Risk User
To modify an existing Risk User
1. Double-click on the details you want to edit
2. Click the “Save” button to apply the changes
Deleting a Risk User
To delete an existing Risk User
1. Click the “Delete” icon next to the desired Risk User
2. Click the “Delete” in the pop-up window to confirm the deletion
Exporting Risk User List
To Export a Risk User
1. Select the desired Risk User from the list
2. Click “Export” and select “Export to Excel” or “Export to CSV”
Exporting a Risk User
To Export a Risk User
1. Select the desired Risk User from the list


2. Tick the checkbox to select a Risk User
3. Click “Export” and select “Export to Excel” or “Export to CSV”



