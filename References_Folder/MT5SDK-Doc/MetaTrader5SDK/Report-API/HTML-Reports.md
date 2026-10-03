[🏠 Document Start](../README.md) / [Report API](README.md) / HTML Reports

[Previous](Tabular-Reports.md) | [Next](Dashboards.md)

<a id="html-reports"></a>
# HTML Reports (#html-reports)

This type of reports is transferred to the MetaTrader 5 Manager terminal as a HTML page. Except the data formatted using HTML such a report may contain [SVG charts](Charts.md). Creation of a HTML report consists of the following basic steps:

  * Creation of the [HTML template](Templates.md) for further formatting. Creation of a template is not necessary but advisable. Working with templates considerably simplifies the process of the report creation, as a template formatting is separated from its logics.
  * Get the data from a MetaTrader 5 server.
  * Transmission of the data to HTML or a template.



> The total size of a generated HTML report must not exceed 128MB.

Let's observe the example of a simple HTML report creation by adding it to a previously created [tabular report](Tabular-Reports.md). This report will also display the list of client names and the size of their leverage. Report creation example is divided into the following subsections:

  * [Adding a Class (#class-add)](HTML-Reports.md#class-add)
  * [Class Implementation (#class-implement)](HTML-Reports.md#class-implement)


  * [Implementation of the Release method (#release)](HTML-Reports.md#release)
  * [Implementation of the Generate method (#generate)](HTML-Reports.md#generate)
  * [Report description (#description)](HTML-Reports.md#description)
  * [Filling of the exported functions (#exported-functions)](HTML-Reports.md#exported-functions)
  * [Template creation (#template)](HTML-Reports.md#template)
  * [Report generation (#generation)](HTML-Reports.md#generation)


  * [Variables (#variables)](HTML-Reports.md#variables)
  * [Checks (#checks)](HTML-Reports.md#checks)
  * [Template loading (#load-template)](HTML-Reports.md#load-template)
  * [Get the list of users (#list-logins)](HTML-Reports.md#list-logins)
  * [Create an object of a client record (#user-create)](HTML-Reports.md#user-create)
  * [Processing the macros (#macro-process)](HTML-Reports.md#macro-process)


  * [Processing the clients output cycle (#macro-user)](HTML-Reports.md#macro-user)
  * [Processing the names output (#macro-name)](HTML-Reports.md#macro-name)
  * [Processing the leverage output (#macro-leverage)](HTML-Reports.md#macro-leverage)
  * [End of the macros processing (#macro-end)](HTML-Reports.md#macro-end)



<a id="class-add"></a>
## Adding a Class (#class-add)

Add a new C++ class to the project using the "Add Class" command in the "Project" menu by assigning the following class settings:

  * Class name: CMyHTMLReport;
  * .h file: MyHTMLReport.h;
  * .cpp file: MyHTMLReport.cpp;
  * Base class: IMTReportContext;
  * Access: public.



The key point here is to specify the [IMTReportContext](Report-Plugin-Interface.md) base class.

<a id="class-implement"></a>
## Class Implementation (#class-implement)

Two IMTReportContext interface methods must be set in the class:

  * [Release](Report-Plugin-Interface/Release.md) — responsible for deleting a report object;
  * [Generate](Report-Plugin-Interface/Generate.md) — responsible for a report generation.



Besides, the report data must be described in a report class using the [MTReportInfo](../Structures/MTReportInfo.md) structure.

Describe necessary structures and methods in the MyHTMLReport.h header file:
    
    
    //+------------------------------------------------------------------+
    //|                                                                  |
    //+------------------------------------------------------------------+
    #pragma once
    //+------------------------------------------------------------------+
    //|                                                                  |
    //+------------------------------------------------------------------+
    class CMyHTMLReport : public IMTReportContext
      {
    private:
       static const MTReportInfo s_info;            // Report data
    public:
       //--- Constructor/destructor
                         CMyHTMLReport(void);
                        ~CMyHTMLReport(void);
       //--- Get the report data
       static void       Info(MTReportInfo& info) { info=s_info; }
       //--- 
       virtual void      Release(void);
       //--- Report generation method
       virtual MTAPIRES  Generate(const UINT type,IMTReportAPI *api);
      };
    //+------------------------------------------------------------------+

As seen in the above listing, in addition to the virtual Release and Generate methods we have created a private class member s_info where the report data will be stored.

Besides, the additional Info method has been declared to transfer the report data to the server. This method will further be [called (#exported-functions)](HTML-Reports.md#exported-functions) in the dllmain.cpp file.

Class constructor and destructor are implemented further.

<a id="release"></a>
### Implementation of the Release method (#release)

Implementation of the Release method is simple, there is only deleting of an object using delete this.

<a id="generate"></a>
### Implementation of the Generate method (#generate)

At this stage Generate method realization contains only the checking of the transferred pointer to the [IMTReportAPI](Main-Interface-of-Reports.md) copy. In case the pointer is not valid, the error code [MT_RET_ERR_PARAMS](../Return-Codes/Common-errors.md) is returned.

Further, direct generation and requested report output will be implemented in this method.

<a id="description"></a>
## Report description (#description)

Report data must be added to the newly created MyHTMLReport.cpp file before the start a request and data output implementation:
    
    
    //+------------------------------------------------------------------+
    //| Module description structure                                     |
    //+------------------------------------------------------------------+
    const MTReportInfo CMyHTMLReport::s_info=
      {
       100,
       MTReportAPIVersion,
       MTReportInfo::IE_VERSION_ANY,
       L"My HTML Report",
       L"Copyright 2001-2011, MetaQuotes Software Corp.",
       L"MetaTrader 5 Report API plug-in",
       0,
       MTReportInfo::TYPE_HTML,
         { 0 },
         {              // params
          { MTReportParam::TYPE_GROUPS, MTAPI_PARAM_GROUPS, L"*" },
         },1            // params_total
      };
    //+------------------------------------------------------------------+

Report information is described by the [MTReportInfo](../Structures/MTReportInfo.md) structure. The key parameters here are:

  * MTReportInfo::IE_VERSION_ANY — Internet Explorer version necessary for the report operation. In the current case it is indicated that any version is suitable. During the creation of a HTML report more care must be given to this parameter, as the Internet Explorer browser installed together with a manager terminal is used to display HTML contents.
  * MTReportInfo::TYPE_HTML — [HTML report (#entypes)](../Structures/MTReportInfo.md#entypes);
  * { MTReportParam::TYPE_GROUPS, MTAPI_PARAM_GROUPS, L"*" } — [external parameters](../Structures/MTReportParam.md) of a report generation (type, name and value by default) that are set during a report request in MetaTrader 5 Manager. A list of the groups, from which the clients will be requested, may be set for that report. All groups is a default value (the symbol "*" is indicated);
  * 1 — number of parameters.



> The [MTAPI_PARAM_GROUPS (#parameters)](../Structures/MTReportParam.md#parameters) macros is used as the parameter name. This macros inserts a name of a field where the groups in the manager terminal are selected.

<a id="exported-functions"></a>
## Filling of the exported functions (#exported-functions)

Report data call must be added to the [MTReportAbout (#mtreportabout)](Creating-a-Simple-Report.md#mtreportabout) entry point:
    
    
    //+------------------------------------------------------------------+
    //| The MTReportAbout entry point                                    |
    //+------------------------------------------------------------------+
    MTAPIENTRY MTAPIRES MTReportAbout(const UINT index,MTReportInfo& info)
      {
    //--- Checking the index
       if(index==0)
         {
          CMyTableReport::Info(info);
          return(MT_RET_OK);
         }
    //---
       if(index==1)
         {
          CMyHTMLReport::Info(info);
          return(MT_RET_OK);
         }
    //--- not found
       return(MT_RET_ERR_NOTFOUND);
      }
    //+------------------------------------------------------------------+

As in a tabular report, transferring the data on a HTML report is performed using the [Info (#class-implement)](HTML-Reports.md#class-implement) function that was earlier implemented in MyHTMLReport.h. Now, index 0 corresponds to a [tabular report](Tabular-Reports.md) and index 1 corresponds to a HTML report.

A copy of the HTML report module object must be created in the [MTReportCreate (#mtreportcreate)](Creating-a-Simple-Report.md#mtreportcreate) entry point similarly to a tabular report:
    
    
    //+------------------------------------------------------------------+
    //| The MTReportCreate entry point                                   |
    //+------------------------------------------------------------------+
    MTAPIENTRY MTAPIRES MTReportCreate(const UINT index,const UINT apiversion,IMTReportContext **context)
      {
    //--- Check of parameters
       if(!context) return(MT_RET_ERR_MEM);
    //--- Checking the index
       if(index==0)
         {
          //--- Creation of a copy
          if((*context=new(std::nothrow) CMyTableReport())==NULL)
             return(MT_RET_ERR_PARAMS);
          //--- Successful
          return(MT_RET_OK);
         }
    //--- Checking the index
       if(index==1)
         {
          //--- Creation of a copy
          if((*context=new(std::nothrow) CMyHTMLReport())==NULL)
             return(MT_RET_ERR_PARAMS);
          //--- Successful
          return(MT_RET_OK);
         }
    //--- Not found
       return(MT_RET_ERR_NOTFOUND);
      }
     
    //+------------------------------------------------------------------+

<a id="template"></a>
## Template creation (#template)

After the preparatory operations are accomplished let us begin the implemetation of a HTML report itself. It is recommended to perform HTML data output using [templates](Templates.md). That considerably simplifies the development, as the report logics is separated from its format in that case.

Declare a new member for storing a template at the private part of the CMyHTMLReport class in the MyHTMLReport.h file:
    
    
    private:
       static const MTReportInfo s_info;            // Report data
       static const LPCWSTR s_template;             // HTML template

Then a template description must be added to the MyHTMLReport.cpp file after the report description:
    
    
    //+------------------------------------------------------------------+
    //| HTML template                                                    |
    //+------------------------------------------------------------------+
    const LPCWSTR CMyHTMLReport::s_template=
       L"<html>"
       L"<head><title>My HTML Report</title></head>"
       L"<body>"
       L"<table width=100% border=1>"
       L"<tr><td width=50%>Name</td><td width=50%>Leverage</td></tr>"
       L"<mt5:users>"
       L"<tr> <td><mt5:name/></td> <td>1 : <mt5:leverage/></td> </tr>"
       L"</mt5:users>"
       L"</table>"
       L"</body>"
       L"</html>";
    //+------------------------------------------------------------------+

A template is created according to the HTML markup rules. Special macros can be used with the templates. That macroses are to be replaced by the data received from a MetaTrader 5 server.

> The macros are thoroughly described in a [separate section](Templates.md). 

There are two types of macros:

  * Simple ones have the <mt5:.../> look. Simple macros do not contain embedded constructions.
  * Complex ones have the <mt5:...>...</mt5:...> look. Such macros can contain embedded constructions consisting of HTML contents or another macros.



The template described in the example has the following structure:

  * HTML page contains the table consisting of two columns: "Name" or "Leverage". The table header is described using the simple <tr> and <td> HTML tags.
  * The table row containing the data is included into the complex <mt5:users>...</mt5:users> macros.
  * Simple <mt5:name/> and <mt5:leverage/> macros are specified as the table cells values. This macros are to be replaced with the appropriate data during the report generation.



<a id="generation"></a>
## Report generation (#generation)

Report generation and output are performed in the CMyHTMLReport::Generate method.
    
    
    //+------------------------------------------------------------------+
    //| Report generation method                                         |
    //+------------------------------------------------------------------+
    MTAPIRES CMyHTMLReport::Generate(const UINT type,IMTReportAPI *api)
      {
       IMTDatasetColumn *column=NULL;
       IMTUser          *user=NULL;
       UINT64           *logins=NULL;
       UINT              logins_total=0,counter=0;
       MTAPISTR          tag={0};
       MTAPIRES          res;
       //--- Check of pointer
       if(!api)
          return(MT_RET_ERR_PARAMS);
       //--- Checking the type of a requested report
       if(type!=MTReportInfo::TYPE_HTML)
          return(MT_RET_ERR_PARAMS);
       //--- Template loading
       if((res=api->HtmlTplLoad(s_template))!=MT_RET_OK) return(res);
       //--- Get the list of users
       if((res=api->ParamLogins(logins,logins_total))!=MT_RET_OK)
          return(res);
       //--- Create an object of a client record
       if((user=api->UserCreate())==NULL)
         {
          api->Free(logins);
          return(MT_RET_ERR_MEM);
         }
       //--- Get the next macros for processing
       //--- The number of the macros processings are placed in counter.
       //--- The macros is processed using the HtmlTplProcess method
       while((res=api->HtmlTplNext(tag,&counter))==MT_RET_OK)
         {
          //--- Clients loop macros
          //--- This macros is used to display the number of table rows appropriate to the number of the received clients
          if(CMTStr::CompareNoCase(tag,L"users")==0)
            {
             //--- Are there any more clients?
             if(logins && counter<logins_total)
               {
                //--- If there are, they must be displayed by processing embedded tags:
                //--- L"<tr> <td><mt5:name/></td> <td>1 : <mt5:leverage/></td> </tr>"
                //--- To do this, call HtmlTplProcess that gives the order
                //--- To process the construction embedded in <mt5:users>...</mt5:users>.
                //--- Embedded macros will be received during the next reference to HtmlTplNext
                if((res=api->HtmlTplProcess(IMTReportAPI::TPL_PROCESS_NONE))!=MT_RET_OK)
                  {
                   if(logins) api->Free(logins);
                   user->Release();
                   return(res);
                  }
                //--- Get the current client description (the client for the current row)
                //--- from its entry we will get the information on the name and the leverage
                if((res=api->UserGet(logins[counter],user))!=MT_RET_OK)
                  {
                   if(logins) api->Free(logins);
                   user->Release();
                   return(res);
                  }
               }
             continue;
            }
          //--- Process the macros belonging to the current row
          //--- All client information is already present in user
          //--- The name of a client
          if(CMTStr::CompareNoCase(tag,L"name")==0)
            {
             //--- Use the HtmlWriteSafe method to screen
             //--- possible special symbols in the client's name (e.g., < or >)
             if((res=api->HtmlWriteSafe(user->Name(),IMTReportAPI::HTML_SAFE_USENOBSP))!=MT_RET_OK)
               {
                if(logins) api->Free(logins);
                user->Release();
                return(res);
               }
             continue;
            }
          //--- Leverage
          if(CMTStr::CompareNoCase(tag,L"leverage")==0)
            {
             //--- Formatting the number
             if((res=api->HtmlWrite(L"%u",user->Leverage()))!=MT_RET_OK)
               {
                if(logins) api->Free(logins);
                user->Release();
                return(res);
               }
             continue;
            }
         }
    //---
       if(logins) api->Free(logins);
       user->Release();
    //--- Check if the template processing has been finished successfully
       if(res!=MT_RET_REPORT_TEMPLATE_END) return(res);
    //--- Successful
       return(MT_RET_OK);
      }
    //+------------------------------------------------------------------+

Let's thoroughly examine the previously mentioned code by dividing it into blocks:

  * [Variables (#variables)](HTML-Reports.md#variables)
  * [Checks (#checks)](HTML-Reports.md#checks)
  * [Template loading (#load-template)](HTML-Reports.md#load-template)
  * [Get the list of users (#list-logins)](HTML-Reports.md#list-logins)
  * [Create an object of a client record (#user-create)](HTML-Reports.md#user-create)
  * [Processing the macros (#macro-process)](HTML-Reports.md#macro-process)


  * [Processing the clients output cycle (#macro-user)](HTML-Reports.md#macro-user)
  * [Processing the names output (#macro-name)](HTML-Reports.md#macro-name)
  * [Processing the leverage output (#macro-leverage)](HTML-Reports.md#macro-leverage)
  * [End of the macros processing (#macro-end)](HTML-Reports.md#macro-end)



<a id="variables"></a>
### Variables (#variables)

Essential variables are declared at first:
    
    
    IMTDatasetColumn *column=NULL;
       IMTUser         *user=NULL;
       UINT64          *logins=NULL;
       UINT             logins_total=0,counter=0;
       MTAPISTR         tag={0};
       MTAPIRES         res;

It is recommended to null all variables during the declaration.

<a id="checks"></a>
### Checks (#checks)
    
    
    //--- Checking for a pointer
       if(!api)
          return(MT_RET_ERR_PARAMS);
    //--- Checking the type of a requested report
       if(type!=MTReportInfo::TYPE_HTML)
          return(MT_RET_ERR_PARAMS);

Checking the pointer validity at the [IMTReportAPI](Main-Interface-of-Reports.md) and also verification of the requested report type (transferred by the type parameter into the CMyHTMLReport::Generate function) are performed in this block.

<a id="load-template"></a>
### Template loading (#load-template)
    
    
    //--- Template loading
       if((res=api->HtmlTplLoad(s_template))!=MT_RET_OK) return(res);

Loading of the previously described HTML template is performed using the [IMTReportAPI::HtmlTplLoad](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplLoad.md) function.

<a id="list-logins"></a>
### Get the list of users (#list-logins)
    
    
    //--- Get the list of users
       if((res=api->ParamLogins(logins,logins_total))!=MT_RET_OK)
          return(res);

The [IMTReportAPI::ParamLogins](Main-Interface-of-Reports/Report-Parameters/ParamLogins.md) method is used to get the list of the requested users. To make the method work, the [report description (#description)](HTML-Reports.md#description) contains the [MTReportParam::TYPE_GROUPS](../Structures/MTReportParam.md) parameter that has been turned on.

<a id="user-create"></a>
### Create an object of a client record (#user-create)
    
    
    //--- create an object of a client record
       if((user=api->UserCreate())==NULL)
         {
          api->Free(logins);
          return(MT_RET_ERR_MEM);
         }

An object of a client record must be created using the [IMTReportAPI::UserCreate](Main-Interface-of-Reports/Users/UserCreate.md) method to store the information on the users that is to be transfered to a template. In case of an object creation error, the previously received list of logins must be freed using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method.

<a id="macro-process"></a>
### Processing the macros (#macro-process)

Each [<mt5:users></mt5::users> (#macro-user)](HTML-Reports.md#macro-user), [<mt5:name/> (#macro-name)](HTML-Reports.md#macro-name) and [<mt5:leverage/> (#macro-leverage)](HTML-Reports.md#macro-leverage) macro containing in the template must be processed in the loop to display the list of all requested clients.
    
    
    while((res=api->HtmlTplNext(tag,&counter))==MT_RET_OK)
         {
          //--- Processing the macros
         }

This loop will process the macros using the command for getting the next [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) macros. The loop is limited by a number of the previously received users. &counter is used to consider the number of processed users. Report API increases this counter at each loop iteration.

Processing the clients output cycle
    
    
    //--- Processing a client output loop tag
          if(CMTStr::CompareNoCase(tag,L"users")==0)
            {
             //--- Are there any more clients?
             if(logins && counter<logins_total)
               {
                //--- If there are, they must be displayed by processing embedded tags:
                //--- L"<tr> <td><mt5:name/></td> <td>1 : <mt5:leverage/></td> </tr>"
                if((res=api->HtmlTplProcess(IMTReportAPI::TPL_PROCESS_NONE))!=MT_RET_OK)
                  {
                   if(logins) api->Free(logins);
                   user->Release();
                   return(res);
                  }
                //--- Get the current client
                if((res=api->UserGet(logins[counter],user))!=MT_RET_OK)
                  {
                   if(logins) api->Free(logins);
                   user->Release();
                   return(res);
                  }
               }
             continue;
            }

Explanation to the code:

  * Using the CMTStr::CompareNoCase auxiliary function (comparing rows without considering the case), we can verify if the macros received by the [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) method is the <mt5:users> macros.
  * In case the logins list is received and the counter current value is less than the number of logins, an embedded construction processing is performed. In fact, counter means the current row or login that must be displayed.
  * Using the [IMTReportAPI::HtmlTplProcess](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplProcess.md) method the order to process the construction embedded in <mt5:users></mt5:users> is given. In case of an error, the previously received list of logins must be freed by using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method. An object of a client record must be freed by using the [IMTUser::Release](../Database-Interfaces/Users/IMTUser/Release.md) method.
  * Then a client record is received by using the [IMTReportAPI::UserGet](Main-Interface-of-Reports/Users/UserGet.md) method by the counter index. In case of an error, the previously received list of logins must be freed by using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method. An object of a client record must be freed by using the [IMTUser::Release](../Database-Interfaces/Users/IMTUser/Release.md) method.
  * The continue statement returns the execution back to the head of the loop to get the next macros by using the [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) method. As long as there are logins for processing (as long as the [IMTReportAPI::HtmlTplProcess](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplProcess.md) method is executed), this method will try to get one of the macroses stored inside <mt5:users></mt5:users>.



Processing a name output
    
    
    //--- The name of a client
          if(CMTStr::CompareNoCase(tag,L"name")==0)
            {
             //---
             if((res=api->HtmlWriteSafe(user->Name(),IMTReportAPI::HTML_SAFE_USENOBSP))!=MT_RET_OK)
               {
                if(logins) api->Free(logins);
                user->Release();
                return(res);
               }
             continue;
            }

Explanation to the code:

  * Using the CMTStr::CompareNoCase auxiliary function, we can verify if the macros received by the [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) method is the <mt5:name/> macros.
  * The [IMTReportAPI::HtmlWriteSafe](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlWriteSafe.md) method is used to output a name from a previously received client record. In the current case a safe output in HTML is used to replace special symbols, in case they are present in users' names.
  * In case of an error, the previously received list of logins must be freed by using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method. An object of a client record must be freed by using the [IMTUser::Release](../Database-Interfaces/Users/IMTUser/Release.md) method.
  * The continue statement returns the execution back to the head of the loop to get the next macros by using the [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) method.



Processing the leverage output
    
    
    //--- Leverage
          if(CMTStr::CompareNoCase(tag,L"leverage")==0)
            {
             if((res=api->HtmlWrite(L"%u",user->Leverage()))!=MT_RET_OK)
               {
                if(logins) api->Free(logins);
                user->Release();
                return(res);
               }
             continue;
            }
         }

Explanation to the code:

  * Using the CMTStr::CompareNoCase auxiliary function, we can verify if the macros received by the [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) method is the <mt5:leverage/> macro.
  * The [IMTReportAPI::HtmlWrite](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlWrite.md) method is used to output a leverage value from a previously received client record.
  * In case of an error, the previously received list of logins must be freed by using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method. An object of a client record must be freed by using the [IMTUser::Release](../Database-Interfaces/Users/IMTUser/Release.md) method.
  * The continue statement returns the execution back to the head of the loop to get the next tag by using the [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) method. If this method reaches the </mt5:users> closing macros, the loop gets back to the beginning (the initial <mt5:users> macros). New loop of all macros processing begins and the counter increases by 1.



End of the macros processing

After received logins are over the [IMTReportAPI::HtmlTplProcess](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplProcess.md) command will not be called when processing <mt5:users>. Therefore, the execution will pass to the </mt5:users> end macros at once without entering inside. Then the rest part of the template is displayed, the logins list is freed by using the [IMTReportAPI::Free](Main-Interface-of-Reports/Common-Functions/Free.md) method. An object of a client record is freed by using the [IMTUser::Release](../Database-Interfaces/Users/IMTUser/Release.md) method.
    
    
    //---
       if(logins) api->Free(logins);
       user->Release();
    //--- Check if the template processing has been finished successfully
       if(res!=MT_RET_REPORT_TEMPLATE_END) return(res);
    //--- Successful
       return(MT_RET_OK);
      }
    //+------------------------------------------------------------------+

At the end of a report generation the verification is made if the last call of the [IMTReportAPI::HtmlTplNext](Main-Interface-of-Reports/HTML-Reports/HTML/HtmlTplNext.md) method has returned the [MT_RET_REPORT_TEMPLATE_END](../Return-Codes/Common-errors.md) code that means the template end. After the verification is successful the [MT_RET_OK](../Return-Codes/Successful-completion.md) code is returned. The code notifies on the successful execution of the [IMTReportAPI::Generate](Report-Plugin-Interface/Generate.md) method.
