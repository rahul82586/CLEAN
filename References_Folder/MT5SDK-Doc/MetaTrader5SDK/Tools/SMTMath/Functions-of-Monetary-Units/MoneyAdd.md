[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Functions of Monetary Units](../Functions-of-Monetary-Units.md) / MoneyAdd

[Previous](../Functions-of-Monetary-Units.md) | [Next](MoneyEqual.md)

# SMTMath::MoneyAdd

Add sums of money in the form of two numbers of type double.

C++
    
    
    static double  SMTMath::MoneyAdd(
       const double  left        // The first amount
       const double  right       // The second amount
       const UCHAR   digits      // Accuracy
       )

.NET (Gateway/Manager API)
    
    
    static double  SMTMath.MoneyAdd(
       double        left        // The first amount
       double        right       // The second amount
       byte          digits      // Accuracy
       )

### Parameters

**left**  
[in] The first sum of money.

**right**  
[in] The second sum of money.

**digits**  
[in] The accuracy (number of decimal places), to which you want to normalize the result of the addition.

### Return Value

The sum of left and right.
