[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatVolume

[Previous](FormatPrices.md) | [Next](FormatVolumeDouble.md)

# SMTFormat::FormatVolume

Formats size (UINT64) to a string.
    
    
    static LPCWSTR  SMTFormat::FormatVolume(
       CMTStr        &str,             // Reference to a string object
       const UINT64  volume,           // Size
       const bool    compact=true      // Flag of a compact form
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**volume**  
[in] Size as a UINT64 number (10000 corresponds to 1 lot).

**compact=true**  
[in] Flag of the compact view of size. If this flag is enabled (true):

  * Size over 1 000 000 lots will be shown with millions replaced by letter "M" and with the up to 5-digit accuracy. For example, 1 500 000 lots (15 000 000 000 in UINT64 format) will be displayed as 1.5M.
  * Size over 1 000 lots will be shown with thousands replaced by letter "K" and with the up to 8-digit accuracy. For example, 1 500 lots (15 000 000 in UINT64 format) will be displayed as 1.5K.



### Return Value

Returns a constant pointer to a string in the str object.

### Note

The method operates with [the standard volume accuracy (#volume)](../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [SMTFomat::FormatVolumeExt](FormatVolumeExt.md) method.
