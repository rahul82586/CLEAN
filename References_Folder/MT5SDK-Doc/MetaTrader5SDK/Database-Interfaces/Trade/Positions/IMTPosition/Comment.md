[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Comment

[Previous](ExpertPositionID.md) | [Next](APIDataUpdate.md)

# IMTPosition::Comment

Get a comment to a position.

C++
    
    
    LPCWSTR  IMTPosition::Comment()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTPosition.Comment()

### Return Value

If successful, it returns a pointer to a string with a comment to a position. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTPosition](../IMTPosition.md) object.

# IMTPosition::Comment

Set a comment to a position.

C++
    
    
    MTAPIRES  IMTPosition::Comment(
       LPCWSTR  comment      // Comment
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Comment(
       string   comment      // Comment
       )

### Parameters

**comment**  
[in] A comment to a position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The length of the comment is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

### An example of how to add your own comment via the Server API when opening a position
    
    
    //+------------------------------------------------------------------+
    //| Adding own comment to a position                                 |
    //+------------------------------------------------------------------+
    MTAPIRES CPluginInstance::HookTradeRequestProcess(const IMTRequest* request, const IMTConfirm* confirm, const IMTConGroup* group, const IMTConSymbol* symbol, IMTPosition* position, IMTOrder* order, IMTDeal* deal)
      {
       MTAPISTR      str;
       //--- Checking
       if(!request || !m_api) return(MT_RET_ERR_PARAMS);
       //--- Notification that a request was received
       m_api->LoggerOut(MTLogOK, L"HookTradeRequestProcess New request: %s", request->Print(str));
       //--- Verify that the requests implies deal execution and operations with a position
       if(position && deal)
         {
          //--- Verify that this is a position opening deal
          if(deal->Entry() == IMTDeal::EnDealEntry::ENTRY_IN)
            {
             //--- Adding our own comment
             position->Comment(L"Custom comment");
            }
         }
       //--- Confirming the operation
       return(MT_RET_OK);
      }
    //+------------------------------------------------------------------+
