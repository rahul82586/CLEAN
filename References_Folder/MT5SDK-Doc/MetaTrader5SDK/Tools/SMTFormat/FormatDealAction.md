[🏠 Document Start](../../README.md) / [Tools](../README.md) / [SMTFormat](../SMTFormat.md) / FormatDealAction

[Previous](FormatOrderPrice.md) | [Next](FormatDealEntry.md)

# SMTFormat::FormatDealAction

Format the type of action performed by a deal to a string with a text description.
    
    
    static LPCWSTR  SMTFormat::FormatDealAction(
       CMTStr      &str,       // Reference to a string object
       const UINT  action      // Type of action
       )

### Parameters

**& str**  
[out] Reference to the string objectCMTStr, into which information is placed.

**action**  
[in] Type of action performed by a deal. Specified by a value of theIMTDeal::EnDealActionenumeration:

  * IMTDeal::DEAL_BUY \- "buy";
  * IMTDeal::DEAL_SELL \- "sell";
  * IMTDeal::DEAL_BALANCE \- "balance";
  * IMTDeal::DEAL_CREDIT \- "credit";
  * IMTDeal::DEAL_CHARGE\- "charge";
  * IMTDeal::DEAL_CORRECTION \- "correction";
  * IMTDeal::DEAL_BONUS \- "bonus";
  * IMTDeal::DEAL_COMMISSION \- "commission";
  * IMTDeal::DEAL_COMMISSION_DAILY \- "daily commission";
  * IMTDeal::DEAL_COMMISSION_MONTHLY \- "monthly commission";
  * IMTDeal::DEAL_AGENT_DAILY \- "daily agent commission";
  * IMTDeal::DEAL_AGENT_MONTHLY \- "monthly agent commission";
  * IMTDeal::DEAL_INTERESTRATE \- "interest rate".



### Return Value

Returns a constant pointer to a string in the str object.
