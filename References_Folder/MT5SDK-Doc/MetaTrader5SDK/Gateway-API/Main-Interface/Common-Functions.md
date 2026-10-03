[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Main Interface](../Main-Interface.md) / Common Functions

[Previous](Enumerations.md) | [Next](Common-Functions/Allocate.md)

# Common Functions

The common functions of the MetaTrader 5 Gateway API include general purpose functions that do not manage any of the settings or data but are required for writing a gateway.

## Memory Management

The MetaTrader 5 Gateway API allows managing the memory used by applications.

Function | Purpose  
---|---  
[Allocate](Common-Functions/Allocate.md) | Memory allocation by an application.  
[Free](Common-Functions/Free.md) | Free memory allocated previously using the Allocate method.  
  
## Journal

MetaTrader 5 Report API provides access to server logs allowing to output records in them and save that records on the hard drive.

Function | Purpose  
---|---  
[LoggerOut](Common-Functions/LoggerOut.md) | Log messages.  
[LoggerOutString](Common-Functions/LoggerOutString.md) | Quick output of unformatted stings to the journal.  
[LoggerFlush](Common-Functions/LoggerFlush.md) | Flush the file buffer of the journal to a disk.  
  
## Service Functions

The following additional functions are available in the MetaTrader 5 Gateway API:

Function | Purpose  
---|---  
[Release](Common-Functions/Release.md) | Delete an object.  
[LicenseCheck](Common-Functions/LicenseCheck.md) | A function for checking the gateway/data feed usage license.
