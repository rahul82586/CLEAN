[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserDepositChangeRaw

[Previous](UserDepositChange.md) | [Next](UserArchive.md)

# IMTServerAPI::UserDepositChangeRaw

Conduct balance operation on a user account without checking the free margin and the current balance on the account.
    
    
    MTAPIRES  IMTServerAPI::UserDepositChangeRaw(
       const UINT64  login,       // User's login
       const double  value,       // Amount
       const UINT    type,        // Type of action
       LPCWSTR       comment,     // Comment
       UINT64&       deal_id      // Deal ID
       )

### Parameters

**login**  
[in] The login of a user, on whose account the balance operation is be conducted.

**value**  
[in] The amount to add to an account or subtract from it. A positive value means that funds will be added, a negative value means withdrawal.

**type**  
[in] Type of the balance operation. The type is specified using the following values of theIMTDeal::EnDealActionenumeration:

**comment**  
[in] A comment to a balance operation. The maximum comment length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

**deal_id**  
[out] The ID of the deal in which a balance operation was executed.

  * DEAL_BALANCE — a balance operation.


  * DEAL_CREDIT — a credit operation.
  * DEAL_CHARGE — additional adding/withdrawing.
  * DEAL_CORRECTION — corrective operations.
  * DEAL_BONUS — adding bonuses.
  * DEAL_COMMISSION — charging commissions.



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

Operations with deposit are represented as deals. The ID of the deal in which a balance operation was executed.
