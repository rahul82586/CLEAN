[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../MTWebAPI-Class.md) / Custom Commands

[Previous](Prices/TickStat.md) | [Next](Custom-Commands/CustomSend.md)

# Custom Commands

The Web API protocol is [extensible](../../../Protocol-Extension.md). The implementation of the protocol in PHP includes a method for sending custom commands to the server.

> Custom Web API commands can be handled using a server plugin created with the MetaTrader 5 Server API. For this purpose, the Server API provides a special hook [IMTCustomSink::HookWebAPICommand](../../../../Server-API/Interface-of-Custom-Events/HookWebAPICommand.md). A detailed description of how custom commands are handled is provided in the MetaTrader 5 Server API documentation.

The [MTWebAPI::CustomSend](Custom-Commands/CustomSend.md) method is used for sending custom commands.
