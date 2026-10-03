[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Groups](../Groups.md) / IMTConGroup

[Previous](../Groups.md) | [Next](IMTConGroup/Enumerations.md)

# IMTConGroup

The IMTConGroup class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTConGroup/Release.md) | Delete the current object.  
[Assign](IMTConGroup/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConGroup/Clear.md) | Clear an object.  
[Group](IMTConGroup/Group.md) | Get and set the name of a group, including a path to it in accordance with the hierarchy.  
[Server](IMTConGroup/Server.md) | Get and set the ID of the trade server, to which the group is linked.  
[PermissionFlags](IMTConGroup/PermissionsFlags.md) | Get and set permission flags for the group.  
[AuthMode](IMTConGroup/AuthMode.md) | Get and set the authorization mode for accounts in the group.  
[AuthOTPMode](IMTConGroup/AuthOTPMode.md) | Get and set authentication mode using one-time passwords.  
[AuthPasswordMin](IMTConGroup/AuthPasswordMin.md) | Get and set the minimum password length for accounts in the group.  
[Company](IMTConGroup/Company.md) | Get and set the name of the company that services the group.  
[CompanyPage](IMTConGroup/CompanyPage.md) | Get and set the website address of the company that services the group.  
[CompanyEmail](IMTConGroup/CompanyEmail.md) | Get and set the email address of the company that services the group.  
[CompanySupportPage](IMTConGroup/CompanySupportPage.md) | Get and set the website address of the technical support of the company that services the group.  
[CompanySupportEmail](IMTConGroup/CompanySupportEmail.md) | Get and set the technical support email address of the company that services the group.  
[CompanyCatalog](IMTConGroup/CompanyCatalog.md) | Get and set the name of the subdirectory that stores the templates of reports, emails, etc. for the company that services this group.  
[CompanyDepositPage](IMTConGroup/CompanyDepositPage.md) | Get and set the deposit page URL for a group of accounts.  
[CompanyWithdrawalPage](IMTConGroup/CompanyWithdrawalPage.md) | Get and set the withdrawal page URL for a group of accounts.  
[Currency](IMTConGroup/Currency.md) | Get and set the deposit currency of the group.  
[CurrencyDigits](IMTConGroup/CurrencyDigits.md) | Get the number of digits after the decimal point in the group deposit currency.  
[CurrencyDigitsSet](IMTConGroup/CurrencyDigitsSet.md) | Set the number of digits after the decimal point in the group deposit currency.  
[ReportsMode](IMTConGroup/ReportsMode.md) | Get and set the mode of report generation.  
[ReportsFlags](IMTConGroup/ReportsFlags.md) | Get and set the options for sending reports.  
[ReportsEmail](IMTConGroup/ReportsEmail.md) | Get and set the mail server which is used for sending reports to clients in the group.  
[ReportsSMTP](IMTConGroup/ReportsSMTP.md) | Get and set the address of the SMTP server for sending reports. The method is obsolete and is no longer used.  
[ReportsSMTPLogin](IMTConGroup/ReportsSMTPLogin.md) | Get and set a login for the authorization on the SMTP server that is used for sending reports. The method is obsolete and is no longer used.  
[ReportsSMTPPass](IMTConGroup/ReportsSMTPPass.md) | Get and set a password for the authorization on the SMTP server that is used for sending reports. The method is obsolete and is no longer used.  
[NewsMode](IMTConGroup/NewsMode.md) | Get and set the mode of news sending to the clients from the group.  
[NewsCategory](IMTConGroup/NewsCategory.md) | Get and set the categories of news received by the group.  
[NewsLangAdd](IMTConGroup/NewsLangAdd.md) | Add a language of news that the group will receive.  
[NewsLangUpdate](IMTConGroup/NewsLangUpdate.md) | Change the language of news that the group will receive.  
[NewsLangDelete](IMTConGroup/NewsLangDelete.md) | Delete a news language by the index.  
[NewsLangClear](IMTConGroup/NewsLangClear.md) | Clear the list of news languages.  
[NewsLangTotal](IMTConGroup/NewsLangTotal.md) | Get the number of languages selected for the group.  
[NewsLangNext](IMTConGroup/NewsLangNext.md) | Get the language of news at the position in the list of selected language.  
[MailMode](IMTConGroup/MailMode.md) | Get and set the mode of operation of the internal mail system for the group.  
[TradeFlags](IMTConGroup/TradeFlags.md) | Get and set trade options of a group.  
[TradeTransferMode](IMTConGroup/TradeTransferMode.md) | Get and set the mode of money transfer between accounts.  
[TradeInterestrate](IMTConGroup/TradeInterestrate.md) | Get and set the annual interest rate on deposits of the group accounts.  
[TradeVirtualCredit](IMTConGroup/TradeVirtualCredit.md) | Get and set the amount of additional funds that a brokerage company can provide to a client for opening a position with a volume larger than allowed by the client's current funds.  
[MarginFreeMode](IMTConGroup/MarginFreeMode.md) | Get and set the mode of including floating profit/loss into free margin calculation.  
[MarginSOMode](IMTConGroup/MarginSOMode.md) | Get and set the mode of checking the levels of Stop Out and Margin Call.  
[MarginCall](IMTConGroup/MarginCall.md) | Get and set the Margin Call level.  
[MarginStopOut](IMTConGroup/MarginStopOut.md) | Get and set the Stop Out level.  
[MarginFreeProfitMode](IMTConGroup/MarginFreeProfitMode.md) | Get and set the mode of use of the profit/loss recorded during a trading day in free margin calculation.  
[MarginMode](IMTConGroup/MarginMode.md) | Get and set the risk management mode applied for the group.  
[Margin Flags](IMTConGroup/MarginFlags.md) | Get and set margin calculation flags.  
[MarginFloatingLeverage](IMTConGroup/MarginFloatingLeverage.md) | Get the floating margin profile applied to the group.  
[DemoLeverage](IMTConGroup/DemoLeverage.md) | Get and set the default credit leverage for demo accounts opened in the group.  
[DemoDeposit](IMTConGroup/DemoDeposit.md) | Get and set the default amount of deposit for demo accounts opened in the group.  
[DemoInactivityPeriod](IMTConGroup/DemoInactivityPeriod.md) | Get and set demo account inactivity period, after which open orders and positions from these accounts will be deleted from the platform databases.  
[LimitHistory](IMTConGroup/LimitHistory.md) | Get and set the maximum number of days, for which the group can request data on conducted trade operation.  
[LimitOrders](IMTConGroup/LimitOrders.md) | Get and set the maximum number of orders that can be simultaneously placed by an account from this group.  
[LimitSymbols](IMTConGroup/LimitSymbols.md) | Get and set the maximum number of symbols, for which an account can simultaneously receive quotes.  
[LimitPositions](IMTConGroup/LimitPositions.md) | Get and set the maximum number of open positions that can be present simultaneously on a client account from this group.  
[CommissionAdd](IMTConGroup/CommissionAdd.md) | Add a commission setting.  
[CommissionUpdate](IMTConGroup/CommissionUpdate.md) | Change a commission setting at the specified position.  
[CommissionDelete](IMTConGroup/CommissionDelete.md) | Delete a commission setting by the index.  
[CommissionClear](IMTConGroup/CommissionClear.md) | Clear the list of commission settings.  
[CommissionShift](IMTConGroup/CommissionShift.md) | Move a commission setting in the list.  
[CommissionTotal](IMTConGroup/CommissionTotal.md) | Get the number of commission settings for a group.  
[CommissionNext](IMTConGroup/CommissionNext.md) | Get a commission setting by the index.  
[CommissionGet](IMTConGroup/CommissionGet.md) | Get a commission setting with the specified name.  
[SymbolAdd](IMTConGroup/SymbolAdd.md) | Add a symbol setting for a group.  
[SymbolUpdate](IMTConGroup/SymbolUpdate.md) | Change a symbol setting for a group at the specified position.  
[SymbolDelete](IMTConGroup/SymboDelete.md) | Delete a symbol setting for a group.  
[SymbolClear](IMTConGroup/SymbolClear.md) | Clear the list of symbols of a group  
[SymbolShift](IMTConGroup/SymbolShift.md) | Move a symbol setting in the list.  
[SymbolTotal](IMTConGroup/SymbolTotal.md) | Get the number of symbol settings for a group.  
[SymbolNext](IMTConGroup/SymbolNext.md) | Get a symbol setting at the specified index.  
[SymbolGet](IMTConGroup/SymbolGet.md) | Get a symbol setting at the specified path (with the full specified name).  
  
The IMTConGroup contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnPermissionsFlags (#enpermissionsflags)](IMTConGroup/Enumerations.md#enpermissionsflags) | Flags of group permissions.  
[EnAuthMode (#enauthmode)](IMTConGroup/Enumerations.md#enauthmode) | Authorization mode.  
[EnReportsMode (#enreportsmode)](IMTConGroup/Enumerations.md#enreportsmode) | Report generation modes.  
[EnReportsFlags (#enreportsflags)](IMTConGroup/Enumerations.md#enreportsflags) | Report generation flags.  
[EnNewsMode (#ennewsmode)](IMTConGroup/Enumerations.md#ennewsmode) | News mode.  
[EnMailMode (#enmailmode)](IMTConGroup/Enumerations.md#enmailmode) | Internal mail system mode.  
[EnHistoryLimit (#enhistorylimit)](IMTConGroup/Enumerations.md#enhistorylimit) | Availability of history for clients.  
[EnFreeMarginMode (#enfreemarginmode)](IMTConGroup/Enumerations.md#enfreemarginmode) | Free margin calculation mode.  
[EnStopOutMode (#enstopoutmode)](IMTConGroup/Enumerations.md#enstopoutmode) | Mode of specifying of Margin Call and Stop Out.  
[EnTradeFlags (#entradeflags)](IMTConGroup/Enumerations.md#entradeflags) | Trade flags.  
[EnMarginFreeProfitFlags (#enmarginfreeprofitflags)](IMTConGroup/Enumerations.md#enmarginfreeprofitflags) | Flags of use of floating profit/loss while calculating free margin.  
[EnAuthOTPMode (#enauthotpmode)](IMTConGroup/Enumerations.md#enauthotpmode) | Authentication using one-time passwords.  
[EnTransferMode (#entransfermode)](IMTConGroup/Enumerations.md#entransfermode) | Mode of transfer of funds between accounts.
