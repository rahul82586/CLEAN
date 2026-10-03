[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatOrderTypeFilling

[Previous](FormatOrderStatus.md) | [Next](FormatOrderTypeTime.md)

# SMTFormat::FormatOrderTypeFilling

Format order filling type in a string with a text description.
    
    
    static LPCWSTR  SMTFormat::FormatOrderTypeFilling(
       CMTStr      &str,     // Reference to a string object
       const UINT  type      // Type of filling
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**type**  
[in] Order filling type. Specified by a value of theIMTOrder::EnOrderFillingenumeration:

  * IMTOrder::ORDER_FILL_FOK \- "fill or kill";
  * IMTOrder::ORDER_FILL_IOC \- "immediate or cancel";
  * IMTOrder::ORDER_FILL_RETURN \- "return".



### Return Value

Returns a constant pointer to a string in the str object.
