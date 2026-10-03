[🏠 Document Start](..\..\README.md) / [Takers](..\README.md) / Takers

# Takers

Overview
The Takers module handles the Liquidity Takers in the Centroid Bridge including a variety of popular front-end platforms as well as direct
FIX APIs connected to the Centroid Bridge in addition to Drop Copy. Platforms include MT4, MT5, Ctrader, or any other FIX-compliant
platforms as well as our own Centroid Trading UI.
From the Taker components, you can configure and manage all pricing and trading settings pertaining to the Takers connected to the
Centroid Bridge, through the different components, Taker Feeds, and Taker Execution Models, which are explained in more detail
hereafter.
This module displays all the liquidity Takers defined in the Centroid Bridge, which could be of type MT4, MT5, FIX, Centroid UI, and Drop
Copy.
In addition to viewing all Takers configured in the Centroid Bridge, additionally you have the capability to:
Create a New Taker (FIX or Drop Copy): Initiate the setup for a new FIX or Drop Copy Taker.
Filter and Look Up Takers: Categorize and search for specific Takers using various criteria.
Enable and Disable Taker: Manage the active status of a particular Taker.
Delete Taker: Remove a Taker of type FIX or Drop Copy by clicking the delete button.
View Taker Connection Settings: Access and review the connection settings for a Taker.
Export Taker FIX Config (Pricing and Trading) or Drop Copy: Save configuration details to Excel or CSV.
Export Taker List: Save the list of Takers to an Excel file or CSV file.
Note: Disabling Taker on this level means, you are disabling the taker to receive quotes/prices from the bridge and disabling the execution
i.e. no trade will be accepted by the bridge from this taker. While enabling a newly added taker will require a restart.
Note: Takers of type MT4 and MT5 cannot be added here, such configurations require assistance from Centroid Support Team.
Creating a Taker
To create a Taker of type FIX or Drop Copy
1. Click the “Add” button
2. Fill out the Wizard. You may refer to the field descriptions hereafter
3. Click “Submit” to submit the changes


Important Notes:
1. Only Takers of type FIX and Drop Copy can be created on the client end, for other types i.e. MT4/MT5, you need to send the request to
support@centroidsol.com and the Centroid Support team will add it for you.
2. Once you have created the Taker, you need to perform a Bridge Restart, after the restart, the Taker will be ready to accept
connectivity and the connecting party will be able to establish the connection to the bridge.
Export Takers List
To Export listed Takers
1. You will need to click on the “Takers” module
2. Click on the “Takers”
3. Click “Export” and select “Export to Excel” or “Export to CSV”
Taker A unique name of the Taker
Type The type of Taker:
FIX: FIX API Pricing and Trading to be given to clients who wish to connect via FIX
DROPCOPY: FIX Drop Copy allowing connection to post-trade information via FIX
Description A short description for reference purposes
IP List IP(s) of the Taker, comma separated in case of multiple IPs
Disclaimer: You need to share Sources IPs of the [Taker] with Centroid Support, so we can create the
whitelisting request, without the IP whitelisted no connection will be established.
Enable Indicates whether the Taker is enabled or disabled
If ticked, the Taker will be enabled upon creation
If unticked, the Taker will be fully disabled upon creation hence, no quotes and no execution of trades from
this Taker.
Field Description

Export FIX or Drop Copy Credentials
You can export the FIX credentials pertaining to Takers of type FIX or Drop Copy. The FIX Taker credentials allow clients to connect to the
Centroid Bridge via FIX to receive prices and send Order requests, whereas Drop Copy Taker settings allow you or any third party to
connect to post-trade information in real-time.
To Export the FIX credentials
1. Click the “Export Fix Config” button next to the desired Taker as seen below
2. Once exported, a text file will be downloaded automatically in which you can see the FIX API configuration
FIX Taker
It contains two sessions with a pricing connection for which the client will be able to connect to receive prices and a trading connection for
the client to be able to send trades and receive order confirmations and execution reports from the Centroid Bridge. FIX client should
target the Taker Execution Model when sending Order requests via FIX tag 1. In the event of having multiple accounts or Taker Execution
Models assigned to the same taker, the accounts or tag #1 will populate all the available values.


Drop Copy
It contains a single session similar to a Trading session through which the client can connect to receive a copy of post-trade information,
as seen below.



