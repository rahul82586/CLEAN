[🏠 Document Start](..\README.md) / [Bridge Changelog](README.md) / UI Changelog

# UI Changelog

04/12/202
5
v1.3.7 New Features:
Introduced Position Comparison Dashboard under Reports
Added Upload Option for Dividends Adjustment
Improvements:
Improved UI for Maker and Taker Config Tables
Fixed minor issue with Symbols filter across components
03/01/202
5
v1.3.6 Improvements
Enhanced Swaps group selection functionality, now supporting an unlimited number of groups for selection
and updates
EOD Risk Account Statement time can now be aligned with Market EOD time (backend configuration
required)
Added a new option under Risk User to enable Monthly Statements alongside the existing Daily Statement
Introduced Swaps Groups Logs under Operations to track the progress and changes made within the
Swaps Groups module
A minor update has been made to the Dividends Adjustment (MT5) under Operations
Enhanced Market Watch to reduce the loading time in the Symbols dropdown menu
02/15/202
5
v1.3.5 No Public News
Internal updates
02/01/202
5
v1.3.4 New Features
Introduced Profile under Market Watch, allowing you to create, save, and switch between predefined
symbol sets for quick access and seamless monitoring
Improvements
Refactored Symbols column search filtering by implementing a tree selection system for more structured
filtering and smoother navigation (UI)
Market Watch Caching is now enabled, preserving your last selected symbols for easy access (UI)
01/11/202
5
v1.3.3 Improvements
Improved the Risk Account Statement (Reports) to support displaying historical data for Open Positions
and Account Balances
Separated the Taker Feed column from the Taker Symbol column in Market Watch List mode
Enhanced Taker Execution Rules by moving Export/Import functionality to the taker level
Introduced Spanish to the list of supported languages
Enhanced the selection style for Market Watch Modes
11/30/202
4
v1.3.2 Improvements & Bug Fixes
Added a warning message to the Maker API Link component for empty tag values
Implemented validation to ensure the Limit Symbol Group cannot be deleted if linked to Account Groups
Release
Date
UI
Version
Release Notes

Restructured the components under the Takers (Side bar)
Divided Logs and Monitoring into distinct sections
Fixed the issue with the availability of the download button for uncompressed logs
Fixed a minor issue with the Notification settings
Resolved the issue with saving Markup Model WL values
Resolved the issue with search filters across multiple components
11/09/202
4
v1.3.1 Improvements & Bug Fixes
Enhanced the Taker and Maker status (UI)
Updated pop-up notifications to the new toast style (UI)
Resolved a minor bug in the Risk User Trade component (UI)
Simplified Symbol Format options in Trade Copier, Giveup Rule, and Hedge Trade Rule (UI)
10/26/202
4
v1.3.0 Improvements
Added Rounding Modes and Precision in the Dividends Adjustment
No Rounding: Rounding is handled entirely by the MT platform.
Round Up: Dividends rounded up before pushing to MT.
Round Down: Dividends rounded down before pushing to MT.
Client: Rounding is adjusted in favor of the client.
Broker: Rounding is adjusted in favor of the broker.
Standard: Follows standard rounding rules
Optimized User Interface
Various internal improvements to boost efficiency and reliability
10/21/202
4
v1.2.9 New Features & Integrations
Introduced a New feature, "Taker Execution Rules (Beta!)" under Takers, that supports trade routing for all
taker types using customizable filters.
Improvements & Bug Fixes
Revamped the Risk User creation form to include Risk Account information configured using the Taker
Risk Filter (UI)
Improved the Order History Report for Risk User by adding a new 'Reason' column, which can be
configured via the Resource column under Permissions in Bridge and is disabled by default (UI)
Resolved the issue with closing trades involving decimal volumes from the positions report for Risk
Account type (UI)
Addressed a minor UI bug affecting Maker selection in give-up rules (UI)
Enhanced Maker Alerts and Status
10/05/202
4
UTC
v1.2.8 New Features
Introduced Branded Logo
Brokers will have the option to upload their logo, which will be displayed to their Risk Users. The logo
can be uploaded from Branded Logo section available under Risk Users from the Bridge
Improvements
Added Tickets Type for the Risk User's Market Watch
Enhanced the Market Watch List Mode for both Bridge and Risk Users
Implemented an option that allows users to manage the visibility of Last Traded Price, Last Traded
Volume and Maker Name on the Bridge Market Watch for Tickets Type
Added a button to expand and collapse the Market Watch search bar

09/13/202
4
UTC
v1.2.7 Improvements and Bug Fixes
Resolved issue with missing symbol descriptions in the Taker Execution Model
09/07/202
4
UTC
v1.2.6 New Features
Enhanced all component creation forms
Enabled exporting of Bridge manual contents
Introduced new REST API endpoints for GET, POST, PUT, and DELETE operations on the following
Bridge components:
Giveup Rules
Taker Feeds
Taker Execution Models
Risk Users
Improvements and Bug Fixes
Added a confirmation button for uploading symbol files
Improved and streamlined the user account window
Fixed the default landing page for Bridge
08/31/202
4
UTC
v1.2.5 No Public News
Internal updates
08/17/202
4
UTC
v1.2.4 New Features
Added a New Feature for Scheduling Bridge Restarts:
A new module has been introduced under Actions Scheduler - Advanced Actions, which now supports
scheduling Bridge Restarts.
The existing Action Scheduler Rules have been relocated to Component Actions under the Actions
Scheduler.
Advanced Actions Logs have been introduced under Monitoring to display the outcomes of actions
scheduled within the Advanced Actions module.
Improvements
Included milliseconds in the timestamp for the Taker Send Time column in the reports.
07/27/202
4
UTC
v1.2.3 New Features
Added New Modes for Book Construction under the Liquidity Model:
VWAP
VWAP_CUM_QTY
CUM_QTY
Improvements and Bug Fixes
Enhanced performance by calibrating the Symbols loading for the following components:
Liquidity Model
Markup Model
Makers
Limit Symbol Group
Fixed a minor bug in Risk User's MarketWatch for symbols containing special characters
Resolved the file Upload issue for the Liquidity Model, Markup Model, and Makers

07/20/202
4
UTC
v1.2.2 No Public News
Internal updates
06/29/202
4
UTC
v1.2.1 New Features
Introduced Notification Sounds for Bridge Alerts
Brokers can now set Notification Sounds from the Account section
Supports Custom Sound Upload
Added New columns under Taker Execution Model:
ODelay Min
ODelay Max
BLast Resort
Implemented Operation Logs to track Swaps and Dividend changes
Improvements and Bug Fixes
Enhanced the One-Click Maker deployment process
Fixed minor issues with the White Theme and Maker Status
Resolved the error in the Workspace for Hedge Trade components
06/08/202
4
UTC
v1.2.0 New Features
Introduced One-Click Maker deployment process for Centroid to Centroid connections (Manual will be
published soon)
Introduced new REST API and WebSocket to GET Positions under Reports
Added Classic theme to the existing list of themes
Improvements and Bug Fixes
Added Security column to Symbols Profile
Fixed multiple issues with the White theme
Fixed the bug where cells remained highlighted even after saving
Resolved a minor issue related to Dividends for the MT4 Operations Plugin
Enhanced the Trading API by introducing external login, group, and orderID fields to the open_orders
endpoint
05/25/202
4
UTC
v1.1.9 Improvements and Bug Fixes
Major Update to Swaps & Dividends Operations with enhanced performance
Added a checkbox under the Maker API Link to include a tag as a header in the FIX message
Fixed the Incorrect Loading in components where rules does not exist
Optimized the Symbol Loading for Taker Execution Model
Fixed the issue where language and theme settings were reverting upon logout
Resolved a minor issue with Push ticks
05/11/202
4
UTC
v1.1.8 Improvements and Bug Fixes
Implemented validation & Enhanced the UI for Hedge Trade Rule
Fixed Session Wizard when creating a new Stale Rule
Improved External Markup precision in various Reports
Enhanced the Password Reset process
Removed BBOOK as Maker from Stale Rules
Resolved a minor issue with the Notification Alerts
Added Risk Account Template Button for Position Upload

04/27/202
4
UTC
v1.1.6 Improvements and Bug Fixes
Enhanced the scrollbar functionality when using the Liquidity Model dropdown menu
Fixed the decimal precision for Prices and Spreads in the MarketWatch
Adjusted default permissions of Users
Fixed volume precision within Trading Platform
04/06/202
4
UTC
v1.1.5 New Features
Implemented new Permissions for read-only Broker users
Permission to Download Reports
Permission to Download Logs
Improvements and Bug Fixes
Improved UI side pane when minimizing all modules
Improved all upload wizard preview
Uploaded file will be removed after a successful upload
Uploaded file will be retained after a failed upload to review
Fixed the Liquidity Model limitation within the Taker Execution Model
Adjusted UI MarketWatch to display price precision based on Symbol Digit settings
Fixed MarketWatch with read-only Broker users
Fixed Session Wizard of the Action Scheduler
03/23/202
4
UTC
v1.1.4 New Features
Revamped and Enhanced Market Watch with the following new features:
Redesigned UI for improved user experience
Ability to capture Screenshots at the Symbol or Global level
Option to display Depth on Symbol level or Global level
Easily toggle the Play or Pause button while reviewing prices
Export option available for list view
Enhanced Symbol Session Wizard and added the following new features:
Timeline & Text Mode
24-hour clock notation
Implemented a new feature for uploading Taker Execution Model Positions
Added option to download the template in Positions Report
Added option to upload Excel file containing new positions in Positions Report
Improvements and Bug Fixes
Restructured Risk Account component arrangement
Fixed minor issues with saved columns in the Reporting module
Fixed minor issues when sending Daily statements
Fixed the Book Construction upload issues under the Liquidity Model
03/09/202
4
UTC
v1.1.3 New Features
Introduced Two-Factor Authentication to Elevate UI Security.
Introduced Depth in MarketWatch for Risk Users.
Added new REST API endpoints to GET, POST, PUT, and DELETE for the following Bridge components:
Account Groups
Limit Symbol Group
Risk Account

Taker Risk Filter
Improvements & Bug Fixes
Enhanced Symbol filtration for Risk User's Trading Platform.
Enhanced Page Summary Panel for Reports Module
02/24/202
4
UTC
v1.1.2 New Features
Integrated new channels for Centroid Bridge alerts
Telegram Messenger
Slack
Added relevant fields for new channels under the profile
Telegram Notification
Slack Notification
Implemented a new design for UI alerts
Added bell icon for historical alerts
Added a news ticker at the bottom of the page for live critical alerts
Improvements & Bug Fixes
Added bulk edit option for Swaps Symbols under Operations
Enhanced Taker Execution Model validation for Min & Max Volumes
Enhanced Taker API Link validation for Min & Max Size
Fixed "View Results" in the Reporting module
Moved MT4/MT5 download folder to the Online Manual
02/10/202
4
UTC
v1.1.1 Improvements & Bug Fixes
Sorted Symbols in alphabetical order for all components
Enhanced Symbol Profile Module
Added Warning message for validations
Updated URL link
Fixed Warning and Error timeout validation
Fixed Book Construction validation during creation
Minor update on Trading API Reference
02/03/202
4
UTC
v1.1.0 New Features
Added Workspace for creating a customized dashboard
Added new REST API endpoint to GET Taker Feed information
Added new REST API endpoint to GET Taker Execution Model information
Improvements
Replaced columns under Symbol Profile
Added Warning Timeout (sec)
Added Error Timeout (sec)
Redesigned and simplified the bridge Search button
01/27/202
4
UTC
v1.0.9 Improvements & Bug Fixes
Added validation of mandatory fields for Balance Transaction
Enhanced Risk Account creation wizard
Enhanced Taker Risk Filter creation wizard
Added export button for Risk User

Enhanced general UI pages and component tables
01/18/202
4
UTC
v1.0.8 New Features & Integrations
Added the following Online Documentation:
Centroid Bridge Manual
Config Rest API and WS
Trading Rest API and WS
Added Risk User Permissions
Added URL "bridge.centroidsol.com" for Rest API & WS endpoints
Improvements & Bug Fixes
Enhanced grid for the following components:
Filtration Pool
Giveup Rule
Limit Symbol Group
Maker API Link
Taker API Link
Trade Copier
Fixed missing actions when editing Concentration Per Login
01/13/202
4
UTC
v1.0.7 New Features & Integrations
Added option to save and reset predefined columns for Reports
Added new REST API endpoint to GET Symbol information
Added new REST API endpoint to GET Limit Symbol Group information
Improvements & Bug Fixes
Enhanced Action Scheduler Grid
Redesigned the pattern picker
Renamed Enabled Multiplier to Multiplier Mode
Enhanced deletion response with Accounts Groups
Removed BBOOK as Maker from various components and filters
12/30/202
3
UTC
v1.0.6 New Features
Added Failover Makers under the Liquidity Model component
Added two new components: Stale Price & Symbols Profile
Added two new columns for Trade Pattern Detection within the Taker API Link: Order Repetition Interval &
Order Repetition Counter.
Added a 'Read-Only' option for users within the Bridge.
Improvements and Bug Fixes
Enhanced the column arrangement in both the Taker Risk Filter and Taker API Link Component.
Enhanced the column layout across various components within Bridge.
Enhanced the presentation of taker symbols within the Risk User interface
Enhanced the Search Window functionality across different components in Bridge, enabling the input of
values
Fixed the UI Time Display


11/18/202
3
UTC
v1.0.5 New Features
Added new component "Taker Risk Filter"
Added new columns within the Taker Execution Model for Negative Slippage Absorption
Added new columns or filters within the Taker API Link for Volume and Scalper Detection
Improvements & Bug Fixes
Added summary box in Maker Notional Chart
Fixed Report date selection filter
Fixed default Risk Alias account in Risk User
Fixed Expiry Date allowed values in Maker Symbol settings

11/11/202
3
UTC
v1.0.4 Enhancement: Sidebar icons when using collapsed mode
Enhancement: Exported details of "Trade Statement" within Risk User
Enhancement: Removed not supported components in the workspace within Risk User
Bug Fix: Reset password link
Bug Fix: Deleting FIX taker

11/04/202
3
UTC
v1.0.3 New Feature: Quick Navigation Search to easily find modules and components
New Feature: Highlight values with Markdown or Negative Markup in the Markup Model
Enhancement: Aligned the "Add Risk account" table under the Risk User
Bug Fix: Taker Config Feeder displaying incorrect information
Bug Fix: Monitoring page getting stuck after clicking Dividends Completed Jobs

10/28/202
3
UTC
v1.0.2 Enhancement: Text Style, Sidebar, and Filtrations
Enhancement: Hide components and columns that are no longer supported (Exposure Multiplier, Asset
Class Group and Markets)
Enhancement: Detailed leg report with Total USD
Enhancement: Action Scheduler Wizard
Enhancement: Color Indicator under Alerts Status Page
Enhancement: Redesigned Risk Account Selection for Risk Users
Enhancement: Edited Values Highlights
Bug Fix: Restart Email for Brokers
Bug Fix: UI crashes due to Popovers
Bug Fix: Password Reset Page

10/21/202
3
UTC
v1.0.1 New Feature: Trading Risk UI is now available for Broker-Clients
New Feature: Added "Delete" confirmation to all components when deleting an item or settings
Enhancement: Redesigned Risk Account Selection for Risk Users
Bug Fix: Closing Position from Trading Risk UI using Taker Symbol


10/14/202
3
UTC
v1.0.0 New Feature: New Report: Detailed Leg Report
New Feature: Broker-Read-Only Access
New Feature: Default Maker Column in Liquidity Model for newly added symbol
Enhancement: Liquidity model is no longer allowing Bbook as a Maker
Enhancement: Renamed "Maker Sessions" as "Makers"
Enhancement: Maker Scaling is no longer allowing Security as a Symbol
Enhancement: Auto re-sizing of monitoring logs windows
Enhancement: Added scrollbar within monitoring logs folder
Bug Fix: Fixed "Save All" action
Bug Fix: Fixed book construction mode selection
Bug Fix: Trading Platform - One Click Trading


