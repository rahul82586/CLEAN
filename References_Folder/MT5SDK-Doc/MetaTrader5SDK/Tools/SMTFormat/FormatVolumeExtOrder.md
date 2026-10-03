[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatVolumeExtOrder

[Previous](FormatVolumeOrder.md) | [Next](FormatSizeOrder.md)

# SMTFormat::FormatVolumeExtOrder

Formats order volume (UINT64) specified with extended accuracy to a string.
    
    
    static LPCWSTR  SMTFormat::FormatVolumeExtOrder(
       CMTStr        &str,               // Reference to the string object
       const UINT64  volume_initial,     // Initial volume
       const UINT64  volume_current      // Current volume
       )

### Program Parameters

**& str**  
[out] Reference to theCMTStrstring object, into which information is placed.

**volume_initial**  
[in] Initial (requested) order volume as a UINT64 number (the value of 100000000 corresponds to 1 lot).

**volume_current**  
[in] Current (unfilled) order volume as a UINT64 number (the value of 100000000 corresponds to 1 lot). The filled volume that is output as a second value in a string is calculated as volume_initial - volume_current.

### Return Value

Returns a constant pointer to a string in the str object.

### Note

The volume of the order consists of two parts - initial volume and volume filled. Appears in the following format: initial volume / volume filled.

### Note

The method operates with [the extended volume accuracy (#volume)](../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [SMTFormat::FormatVolumeOrder](FormatVolumeOrder.md) method.
