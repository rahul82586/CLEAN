[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealPerform

[Previous](DealDeleteBatch.md) | [Next](DealPerformBatch.md)

# IMTManagerAPI::DealPerform

Perform a deal on the client's account. This method performs a market buy or sell operation on the account as if it were performed by the client through the terminal. The only difference is that no trade request and no order is created to perform the deal, and thus routing rules are not applied to the operation. In all other respects, the behavior is the same: the deal execution result is applied to the position and the account trading state; commission is calculated and charged for the deal in accordance with the relevant account group settings.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealPerform(
       IMTDeal*  deal      // deal object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealPerform(
       CIMTDeal  deal      // deal object
       )

Python
    
    
    ManagerAPI.DealPerform(
       deal      # deal object
       )

### Parameters

**deal**  
[in/out] Deal object. The deal object must be first created using theIMTManagerAPI::DealCreatemethod.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code means that the deals has been successfully performed. The object of the performed deal from the server database is added to the 'deal' array. If the deal could not be performed, the method will return the relevant error code.

### Note

A deal can only be performed on the account that is opened on the same server to which the application is connected.

  * [IMTDeal::Login](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md)
  * [IMTDeal::Symbol](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md)
  * [IMTDeal::Action](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md) (only IMTDeal::DEAL_BUY and IMTDeal::DEAL_SELL values are allowed)
  * [IMTDeal::Volume](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Volume.md)
  * [IMTDeal::Price](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md)
  * [IMTDeal::PositionID](../../../../Database-Interfaces/Trade/Deals/IMTDeal/PositionID.md) (when closing a position on a hedging account)



You can additionally specify individual margin ([IMTDeal::RateMargin](../../../../Database-Interfaces/Trade/Deals/IMTDeal/RateMargin.md)) and profit ([IMTDeal::RateProfit](../../../../Database-Interfaces/Trade/Deals/IMTDeal/RateProfit.md)) recalculation rates in the deal. If not specified, calculated rates will be used.

If commission ([IMTDeal::Commission](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Commission.md)) is specified in the deal, it will be applied to the client account. However, it does not replace the commission charged in accordance with the trader's group settings ([IMTConGroup::Commission*](../../../../Configuration-Interfaces/Groups/IMTConGroup/CommissionAdd.md)). Therefore, the commission specified in the deal is summed up with the calculated commission. 

The deal profit is always calculated by the server even if you specify it in the [IMTDeal::Profit](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Profit.md) field. If necessary, the server charges the deal commission automatically (in accordance with the [commission settings](../../../../Configuration-Interfaces/Groups/IMTConCommission.md)).

It is not recommended to call the IMTManagerAPI::DealPerform method from the [IMTDealSink::OnDealAdd](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealAdd.md), [IMTDealSink::OnDealUpdate](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealUpdate.md) and [IMTDealSink::OnDealPerform](../../../../Database-Interfaces/Trade/Deals/IMTDealSink/OnDealPerform.md) handlers.

### An example of closing positions (even if trading is disabled for an instrument)
    
    
    //+------------------------------------------------------------------+
    //| Close client's all positions at the current price                |
    //+------------------------------------------------------------------+
    MTAPIRES CPluginInstance::CloseAll(UINT64 login)
      {
       IMTPositionArray* positions={0};
       IMTDeal*          deal_tmp ={0};
       IMTPosition*      pos_tmp={0};
       MTAPIRES          res;
       //--- check
       if(m_api)
         {
          positions=m_api->PositionCreateArray();
          deal_tmp=m_api->DealCreate();
          pos_tmp=m_api->PositionCreate();
         }
       else return(MT_RET_ERR_PARAMS);
       //--- get positions
       if(res=m_api->PositionGet(login, positions)!=MT_RET_OK)
         {
          m_api->LoggerOut(MTLogOK, L"PositionGet failed [%d]", res);
          return(MT_RET_ERR_PARAMS);
         }
       else
         {
          m_api->LoggerOut(MTLogOK, L"client '%I64u' has %d positions, try to close them", login, positions->Total());
          //---
          for(UINT index=0;index<positions->Total();index++)
            {
             pos_tmp=positions->Next(index);
             if(pos_tmp)
               {
                //--- fill the deal object
                deal_tmp->Login(pos_tmp->Login());
                deal_tmp->Symbol(pos_tmp->Symbol());
                //--- set the direction of the closing deal depending on the position direction
                if(pos_tmp->Action() == IMTPosition::POSITION_BUY)
                   deal_tmp->Action(IMTDeal::DEAL_SELL);
                else
                   deal_tmp->Action(IMTDeal::DEAL_BUY);
                //--- fill other deal parameters
                deal_tmp->Volume(pos_tmp->Volume());
                deal_tmp->Price(pos_tmp->PriceCurrent());
                deal_tmp->PositionID(pos_tmp->Position()); // only filled for hedging accounts
                //--- close the position            
                if(res=m_api->DealPerform(deal_tmp)!=MT_RET_OK)
                   m_api->LoggerOut(MTLogOK, L"DealPerform failed [%d]", res);
               }
            }
         }
       //--- clear the objects
       if(positions)
          positions->Release();
       //--- clear the objects
       if(pos_tmp)
          pos_tmp->Release();
        //--- clear the objects
        if(deal_tmp)
           deal_tmp->Release();
    }
    //+------------------------------------------------------------------+
