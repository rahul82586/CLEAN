[🏠 Document Start](..\README.md) / [MT4 Centroid Installers](README.md) / MT4 Centroid Feeder Manual

# MT4 Centroid Feeder Manual

Before initiating the setup for the Centroid MT4 Feeder, you'll need to provide the following information to whitelist your IPs:
1. Provide the IP or DNS of all MT4 Live Servers where the MT4 Feeder will be installed
2. Provide the IP or DNS of all MT4 Live Backup Servers
Configuration Steps for Centroid MT4 Feeder
1. Remote Server Access: Remotely access the server hosting the MT4 Server using tools such as RDP or any other remote access
method
2. Stop MT4 Server: Stop the MT4 Server through Windows Services by stopping the corresponding service named "MetaTrader 4
Server"
3. File and Configuration Transfer: Place the Centroid MT4 Feeder .feed File in the 'datafeed' Directory of Your MT4 Server Installation.
The Path Typically Resides at D:\MetaTrader4Server\datafeed.
4. Restart MT4 Server: Initiate the MT4 Server once again through Windows Services by launching the relevant service named
"MetaTrader 4 Server"
5. Consistent Configuration on Backup Server: Repeat the aforementioned steps on your MT4 Backup Server for ensuring consistent
configuration
To set up the Centroid MT4 Feeder, follow these simple instructions:
1. Log in to MT4 Administrator and navigate to Data Feeds.
2. Add a new Data Feed.
3. Configure the newly added Data Feed with the following details:
Name: Enter the name of the configured feeder.
Type: Select "Quotes" from the dropdown list.
File: Locate the feeder file uploaded to the feeder folder on the MT4 Server, ensuring it matches the exact name.
Server: Provide the DNS and Port details given by Centroid.
Login: Enter the trading login ID provided by Centroid.
Password: Input the trading password provided by Centroid.
Keywords: This optional field allows you to specify certain Symbols to be quoted via the Data Feed or excluded. Use "*" for wildcard or
"!" for negation.
Essential Setup Information
Installation of MT4 Feeder
Configuration

When upgrading the Centroid MT4 Feeder to a newer version, adhere to the following steps, ensuring the new folder supersedes the old
one for simplicity:
1. Access the Server: Remotely access the server where the MT4 Server is installed, using RDP or any other tool.
2. Backup the Old Version: Create a backup by copying the existing Centroid feeder to another folder. This backup ensures you can
easily revert the update if needed.
3. Stop MT4 Server: Stop the MetaTrader 4 Server from Windows Services by stopping the relevant service, "MetaTrader 4 Server."
4. Replace the File: Override the existing feeder by copying the new Centroid Feeder .feed file into the "datafeed" folder of your MT4
Server installation.
5. Restart MT4 Server: Start the MetaTrader 4 Server from Windows Services by initiating the relevant service, "MetaTrader 4 Server."
6. Version Monitor: In the MT4 Administrator, monitor the disabled feeder's version under status. Once the correct version is loaded
successfully, enable the Feeder.
7. Enable the Centroid Feeder: Re-enable the Feeder from the MT4 Administrator.
Updating the Feeder

