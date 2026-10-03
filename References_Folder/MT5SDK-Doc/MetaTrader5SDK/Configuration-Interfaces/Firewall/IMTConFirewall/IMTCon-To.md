[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewall](../IMTCon.md) / IMTCon To

[Previous](IMTCon-From.md) | [Next](IMTCon-Comment.md)

# IMTConFirewall::To

Get the end of the range of IP addresses to which the firewall rule is applied.

C++
    
    
    LPCWSTR  IMTConFirewall::To()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFirewall.To()

Python (Manager API)
    
    
    MTConFirewall.To

### Return Value

If successful, returns a pointer to a string with the last IP address of the range. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFirewall](../IMTCon.md) object.

# IMTConFirewall::To

Set the end of the range of IP addresses to which the firewall rule is applied.

C++
    
    
    MTAPIRES  IMTConFirewall::To(
       LPCWSTR  value      // End of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFirewall.To(
       string   value      // End of the range
       )

Python (Manager API)
    
    
    MTConFirewall.To

### Parameters

**value**  
[in] The last IP address of the range to which the firewall rule is applied.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the address is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
