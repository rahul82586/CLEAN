[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatVolumeExt

[Previous](FormatVolumeDouble.md) | [Next](FormatSize.md)

# SMTFormat::FormatVolumeExt

Formats extended accuracy volume (UINT64) to a string.
    
    
    static LPCWSTR  SMTFormat::FormatVolumeExt(
       CMTStr        &str,             // Reference to the string object
       const UINT64  volume,           // Volume
       const bool    compact=true      // Compact view flag
       )

### Program Parameters

**& str**  
[out] Reference to theCMTStrstring object, into which information is placed.

**volume**  
[in] Volume as a UINT64 number (100000000 corresponds to one lot).

**compact=true**  
[in] Flag of the compact volume view. If this flag is enabled (true):

  * Volume over 1 000 000 lots will be shown with millions replaced by letter "M" and with the up to 5-digit accuracy. For example, 1 500 000 lots (15 000 000 000 in UINT64 format) will be displayed as 1.5M.
  * Volume over 1 000 lots will be shown with thousands replaced by letter "K" and with the up to 8-digit accuracy. For example, 1 500 lots (15 000 000 in UINT64 format) will be displayed as 1.5K.



### Return Value

Returns a constant pointer to a string in the str object.

### Note

The method operates with [the extended volume accuracy (#volume)](../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [SMTFormat::FormatVolume](FormatVolume.md) method.
