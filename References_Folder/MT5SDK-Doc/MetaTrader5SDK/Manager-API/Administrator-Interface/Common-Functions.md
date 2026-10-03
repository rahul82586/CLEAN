[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Administrator Interface](../Administrator-Interface.md) / Common Functions

[Previous](../Administrator-Interface.md) | [Next](Common-Functions/Allocate.md)

# Common Functions

The common functions of the [IMTAdminAPI](../Administrator-Interface.md) interface include general purpose functions that do not control any of the platform configurations or information on the server, but are required for developing applications.

## Memory Management

The MetaTrader 5 Manager API allows managing the memory used by applications.

Function | Purpose  
---|---  
[Allocate](Common-Functions/Allocate.md) | Memory allocation by an application.  
[Free](Common-Functions/Free.md) | Free memory allocated previously using the Allocate method.  
  
## Journal

The MetaTrader 5 Manager API provides access to server logs. The API includes functions for working with the logs. The [IMTAdminAPI](../Administrator-Interface.md) interface allows to output messages in the log, as well as to request logs of the server, data feeds and gateways.

Function | Purpose  
---|---  
[LoggerOut](Common-Functions/LoggerOut.md) | Log messages.  
[LoggerOutString](Common-Functions/LoggerOutString.md) | Fast output method which prints unformatted logs to the Administrator API local journal.  
[LoggerFlush](Common-Functions/LoggerFlush.md) | Flush the file buffer of the server journal to a disk.  
[LoggerServerRequest](Common-Functions/LoggerServerRequest.md) | Request the server logs.  
[LoggerGatewayRequest](Common-Functions/LoggerGatewayRequest.md) | Request the gateway logs.  
[LoggerFeederRequest](Common-Functions/LoggerFeederRequest.md) | Request the logs of data feeds.  
  
The MetaTrader 5 Manager API contains a number of constants for working with logs. They are described in a [separate section](../../Journal-Constants/README.md).

## Service Functions

The following additional functions are available in the MetaTrader 5 Manager API:

Function | Purpose  
---|---  
[Release](Common-Functions/Release.md) | Delete the IMTAdminAPI object.  
[LicenseCheck](Common-Functions/LicenseCheck.md) | Check the application license.  
[PasswordChange](Common-Functions/PasswordChange.md) | Change password of an account that is used to connect the application to the server.
