[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealVolumeRemaindExt

[Previous](Requests-DealVolumeRemaind.md) | [Next](Requests-DealPrice.md)

# IMTExecution::DealVolumeRemaindExt

Gets and sets the remaining (unfilled) order volume with an extended accuracy.

C++
    
    
    UINT64  IMTExecution::DealVolumeRemaindExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTExecution.DealVolumeRemaindExt()

### Return Value

The remaining (unfilled) order volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTExecution::DealVolumeRemaind](Requests-DealVolumeRemaind.md) method.

# IMTExecution::DealVolumeRemaindExt

Sets the remaining (unfilled) order volume with an extended accuracy.

C++
    
    
    MTAPIRES  IMTExecution::DealVolumeRemaindExt(
       const UINT64  volume      // Remaining volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealVolumeRemaindExt(
       ulong         volume      // Remaining volume
       )

### Program Parameters

**volume**  
[in] The remaining (unfilled) order volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTExecution::DealVolumeRemaind](Requests-DealVolumeRemaind.md) method.

If the order is created with the Fill or Kill ([IMTOrder::ORDER_FILL_FOK (#enorderfilling)](../../Orders/IMTOrder/Enumerations.md#enorderfilling)) fill policy and with the Instant ([IMTConSymbol::EXECUTION_INSTANT (#enexecutionmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enexecutionmode)) or Request ([IMTConSymbol::EXECUTION_REQUEST (#enexecutionmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enexecutionmode)) execution mode, this order can only be filled in the specified volume and at the specified price. If you specify a smaller volume in the trade execution, the trading platform will reject the operation. In the Market ([IMTConSymbol::EXECUTION_MARKET (#enexecutionmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enexecutionmode)) and Exchange ([IMTConSymbol::EXECUTION_EXCHANGE (#enexecutionmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enexecutionmode)) execution modes, the price is not specified in the order and the required volume can be made up of several offers from the order book. Therefore, you can specify a lower volume in the trade execution for these modes.
