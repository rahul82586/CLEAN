[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Firewall](../../Firewall.md) / [IMTConFirewall](../IMTCon.md) / IMTCon Comment

[Previous](IMTCon-To.md) | [Next](../IMTConSink.md)

# IMTConFirewall::Comment

Get a comment to the firewall rule.

C++
    
    
    LPCWSTR  IMTConFirewall::Comment()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFirewall.Comment()

Python (Manager API)
    
    
    MTConFirewall.Comment

### Return Value

If successful, it returns a pointer to a string with a comment to the rule. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFirewall](../IMTCon.md) object.

# IMTConFirewall::Comment

Set a comment to the firewall rule.

C++
    
    
    MTAPIRES  IMTConFirewall::Comment(
       LPCWSTR  comment      // Comment
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFirewall.Comment(
       srting   comment      // Comment
       )

Python (Manager API)
    
    
    MTConFirewall.Comment

### Parameters

**comment**  
[in] A comment to the firewall rule.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum comment length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
