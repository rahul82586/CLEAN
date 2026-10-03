[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatPositionType

[Previous](FormatIP.md) | [Next](FormatOrderType.md)

# SMTFormat::FormatPositionType

Format the type of a position in a string with a text description.
    
    
    static LPCWSTR  SMTFormat::FormatPositionType(
       CMTStr      &str,     // Reference to a string object
       const UINT  type      // Position type
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**type**  
[in] Position type. Specified by a value of theIMTPosition::EnPositionActionenumeration:

  * IMTPosition::POSITION_BUY \- "buy";
  * IMTPosition::POSITION_SELL \- "sell".



### Return Value

Returns a constant pointer to a string in the str object.
