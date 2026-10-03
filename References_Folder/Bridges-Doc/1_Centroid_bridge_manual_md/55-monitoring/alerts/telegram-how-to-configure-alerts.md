[🏠 Document Start](..\..\README.md) / [Taker Status](..\README.md) / [Alerts](README.md) / Telegram: How to configure alerts

# Telegram: How to configure alerts

Overview
A lot of companies started utilizing telegram as one of their main channels to monitor systems and receive notifications or alerts. Within the
telegram messaging platform, a bot tool can be created to enable automated interactions with users via text commands. The Telegram Bot
API facilitates bot delivering messages which Centroid Solutions integrated into our Centroid Bridge. This integration empowers real-time
alerting for critical events, enhancing responsiveness and communication for bridge broker administrators.
Main Requirements
1. Dedicated Telegram Bot
2. Bot Token ID
3. User ID

Important notes:
1. Only 1 telegram bot is required per company
2. Company users must subscribe to the telegram bot that you created
3. Company users are required to retrieve their personal User ID number
4. Company users are required to configure their profile with the token and their User ID
Creating a Telegram bot and retrieving Token ID
1. Download and install Telegram then register for an account
2. To create a bot, search for @BotFather
3. Click on Start then type /newbot
4. Give your bot a unique company name and create a unique username (e.g., Centroid Bridge FXBroker with username
CBFXBroker_Bot)
5. Upon confirmation that the bot has been created, retrieve the token ID
6. Save the “token ID” for later configuration
Warning: The above bot name is only an example. Please do not copy it to avoid having the same bot name with other Brokers or
Centroid Clients.


A quick guide on how to create a bot
Retrieving your User ID
1. Download and Install Telegram then register for an account
2. Search for @userinfobot
3. Click Start then retrieve your UserID number
4. Save the “User ID” for later configuration


Subscribing to your Company's Telegram Bot
1. Download and Install Telegram then register for an account
2. Search for the name or username of the bot that your company created for the Bridge alerts
3. Click Start to subscribe and receive alerts
Configuring Telegram Bridge Alerts
1. Login to bridge
2. On the left lower pane, click on Account
3. Within the account, click on “Update your profile”
4. Go to “Telegram Notification”
5.Add the Bot Token ID & User ID following the below format
Example only:
7110000034:AAGg4No0000Q2sJKnx9s5_ifRc00000Nfk;920000052



