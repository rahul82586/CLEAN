[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Plugins](../../Plugins.md) / [IMTConPlugin](../IMTConPlugin.md) / ParameterGet

[Previous](ParameterNext.md) | [Next](../IMTConPluginModule.md)

# IMTConPlugin::ParameterGet

Get the plugin parameter by the name.

C++
    
    
    MTAPIRES  IMTConPlugin::ParameterGet(
       LPCWSTR       name,      // Parameter name
       IMTConParam*  param      // An object of the plugin parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConPlugin.ParameterGet(
       string        name,      // Parameter name
       CIMTConParam  param      // An object of the plugin parameter
       )

Python (Manager API)
    
    
    MTConParam  MTConPlugin.ParameterGet(
       str           name       # Parameter name
       )
    
    
    list[MTConParam]  MTConPlugin.ParameterGet()

### Parameters

**name**  
[in] Parameter Name.

**param**  
[out] An object of the plugin parameter. The param object must first be created using theIMTAdminAPI::PluginParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConParam::Name()](../../Additional-Parameters/IMTConParam/Name.md) value is used as the parameter name.
