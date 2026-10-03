[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatSize

[Previous](FormatVolumeExt.md) | [Next](FormatVolumeOrder.md)

# SMTFormat::FormatSize

Format size in units to a string.
    
    
    static LPCWSTR  SMTFormat::FormatSize(
       CMTStr        &str,             // Reference to a string object
       const double  size,             // Size
       const bool    compact=true      // Flag of a compact form
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**size**  
[in] Size in units.

**compact=true**  
[in] Flag of the compact view of size. If this flag is enabled (true):

  * Size over 1 000 000 units will be shown with millions replaced by letter "M" and with the up to 5-digit accuracy. For example, 1 500 000 units will be displayed as 1.5M.
  * Size over 1 000 units will be shown with thousands replaced by letter "K" and with the up to 8-digit accuracy. For example, 1 500 units will be displayed as 1.5K.



### Return Value

Returns a constant pointer to a string in the str object.
