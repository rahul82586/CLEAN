[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Data Feeds](../../Data-Feeds.md) / [IMTConFeederModule](../IMTConFeederModule.md) / ParameterGet

[Previous](ParameterNext.md) | [Next](../IMTConFeederTranslate.md)

# IMTConFeederModule::ParameterGet

Get the parameter of the data feed module by name.

C++
    
    
    MTAPIRES  IMTConFeederModule::ParameterGet(
       LPCWSTR       name,      // Parameter name
       IMTConParam*  param      // An object of a data feed parameter
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFeederModule.ParameterGet(
       string        name,      // Parameter name
       CIMTConParam  param      // An object of a data feed parameter
       )

Python (Manager API)
    
    
    MTConFeederModule.ParameterGet(
       name          # Parameter name
       )

### Parameters

**name**  
[in] Parameter Name.

**param**  
[out] The object of a data feed parameter. The 'param' object must first be created using theIMTAdminAPI::FeederParamCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The [IMTConParam::Name()](../../Additional-Parameters/IMTConParam/Name.md) value is used as the parameter name.
