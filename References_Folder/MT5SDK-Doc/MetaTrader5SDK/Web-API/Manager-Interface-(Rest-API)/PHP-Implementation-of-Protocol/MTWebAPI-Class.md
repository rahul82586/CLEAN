[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../PHP-Implementation-of-Protocol.md) / MTWebAPI Class

[Previous](../PHP-Implementation-of-Protocol.md) | [Next](MTWebAPI-Class/ConnectDisconnect.md)

# MTWebAPI Class

the implementation of protocol in PHP, all the Web API commands are called through the methods of the MTWebAPI class (file mt5_api.php). Description of the methods of this class is divided into the following sections:

  * [Connect/Disconnect](MTWebAPI-Class/ConnectDisconnect.md)
  * [Manage Logging](MTWebAPI-Class/Logging-Management.md)
  * [Service Commands](MTWebAPI-Class/Service-Commands.md)
  * [Common Configuration](MTWebAPI-Class/Common-Configuration.md)
  * [Timing](MTWebAPI-Class/Timing.md)
  * [Groups](MTWebAPI-Class/Groups.md)
  * [Symbols](MTWebAPI-Class/Symbols.md)
  * [Clients](MTWebAPI-Class/Clients.md)
  * [Orders](MTWebAPI-Class/Orders.md)
  * [Deals](MTWebAPI-Class/Deals.md)
  * [Positions](MTWebAPI-Class/Positions.md)
  * [Trade](MTWebAPI-Class/Trade.md)
  * [Mailbox](MTWebAPI-Class/Mailbox.md)
  * [News Event](MTWebAPI-Class/News-Event.md)
  * [Prices](MTWebAPI-Class/Prices.md)
  * [Custom Commands](MTWebAPI-Class/Custom-Commands.md)



> To begin using the methods of the MTWebAPI class, just include the mt5_api.php file into your PHP project.

## The Structure of the Protocol Implementation Files

The protocol implementation files are located in the /Examples/PHP/mt5_api/ subfolder of the [Web API installation](../../../Getting-Started/Setup.md) directory. It contains the following files:

  * mt5_api.php — the MTWebAPI class that describes calls of the Web API commands.
  * mt5_auth.php — implementation of the authorization process.
  * mt5_common.php — implementation of receiving common configuration.
  * mt5_connect.php — implementation of connection/disconnection of the Web client.
  * mt5_cryptaes256.php — implementation of encryption of data transmitted.
  * mt5_custom.php — implementation of function for sending custom commands.
  * mt5_deal.php — implementation of functions for working with deals.
  * mt5_group.php — implementation of receiving client groups configurations.
  * mt5_history.php — implementation of functions for working with orders.
  * mt5_logger.php — implementation of journal functions.
  * mt5_mail.php — implementation of functions for working with mail.
  * mt5_news.php — implementation of functions for working with news.
  * mt5_ping.php — implementation of function for maintaining of connection.
  * mt5_protocol.php — description of constants and header of messages.
  * mt5_retcode.php — description of return codes.
  * mt5_symbol.php — implementation of receiving symbol configurations.
  * mt5_tick.php — implementation of receiving of price data.
  * mt5_time.php — implementation of receiving time settings.
  * mt5_user.php — implementation of functions for working with users.
  * mt5_utils.php — implementation of common functions.


