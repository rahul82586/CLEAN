[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatError

[Previous](Enumerations.md) | [Next](FormatDouble.md)

# SMTFormat::FormatError

Convert [an error code](../../Return-Codes/README.md) used in the MetaTrader 5 platform into a text description.
    
    
    static LPCWSTR  SMTFormat::FormatError(
       const MTAPIRES  retcode      // Error code
       )

### Parameters

**retcode**  
[in] Error code.

### Return Value

Returns a constant pointer to a string with the text description.
