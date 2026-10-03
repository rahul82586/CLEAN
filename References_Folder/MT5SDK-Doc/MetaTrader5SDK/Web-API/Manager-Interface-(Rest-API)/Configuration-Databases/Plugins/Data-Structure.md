[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Plugins](../Plugins.md) / Data Structure

[Previous](../Plugins.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

The plugin configuration is passed in JSON format in response to the [/api/plugin/add](Add.md), [/api/plugin/next](Get-by-Index.md) and [/api/plugin/get](Get-by-Name.md) requests.

Parameter | Type | Purpose  
Name | String | The name of the plugin configuration.  
Server | String | The identifier of the server for which the configuration is configured.  
Module | String | The name of the plugin module.  
Enable | Integer | Configuration status. Passed as a value of the [EnPluginMode (#enpluginmode)](../../../../Configuration-Interfaces/Plugins/IMTConPlugin/Enumerations.md#enpluginmode) enumeration.  
Flags |  | Plugin operation flags. Passed using the [EnPluginFlags (#enpluginflags)](../../../../Configuration-Interfaces/Plugins/IMTConPlugin/Enumerations.md#enpluginflags) enumeration.  
Params | Array | [Plugin parameters (#param)](Data-Structure.md#param).  
  
<a id="param"></a>
## Plugin parameters (#param)

Parameter | Type | Purpose  
Type | Integer | Parameter type. Passed as a value of the [ParamType](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Enumerations.md) enumeration.  
Name | Integer | Parameter name.  
Value | String | The value of the parameter.  
  
<a id="module"></a>
## Plugin module parameters (#module)

Methods | Type | Purpose  
Server | Integer | The ID of the server, on which the dll-module of the plugin is stored physically.  
Module | String | The name of the plugin module.  
Version | Integer | Report module version.  
VersionAPI | Integer | The version of the Server API with which the module is compiled.  
Name | String | The plugin name which is inserted by default to a configuration when this module is selected.  
Copyright | String | Copyright of the report module.  
Description | String | Report module description.  
Path | String | Path to the plugin file relative to the /plugins directory on the server.  
Params | Array | [Plugin module parameters (#param)](Data-Structure.md#param).
