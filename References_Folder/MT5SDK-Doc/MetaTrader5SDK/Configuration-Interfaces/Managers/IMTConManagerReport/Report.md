[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerReport](../IMTConManagerReport.md) / Report

[Previous](Clear.md) | [Next](Permissions.md)

# IMTConManagerReport::Report

Get the name and path to the report for which access is being configured.

C++
    
    
    LPCWSTR  IMTConManagerReport::Report()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConManagerReport.Report()

Python (Manager API)
    
    
    MTConManagerReport.Report

### Return Value

If successful, a pointer to a string with the name and path to the report is returned. Otherwise NULL is returned.

### Note

A pointer to the result string is valid for the lifetime of the [IMTConManagerReport](../IMTConManagerReport.md) object.

# IMTConManagerReport::Report

Set the name and path to the report for which access is being configured.

C++
    
    
    MTAPIRES  IMTConManagerReport::Report(
       LPCWSTR  name      // Report name and path
       )

.NET (Gateway/Manager API)
    
    
    MTRetCoe  CIMTConManagerReport.Report(
       string   name      // Report name and path
       )

Python (Manager API)
    
    
    MTConManagerReport.Report

### Parameters

**name**  
[in] Report name and path. Equal to the value ofIMTConReport::Name.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.

### Note

The name and path length is limited to 32 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
