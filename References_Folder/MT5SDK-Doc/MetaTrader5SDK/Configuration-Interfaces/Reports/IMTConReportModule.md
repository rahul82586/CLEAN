[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Reports](../Reports.md) / IMTConReportModule

[Previous](IMTConReport/ParameterGet.md) | [Next](IMTConReportModule/Enumerations.md)

# IMTConReportModule

The IMTConReportModule class contains methods for getting and changing parameters of report modules:

Methods | Purpose  
---|---  
[Release](IMTConReportModule/Release.md) | Delete the current object.  
[Assign](IMTConReportModule/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConReportModule/Clear.md) | Clear an object.  
[Name](IMTConReportModule/Name.md) | Get the report name, which is inserted by default to a configuration when selecting this module.  
[Vendor](IMTConReportModule/Vendor.md) | Get the name of the report module provider.  
[Description](IMTConReportModule/Description.md) | Get the description of a report module.  
[Module](IMTConReportModule/Module.md) | Get the name of the file of a report module.  
[Index](IMTConReportModule/Index.md) | Get the report index in a module.  
[Server](IMTConReportModule/Server.md) | Get the ID of the server on which the module is installed.  
[Version](IMTConReportModule/Version.md) | Get the version of a report module.  
[VersionAPI](IMTConReportModule/VersionAPI.md) | Get the version of the Report API.  
[VersionIE](IMTConReportModule/VersionIE.md) | Get the minimum version of the Internet Explorer required for the module of reports.  
[Types](IMTConReportModule/Types.md) | Get the types of reports supported by the module.  
[Snapshots](IMTConReportModule/Snapshots.md) | Get the modes of database snapshots required for the module of reports.  
[ParameterTotal](IMTConReportModule/ParameterTotal.md) | It returns the number of parameters of a report module.  
[ParameterNext](IMTConReportModule/ParameterNext.md) | Get report module parameters by the index.  
[ParameterGet](IMTConReportModule/ParameterGet.md) | Get a report module parameter by its name.  
[InputTotal](IMTConReportModule/InputTotal.md) | Get the total number of the parameters that can be set when requesting reports of the module from a manager terminal.  
[InputNext](IMTConReportModule/InputNext.md) | Get the parameter of a report request by the index.  
[InputGet](IMTConReportModule/InputGet.md) | Get the parameter of a report request by the name.  
  
The IMTConReportModule contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnSnapshots (#ensnapshots)](IMTConReportModule/Enumerations.md#ensnapshots) | Modes of database snapshots.  
[EnTypes (#entypes)](IMTConReportModule/Enumerations.md#entypes) | Types of supported reports.
