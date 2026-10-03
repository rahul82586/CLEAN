[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / Data Structure

[Previous](../Reports.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

The report configuration is passed in JSON format in response to the [/api/report/add](Add.md), [/api/report/next](Get-by-Index.md) and [/api/report/get](Get-by-Name.md) requests.

Parameter | Type | Purpose  
Name | String | The name of the report configuration.  
Server | String | The identifier of the server for which the report is set.  
Template | String | Report name from the module.  
Enable | Integer | Configuration status. Passed as a value of the [EnReportMode (#enreportmode)](../../../../Configuration-Interfaces/Reports/IMTConReport/Enumerations.md#enreportmode) enumeration.  
Params | Array | [Report parameters (#param)](Data-Structure.md#param).  
  
<a id="param"></a>
## Report parameters (#param)

Parameter | Type | Purpose  
Type | Integer | Parameter type. Passed as a value of the [ParamType](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Enumerations.md) enumeration.  
Name | Integer | Parameter name.  
Value | String | The value of the parameter.  
  
<a id="module"></a>
## Report module parameters (#module)

Methods | Type | Purpose  
Server | Integer | The ID of the server, on which the dll-module of the report is stored physically.  
Name | String | The report name which is inserted by default to a configuration when this module is selected.  
Filename | String | The name of the report module file.  
Copyright | String | Copyright of the report module.  
Description | String | Report module description.  
Version | Integer | Report module version.  
VersionAPI | Integer | The version of the Report API with which the module is compiled.  
VersionIe | Integer | The minimum version of the Internet Explorer required for the module of reports.  
Timeout | Integer | The time period in seconds during which the report remains relevant.  
Types | Integer | Report types supported by the module. Passed as a value of the [EnTypes (#entypes)](../../../../Configuration-Interfaces/Reports/IMTConReportModule/Enumerations.md#entypes) enumeration.  
Snapshots | Integer | Modes of database snapshots required for the operation of the report module. Passed as a value of the [EnSnapshots (#ensnapshots)](../../../../Configuration-Interfaces/Reports/IMTConReportModule/Enumerations.md#ensnapshots) enumeration.  
ParamsConfig | Array | Report module [parameters (#param)](Data-Structure.md#param).  
ParamsRequest | Array | Available [parameters (#param)](Data-Structure.md#param) when requesting a report via the MetaTrader 5 Manager terminal.
