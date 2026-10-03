[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Data Feeds](../Data-Feeds.md) / IMTConFeederModule

[Previous](IMTConFeeder/StateTrafficOut.md) | [Next](IMTConFeederModule/Enumerations.md)

# IMTConFeederModule

The IMTConFeederModule interface contains methods for managing parameters of the data feed modules.

Method | Purpose  
---|---  
[Release](IMTConFeederModule/Release.md) | Delete the current object.  
[Assign](IMTConFeederModule/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConFeederModule/Clear.md) | Clear an object.  
[Name](IMTConFeederModule/Name.md) | Get the data feed name, which is inserted by default to a configuration when selecting this module.  
[Vendor](IMTConFeederModule/Vendor.md) | Get the name of the provider of the data feed module.  
[Description](IMTConFeederModule/Description.md) | Get the description of the data feed module.  
[Module](IMTConFeederModule/Module.md) | Get the name of the file of the data feed module.  
[FeedServer](IMTConFeederModule/FeedServer.md) | Get the default address of the server to which the data feed module will connect.  
[FeedLogin](IMTConFeederModule/FeedLogin.md) | Get a default login that will be used by a data feed to connect to the server.  
[FeedPassword](IMTConFeederModule/FeedPassword.md) | Get a default password that will be used by a data feed to connect to the server.  
[Version](IMTConFeederModule/Version.md) | Get the version of the data feed module.  
[Modes](IMTConFeederModule/Modes.md) | Get the available modes of data feed operation.  
[Fields](IMTConFeederModule/Fields.md) | Get the editable fields of a data feed.  
[ParameterTotal](IMTConFeederModule/ParameterTotal.md) | Get the number of parameters of a data feed module.  
[ParameterNext](IMTConFeederModule/ParameterNext.md) | Get parameters of a data feed module by the index.  
[ParameterGet](IMTConFeederModule/ParameterGet.md) | Get the parameter of the data feed module by name.  
  
The IMTConFeederModule class contains one enumeration:

Enumeration | Purpose  
---|---  
[EnFeedersFieldFlags](IMTConFeederModule/Enumerations.md) | Flags of editable fields.
