[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerAccess](../IMTConManagerAccess.md) / To

[Previous](From.md) | [Next](../IMTConManagerReport.md)

# IMTConManagerAccess::To

Get the end of the range of IP addresses, from which a manager account can connect.

C++
    
    
    LPCWSTR  IMTConManagerAccess::To()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConManagerAccess.To()

Python (Manager API)
    
    
    MTConManagerAccess.To

### Return Value

If successful, returns a pointer to a string with the last IP address of the range. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConManagerAccess](../IMTConManagerAccess.md) object.

# IMTConManagerAccess::To

Set the end of the range of IP addresses, from which a manager account can connect.

C++
    
    
    MTAPIRES  IMTConManagerAccess::To(
       LPCWSTR  value      // End of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManagerAccess.To(
       srting   value      // End of the range
       )

Python (Manager API)
    
    
    MTConManagerAccess.To

### Parameters

**value**  
[in] The last IP address of the range of allowed addresses.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the address is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
