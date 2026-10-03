[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Functions of Monetary Units](../Functions-of-Monetary-Units.md) / MoneyEqual

[Previous](MoneyAdd.md) | [Next](MoneyDigits.md)

# SMTMath::MoneyEqual

Compare two quantities of money in the form of numbers of type double.

C++
    
    
    static bool  SMTMath::MoneyEqual(
       const double  left        // The first amount
       const double  right       // The second amount
       const UCHAR   digits      // Accuracy
       )

.NET (Gateway/Manager API)
    
    
    static bool  SMTMath.MoneyEqual(
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
[in] The accuracy (number of decimal places), with which the two number are compared.

### Return Value

If the amounts are equal, returns true, otherwise - false.

### Note

The following formula is used for comparison: |left-right| < 1/ [10 ^ (digits+1)].
