[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Price Functions](../Price-Functions.md) / PriceNormalize

[Previous](../Price-Functions.md) | [Next](PriceToInt.md)

# SMTMath::PriceNormalize

Normalizing the transmitted price to the specified number of decimal places.

C++
    
    
    static double  SMTMath::PriceNormalize(
       const double  price,      // Input price
       UINT          digits      // Decimal places
       )

.NET (Gateway/Manager API)
    
    
    static double  SMTMath.PriceNormalize(
       double        price,      // Input price
       uint          digits      // Decimal places
       )

### Parameters

**price**  
[in] The price that needs to be normalized.

**digits**  
[in] Accuracy (number of digits after the decimal point), to which the input price should be normalized.

### Return Value

A normalized price.

### Note

The value of the digits parameter should not exceed the value of the 
