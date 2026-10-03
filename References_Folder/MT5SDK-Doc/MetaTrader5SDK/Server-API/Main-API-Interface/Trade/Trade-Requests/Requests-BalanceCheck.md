[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests BalanceCheck

[Previous](Requests-MarginCheckExt.md) | [Next](Requests-SubscribeEOD.md)

# IMTServerAPI::TradeBalanceCheck

Check and correction of a client's balance and credit assets.
    
    
    MTAPIRES  IMTServerAPI::TradeBalanceCheck(
       const UINT64  login,               // Login
       const UINT    fixflag,             // Flag of balance correction
       double&       balance_user,        // Balance at the moment of check
       double&       balance_history      // Balance calculated on the basis of the history of deals
       double&       credit_user,         // Credit assets at the moment of check
       double&       credit_history       // Credit assets calculated on the basis of the history of deals
       )

### Parameters

**login**  
[in] The login of a user whose balance should be checked.

**fixflag**  
[in] Flag of the need to correct a client's balance after the check. If fixflag is equal to 1, the client's balance is corrected in accordance with history ofdeals. If the flag is 0, no correction will be made.

**balance_user**  
[out] The value of theclient's balancestored in the client record at the time of check.

**balance_history**  
[out] The value of the client's balance calculated by analyzing the history of deals.

**credit_user**  
[out] The value of theclient's credit assetsstored in the client record at the time of check.

**credit_history**  
[out] The value of the client's credit assets calculated by analyzing the history of deals.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This function checks the client's balance on the basis of the history of his or her deals and makes corrections in the client's balance if necessary. Credit assets are checked on the basis of deals of the [IMTDeal::Credit (#endealaction)](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction) type.
