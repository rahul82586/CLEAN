[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Summary Positions](../Summary-Positions.md) / SummaryCurrency

[Previous](SummaryUnsubscribe.md) | [Next](SummaryTotal.md)

# IMTManagerAPI::SummaryCurrency

Get the currency used for calculating profits of the summary positions.

C++
    
    
    LPCWSTR  IMTManagerAPI::SummaryCurrency()

.NET
    
    
    string   CIMTManagerAPI.SummaryCurrency()

Python
    
    
    ManagerAPI.SummaryCurrency()

### Return Value

If successful, it returns a pointer to the string with the currency. Otherwise, it returns NULL.

# IMTManagerAPI::SummaryCurrency

Sets the currency, in which clients' summary positions for a symbol are calculated.

C++
    
    
    MTAPIRES  IMTManagerAPI::SummaryCurrency(
       LPCWSTR  currency      // Currency
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SummaryCurrency(
       string   currency      // Currency
       )

Python
    
    
    ManagerAPI.SummaryCurrency(
       str      currency      # Currency
       )

### Parameters

**currency**  
[in] The currency used for calculating profits of the summary positions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
