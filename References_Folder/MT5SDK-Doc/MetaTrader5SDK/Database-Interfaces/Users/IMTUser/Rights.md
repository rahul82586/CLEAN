[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Rights

[Previous](CertSerialNumber.md) | [Next](Registration.md)

# IMTUser::Rights

Get permissions of a user.

C++
    
    
    UINT64  IMTUser::Rights()  const

.NET (Gateway/Manager API)
    
    
    EnUsersRights  CIMTUser.Rights()

### Return Value

A value of the [IMTUser::EnUsersRights (#enusersrights)](Enumerations.md#enusersrights) enumeration.

# IMTUser::Rights

Set permissions of a user.

C++
    
    
    MTAPIRES  IMTUser::Rights(
       const UINT64   rights     // User permissions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Rights(
       EnUsersRights  rights     // User permissions
       )

### Parameters

**rights**  
[in] To pass the user permissions, theIMTUser::EnUsersRightsenumeration is used.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Rights are verified and set using bit operations & ("AND") and | ("OR").

### Example showing how to set a separate right
    
    
    //+------------------------------------------------------------------+
    //| Enabling separate rights for a user                              |
    //+------------------------------------------------------------------+
    bool CPluginInstance::UserRightUpdate(UINT64 login)
      {
       IMTUser* user=NULL;
       MTAPIRES res;
       bool     result=false;
       if(m_api)
         {
          user=m_api->UserCreate();
          if(res=m_api->UserGet(login,user)==MT_RET_OK)
            {
             //--- Enable the account and set forced password change
             user->Rights(IMTUser::USER_RIGHT_ENABLED|IMTUser::USER_RIGHT_RESET_PASS);
             //--- Send changes
             if(res=m_api->UserUpdate(user)==MT_RET_OK)
               {
                m_api->LoggerOut(MTLogOK,L"Rights for user %u updated successfully",login);
                result=true;
               }
            }
          user->Release();
         }
       return(result);
      }

### Example showing how to disable an individual right
    
    
    //+------------------------------------------------------------------+
    //| Disabling individual rights for a user                           |
    //+------------------------------------------------------------------+
    bool CPluginInstance::UserRightUpdate(UINT64 login)
      {
       IMTUser* user=NULL;
       MTAPIRES res;
       bool     result=false;
       if(m_api)
         {
          user=m_api->UserCreate();
          if(res=m_api->UserGet(login,user)==MT_RET_OK)
            {
             //--- Enable the account
             user->Rights(user->Rights() & ~IMTUser::USER_RIGHT_ENABLED);
             //--- Send changes
             if(res=m_api->UserUpdate(user)==MT_RET_OK)
               {
                m_api->LoggerOut(MTLogOK,L"Rights for user %u updated successfully",login);
                result=true;
               }
            }
          user->Release();
         }
       return(result);
      }

### Example showing how to check a permission
    
    
    //+------------------------------------------------------------------+
    //| Check if permission is available                                 |
    //+------------------------------------------------------------------+
    bool CPluginInstance::UserRightCheck(UINT64 login)
      {
       IMTUser* user=NULL;
       MTAPIRES res;
       bool     result=false;
       if(m_api)
         {
          user=m_api->UserCreate();
          if(res=m_api->UserGet(login,user)==MT_RET_OK))
            {
             //--- Check permission
             UINT64 user_rights=user->Rights(); 
             if((user_rights&IMTUser::USER_RIGHT_TRADE_DISABLED)>0)
               {
                m_api->LoggerOut(MTLogOK,L"User %u is not allowed to trade",login);
                result=true;
               }
             else
               {
                m_api->LoggerOut(MTLogOK,L"User %u is allowed to trade",login);
               }
            }
         }
       //--- release object
       if(m_api)
         {
          user->Release();
          user->NULL;
         }  
       return(result);
      }
