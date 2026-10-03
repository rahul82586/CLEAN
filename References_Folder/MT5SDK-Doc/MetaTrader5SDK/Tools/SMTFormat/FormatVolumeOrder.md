[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatVolumeOrder

[Previous](FormatSize.md) | [Next](FormatVolumeExtOrder.md)

# SMTFormat::FormatVolumeOrder

Formats order volume (UINT64) to a string.
    
    
    static LPCWSTR  SMTFormat::FormatVolumeOrder(
       CMTStr        &str,               // Reference to a string object
       const UINT64  volume_initial,     // Initial volume
       const UINT64  volume_current      // Current volume
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**volume_initial**  
[in] Initial (requested) order volume as a UINT64 number (10000 corresponds to 1 lot).

**volume_current**  
[in] Current (unfilled) order volume as a UINT64 number (10000 corresponds to 1 lot). The filled volume that is output as a second value in a string is calculated as volume_initial - volume_current.

### Return Value

Returns a constant pointer to a string in the str object.

### Note

The volume of the order consists of two parts - initial volume and volume filled. Appears in the following format: initial volume / volume filled.
