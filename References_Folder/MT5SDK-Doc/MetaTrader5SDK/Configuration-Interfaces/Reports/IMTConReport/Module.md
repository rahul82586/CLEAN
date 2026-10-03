[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / Module

[Previous](Server.md) | [Next](Mode.md)

# IMTConReport::Module

Get the name of a report module.

C++
    
    
    LPCWSTR  IMTConReport::Module()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConReport.Module()

Python (Manager API)
    
    
    MTConReport.Module

### Return Value

If successful, it returns a pointer to a string with the name of a report module. Otherwise, it returns NULL.

### Note

It returns the name of the module (DLL) that corresponds to the report.

# IMTConReport::Module

Set the name of a report module.

C++
    
    
    MTAPIRES  IMTConReport::Module(
       LPCWSTR  name      // The name of the report module
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.Module(
       string   name      // The name of the report module
       )

Python (Manager API)
    
    
    MTConReport.Module

### Parameters

**name**  
[in] The name of a report module.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
