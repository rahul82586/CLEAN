[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Price Functions](../Price-Functions.md) / PriceToDouble

[Previous](PriceToInt.md) | [Next](../Volume-Functions.md)

# SMTMath::PriceToDouble

Converting a price from int to double.

C++
    
    
    static double  SMTMath::PriceToDouble(
       const INT64  value,      // Input price
       UINT         digits      // Accuracy
       )

.NET (Gateway/Manager API)
    
    
    static double  SMTMath.PriceToDouble(
       long         value,      // Input price
       uint         digits      // Accuracy
       )

### Parameters

**value**  
[in] A fixed-point input price.

**digits**  
[in] The number of digits after the decimal point in the resulting price.

### Return Value

The resulting price.

### Note

The value of the digits parameter should not exceed the value of the 
