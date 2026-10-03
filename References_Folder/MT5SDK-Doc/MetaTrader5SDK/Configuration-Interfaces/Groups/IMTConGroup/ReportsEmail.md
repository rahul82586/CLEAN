[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / ReportsEmail

[Previous](ReportsFlags.md) | [Next](ReportsSMTP.md)

# IMTConGroup::ReportsEmail

Get the mail server which is used for sending reports to clients in the group.

C++
    
    
    LPCWSTR  IMTConGroup::ReportsEmail()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.ReportsEmail()

Python (Manager API)
    
    
    MTConGroup.ReportsEmail

### Return Value

If successful, it returns a pointer to a string with the mail server configuration name. If a default mail server is set for the group, an empty string is returned. NULL is returned if there is an error.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGroup](../IMTConGroup.md) object.

# IMTConGroup::ReportsEmail

Set the mail server to be used for sending reports to clients in the group.

C++
    
    
    MTAPIRES  IMTConGroup::ReportsEmail(
       LPCWSTR  email        // Mail server
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.ReportsEmail(
       string   email        // Mail server
       )

Python (Manager API)
    
    
    MTConGroup.ReportsEmail

### Parameters

**catalog**  
[in] Mail server configuration name. To set the default mail server, pass in an empty string.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum server address length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
