[🏠 Document Start](../README.md) / [Server API](README.md) / Debugging

[Previous](Recommendations-for-Developers.md) | [Next](Ready-made-Examples.md)

# Debugging

All components of the MetaTrader 5 trading platform are reliably protected and do not permit connection in debug mode. In order to facilitate the plugin development and debugging, the special debug (developer) versions of trade and history servers are available. They have functional limitations and cannot be used for real work but allow you to debug plugins instead.

## Dev server limitations

  * The same master password "Trader" and investor password "Invest" is used for all accounts including manager ones. The password that is actually set for an account will not be accepted by the server. For example, if the account master password is "abc123", you should use "Trader" instead; if the account investor password is "def456", you should use "Invest" instead.
  * The "Manager" password is always used for [connections via Web API (#account-setup)](../Web-API/Getting-Started.md#account-setup), regardless of the password actually set for the account.
  * [Extended authorization](https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization) via SSL certificates and [one-time passwords](https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/server_connect/otp) (OTP) are disabled. Even if these functions are enabled, only the Trader password can be used for authorization.
  * No [account import](https://support.metaquotes.net/en/docs/mt5/platform/migration/migration_account_trade) either from MetaTrader 4, or from MetaTrader 5.
  * Crash logs are disabled.



## Where to find the dev servers

The dev servers are distributed similarly to other components — when updating via LiveUpdate and in the installers. The executable files are placed near the server main files:

  * mt5trade64.dev.exe — dev version in the trade server installation directory.
  * mt5history64.dev.exe — dev version in the history server installation directory.



## How to debug plugins

First, compile a plugin in debug mode and copy its DLL file to the \plugins directory of the trade or history server. Next, enable the plugin via MetaTrader 5 Administrator.

![Enabling a plugin in MetaTrader 5 Administrator](images/debug_plugin_config.png)

[Profiling (#profiling)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_plugins#profiling) can be of use at this stage in order to evaluate the plugin performance. The server collects its operation statistics and sends it to the journal every 5 minutes.

After enabling the plugin, open its project in Microsoft Visual Studio and go to the debugging settings: Debug -> project properties. Specify the following parameters:

  * Command — path to the debug server
  * Command Arguments — /console for running in console mode
  * Working Directory — path to the server directory



![Setting up a plugin project for debugging in Microsoft Visual Studio](images/debug_studio_settings.png)

Now you can start debugging.

> Do not forget to re-compile the plugin and copy its new version to the \plugins directory of the server after changing the source code.
