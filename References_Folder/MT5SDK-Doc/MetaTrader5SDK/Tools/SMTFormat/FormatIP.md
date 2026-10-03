[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatIP

[Previous](FormatTimeMsc.md) | [Next](FormatPositionType.md)

# SMTFormat::FormatIP

Format an IP address (IPv4) and a port to a string.
    
    
    static LPCWSTR  SMTFormat::FormatIP(
       CMTStr      &str,       // Reference to a string object
       const UINT  ip,         // IP address
       const UINT  port=0      // Port
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**ip**  
[in] IP address (IPv4) in the form of a UINT number.

**port=0**  
[in] Port number. This parameter is optional.

### Return Value

Returns a constant pointer to a string in the str object.

# SMTFormat::FormatIP

Format an IP address (IPv6) and a port to a string.
    
    
    static LPCWSTR  SMTFormat::FormatIP(
       CMTStr         &str,       // Reference to a string object
       const USHORT   *ip,        // IP address
       const UINT     port=0      // Port
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**ip**  
[in] A pointer to the IP address (IPv6) in the form of a USHORT number.

**port=0**  
[in] Port number. This parameter is optional.

### Return Value

Returns a constant pointer to a string in the str object.
