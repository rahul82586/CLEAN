[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSCondition](../IMTConCondition.md) / IMTConCondition Enumerations

[Previous](../IMTConCondition.md) | [Next](IMTConCondition-Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConVPSCondition](../IMTConCondition.md) class contains the following enumerations:

  * [IMTConVPSCondition::EnCondition (#encondition)](IMTConCondition-Enumerations.md#encondition)
  * [IMTConVPSCondition::EnConditionRule (#enconditionrule)](IMTConCondition-Enumerations.md#enconditionrule)
  * [IMTConVPSCondition::EnConditionType (#enconditiontype)](IMTConCondition-Enumerations.md#enconditiontype)



<a id="encondition"></a>
## IMTConVPSCondition::EnCondition (#encondition)

IMTConVPSCondition::EnConditions lists conditions for VPS allocation rules.

ID | Value | Description  
CONDITION_DATETIME_DATETIME | 0 | Date and time.  
CONDITION_DATETIME_DATE | 1 | Date.  
CONDITION_DATETIME_TIME | 2 | Time  
CONDITION_DATETIME_FIRST | 0 | Beginning of the enumeration of conditions by date and time.  
CONDITION_DATETIME_LAST | 1000 | End of the enumeration of conditions by date and time.  
CONDITION_ACCOUNT_LOGIN | 1001 | Account number.  
CONDITION_ACCOUNT_GROUP | 1002 | Group name.  
CONDITION_ACCOUNT_COUNTRY | 1003 | Account owner country.  
CONDITION_ACCOUNT_CITY | 1004 | Account owner city.  
CONDITION_ACCOUNT_LANGUAGE | 1005 | Account owner language.  
CONDITION_ACCOUNT_PHONE | 1006 | Account owner phone number.  
CONDITION_ACCOUNT_EMAIL | 1007 | Account owner email address .  
CONDITION_ACCOUNT_COLOR | 1008 | Account color.  
CONDITION_ACCOUNT_COMMENT | 1009 | Comment to the account.  
CONDITION_ACCOUNT_REGISTRATION | 1010 | The date of account creation in the platform.  
CONDITION_ACCOUNT_LASTTIME | 1011 | The date of the last account connection to the server.  
CONDITION_ACCOUNT_LEVERAGE | 1012 | Account leverage  
CONDITION_ACCOUNT_BALANCE | 1013 | Account balance.  
CONDITION_ACCOUNT_CREDIT | 1014 | Credit funds on the account.  
CONDITION_ACCOUNT_POSITIONS | 1015 | The amount of open positions on the account.  
CONDITION_ACCOUNT_ORDERS | 1016 | The number of active pending orders on the account.  
CONDITION_ACCOUNT_PROFIT | 1017 | Floating profit on the account.  
CONDITION_ACCOUNT_EQUITY | 1018 | Account equity.  
CONDITION_ACCOUNT_MARGIN | 1019 | Reserved margin on the account.  
CONDITION_ACCOUNT_MARGIN_FREE | 1020 | Free margin on the account.  
CONDITION_ACCOUNT_MARGIN_LEVEL | 1021 | Account margin level.  
CONDITION_ACCOUNT_CURRENCY | 1022 | Account deposit currency.  
CONDITION_ACCOUNT_REGISTRATION_ELAPSED | 1023 | The number of days that have elapsed since account creation.  
CONDITION_ACCOUNT_LASTTIME_ELAPSED | 1024 | The number of days that have elapsed since the last connection to the account.  
CONDITION_ACCOUNT_LEAD_SOURCE | 1025 | Lead source specified in the account.  
CONDITION_ACCOUNT_LEAD_CAMPAIGN | 1026 | Lead campaign specified in the account.  
CONDITION_ACCOUNT_ONLINE | 1027 | Status of account connection to the trade server: "true" — connected, "false" — not connected.  
CONDITION_ACCOUNT_ACTIVITY_TRADE_ELAPSED | 1028 | The number of days since the last trading operation on the account. Any operations are checked: trading, balance, commission accrual, etc. In addition, the system checks if the account has any open positions or active pending orders.  
CONDITION_ACCOUNT_ENABLED | 1029 | Account status: enabled or disabled ([IMTUser::USER_RIGHT_ENABLED (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)).  
CONDITION_ACCOUNT_TRADING_ENABLED | 1030 | Permission for an account to trade ([IMTUser::USER_RIGHT_TRADE_DISABLED (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)).  
CONDITION_ACCOUNT_EXPERT_ENABLED | 1031 | Permission to trade using EAs ([IMTUser::USER_RIGHT_EXPERT (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)).  
CONDITION_ACCOUNT_OWN_FUNDS_PERCENT | 1032 | Client's funds share consisting of money the client deposited to their account. The calculation equation: (1 - (Credit / Equity)) * 100.  
CONDITION_ACCOUNT_OWN_FUNDS_VOLUME | 1033 | Client's funds volume consisting of money the client deposited to their account. The calculation equation: Equity - Credit.  
CONDITION_ACCOUNT_STATUS | 1036 | Account holder status, RE (resident) or NR (non-resident).  
CONDITION_ACCOUNT_FIRST | 1001 | Start of the enumeration of conditions by [trading account parameters](../../../Database-Interfaces/Users/IMTUser.md).  
CONDITION_ACCOUNT_LAST | 2000 | End of the enumeration of conditions by trading account parameters.  
CONDITION_FIRST |  | Enumeration start. Corresponds to CONDITION_DATETIME_FIRST.  
CONDITION_LAST |  | Enumeration end. Corresponds to CONDITION_ACCOUNT_LAST.  
  
The enumeration is used in the [IMTConVPSCondition::Condition](IMTConCondition-Condition.md) method.

<a id="enconditionrule"></a>
## IMTConVPSCondition::EnConditionRule (#enconditionrule)

IMTConVPSCondition::EnConditionRule lists parameter and value comparison types in the condition.

ID | Value | Description  
RULE_EQ | 0 | Condition of equality.  
RULE_NOT_EQ | 1 | Condition of inequality.  
RULE_GREATER | 2 | Condition of "greater than".  
RULE_NOT_LESS | 3 | Condition of "not less than".  
RULE_LESS | 4 | Condition of "less than".  
RULE_NOT_GREATER | 5 | Condition of "not greater than".  
RULE_MATCH_MASK | 6 | Mask matching condition. Here you can specify strings with the "*" mask. For example: Condition IMTConVPSCondition::CONDITION_ACCOUNT_GROUP, value "real*" — all real groups.  
RULE_FIRST |  | Enumeration start. Corresponds to RULE_EQ.  
RULE_LAST |  | Enumeration end. Corresponds to RULE_MATCH_MASK.  
  
The enumeration is used in the [IMTConVPSCondition::Rule](IMTConCondition-Rule.md) method.

<a id="enconditiontype"></a>
## IMTConVPSCondition::EnConditionType (#enconditiontype)

IMTConVPSCondition::EnConditionType lists types of parameters in the condition.

ID | Value | Description  
TYPE_NONE | 0 | Parameter is not specified.  
TYPE_STRING | 1 | The parameter is of the string type.  
TYPE_INT | 2 | The parameter is of the int type.  
TYPE_UINT | 3 | The parameter is of the uint type.  
TYPE_COLOR | 4 | The parameter is of the color type.  
TYPE_MONEY | 5 | The parameter sets the amount of money.  
TYPE_DATETIME | 6 | The parameter sets date and time (in seconds elapsed since 01.01.1970).  
TYPE_LEVERAGE | 7 | The parameter sets the leverage.  
TYPE_BOOL | 8 | The parameter sets the bool type.  
TYPE_TIME | 9 | The parameter sets time (in minutes since 00:00).  
TYPE_DATE | 10 | The parameter sets the day.  
TYPE_PERCENT | 11 | The parameter sets the percentage.  
TYPE_LANGUAGE | 12 | The parameter sets the language.  
TYPE_LOGIN | 13 | The parameter sets the account number.  
TYPE_FIRST |  | Enumeration start. Corresponds to TYPE_NONE.  
TYPE_LAST |  | Enumeration end. Corresponds to TYPE_LOGIN.  
  
The enumeration is used in the [IMTConVPSCondition::ValueType](IMTConCondition-ValueType.md) method.
