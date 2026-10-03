[🏠 Document Start](..\README.md) / [MT5 Centroid TOB Feeder Manual](README.md) / MT5 Centroid DOM Feeder Manual

# MT5 Centroid DOM Feeder Manual

Before initiating the setup for the Centroid MT5 DOM Feeder, you'll need to provide the following information to whitelist your IPs:
1. Provide the IP of all MT5 Live Servers where the MT5 Feeder will be installed.
2. Supply the IP of all MT5 Live Backup Servers.
To configure the Centroid MT5 DOM Feeder, follow the instructions below:
1. Remotely log in to the server where the MT5 Server is installed using RDP or another tool.
2. Copy the Centroid MT5 Datafeed folder into the "Feeder" directory of your MT5 History Server installation. “The path will resemble D
or C:\MetaTrader 5 Platform\History\Datafeed.”
Note:
1. The installation process does not necessitate stopping the MT5 Service.
2. The Centroid MT5 Feeder will be automatically duplicated to the MT5 Backup Server.
To set up the Centroid MT5 DOM Feeder:
1. Log into MT5 Administrator and navigate to Datafeed.
2. Add a new Datafeed.
3. Customize the newly added Feeder as follows:
Name: Specify the configured Feeder's name.
Module: Locate the Feeder file within the uploaded folder.
Select: Choose "Quotes" from the dropdown.
Trading Server: Provide the DNS and Port details given by Centroid.
Trading Login: Enter the trading login ID provided by Centroid.
Password: Input the trading password provided by Centroid.
Parameters: Sender and Input the TargetCompID provided by Centroid.
Essential Setup Information
Installation
The new plugin can be installed as either a Data Feed or a Gateway. It is recommended that this feeder be installed under
datafeed. If there’s a requirement to install it as a Gateway, please contact our support team via Skype/Slack or email.
Configuration

Note: Make certain that all the Symbols intended for pricing by the Centroid Feeder are appropriately listed in the Symbols tabs,
respectively.
If the Sender is not added in the parameters, the DOM Feeder will not be able to establish a connection with the bridge.

When upgrading the Centroid MT5 DOM Feeder to a newer version, adhere to the following steps, ensuring the new folder supersedes the
old one for simplicity:
To enhance the Centroid DOM MT5 Feeder, proceed with the following instructions:
1. Access the Server: Remotely access the server where the MT5 History Server is installed, using RDP or any other tool.
2. Backup the Old Version: Create a backup by copying the existing Centroid DOM Feeder to another folder, ensuring the ability to
revert the update if needed.
3. Disable the Centroid Feeder: Before replacing the file, it is recommended to disable the “Centroid DOM Feeder” from the MT5
Administrator.
4. Replace the File: Replace the existing Centroid DOM Feeder .exe file in the "Datafeed" folder of your MT5 History Server installation
with the new one, maintaining the exact name.
5. Version Monitor: In the MT5 Administrator, monitor the disabled feeder's version under status. Once the correct version is loaded
successfully, enable the Feeder.
6. Enable the Centroid Feeder: Re-enable the Feeder using the MT5 Administrator.
Enhancing the Feeder
How to Backup:
Please ensure that the existing Centroid DOM Feeder is copied to a location outside the DataFeed folder (e.g., Desktop or any
other preferred directory). This will prevent the backup file from appearing in the drop-down menu in MT5.
The DOM Feeder will remain connected, as the continuous heartbeat exchange ensures an active connection, even if the prices
are not streamed from your bridge to MT5.

