[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Funds and ETF](../Funds-and-ETF.md) / IMTConFund

[Previous](../Funds-and-ETF.md) | [Next](IMTConFund/Enumerations.md)

# IMTConFund

The IMTConFund class contains methods for obtaining and changing [fund settings (#common)](https://support.metaquotes.net/en/docs/mt5/platform/administration/fund_etf#common):

Method | Purpose  
---|---  
[Release](IMTConFund/Release.md) | Delete the current object.  
[Assign](IMTConFund/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConFund/Clear.md) | Clear an object.  
[Name](IMTConFund/Name.md) | Get and set the fund name.  
[Symbol](IMTConFund/Symbol.md) | Get and set the name of the symbol used for displaying the value of one share.  
[SymbolPerfomance](IMTConFund/SymbolPerfomance.md) | Get and set the name of the symbol used for displaying the current value of assets.  
[SymbolAssets](IMTConFund/SymbolAssets.md) | Get and set the name of the symbol used for displaying the fund yield.  
[Server](IMTConFund/Server.md) | Get and set the identifier of the trade server on which the fund is managed.  
[Manager](IMTConFund/Manager.md) | Get and set the login of the manager responsible for the fund.  
[Flags](IMTConFund/Flags.md) | Get and set additional fund properties.  
[Type](IMTConFund/Type.md) | Get and set the fund type.  
[Recalculation](IMTConFund/Recalculation.md) | Get and set fund chart recalculation mode.  
[StartDate](IMTConFund/StartDate.md) | Get and set the fund operation start date.  
[EndDate](IMTConFund/EndDate.md) | Get and set the fund operation end date.  
[MaxCapital](IMTConFund/MaxCapital.md) | Get and set the maximum allowable investment amount for a fund.  
[Currency](IMTConFund/Currency.md) | Get and set the currency in which the maximum allowable fund investment amount is specified.  
[MaxInvestors](IMTConFund/MaxInvestors.md) | Get and set the maximum allowable number of investors who can purchase shares in the fund.  
[FeeMode](IMTConFund/FeeMode.md) | Get and set the fund management and success fee calculation mode.  
[FeePeriod](IMTConFund/FeePeriod.md) | Get and set the fund management and success fee calculation period.  
[FeeAccount](IMTConFund/FeeAccount.md) | Get and set the account to which the fund management and success fees are charged.  
[FeeManagementType](IMTConFund/FeeManagementType.md) | Get and set the type of fund management fee. The method is currently not used.  
[FeeManagementValue](IMTConFund/FeeManagementValue.md) | Get and set the fund management fee amount.  
[FeeManagementAssets](IMTConFund/FeeManagementAssets.md) | Get and set the fund management fee calculation mode.  
[FeeSuccessCalc](IMTConFund/FeeSuccessCalc.md) | Get and set the success fee calculation mode.  
[FeeSuccessMode](IMTConFund/FeeSuccessMode.md) | Get and set the time for calculating the success fee in relation to the management fee charges.  
[FeeSuccessValue](IMTConFund/FeeSuccessValue.md) | Get and set the success fee amount.  
[FeeSuccessHWM](IMTConFund/FeeSuccessHWM.md) | Get and set the period for which the excess of the hurdle rate is determined when assessing the fund management success.  
[FeeSuccessHurdleRate](IMTConFund/FeeSuccessHurdleRate.md) | Get and set the hurdle rate.  
[StateCurrentInvestors](IMTConFund/StateCurrentInvestors.md) | Get the current number of fund investors.  
[StateCurrentCaptital](IMTConFund/StateCurrentCaptital.md) | Get the current amount of capital invested into the fund.  
[AccountAdd](IMTConFund/AccountAdd.md) | Add a fund manager account.  
[AccountUpdate](IMTConFund/AccountUpdate.md) | Update a fund manager account.  
[AccountDelete](IMTConFund/AccountDelete.md) | Delete a fund manager account.  
[AccountClear](IMTConFund/AccountClear.md) | Clear the list of fund managers.  
[AccountShift](IMTConFund/AccountShift.md) | Change the position of a manager account in the list.  
[AccountTotal](IMTConFund/AccountTotal.md) | Get the number of fund managers.  
[AccountNext](IMTConFund/AccountNext.md) | Get a fund manager by index.  
[InvestorAdd](IMTConFund/InvestorAdd.md) | Add an investor for a fund.  
[InvestorUpdate](IMTConFund/InvestorUpdate.md) | Edit a fund investor.  
[InvestorDelete](IMTConFund/InvestorDelete.md) | Delete an investor from the fund.  
[InvestorClear](IMTConFund/InvestorClear.md) | Clear the list of fund investors.  
[InvestorShift](IMTConFund/InvestorShift.md) | Change the position of a fund investor in the list.  
[InvestorTotal](IMTConFund/InvestorTotal.md) | Get the number of fund investors.  
[InvestorNext](IMTConFund/InvestorNext.md) | Get a fund investor by index.  
  
The IMTConFund class contains the following enumerations:

Enumeration | Description  
---|---  
[EnFlags (#enflags)](IMTConFund/Enumerations.md#enflags) | Additional properties of the fund.  
[EnType (#entype)](IMTConFund/Enumerations.md#entype) | Fund types.  
[EnRecalculation (#enrecalculation)](IMTConFund/Enumerations.md#enrecalculation) | Fund chart recalculation modes.  
[EnFeeMode (#enfeemode)](IMTConFund/Enumerations.md#enfeemode) | Fund management and success fee calculation modes.  
[EnFeePeriod (#enfeeperiod)](IMTConFund/Enumerations.md#enfeeperiod) | Fund management and success fee calculation periods.  
[EnFeeAssests (#enfeeassests)](IMTConFund/Enumerations.md#enfeeassests) | Fund management fee calculation modes.  
[EnFeeSuccessCalc (#enfeesuccesscalc)](IMTConFund/Enumerations.md#enfeesuccesscalc) | Success fee calculation modes.  
[EnFeeSuccessModes (#enfeesuccessmodes)](IMTConFund/Enumerations.md#enfeesuccessmodes) | Success fee calculation modes.  
[EnFeeSuccessHWMType (#enfeesuccesshwmtype)](IMTConFund/Enumerations.md#enfeesuccesshwmtype) | Modes for determining the fund management success.
