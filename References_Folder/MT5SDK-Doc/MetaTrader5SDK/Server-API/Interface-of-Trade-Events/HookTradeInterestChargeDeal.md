[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Trade Events](../Interface-of-Trade-Events.md) / HookTradeInterestChargeDeal

[Previous](HookTradeInterestCharge.md) | [Next](HookTradeCommissionOrder.md)

# IMTTradeSink::HookTradeInterestChargeDeal

A hook of a balance deal for charging annual interest. A hook is called immediately prior to a balance operation.
    
    
    virtual MTAPIRES  IMTTradeSink::HookTradeInterestChargeDeal(
       const INT64         datetime,           // time of interest adding
       const IMTConGroup*  group,              // pointer to the group object
       const IMTUser*      user,               // pointer to the user object
       IMTDeal*            deal                // pointer to the deal object
       )

### Parameters

**datetime**  
[in] The time of interest charging in seconds that have elapsed since 01.01.1970.

**group**  
[in] A pointer to the object of theconfiguration of the groupof a client, for whom the interest is added.

**user**  
[in] A pointer to theobject of the client record, for which the interest is added.

**deal**  
[in/out] A pointer to theobject of the dealused to charge the annual interest.

### Return Value

In case of confirmation, [MT_RET_OK](../../Return-Codes/Successful-completion.md) should be returned, otherwise, the request will be rejected with a response code returned from the hook. Thus, if the response code is different from MT_RET_OK, the interest is not added.

### Note

The hook is called after [IMTTradeSink::HookTradeInterestCharge](HookTradeInterestCharge.md). Unlike the latter, it allows modifying different parameters of the deal executed on a client account in addition to a charged amount. For example, it allows you to set custom comments to annual interest charging deals ([IMTDeal::Comment](../../Database-Interfaces/Trade/Deals/IMTDeal/Comment.md)).
