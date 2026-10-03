[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / ReportsSMTP

[Previous](ReportsEmail.md) | [Next](ReportsSMTPLogin.md)

# IMTConGroup::ReportsSMTP

Get the address of the SMTP server for sending reports.

C++
    
    
    LPCWSTR  IMTConGroup::ReportsSMTP()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.ReportsSMTP()

Python (Manager API)
    
    
    MTConGroup.ReportsSMTP

### Return Value

If successful, it returns a pointer to a string with the address of the SMTP server. Otherwise, it returns NULL.

### Note

The method is obsolete and is no longer used. It always returns an empty line. Please use [IMTConGroup::ReportsEmail](ReportsEmail.md) instead.

# IMTConGroup::ReportsSMTP

Set the address of the SMTP server for sending reports.

C++
    
    
    MTAPIRES  IMTConGroup::ReportsSMTP(
       LPCWSTR  catalog      // Server address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.ReportsSMTP(
       string   catalog      // Server address
       )

Python (Manager API)
    
    
    MTConGroup.ReportsSMTP

### Parameters

**catalog**  
[in] Address of SMTP server for sending reports.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used. It always returns [MT_RET_OK](../../../Return-Codes/Successful-completion.md). Please use [IMTConGroup::ReportsEmail](ReportsEmail.md) instead.
