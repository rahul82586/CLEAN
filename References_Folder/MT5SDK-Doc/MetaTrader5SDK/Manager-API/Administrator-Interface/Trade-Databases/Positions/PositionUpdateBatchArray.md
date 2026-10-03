[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionUpdateBatchArray

[Previous](PositionUpdateBatch.md) | [Next](PositionDelete.md)

# IMTAdminAPI::PositionUpdateBatchArray

Update positions in a server database in bulk.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionUpdateBatchArray(
       IMTPosition**   positions,       // An array of positions
       const UINT      positions_total, // Number of positions in the array
       MTAPIRES*       results          // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionUpdateBatchArray(
       CIMTPosition[]  positions,       // Array of positions
       MTRetCode[]     retcodes         // Array of results
       )

### Parameters

**positions**  
[in] A pointer to the array of positions.

**positions_total**  
[in] The number of positions in the 'positions' array.

**results**  
[out] An array with position update results. The size of the 'results' array must not be less than that of 'positions'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all positions have been updated. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the positions have been updated. Analyze the 'results' array for more details concerning the execution results. The result of update of each position from the 'positions' array is added to 'results'. The index of a result corresponds to the index of a position in the source array.

### Note

Positions can only be updated from the applications connected to the trade server, on which the positions have been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

  * [IMTPosition::Login](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Login.md) (an account with this login must exist on the server)
  * [IMTPosition::Symbol](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Symbol.md)
  * [IMTPosition::Action](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Action.md)
  * [IMTPosition::Volume](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Volume.md) or [IMTPosition::VolumeExt](../../../../Database-Interfaces/Trade/Positions/IMTPosition/VolumeExt.md)
  * [IMTPosition::PriceOpen](../../../../Database-Interfaces/Trade/Positions/IMTPosition/PriceOpen.md)
  * [IMTPosition::Digits](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Digits.md)
  * [IMTPosition::DigitsCurrency](../../../../Database-Interfaces/Trade/Positions/IMTPosition/DigitsCurrency.md)
  * [IMTPosition::ContractSize](../../../../Database-Interfaces/Trade/Positions/IMTPosition/ContractSize.md)
  * [IMTPosition::TimeCreate](../../../../Database-Interfaces/Trade/Positions/IMTPosition/TimeCreate.md)


  * [IMTPosition::RateMargin](../../../../Database-Interfaces/Trade/Positions/IMTPosition/RateMargin.md)


