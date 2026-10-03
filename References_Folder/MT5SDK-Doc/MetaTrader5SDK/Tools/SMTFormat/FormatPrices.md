[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatPrices

[Previous](FormatPrice.md) | [Next](FormatVolume.md)

# SMTFormat::FormatPrices

Format values of Bid, Ask and Last from a passed structure [MTTickShort](../../Structures/MTTickShort.md) to a string.
    
    
    static LPCWSTR  SMTFormat::FormatPrices(
       CMTStr        &str,       // Reference to a string object
       MTTickShort  &tick,       // Reference to the MTTickShort structure
       const UINT    digits      // Number of decimal places
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**tick**  
[in] Reference to theMTTickShortstructure.

**digits**  
[in] The number of digits after the decimal point in the Bid, Ask and Last prices.

### Return Value

Returns a constant pointer to a string in the str object.

### Note

Prices are shown in the following format: Bid / Ask / Last. If there is no Last price in the structure, only Bid and Ask are shown: Bid / Ask.
