[🏠 Document Start](..\..\README.md) / [Alerts](..\README.md) / [Alerts](README.md) / Slack: How to configure Alerts

# Slack: How to configure Alerts

Overview
Slack is a cloud-based communication and collaboration platform designed for teams to streamline messaging, share files, and integrate
with various productivity tools including custom applications for automation. Within the Slack application, a bot app can be created to
enable automated interactions with users via text commands. The Slack Bot API facilitates bot delivering messages which Centroid
Solutions integrated into our Centroid Bridge. This integration empowers real-time alerting for critical events, enhancing responsiveness
and communication for bridge broker administrators.
Main Requirements
1. Dedicated Slack App for Bot
2. Bot OAuth Token
3. Channel ID
Important notes:
1. Only 1 Slack app bot is needed per company
2. For the public channel, any users within the company can join the channel
3. For the private channel, the administrator must add their employees to the channel
Creating a Dedicated Slack App (bot) and retrieving Bot OAuth Token
1. Download and install Slack then register for an account
2. Go to https://api.slack.com/apps
3. Click on “Create an App”
4. Select “From an app manifest”
5. Select your workspace
6. Select “YAML” then clear the script
7. Add the below Script
8. Click “Next” then “Create”
9. Click “OAuth & Permissions”
YAML
display_information:
name: Centroid Bridge
features:
bot_user:
display_name: Centroid Bridge
always_online: false
oauth_config:
scopes:
bot:
* chat:write
* chat:write.public
settings:
org_deploy_enabled: false
socket_mode_enabled: false
token_rotation_enabled: false

10. Click on “Install to Workspace” then “Allow”
11. Click on “Copy” to copy the Bot User OAuth Token
12. Save the “Bot User OAuth Token” for later configuration
A quick guide on how to create a Slack App (bot)
Creating a Channel and Retrieving Channel ID
1. Go to Slack Application
2. On the lower left pane, click on the plus + icon
3. Select Channel
4. Name the channel
5. You can select the visibility and privacy of the channel
Public - anyone in your workspace can join the channel
Private - Only specific of invited people can join the channel (please refer below for additional steps)
6. Click on the channel name to access its information
7. Scroll down and copy the “Channel ID”
8. Save the “Channel ID” for later Configuration


A quick guide on how to create a public channel
Channels with “Private” visibility settings
1. Bot App is required to join or be added to the channel
2. Click on the channel name
3. Click on “Integrations” then “Add an App”
4. Search for the “Centroid Bridge” app then “Install”
A quick guide on how to create and configure a private channel


Configuring Slack Bridge Alerts
1. Login to bridge
2. On the left lower pane, click on Account
3. Within the account, click on “Update your profile”
4. Go to “Slack Notification”
5. Add the Bot User OAuth Token & Channel ID following the below format
Example only:
xoxb-6676000001859-6600000004022-bd7Gx0000000Y0NYj7w8uV7r;C06L000007B



