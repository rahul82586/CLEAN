[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / Data Structure

[Previous](../Groups.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

A group configuration is passed in JSON format in a response to the [/api/group/next](Get-by-Index.md) and [/api/group/get](Get-by-Name.md) requests.

<a id="group"></a>
## Group Parameters (#group)

The group configuration includes the following parameters:

Option Field | Type | Description  
Group | String | The name of a group, including a path to it in accordance with the hierarchy.  
Server | Integer | The ID of the trade server, to which the group is linked.  
PermissionsFlags | Integer | Flags of group permissions. Passed as a value of the [EnPermissionsFlags (#enpermissionsflags)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enpermissionsflags) enumeration (sum of values of appropriate flags).  
AuthMode | Integer | Authorization mode for accounts in the group. Passed in a value of the [EnAuthMode (#enauthmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enauthmode) enumeration.  
AuthPasswordMin | Integer | The minimum password length for accounts in the group. The minimum possible password length is 8 characters and the maximum is 16 characters.  
Company | String | Name of the company that services the group.  
CompanyPage | String | The website address of the company that services the group.  
CompanyEmail | String | The email address of the company that services the group.  
CompanySupportPage | String | The technical support website address of the company that services the group.  
CompanySupportEmail | String | The technical support email address of the company that services the group.  
CompanyCatalog | String | The name of the subdirectory that stores the templates of reports, emails, etc. for the company that services this group. for the company that services this group.  
Currency | String | The group deposit currency.  
CurrencyDigits | Integer | The number of digits after the decimal point in the group deposit currency.  
ReportsMode | Integer | Report generation modes. Passed in a value of the [EnReportsMode (#enreportsmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enreportsmode) enumeration.  
ReportsFlags | Integer | Report sending options. Passed as a value of the [EnReportsFlags (#enreportsflags)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enreportsflags) enumeration (sum of values of appropriate flags).  
ReportsSMTP | String | Address of SMTP server for sending reports.  
ReportsSMTPLogin | String | A login for the authorization on the SMTP server that is used for sending reports.  
ReportsSMTPPass | String | A password for the authorization on the SMTP server that is used for sending reports.  
NewsMode | Integer | The mode of news sending to the clients from the group. Passed in a value of the [EnNewsMode (#ennewsmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#ennewsmode) enumeration.  
NewsCategory | String | The categories of news received by the group. Use the backslash character "\" to specify subcategories.  
NewsLangs | Array of integers | The array of languages, in which the group receives news. The language is specified in the LANGID format used in the [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) (value from Prim.lang.identifier).  
MailMode | Integer | The mode of operation of the internal mail system for the group. Passed in a value of the [EnMailMode (#enmailmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmailmode) enumeration.  
TradeFlags | Integer | Trade options of the group. Passed as a value of the [EnTradeFlags (#entradeflags)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#entradeflags) enumeration (sum of values of appropriate flags).  
TradeInterestrate | Float | The annual interest rate on deposits of the group accounts.  
TradeVirtualCredit | Float | The amount of additional funds that a brokerage company can provide to a client for opening a position with a volume larger than allowed by the client's current funds.  
MarginFreeMode | Integer | The mode of using of floating profit/loss in the free margin. Passed in a value of the [EnFreeMarginMode (#enfreemarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enfreemarginmode) enumeration.  
MarginSOMode | Integer | The mode of checking the levels of Stop Out and Margin Call. Passed in a value of the [EnStopOutMode (#enstopoutmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enstopoutmode) enumeration.  
MarginCall | Float | The level of Margin Call. Units are determined by the MarginSOMode parameter.  
MarginStopOut | Float | The level of Stop Out. Units are determined by the MarginSOMode parameter.  
MarginFreeProfitMode | Integer | The mode of using the profit/loss fixed during a trade day in the free margin.  
MarginMode | Integer | The risk management model of the group. Passed in a value of the [EnMarginMode (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode) enumeration.  
MarginLeverageProfile | String | [Floating margin](../../../../Configuration-Interfaces/Floating-Margin/IMTConLeverage.md) profile applied to the group.  
DemoLeverage | Integer | The default credit leverage for demo accounts opened in the group.  
DemoDeposit | Float | The default amount of deposit for demo accounts opened in the group.  
LimitHistory | Integer | The maximum number of days, for which the group can request data on conducted trade operation. Passed in a value of the [EnHistoryLimit (#enhistorylimit)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enhistorylimit) enumeration.  
LimitOrders | Integer | The maximum number of orders that can be simultaneously placed by an account from this group.  
LimitSymbols | Integer | The maximum number of symbols, for which an account can simultaneously receive quotes.  
LimitPositions | Integer | Get and set the maximum number of open positions that can be present simultaneously on a client account from this group.  
LimitPositionsVolume | Float | Currently the field is not used.  
Commissions | Array of objects | The array of [commission settings (#commission)](Data-Structure.md#commission).  
Symbols | Array of objects | The array of individual [symbol settings (#symbol)](Data-Structure.md#symbol) symbol settings.  
TradeTransferMode | Integer | Get and set the mode of money transfer between accounts.  
  
<a id="commission"></a>
## Commission Parameters (#commission)

Commission parameters are passed in an array inside the [Commissions (#group)](Data-Structure.md#group) parameter of a group.

Option Field | Type | Description  
Name | String | Name of the commission configuration.  
Description | String | Description of the commission configuration.  
Path | String | The path to a symbol or group of symbols that are subject to commission.  
Mode | Integer | Type of commission. Passed in a value of the [EnCommMode (#encommmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommmode) enumeration.  
RangeMode | Integer | Type of commission ranges — by trade volume or turnover. Passed in a value of the [EnCommRangeMode (#encommrangemode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommrangemode) enumeration.  
ChargeMode | Integer | Time of commission charging. Passed in a value of the [EnCommChargeMode (#encommchargemode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommchargemode) enumeration.  
TurnoverCurrency | String | Currency, in which the [money turnover](../../../../Configuration-Interfaces/Groups/IMTConCommission/TurnoverCurrency.md) is calculated.  
EntryMode | Integer | Commission calculation mode depending on the trade direction. The mode is passed as a value of the [EnCommEntryMode (#encommentrymode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommentrymode) enumeration.  
ActionMode | Integer | Commission calculation mode depending on the trade type. The mode is passed as a value of the [EnCommActionMode (#encommactionmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommactionmode) enumeration.  
ProfitMode | Integer | Commission calculation mode depending on the trade result (profit/loss). The mode is passed as a value of the [EnCommProfitMode (#encommprofitmode)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommprofitmode) enumeration.  
ReasonMode | Integer | Commission calculation mode depending on the trade reason. The mode is passed as a value of the [EnCommReasonFlags (#encommreasonflags)](../../../../Configuration-Interfaces/Groups/IMTConCommission/Enumerations.md#encommreasonflags) enumeration.  
Tiers | Array of objects | An array of [commission ranges (#comm-level)](Data-Structure.md#comm-level).  
  
<a id="comm-level"></a>
## Commission Level Parameters (#comm-level)

Commission levels are passed in an array in the [Tiers (#commission)](Data-Structure.md#commission) parameter of commission.

Option Field | Type | Description  
Mode | Integer | The method of commission charging. Passed in a value of the [EnCommissionMode (#encommissionmode)](../../../../Configuration-Interfaces/Groups/IMTConCommTier/Enumerations.md#encommissionmode) enumeration.  
Type | Integer | The type of commission charging. Passed in a value of the [EnCommissionVolumeType (#encommissionvolumetype)](../../../../Configuration-Interfaces/Groups/IMTConCommTier/Enumerations.md#encommissionvolumetype) enumeration.  
Value | Float | Commission amount.  
Minimal | Float | The minimum amount of commission charged.  
RangeFrom | Float | The minimum trade volume (turnover) from which the commission will be charged.  
RangeTo | Float | The maximum trade volume (turnover) from which the commission will be charged.  
Currency | String | Currency, which is used for commission calculation. This field is used only in the [COMM_MONEY_SPECIFIED (#encommissionmode)](../../../../Configuration-Interfaces/Groups/IMTConCommTier/Enumerations.md#encommissionmode) mode of commission calculation.  
  
<a id="symbol"></a>
## Group Symbol Parameters (#symbol)

Individual settings of symbols for a group are passed in an array inside the [Symbols (#group)](Data-Structure.md#group) parameter of the group configuration.

> The "default" value of the parameter means that for this group the parameter is not defined and its value corresponds to common symbol settings of the platform.

Option Field | Type | Description  
Path | String | The path to a symbol or group of symbols that are subject to the special group settings.  
TradeMode | Integer | The symbol trading mode for the group. Passed in a value of the [EnTradeMode (#entrademode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entrademode) enumeration.  
ExecMode | Integer | The symbol execution mode for the group. Passed in a value of the [EnExecutionMode (#enexecutionmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enexecutionmode) enumeration.  
FillFlags | Integer | Types of filling allowed for the symbol in this group. Passed as a value of the [EnFillingFlags (#enfillingflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enfillingflags) enumeration (sum of values of appropriate flags).  
ExpirFlags | Integer | Types of order expiration allowed for the symbol in this group. Passed as a value of the [EnExpirtationFlags (#enexpirationflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enexpirationflags) enumeration (sum of values of appropriate flags).  
SpreadDiff | Integer | Difference between the symbol spread for the group and the default spread.  
SpreadDiffBalance | Integer | The balance of spread difference set for the group. he balance of spread difference is set a shift from the equal distribution of the spread difference value between Bid and Ask prices. For example, if the spread difference is equal to 4 and it is distributed as -2 Bid/+2 Ask, then the balance of spread difference value is 0. Ratio -3 Bid/+1 Ask corresponds to -1, ratio -1 Bid/+3 Ask corresponds to 1.  
StopsLevel | Integer | The price band, within which the group is not allowed to place stop orders for a symbol.  
FreezeLevel | Integer | The price band, within which it is not allowed to modify orders and positions for the group.  
VolumeMin | Integer | The minimum volume of trade operations for a symbol for the group. One unit corresponds to 1/10000 lot.  
VolumeMax | Integer | The maximum volume of trade operations for a symbol for the group. One unit corresponds to 1/10000 lot.  
VolumeStep | Integer | The step of change of trade operations volume for a symbol for the group. One unit corresponds to 1/10000 lot.  
VolumeLimit | Integer | The maximum allowable aggregate volume of positions and orders on a symbol in one direction for this group. One unit corresponds to 1/10000 lot.  
MarginFlags | Integer | The additional modes of symbol margin checking for the group. Passed in a value of the [EnMarginFlags (#enmarginflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enmarginflags).  
MarginInitial | Float | The size of initial symbol margin for the group.  
MarginMaintenance | Float | The size of symbol maintenance margin for the group.  
MarginInitialBuy | Float | The initial margin rate for market Buy orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY.  
MarginInitialSell | Float | The initial margin rate for market Sell orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL.  
MarginInitialBuyLimit | Float | The initial margin rate for Buy Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_LIMIT.  
MarginInitialSellLimit | Float | The initial margin rate for Sell Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_LIMIT.  
MarginInitialBuyStop | Float | The initial margin rate for Buy Stop orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_STOP.  
MarginInitialSellStop | Float | The initial margin rate for Sell Stop orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_STOP.  
MarginInitialBuyStopLimit | Float | The initial margin rate for Buy Stop Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_STOP_LIMIT.  
MarginInitialSellStopLimit | Float | The initial margin rate for Sell Stop Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_STOP_LIMIT.  
MarginMaintenanceBuy | Float | The maintenance margin rate for market Buy orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY.  
MarginMaintenanceSell | Float | The maintenance margin rate for market Sell orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL.  
MarginMaintenanceBuyLimit | Float | The maintenance margin rate for Buy Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_LIMIT.  
MarginMaintenanceSellLimit | Float | The maintenance margin rate for Sell Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_LIMIT.  
MarginMaintenanceBuyStop | Float | The maintenance margin rate for Buy Stop orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_STOP.  
MarginMaintenanceSellStop | Float | The maintenance margin rate for Sell Stop orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_STOP.  
MarginMaintenanceBuyStopLimit | Float | The maintenance margin rate for Buy Stop Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_BUY_STOP_LIMIT.  
MarginMaintenanceSellStopLimit | Float | The maintenance margin rate for Sell Stop Limit orders. In the PHP and .NET implementation, the coefficient is stored in the MarginRateInitial array and is available by index MTEnMarginRateTypes::MARGIN_RATE_SELL_STOP_LIMIT.  
MarginHedged | Float | The hedged margin value.  
SwapMode | Integer | The swap calculation mode for a certain symbol for the group. Passed in a value of the [EnSwapMode (#enswapmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enswapmode) enumeration. To use basic swap settings for the group, you should specify default values for all parameters, including SwapMode, SwapLong, SwapShort, Swap3Day and SwapYearDays. Thus, setting a default value for SwapMode alone is not enough.  
SwapLong | Float | The long position swap for a symbol for the group.  
SwapShort | Float | The short position swap for a symbol for the group.  
Swap3Day | Integer | A day of charging a triple swap for a symbol for this group.  
SwapYearDays | Integer | The number of days in a year used in calculating swap percent for a given group. Passed by the [EnSwapDays (#enswapdays)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enswapdays) enumeration value.  
SwapFlags | Integer | Additional swap settings by symbol for the given group. Passed by the [EnSwapFlags (#enswapflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enswapflags) enumeration value.  
SwapRateSunday | Float | Sunday swap multiplier in symbol settings for the given group.  
SwapRateMonday | Float | Monday swap multiplier in symbol settings for the given group.  
SwapRateTuesday | Float | Tuesday swap multiplier in symbol settings for the given group.  
SwapRateWednesday | Float | Wednesday swap multiplier in symbol settings for the given group.  
SwapRateThursday | Float | Thursday swap multiplier in symbol settings for the given group.  
SwapRateFriday | Float | Friday swap multiplier in symbol settings for the given group.  
SwapRateSaturday | Float | Saturday swap multiplier in symbol settings for the given group.  
RETimeout | Integer | Time in seconds during which the price issued by a dealer in the request execution mode is valid.  
IECheckMode | Integer | The mode of checking during instant execution set for a group. Passed in a value of the [EnInstantMode (#eninstantmode)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#eninstantmode) enumeration.  
IETimeout | Integer | The maximum allowed difference between the time of arrival of the price, at which the client places an order, and the time of the last price. Specified in seconds.  
IESlipProfit | Integer | The maximum allowed slippage in the profitable direction during instant execution.  
IESlipLosing | Integer | The maximum allowed slippage in the loss direction during instant execution.  
IEVolumeMax | Integer | The maximum volume of a trade operation that can be executed in the instant execution mode. One unit corresponds to 1/10000 lot.  
OrderFlags | Integer | The flags of order types that are allowed for the symbol. Passed in a value of the [EnOrderFlags (#enorderflags)](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#enorderflags) enumeration (sum of values of appropriate flags).  
MarginRateLiquidity | Float | The liquidity rate of the symbol for the group. It determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity).  
REFlags | Integer | The flags of request execution for the group. Passed in a value of the [EnREFlags (#enreflags)](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/Enumerations.md#enreflags) enumeration (sum of values of appropriate flags).  
PermissionsFlags | Integer | Get and set permission flags for the group symbols. Passed in a value of the [EnPermissionsFlags (#enpermissionsflags)](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/Enumerations.md#enpermissionsflags) enumeration (sum of values of appropriate flags).
