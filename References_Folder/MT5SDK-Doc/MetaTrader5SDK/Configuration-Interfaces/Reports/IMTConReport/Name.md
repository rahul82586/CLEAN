[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / Name

[Previous](Clear.md) | [Next](Server.md)

# IMTConReport::Name

Get the name of a report.

C++
    
    
    LPCWSTR  IMTConReport::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConReport.Name()

Python (Manager API)
    
    
    MTConReport.Name

### Return Value

If successful, it returns a pointer to a string with the name of a report. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConReport](../IMTConReport.md) object.

# IMTConReport::Name

Set the name of a report.

C++
    
    
    MTAPIRES  IMTConReport::Name(
       LPCWSTR  name      // Report name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.Name(
       srting   name      // Report name
       )

Python (Manager API)
    
    
    MTConReport.Name

### Parameters

**name**  
[in] The name of a report.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum name length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
