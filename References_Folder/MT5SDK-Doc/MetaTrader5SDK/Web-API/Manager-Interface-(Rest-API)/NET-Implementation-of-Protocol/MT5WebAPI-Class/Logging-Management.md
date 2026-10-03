[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../MT5WebAPI-Class.md) / Logging Management

[Previous](Connect-Disconnect/Ping.md) | [Next](Logging-Management/IsWriteDebugLog.md)

# Manage Logging

In the .NET implementation of the Web API, messages about Web actions appear on the common journal of a project (site). A pointer to the logging function is passed in the [MT5WebAPI class constructor](Constructor.md).

This section describes the methods for managing logging:

Method | Purpose  
---|---  
[IsWriteDebugLog](Logging-Management/IsWriteDebugLog.md) | Get and set the mode of output of debug messages in the Web API journal.
