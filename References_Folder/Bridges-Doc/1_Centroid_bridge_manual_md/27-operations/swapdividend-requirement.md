[🏠 Document Start](..\README.md) / [Swaps Groups](README.md) / Swap/Dividend Requirement

# Swap/Dividend Requirement

MT4 Required Configurations & Actions
For the installation of the MT4 Centroid plugin, follow these steps:
a. Open port 11000 on the MT4 server or allow the bridge IP on port 11000.
b. Send the following details to support@centroidsol.com:
Confirmation that the plugin is successfully installed.
Target Server IP: 11000
Installation
1. Stop the MT4 service via Windows Services
2. Add the centroid_mt4_operations.dll file to the plugin folder (download here).
3. Start the MT4 service via Windows Services.
Note: Config file will be automatically created during the installation with a default port of 11000.
MT5 Required Configurations & Actions
Provisioning MT5 Manager
1. Create a dedicated MT5 Manager for Swap Uploader
2. Manager Group Permission must be configured
3. Manager Permission must be configured with the below rights:


4. Send the following details to support@centroidsol.com
* Desired Swap Uploader name (e.g., “Main MT5 Server”)
* Manager Login
* Manager Master Password
* Public Access Server


