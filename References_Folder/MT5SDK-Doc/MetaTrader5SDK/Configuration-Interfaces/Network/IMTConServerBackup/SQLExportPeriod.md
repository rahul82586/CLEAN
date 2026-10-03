[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerBackup](../IMTConServerBackup.md) / SQLExportPeriod

[Previous](SQLExportFlags.md) | [Next](SQLExportServer.md)

# IMTConServerBackup::SQLExportPeriod

Getting the frequency of price and profit data export.

C++
    
    
    UINT  IMTConServerBackup::SQLExportPeriod()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerBackup.SQLExportPeriod()

Python (Manager API)
    
    
    MTConServerBackup.SQLExportPeriod

### Return Value

The frequency of price and profit data export.

# IMTConServerBackup::SQLExportPeriod

Setting the frequency of price and profit data export.

C++
    
    
    MTAPIRES  IMTConServerBackup::SQLExportPeriod(
       const UINT  period      // Export periodicity
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerBackup.SQLExportPeriod(
       uint        period      // Export periodicity
       )

Python (Manager API)
    
    
    MTConServerBackup.SQLExportPeriod

### Parameters

**period**  
[in] The frequency of price and profit data export.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To reduce the consumption of resources, you can limit the frequency of price and profit export. These data include prices of symbols, current prices of positions and orders, as well as almost all of the data in the accounts state table.
