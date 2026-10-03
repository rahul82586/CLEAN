[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / ParameterUpdate

[Previous](ParameterAdd.md) | [Next](ParameterDelete.md)

# IMTConReport::ParameterUpdate

Update the parameter of a report in the list.

C++
    
    
    MTAPIRES  IMTConReport::ParameterUpdate(
       const UINT          pos,       // Position of the parameter
       const IMTConParam*  param      // An object of the report parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.ParameterUpdate(
       uint                pos,       // Position of the parameter
       CIMTConParam        param      // An object of the report parameter
       )

Python (Manager API)
    
    
    MTConReport.ParameterUpdate(
       pos,                # Position of the parameter
       param               # An object of the report parameter
       )
    
    
    MTConReport.ParameterSet(
       parameter_list      # A list of report parameters
       )

### Parameters

**pos**  
[in] Position of the parameter, starting with 0.

**param**  
[in] An object of a report parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
