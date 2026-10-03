[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Common Functions](../Common-Functions.md) / Free

[Previous](Allocate.md) | [Next](LoggerRequest.md)

# IMTReportAPI::Free

Free memory allocated earlier by [IMTReportAPI::Allocate](Allocate.md) method. It is used to free memory allocated by the functions and interfaces of the MetaTrader 5 Report API.
    
    
    void  IMTReportAPI::Free(
       void*  ptr      // Pointer to a memory block
       )

### Parameters

**ptr**  
[in] A pointer to the released memory block allocated earlier by theIMTReportAPI::Allocatemethod.
