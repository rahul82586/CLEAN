[🏠 Document Start](../README.md) / [Manager API](README.md) / .NET Implementation

[Previous](Ready-made-Examples.md) | [Next](Python-Implementation.md)

# Implementation of MetaTrader 5 Manager API in .NET

The MetaTrader 5 Manager API includes a ready implementation in .NET. The implementation is available in the form of ready to use DLLs. To be able to use their functions, you need to add them to a project.

The libraries are available in [SDK installation folder]\Libs:

  * MetaQuotes.MT5CommonAPI(64).dll — library of common API interfaces ([configuration bases](../Configuration-Interfaces/README.md) and [databases](../Database-Interfaces/README.md)).
  * MetaQuotes.MT5ManagerAPI(64).dll — Manager API library.



Aside from DLLs, the package includes examples BalanceExample.NET and DealerExample.NET. They are available in [Manager API installation folder]\Examples.

  * .NET Framework 4.7.2 or newer and all [Visual C++ Redistributable for Visual Studio packages starting from 2015](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) are required to develop applications.


  * .NET implementation is a wrapper over the main Manager API C++ library. Therefore, the MT5APIManager(64).dll file is also required.

  
---  
  
## Basic Terms

A short glossary of the terms used:

  * Managed — code, method, class running in the .NET CLI environment with the so called garbage collection management via the [GC class](https://msdn.microsoft.com/ru-ru/library/system.gc%28v=vs.110%29.aspx). The class controls the system garbage collector — the service that automatically releases unused memory.
  * Native — the native code, method, class running directly in the operating system environment.
  * Native code or API — classes and interfaces of API.
  * Managed wrapper — a .NET class providing an interface of the native API without inheritance.
  * Unsafe code — code in C# or any other managed language that can access pointers, low-level memory management, etc.



## Use the reference of the native Manager API for the .NET wrapper — almost all functions and methods are identical

All managed wrappers are identical to their native interfaces except for the methods that use arrays. For example:
    
    
    // Native API:
    MTAPIRES NotificationsSend(const UINT64* logins,const UINT logins_total,LPCWSTR message)...
    // Managed API C#
    MTRetCode NotificationsSend(UInt64[] logins,string message)...
    // Managed API C++
    MTRetCode NotificationsSend(array<UInt64>^ logins,String^ message)...

Description of each API method contains its variant in .NET:

![The method signature in .NET](images/net.png)

## No Exceptions

Managed wrappers do not generate exceptions. If any library calls generate exceptions, the wrapped code will not let them out.

## Always Use Factory

All managed wrappers of API interfaces should only be created using factories, special methods (for example, [UserCreate](Manager-Interface/Users/UserCreate.md), [UserCreateAccount](Manager-Interface/Users/UserCreateAccount.md), etc). This will prevent from passing incorrect pointers to the native code and from using unsafe client code. A separate factory is implemented for each API library.

## Register Event Handler Classes, Do Not Allow Exceptions

For sink classes, you must call the RegisterSink method in the child class constructor and check the return value. This is connected with the possibility to process errors binding a native sink interface to its managed wrapper.

It is important to not let exceptions out of the sink classes handler methods. Otherwise, logging exceptions will be impossible. It is especially important not to let the exceptions out of the hook methods, which may cause unpredictable behavior of the trading platform.

## Use the "using" Operator

All API managed wrappers inherit the [IDisposable](https://msdn.microsoft.com/ru-ru/library/system.idisposable%28v=vs.110%29.aspx) interface, which provides a mechanism for releasing unmanaged resources. Use the ["using"](https://msdn.microsoft.com/ru-ru/library/yh598w02.aspx) operator for easy and correct use of IDispose objects.
    
    
    void UserFunction()
      {
    ...
       using(CIMTUser user=m_manager.UserCreate())
         {
          user.Name("<UserName>");
    ...
          user.Leverage(leverage);
    ...
          m_manager.UserAdd(user,master_password,investor_password);
         }
         //--- Will surely destroy the user object and its native resources
      }

In the above example, the 'user' object and its native resources will be released once code execution exits the 'using' block. Without using the "using" operator, it is unknown when and under what circumstances the object will be deleted.

> To explicitly release resources, you can also use the 'Release' and 'Dispose' methods of managed wrappers. These methods are similar.

## ToArray Methods in Managed Wrappers for Working with Arrays

ToARray methods are implemented in all managed wrappers for working with array objects, such as [CIMTUserArray](../Database-Interfaces/Users/IMTUserArray.md), [CIMTOrderArray](../Database-Interfaces/Trade/Orders/IMTOrderArray.md) and others. These methods create an array and fill it with the elements of the array source object.

  * No element copying is performed during ToArray call. Elements in the new array refer to the elements of the original array. Therefore, when an element is destroyed by calling Dispose or Release in one array, the appropriate element becomes invalid (destroyed) on the other array. Do not call Dispose/Release methods for the []ToArray array elements.
  * Use the Detach method to detach an element from the array object (CIMT*Array).
  * If the source array does not have elements, ToArray returns an empty array, not nullptr.



## Memory Management

Memory in .NET implementation is managed by the programmer. The programmer must explicitly call the Dispose or Release methods for the created objects in the required places of the application. In .NET finalizers memory is not released automatically: if a .NET wrapper object is not released through Dispose, it will lead to memory and native API object leaks.

When working with the .NET implementation, a situation may occur where two or more wrappers refer to the same native object. For example, this may occur when using the aforementioned ToArray methods. In this case, the programmer must control the lifetime of the objects and avoid access to already released objects.

> Dispose and Release perform the same function, i.e. they release the previously created object. Dispose is designed to match the .NET style and enable the use of the 'using' construct.

## Operation Speed

The speed of calling wrapped methods is much slower than calling its native analogue. This is connected with the check of the to native pointer, managed arguments, etc.

Speed ​​of calls of some wrapped methods that return arrays, particularly arrays of structures, can slow down performance significantly. Example — creating a copy of the array:
    
    
    array<INT64>^ CIMTAdminAPI::UserBackupList(const UINT64 server,const INT64 from,const INT64 to,MTRetCode% res)
            {
             res=MTRetCode::MT_RET_ERR_MEM;
             array<INT64>^ result=nullptr;
             if(m_this)
               {
                INT64* narray=NULL;
                UINT   total =0;
                //--- Call implementation
                if((res=(MTRetCode)m_this->UserBackupList(server,from,to,narray,total))==MTRetCode::MT_RET_OK)
                  {
                   res=(MTRetCode)NativeToManagedArrayCopy(result,narray,total);
                   //--- Releasing the native array
                   if(narray) m_this->Free(narray);
                  }
               }
             return(result);
            }

Example of using the .NET wrapper of Manager API
    
    
    namespace SomeClientNamespace
      {
       using MetaQuotes.MT5CommonAPI;
       using MetaQuotes.MT5ManagerAPI;
       using System;
    ...
     
       class CSomeClientClass
         {
          //--- Manager API 
          public CIMTManagerAPI m_manager=null;
    ...
          public MTRetCode Initialize()
            {
             MTRetCode res=MTRetCode.MT_RET_ERROR;
             //--- Initialize the factory
             if((res=SMTManagerAPIFactory.Initialize())!=MTRetCode.MT_RET_OK)
               {
                LogOutFormat("SMTManagerAPIFactory.Initialize failed - {0}",res);
                return(res);
               }
             //--- Receive the API version
             uint version=0;
             if((res=SMTManagerAPIFactory.GetVersion(out version))!=MTRetCode.MT_RET_OK)
               {
                LogOut("SMTManagerAPIFactory.GetVersion failed - {0}",res);
                return(res);
               }
             //--- Compare the obtained version with the library one
             if(version!=SMTManagerAPIFactory.ManagerAPIVersion)
               {
                LogOutFormat("Manager API version mismatch - {0}!={1}",version,SMTManagerAPIFactory.ManagerAPIVersion);
                return(MTRetCode.MT_RET_ERROR);
               }
             //--- Create an instance
             m_manager=SMTManagerAPIFactory.CreateManager(SMTManagerAPIFactory.ManagerAPIVersion,out res);
             if(res!=MTRetCode.MT_RET_OK)
               {
                LogOut("SMTManagerAPIFactory.CreateManager failed - {0}",res);
                return(res);
               }
             //--- For some reasons, the creation method returned OK and the null pointer
             if(m_manager==null)
               {
                LogOut("SMTManagerAPIFactory.CreateManager was ok, but ManagerAPI is null");
                return(MTRetCode.MT_RET_ERR_MEM);
               }
             //--- All is well
             LogOutFormat("Using ManagerAPI v. {0}", version);
             return (res);
            }
    ...
          public MTRetCode Connect(string server,UInt64 login,string password,uint timeout)
            {
             MTRetCode res=MTRetCode.MT_RET_ERROR;
             if(m_manager==null)
               {
                LogOut(EnMTLogCode.MTLogErr,server,"Connection to {0} failed: .NET Manager API is NULL",server);
                return(res);
               }
             //--- 
             res=m_manager.Connect(server,login,password,null,CIMTManagerAPI.EnPumpModes.PUMP_MODE_FULL,timeout);
             if(res!=MTRetCode.MT_RET_OK)
               {
                LogOut(EnMTLogCode.MTLogErr,server,"Connection by Managed API to {0} failed: {1}",server,res);
                return (res);
               }
             //---
             LogOut("Connected");
             return(res);
            }
    ...
          //+------------------------------------------------------------------+
          //| API call example                                                 |
          //+------------------------------------------------------------------+
          private void OnRequestServerLogs(EnMTLogRequestMode requestMode,
                                           EnMTLogType        logType,
                                           Int64              from,
                                           Int64              to,
                                           string             filter=null)
            {
             if(m_manager==null)
               {
                LogOut("ERROR: Manager was not created");
                return;
               }
             //---
             LogOut(EnMTLogCode.MTLogAtt,"LogTests",CAPITester.LOGSEPARATOR);
             try
               {
                MTRetCode result=MTRetCode.MT_RET_ERROR;
                //---
                MTLogRecord[] records=m_manager.LoggerServerRequest(requestMode,logType,from,to,filter,out result);
                //---
                LogOutFormat("LoggerServerRequest {0} ==> [{1}] return {2} record(s)",
                             (result==MTRetCode.MT_RET_OK ? "ok" : "failed"), 
                             result,(records!=null ? records.Length : 0));
                //---
                if((result==MTRetCode.MT_RET_OK) && (records!=null))
                  {
                   foreach(MTLogRecord rec in records)
                      LogOut(rec);
                  }
               }
             catch(Exception ex)
               {
                ...
               }
            }
    ...
         }
      }
