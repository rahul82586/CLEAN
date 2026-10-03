[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatOrderTypeTime

[Previous](FormatOrderTypeFilling.md) | [Next](FormatOrderTypeReason.md)

# SMTFormat::FormatOrderTypeTime

Format order expiration type in a string with a text description.
    
    
    static LPCWSTR  SMTFormat::FormatOrderTypeTime(
       CMTStr      &str,     // Reference to a string object
       const UINT  type      // Expiration type
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**type**  
[in] Order expiration type. Specified by a value of theIMTOrder::EnOrderTimeenumeration:

  * IMTOrder::ORDER_TIME_GTC \- "gtc";
  * IMTOrder::ORDER_TIME_DAY \- "day";
  * IMTOrder::ORDER_TIME_SPECIFIED \- "specified".



### Return Value

Returns a constant pointer to a string in the str object.
