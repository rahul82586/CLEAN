[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [History Data](../History-Data.md) / ChartUpdate

[Previous](ChartDelete.md) | [Next](ChartReplace.md)

# IMTManagerAPI::ChartUpdate

Change historical data of a symbol.

C++
    
    
    MTAPIRES  IMTManagerAPI::ChartUpdate(
       LPCWSTR            symbol,         // Symbol
       const MTChartBar*  bars,           // Bars to change
       const UINT         bars_total      // The number of bars to change
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.ChartUpdate(
       string             symbol,         // Symbol
       MTChartBar[]       bars            // Bars to change   
       )

Python
    
    
    ManagerAPI.ChartUpdate(
       symbol,            # Symbol
       bars               # Bars to change
       )

### Parameters

**symbol**  
[in] The symbol, for which you want to update historical data.

**bars**  
[in] Bars you want to update, described by theMTChartBarstructure.

**bars_total**  
[in] The number of bars to update.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the bar open price ([MTChartBar.open](../../../Structures/MTChartBar.md)) in the passed structure is equal to 0, this bar will be deleted.
