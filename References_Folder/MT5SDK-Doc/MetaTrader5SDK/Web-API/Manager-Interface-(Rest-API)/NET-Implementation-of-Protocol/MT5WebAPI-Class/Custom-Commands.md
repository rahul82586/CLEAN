[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../MT5WebAPI-Class.md) / Custom Commands

[Previous](Prices/TickStat.md) | [Next](Custom-Commands/CustomSend.md)

# Custom Commands

The Web API protocol is [extensible](../../../Protocol-Extension.md). The protocol implementation in .NET includes methods for sending custom commands to the server.

> Custom Web API commands can be handled using a server plugin created with the MetaTrader 5 Server API. For this purpose, the Server API provides a special hook [IMTCustomSink::HookWebAPICommand](../../../../Server-API/Interface-of-Custom-Events/HookWebAPICommand.md). A detailed description of how custom commands are handled is provided in the MetaTrader 5 Server API documentation.

The [MT5WebAPI.CustomSend](Custom-Commands/CustomSend.md) method is used for sending custom commands.
