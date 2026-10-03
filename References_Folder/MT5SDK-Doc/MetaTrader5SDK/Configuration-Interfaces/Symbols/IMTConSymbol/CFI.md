[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CFI

[Previous](Exchange.md) | [Next](Sector.md)

# IMTConSymbol::CFI

Get instrument classification in accordance with the [ISO 10962](https://www.iso.org/standard/44799.html) standard.

C++
    
    
    LPCWSTR  IMTConSymbol::CFI()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.CFI()

Python (Manager API)
    
    
    MTConSymbol.CFI

### Return Value

If successful, it returns a pointer to a string with the symbol CFI. Otherwise, NULL is returned.

### Note

Information from the CFI field is used for [EMIR reports](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_reports/emir_report).

# IMTConSymbol::CFI

Set instrument classification in accordance with the [ISO 10962](https://www.iso.org/standard/44799.html) standard.

C++
    
    
    MTAPIRES  IMTConSymbol::CFI(
       LPCWSTR  cfi         // Instrument classification
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.CFI(
       string   cfi        // Instrument classification
       )

Python (Manager API)
    
    
    MTConSymbol.CFI

### Program Parameters

**cfi**  
[in] Instrument classification.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Information from the CFI field is used for [EMIR reports](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_reports/emir_report).
