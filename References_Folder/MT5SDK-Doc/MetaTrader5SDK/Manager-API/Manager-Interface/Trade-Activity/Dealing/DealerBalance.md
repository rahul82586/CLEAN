[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Dealing](../Dealing.md) / DealerBalance

[Previous](DealerSend.md) | [Next](DealerBalanceRaw.md)

# IMTManagerAPI::DealerBalance

Conduct balance operations on an account.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealerBalance(
       const UINT64  login,       // Login
       const double  value,       // Amount
       const UINT    type,        // Type of operation
       LPCWSTR       comment      // Comment
       UINT64&       deal_id      // Deal ID
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealerBalance(
       ulong         login,       // Login
       double        value,       // Amount
       uint          type,        // Type of operation
       string        comment      // Comment
       out ulong     deal_id      // Deal ID
       )

Python
    
    
    ManagerAPI.DealerBalance(
       login,        # Login
       value,        # Amount
       type,         # Type of operation
       comment       # Comment
       )

### Parameters

**login**  
[in] A login for conducting a balance operation.

**value**  
[in] The amount to add or subtract from an account. In order to deposit to the account, specify a positive value; to withdraw, specify a negative value.

**type**  
[in] Type of the balance operation. To pass the type, the following values of theIMTDeal::EnDealActionenumeration are used: DEAL_BALANCE, DEAL_CREDIT, DEAL_CHARGE, DEAL_CORRECTION, DEAL_BONUS, DEAL_COMMISSION, DEAL_TAX, DEAL_DIVIDEND, DEAL_DIVIDEND_FRANKED.

**comment**  
[in] A comment to a balance operation. The length of the comment is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

**deal_id**  
[out] The ID of the deal in which a balance operation was executed.

### Return Value

An indication of successful completion is the [MT_RET_REQUEST_DONE](../../../../Return-Codes/Trade-Requests.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Balance operations are represented as [deals](../../../../Database-Interfaces/Trade/Deals.md). The ID of the resulting deal is passed in the deal_id parameter.
