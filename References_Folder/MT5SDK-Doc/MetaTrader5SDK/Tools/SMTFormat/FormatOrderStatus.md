[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatOrderStatus

[Previous](FormatOrderType.md) | [Next](FormatOrderTypeFilling.md)

# SMTFormat::FormatOrderStatus

Format the state of an order in a string with a text description.
    
    
    static LPCWSTR  SMTFormat::FormatOrderStatus(
       CMTStr      &str,       // Reference to a string object
       const UINT  status      // Order state
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**status**  
[in] Order state. Specified by a value of theIMTOrder::EnOrderStateenumeration:

  * IMTOrder::ORDER_STATE_STARTED \- "started";
  * IMTOrder::ORDER_STATE_PLACED \- "placed";
  * IMTOrder::ORDER_STATE_CANCELED \- "canceled";
  * IMTOrder::ORDER_STATE_PARTIAL \- "partial";
  * IMTOrder::ORDER_STATE_FILLED \- "filled";
  * IMTOrder::ORDER_STATE_REJECTED \- "rejected";
  * IMTOrder::ORDER_STATE_EXPIRED \- "expired";
  * IMTOrder::ORDER_STATE_REQUEST_ADD \- "request adding";
  * IMTOrder::ORDER_STATE_REQUEST_MODIFY \- "request modification";
  * IMTOrder::ORDER_STATE_REQUEST_CANCEL \- "request cancelling".



### Return Value

Returns a constant pointer to a string in the str object.
