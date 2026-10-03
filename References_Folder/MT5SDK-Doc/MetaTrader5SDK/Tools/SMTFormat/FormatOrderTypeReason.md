[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatOrderTypeReason

[Previous](FormatOrderTypeTime.md) | [Next](FormatOrderPrice.md)

# SMTFormat::FormatOrderTypeReason

Format the order placing reason in a string with a text description.
    
    
    static LPCWSTR  SMTFormat::FormatOrderTypeReason(
       CMTStr  &str,       // Reference to a string object
       UINT    reason      // Reason for placing the order
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**reason**  
[in] Reason for placing the order. Specified by a value of theIMTOrder::EnOrderReasonenumeration:

  * IMTOrder::ORDER_REASON_CLIENT \- "Client";
  * IMTOrder::ORDER_REASON_EXPERT \- "Expert";
  * IMTOrder::ORDER_REASON_DEALER \- "Dealer";
  * IMTOrder::ORDER_REASON_SL \- "Stop loss";
  * IMTOrder::ORDER_REASON_TP -"Take profit";
  * IMTOrder::ORDER_REASON_SO \- "Stop out";
  * IMTOrder::ORDER_REASON_ROLLOVER \- "Rollover";



### Return Value

Returns a constant pointer to a string in the str object.
