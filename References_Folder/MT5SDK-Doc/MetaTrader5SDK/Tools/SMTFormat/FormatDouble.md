[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatDouble

[Previous](FormatError.md) | [Next](FormatMoney.md)

# SMTFormat::FormatDouble

Format a number with a given number of decimal places to a string.
    
    
    static LPCWSTR  SMTFormat::FormatDouble(
       CMTStr  &str,       // Reference to a string object
       double  val,        // Number
       UINT    digits      // Number of decimal places
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which number is placed.

**val**  
[in] The number being formated.

**digits**  
[in] The number of digits after the decimal point in the formatted number.

### Return Value

Returns a constant pointer to a string in the str object.

### Note

A point is used as a decimal mark.
