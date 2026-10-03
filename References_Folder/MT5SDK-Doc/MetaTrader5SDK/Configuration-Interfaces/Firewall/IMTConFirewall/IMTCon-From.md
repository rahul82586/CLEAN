[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewall](../IMTCon.md) / IMTCon From

[Previous](IMTCon-Action.md) | [Next](IMTCon-To.md)

# IMTConFirewall::From

Get the beginning of the range of IP addresses to which the firewall rule is applied.

C++
    
    
    LPCWSTR  IMTConFirewall::From()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFirewall.From()

Python (Manager API)
    
    
    MTConFirewall.From

### Return Value

If successful, returns a pointer to a string with the first IP address of the range. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFirewall](../IMTCon.md) object.

# IMTConFirewall::From

Set the beginning of the range of IP addresses to which the firewall rule is applied.

C++
    
    
    MTAPIRES  IMTConFirewall::From(
       LPCWSTR  name      // Beginning of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFirewall.From(
       string   name      // Beginning of the range
       )

Python (Manager API)
    
    
    MTConFirewall.From

### Parameters

**name**  
[in] The first IP address of the range to which the firewall rule is applied.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the address is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
