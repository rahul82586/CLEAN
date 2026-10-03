[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / Common Functions

[Previous](../Main-API-Interface.md) | [Next](Common-Functions/Allocate.md)

# Common Functions

The common functions of the MetaTrader 5 Server API include general purpose functions that do not manage any of the platform configurations or information on the server, but are required for writing a plugin.

## Memory Management

The MetaTrader 5 Server API allows managing the memory used by plugins. Recommendations for memory management are given in the [appropriate section (#memory-manage)](../Recommendations-for-Developers.md#memory-manage).

Function | Purpose  
---|---  
[Allocate](Common-Functions/Allocate.md) | Memory allocation by a server plugin.  
[Free](Common-Functions/Free.md) | Free memory allocated previously using the Allocate method.  
  
## Journal

The MetaTrader 5 Server API provides access to server logs. The API includes functions for working with the logs. Currently only the functions for message logging and saving them to a hard disk are supported. Further new functions for log analyzing will be added.

Function | Purpose  
---|---  
[LoggerOut](Common-Functions/LoggerOut.md) | Logging messages.  
[LoggerOutString](Common-Functions/LoggerOutString.md) | Output unformatted stings to the server journal (quick output).  
[LoggerRequest](Common-Functions/LoggerRequest.md) | Request the server logs.  
[LoggerFlush](Common-Functions/LoggerFlush.md) | Flush the file buffer of the journal to a disk.  
  
## Service Functions

The following additional functions are available in the MetaTrader 5 Server API:

Function | Purpose  
---|---  
[About](Common-Functions/About.md) | Quickly receive the description of the server on which the plugin is running.  
[LicenseCheck](Common-Functions/LicenseCheck.md) | Check the plugin license.
