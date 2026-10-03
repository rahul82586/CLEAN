[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Main Interface of Reports](../Main-Interface-of-Reports.md) / Common Functions

[Previous](Enumerations.md) | [Next](Common-Functions/Allocate.md)

# Common Functions

The common functions of the MetaTrader 5 Report API include general purpose functions that do not manage any of the platform configurations or information on the server, but are required for writing a plugin.

## Memory Management

MetaTrader 5 Report API allows managing the memory used by modules.

Function | Purpose  
---|---  
[Allocate](Common-Functions/Allocate.md) | Memory allocation by areports module.  
[Free](Common-Functions/Free.md) | Free memory allocated previously using the Allocate method.  
  
## Journal

MetaTrader 5 Report API provides access to server logs allowing to output records in them and save that records on the hard drive.

Function | Purpose  
---|---  
[LoggerOut](Common-Functions/LoggerOut.md) | Log messages.  
[LoggerOutString](Common-Functions/LoggerOutString.md) | Quick output of unformatted stings to the journal.  
[LoggerFlush](Common-Functions/LoggerFlush.md) | Flush the file buffer of the journal to a disk.  
[LoggerRequest](Common-Functions/LoggerRequest.md) | Request the journal of the trade server where the module is running.  
  
## Service Functions

The following additional functions are available in the MetaTrader 5 Report API:

Function | Purpose  
---|---  
[About](Common-Functions/About.md) | Quickly receive the description of the server on which the module is running.  
[LicenseCheck](Common-Functions/LicenseCheck.md) | Check the module license.  
[Clear](Common-Functions/Clear.md) | Clear the object.  
[IsStopeed](Common-Functions/IsStopeed.md) | Check the presence of the request to stop a report generation.
