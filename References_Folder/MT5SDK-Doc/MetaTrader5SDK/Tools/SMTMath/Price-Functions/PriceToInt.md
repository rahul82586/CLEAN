[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Price Functions](../Price-Functions.md) / PriceToInt

[Previous](PriceNormalize.md) | [Next](PriceToDouble.md)

# SMTMath::PriceToInt

Converting a price from double to int.

C++
    
    
    static INT64  SMTMath::PriceToInt(
       const double  price,      // Input price
       const UINT    digits      // Accuracy
       )

.NET (Gateway/Manager API)
    
    
    static long  SMTMath.PriceToInt(
       double        price,      // Input price
       uint          digits      // Accuracy
       )

### Parameters

**price**  
[in] An input price with a floating point.

**digits**  
[in] The number of digits after the decimal point in the resulting price.

### Return Value

The resulting price.

### Note

The value of the digits parameter should not exceed the value of the 
