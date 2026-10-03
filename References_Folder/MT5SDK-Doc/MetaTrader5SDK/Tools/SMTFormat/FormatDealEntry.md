[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatDealEntry

[Previous](FormatDealAction.md) | [Next](../SMTMath.md)

# SMTFormat::FormatDealEntry

Format the type of action performed by a deal relative to a position, to a string with a text description.
    
    
    static LPCWSTR  SMTFormat::FormatDealEntry(
       CMTStr      &str,      // Reference to a string object
       const UINT  entry      // Type of action relative to a position
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**entry**  
[in] Type of action performed by a deal relative to a position. Specified by a value of theIMTDeal::EnDealEntryenumeration:

  * IMTDeal::ENTRY_IN \- "in";
  * IMTDeal::ENTRY_OUT \- "out";
  * IMTDeal::ENTRY_INOUT \- "in/out";



### Return Value

Returns a constant pointer to a string in the str object.
