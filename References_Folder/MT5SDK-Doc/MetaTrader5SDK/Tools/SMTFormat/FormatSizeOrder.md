[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatSizeOrder

[Previous](FormatVolumeExtOrder.md) | [Next](FormatDateTime.md)

# SMTFormat::FormatSizeOrder

Format order size in units to a string.
    
    
    static LPCWSTR  SMTFormat::FormatSizeOrder(
       CMTStr        &str,             // Reference to a string object
       const double  size_initial,     // Initial size
       const double  size_current      // Current size
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**size_initial**  
[in] Initial (requested) order size in units.

**size_current**  
[in] Current (unfilled) order size in units. The filled size that is output as a second value in a string is calculated as size_initial - size_current.

### Return Value

Returns a constant pointer to a string in the str object.
