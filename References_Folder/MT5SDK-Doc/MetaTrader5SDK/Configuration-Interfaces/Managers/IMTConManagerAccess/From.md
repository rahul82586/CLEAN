[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerAccess](../IMTConManagerAccess.md) / From

[Previous](Clear.md) | [Next](To.md)

# IMTConManagerAccess::From

Get the beginning of the range of IP addresses, from which a manager account can connect.

C++
    
    
    LPCWSTR  IMTConManagerAccess::From()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConManagerAccess.From()

Python (Manager API)
    
    
    MTConManagerAccess.From

### Return Value

If successful, returns a pointer to a string with the first IP address of the range. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConManagerAccess](../IMTConManagerAccess.md) object.

# IMTConManagerAccess::From

Set the beginning of the range of IP addresses, from which a manager account can connect.

C++
    
    
    MTAPIRES  IMTConManagerAccess::From(
       LPCWSTR  name      // Beginning of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCoe  CIMTConManagerAccess.From(
       string   name      // Beginning of the range
       )

Python (Manager API)
    
    
    MTConManagerAccess.From

### Parameters

**name**  
[in] The first IP address of the range of allowed addresses.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the address is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
