[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatPrice

[Previous](FormatMoney.md) | [Next](FormatPrices.md)

# SMTFormat::FormatPrice

Format a number into a string. Basic and additional accuracy are separately set for a number. As a rule, is used to format the position price.
    
    
    static LPCWSTR  SMTFormat::FormatPrice(
       CMTStr  &str,               // Reference to a string object
       double  val,                // Number
       UINT    digits,             // Number of decimal places
       UINT    extra_digits=0      // Number of additional decimal places
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which number is placed.

**val**  
[in] The number being formated.

**digits**  
[in] The basic number of digits after the decimal point in the formatted number.

**extra_digits=0**  
[in] Additional accuracy for the number. Zero values ​​within the additional fractional part are omitted.

### Return Value

Returns a constant pointer to a string in the str object.

### Note

The method works in the same as [SMTFormat::FormatDouble](FormatDouble.md), but the accuracy for the number is given in two values: digits + extra_digits. In the additional fractional part (extra_digits) zero values are omitted. The basic fractional part is shown as is. For example:

  * As a result of execution of SMTFormat::FormatPrice(1.254,2,3) we receive a string 1.254 (general accuracy is 5 digits, but after the third digit 0 is omitted).
  * As a result of SMTFormat::FormatPrice (1.24500,4,1) we receive 1.2450.


