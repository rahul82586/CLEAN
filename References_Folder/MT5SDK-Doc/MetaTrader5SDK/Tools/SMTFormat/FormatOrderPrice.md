[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatOrderPrice

[Previous](FormatOrderTypeReason.md) | [Next](FormatDealAction.md)

# SMTFormat::FormatOrderPrice

Format the order price and its triggering price (if any) in a string with a text description.
    
    
    static LPCWSTR  SMTFormat::FormatOrderPrice(
       CMTStr        &str,              // Reference to a string object
       const double  price_order,       // Order placing price
       const double  price_trigger,     // Order triggering price
       const UINT    digits             // Number of decimal place
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**price_order**  
[in] Order placing price.

**price_trigger**  
[in] Order triggering price. This price is specified for Stop-Limit orders (IMTOrder::OP_BUY_STOP_LIMITandIMTOrder::OP_SELL_STOP_LIMIT).

**digits**  
[in] Number of decimal places in prices.

### Return Value

Returns a constant pointer to a string in the str object.
