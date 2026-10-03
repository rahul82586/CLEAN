[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDatasetField](../IMTDatasetField.md) / Enumerations

[Previous](../IMTDatasetField.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTDatasetField](../IMTDatasetField.md) interface contains the following enumerations:

  * [IMTDatasetField::EnFieldType (#enfieldtype)](Enumerations.md#enfieldtype)
  * [IMTDatasetField::EnFieldId (#enfieldid)](Enumerations.md#enfieldid)
  * [IMTDatasetField::EnFieldFlags (#enfieldflags)](Enumerations.md#enfieldflags)
  * [IMTDatasetField::EnGender (#engender)](Enumerations.md#engender)
  * [IMTDatasetField::EnClientType (#enclienttype)](Enumerations.md#enclienttype)
  * [IMTDatasetField::EnClientStatus (#enclientstatus)](Enumerations.md#enclientstatus)
  * [IMTDatasetField::EnEmployment (#enemployment)](Enumerations.md#enemployment)
  * [IMTDatasetField::EnEmploymentIndustry (#enemploymentindustry)](Enumerations.md#enemploymentindustry)
  * [IMTDatasetField::EnEducationLevel (#eneducationlevel)](Enumerations.md#eneducationlevel)
  * [IMTDatasetField::EnWealthSource (#enwealthsource)](Enumerations.md#enwealthsource)
  * [IMTDatasetField::EnPreferredCommunication (#enpreferredcommunication)](Enumerations.md#enpreferredcommunication)
  * [IMTDatasetField::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience)



<a id="enfieldtype"></a>
## IMTDatasetField::EnFieldType (#enfieldtype)

Field types are enumerated in IMTDatasetField::EnFieldType:

Identifier | Value | Description  
TYPE_NONE | 0 | None.  
TYPE_INT | 1 | Integer.  
TYPE_UINT | 2 | Unsigned integer.  
TYPE_DOUBLE | 3 | Floating point number.  
TYPE_STRING | 4 | String.  
TYPE_FIRST |  | Beginning of enumeration. Corresponds to TYPE_NONE.  
TYPE_LAST |  | End of enumeration. It corresponds to TYPE_STRING.  
  
The enumeration is used in the [IMTDatasetField::Type](Type.md) method.

<a id="enfieldid"></a>
## IMTDatasetField::EnFieldId (#enfieldid)

IMTDatasetField::EnFieldId contains identifiers for matching IMTDatasetField fields and user/client/deal record fields:

Identifier | Value | Type | Description  
---|---|---|---  
Trading Account Fields  
FIELD_USER_LOGIN | 1 | int | User login (account number). Corresponds to [IMTUser::Login](../../../Database-Interfaces/Users/IMTUser/Login.md).  
FIELD_USER_GROUP | 2 | string | User group. Corresponds to [IMTUser::Group](../../../Database-Interfaces/Users/IMTUser/Group.md).  
FIELD_USER_CERT_SERIAL_NUMBER | 3 | uint | The number of the last certificate which was used by the client for authorization. Corresponds to [IMTUser::CertSerialNumber](../../../Database-Interfaces/Users/IMTUser/CertSerialNumber.md).  
FIELD_USER_RIGHTS | 4 | uint | User permissions. Corresponds to [IMTUser::Rights](../../../Database-Interfaces/Users/IMTUser/Rights.md).  
FIELD_USER_REGISTRATION | 5 | int | Account creation dates. Corresponds to [IMTUser::Registration](../../../Database-Interfaces/Users/IMTUser/Registration.md).  
FIELD_USER_LAST_ACCESS | 6 | int | The date of the last connection using the account. Corresponds to [IMTUser::LastAccess](../../../Database-Interfaces/Users/IMTUser/LastAccess.md).  
FIELD_USER_NAME | 7 | string | The name of the client in the account. Corresponds to [IMTUser::Name](../../../Database-Interfaces/Users/IMTUser/Name.md).  
FIELD_USER_COMPANY | 8 | string | Client's company name. Corresponds to [IMTUser::Company](../../../Database-Interfaces/Users/IMTUser/Company.md).  
FIELD_USER_ACCOUNT | 9 | string | Client account in the external trading system. Corresponds to [IMTUser::Account](../../../Database-Interfaces/Users/IMTUser/Account.md).  
FIELD_USER_COUNTRY | 10 | string | Client's country of residence. Corresponds to [IMTUser::Country](../../../Database-Interfaces/Users/IMTUser/Country.md).  
FIELD_USER_LANGUAGE | 11 | string | User language. Corresponds to [IMTUser::Language](../../../Database-Interfaces/Users/IMTUser/Language.md).  
FIELD_USER_CITY | 12 | string | Client's city of residence. Corresponds to [IMTUser::City](../../../Database-Interfaces/Users/IMTUser/City.md).  
FIELD_USER_STATE | 13 | string | Client's state (region) of residence. Corresponds to [IMTUser::State](../../../Database-Interfaces/Users/IMTUser/State.md).  
FIELD_USER_ZIP_CODE | 14 | string | Client's postal code. Corresponds to [IMTUser::ZIPCode](../../../Database-Interfaces/Users/IMTUser/ZipCode.md).  
FIELD_USER_ADDRESS | 15 | string | Client's address. Corresponds to [IMTUser::Address](../../../Database-Interfaces/Users/IMTUser/Address.md).  
FIELD_USER_PHONE | 16 | string | Client's phone number. Corresponds to [IMTUser::Phone](../../../Database-Interfaces/Users/IMTUser/Phone.md).  
FIELD_USER_EMAIL | 17 | string | Client's email address. Corresponds to [IMTUser::EMail](../../../Database-Interfaces/Users/IMTUser/EMail.md).  
FIELD_USER_ID | 18 | string | The number of a client's identity document. Corresponds to [IMTUser::ID](../../../Database-Interfaces/Users/IMTUser/ID.md).  
FIELD_USER_STATUS | 19 | string | Client status. Corresponds to [IMTUser::Status](../../../Database-Interfaces/Users/IMTUser/Status.md).  
FIELD_USER_COMMENT | 20 | string | Comment to the account. Corresponds to [IMTUser::Comment](../../../Database-Interfaces/Users/IMTUser/Comment.md).  
FIELD_USER_COLOR | 21 | uint | The color of the client entry. Corresponds to [IMTUser::Color](../../../Database-Interfaces/Users/IMTUser/Color.md).  
FIELD_USER_PHONE_PASSWORD | 22 | string | Client's phone password. Corresponds to [IMTUser::PhonePassword](../../../Database-Interfaces/Users/IMTUser/PhonePassword.md).  
FIELD_USER_LEVERAGE | 23 | uint | Account leverage. Corresponds to [IMTUser::Leverage](../../../Database-Interfaces/Users/IMTUser/Leverage.md).  
FIELD_USER_AGENT | 24 | uint | Client's agent account number. Corresponds to [IMTUser::Agent](../../../Database-Interfaces/Users/IMTUser/Agent.md).  
FIELD_USER_BALANCE | 25 | double | Account balance. Corresponds to [IMTUser::Balance](../../../Database-Interfaces/Users/IMTUser/Balance.md).  
FIELD_USER_CREDIT | 26 | double | The amount of funds credited to the account. Corresponds to [IMTUser::Credit](../../../Database-Interfaces/Users/IMTUser/Credit.md).  
FIELD_USER_INTEREST_RATE | 27 | double | The annual interest rate amount accrued for the current month. Corresponds to [IMTUser::InterestRate](../../../Database-Interfaces/Users/IMTUser/InterestRate.md).  
FIELD_USER_COMMISSION_DAILY | 28 | double | The amount of commissions charged from the account per day. Corresponds to [IMTUser::CommissionDaily](../../../Database-Interfaces/Users/IMTUser/CommissionDaily.md).  
FIELD_USER_COMMISSION_MONTHLY | 29 | double | The total amount of commissions charged from the account for the current month. Corresponds to [IMTUser::CommissionMonthly](../../../Database-Interfaces/Users/IMTUser/CommissionMonthly.md).  
FIELD_USER_COMMISSION_AGENT_DAILY | 30 | double | The amount of agent commissions charged for trade operations performed on the account, for the day. Corresponds to [IMTUser::CommissionAgentDaily](../../../Database-Interfaces/Users/IMTUser/CommissionAgentDaily.md).  
FIELD_USER_COMMISSION_AGENT_MONTHLY | 31 | double | The amount of agent commissions charged for trade operations on the account for the current month. Corresponds to [IMTUser::CommissionAgentMonthly](../../../Database-Interfaces/Users/IMTUser/CommissionAgentMonthly.md).  
FIELD_USER_BALANCE_PREV_DAY | 32 | double | Account balance as of the end of the previous day. Corresponds to [IMTUser::BalancePrevDay](../../../Database-Interfaces/Users/IMTUser/BalancePrevDay.md).  
FIELD_USER_BALANCE_PREV_MONTH | 33 | double | Account balance as of the end of the previous trading month. Corresponds to [IMTUser::BalancePrevMonth](../../../Database-Interfaces/Users/IMTUser/BalancePrevMonth.md).  
FIELD_USER_EQUITY_PREV_DAY | 34 | double | Account equity as of the end of the previous day. Corresponds to [IMTUser::EquityPrevDay](../../../Database-Interfaces/Users/IMTUser/EquityPrevDay.md).  
FIELD_USER_EQUITY_PREV_MONTH | 35 | double | Account equity as of the end of the previous month. Corresponds to [IMTUser::EquityPrevMonth](../../../Database-Interfaces/Users/IMTUser/EquityPrevMonth.md).  
FIELD_USER_LAST_PASS_CHANGE | 36 | int | Date of the last account password change. Corresponds to [IMTUser::LastPassChange](../../../Database-Interfaces/Users/IMTUser/LastPassChange.md).  
FIELD_USER_MQID | 37 | string | Client's MetaQuotes ID. Corresponds to [IMTUser::MQID](../../../Database-Interfaces/Users/IMTUser/MQID.md).  
FIELD_USER_LEAD_CAMPAIGN | 38 | string | Lead campaign — the name of an advertising campaign by which the client who opened this account, was attracted. Corresponds to [IMTUser::LeadSource](../../../Database-Interfaces/Users/IMTUser/LeadSource.md).  
FIELD_USER_LEAD_SOURCE | 39 | string | Lead source — a website the a client has come from. Corresponds to [IMTUser::LeadCampaign](../../../Database-Interfaces/Users/IMTUser/LeadCampaign.md).  
FIELD_USER_CLIENT_ID | 40 | uint | The ID of the client to whom the account belongs. Corresponds to [IMTUser::Login](../../../Database-Interfaces/Users/IMTUser/Login.md).  
FIELD_USER_FIRST |  |  | Beginning of enumeration of trading account fields. Corresponds to FIELD_USER_LOGIN.  
FIELD_USER_LAST |  |  | End of enumeration of trading account fields. Corresponds to FIELD_USER_CLIENT_ID.  
Client Fields  
FIELD_CLIENT_ID | 1001 | uint | Client ID.  
FIELD_CLIENT_CREATED_TIME | 1002 | int | Client creation date in the number of seconds since 01.01.1970.  
FIELD_CLIENT_CREATED_BY | 1003 | int | The login of the manager who created the client.  
FIELD_CLIENT_MODIFIED_TIME | 1004 | int | The date of the last modification of the client record, in seconds since 01.01.1970.  
FIELD_CLIENT_MODIFIED_BY | 1005 | int | The login of the manager who made the last changes to the client record.  
FIELD_CLIENT_TYPE | 1006 | uint | Client type. Passed as a value from the [IMTDatasetField::EnClientType (#enclienttype)](Enumerations.md#enclienttype) enumeration.  
FIELD_CLIENT_STATUS | 1007 | uint | Client status. Passed as a value from the [IMTDatasetField::EnClientStatus (#enclientstatus)](Enumerations.md#enclientstatus) enumeration.  
FIELD_CLIENT_ASSIGNED_MANAGER | 1008 | int | The login of the manager who is responsible the client.  
FIELD_CLIENT_COMMENT | 1009 | string | A comment to the client record.  
FIELD_CLIENT_COMPLIANCE_APPROVED_BY | 1010 | int | The login of the manager who approved the client.  
FIELD_CLIENT_COMPLIANCE_CLIENT_CATEGORY | 1011 | string | Client compliance category (client classification based on the regulator rules).  
FIELD_CLIENT_COMPLIANCE_TIME_APPROVAL | 1012 | int | Client approval time in seconds since 01.01.1970.  
FIELD_CLIENT_COMPLIANCE_TIME_TERMINATION | 1013 | int | Date of termination of service provision to the client in seconds since 01.01.1970.  
FIELD_CLIENT_LEAD_CAMPAIGN | 1014 | string | Lead campaign — the name of an advertising campaign the client was attracted by.  
FIELD_CLIENT_LEAD_SOURCE | 1015 | string | Lead source — a website the client has come from.  
FIELD_CLIENT_INTRODUCER | 1016 | int | The login (trading account) of the user who attracted this client.  
FIELD_CLIENT_PERSON_TITLE | 1017 | string | Client title, such as Mr. or Mrs.  
FIELD_CLIENT_PERSON_NAME | 1018 | string | The client's first name.  
FIELD_CLIENT_PERSON_MIDDLE_NAME | 1019 | string | The client's middle name.  
FIELD_CLIENT_PERSON_LAST_NAME | 1020 | string | The client's last name.  
FIELD_CLIENT_PERSON_BIRTH_DATE | 1021 | int | The client's date birth in seconds since 01.01.1970.  
FIELD_CLIENT_PERSON_CITIZENSHIP | 1022 | string | The client's citizenship.  
FIELD_CLIENT_PERSON_GENDER | 1023 | int | The client's gender. Passed as a value from the [IMTDatasetField::EnClientType (#engender)](Enumerations.md#engender) enumeration.  
FIELD_CLIENT_PERSON_TAX_ID | 1024 | string | The client's tax payer ID, such as TIN.  
FIELD_CLIENT_PERSON_DOCUMENT_TYPE | 1025 | string | Client's document: passport, driver's license, etc.  
FIELD_CLIENT_PERSON_DOCUMENT_NUMBER | 1026 | string | Document number.  
FIELD_CLIENT_PERSON_DOCUMENT_DATE | 1027 | int | Client's document issue date in seconds since 01.01.1970.  
FIELD_CLIENT_PERSON_DOCUMENT_EXTRA | 1028 | string | Additional client details.  
FIELD_CLIENT_PERSON_EMPLOYMENT | 1029 | uint | Client's employment status. Passed as a value of the [IMTDatasetField::EnEmployment (#enemployment)](Enumerations.md#enemployment) enumeration.  
FIELD_CLIENT_PERSON_INDUSTRY | 1030 | uint | Client's employment industry. Passed as a value of the [IMTDatasetField::EnEmploymentIndustry (#enemploymentindustry)](Enumerations.md#enemploymentindustry) enumeration.  
FIELD_CLIENT_PERSON_EDUCATION | 1031 | uint | Client's education. Passed as a value of the [IMTDatasetField::EnEducationLevel (#eneducationlevel)](Enumerations.md#eneducationlevel) enumeration.  
FIELD_CLIENT_PERSON_WEALTH_SOURCE | 1032 | uint | Client's income source. Passed as a value of the [IMTDatasetField::EnWealthSource (#enwealthsource)](Enumerations.md#enwealthsource) enumeration.  
FIELD_CLIENT_PERSON_ANNUAL_INCOME | 1033 | int | Client's annual income.  
FIELD_CLIENT_PERSON_NET_WORTH | 1034 | int | Client's net assets.  
FIELD_CLIENT_PERSON_ANNUAL_DEPOSIT | 1035 | int | Client's annual deposit.  
FIELD_CLIENT_COMPANY_NAME | 1036 | string | Company name (for corporate clients).  
FIELD_CLIENT_COMPANY_REG_NUMBER | 1037 | string | Registration number (for corporate clients).  
FIELD_CLIENT_COMPANY_REG_DATE | 1038 | int | Company registration date (for corporate clients).  
FIELD_CLIENT_COMPANY_REG_AUTHORITY | 1039 | string | Company registration authority (for corporate clients).  
FIELD_CLIENT_COMPANY_VAT | 1040 | string | VAT number (for corporate clients).  
FIELD_CLIENT_COMPANY_LEI | 1041 | string | LEI number for EMIR reports (for corporate clients).  
FIELD_CLIENT_COMPANY_LICENSE_NUMBER | 1042 | string | License number (for corporate clients).  
FIELD_CLIENT_COMPANY_LICENSE_AUTHORITY | 1043 | string | Licensing authority (for corporate clients).  
FIELD_CLIENT_COMPANY_COUNTRY | 1044 | string | Company registration country (for corporate clients).  
FIELD_CLIENT_COMPANY_ADDRESS | 1045 | string | Legal address of the company (for corporate clients).  
FIELD_CLIENT_COMPANY_WEBSITE | 1046 | string | Website address (for corporate clients).  
FIELD_CLIENT_CONTACT_PREFERRED | 1047 | string | Preferred contact method. Passed as a value of the [IMTDatasetField::EnPreferredCommunication (#enpreferredcommunication)](Enumerations.md#enpreferredcommunication) enumeration.  
FIELD_CLIENT_CONTACT_LANGUAGE | 1048 | uint | The language spoken by the client. Specified in the LANGID format used in [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) systems (a value from Prim.lang.identifier).  
FIELD_CLIENT_CONTACT_EMAIL | 1049 | string | Client's email address.  
FIELD_CLIENT_CONTACT_PHONE | 1050 | string | Client's phone number.  
FIELD_CLIENT_CONTACT_MESSENGERS | 1051 | string | List of the client's accounts in instant messengers.  
FIELD_CLIENT_CONTACT_SOCIALNETWORKS | 1052 | string | List of the client's accounts in social networks.  
FIELD_CLIENT_CONTACT_LAST_DATE | 1053 | int | The date of the last contact with the client, in seconds since 01.01.1970.  
FIELD_CLIENT_ADDRESS_COUNTRY | 1054 | string | The client's country of residence.  
FIELD_CLIENT_ADDRESS_POSTCODE | 1055 | string | The client's zip code.  
FIELD_CLIENT_ADDRESS_STREET | 1056 | string | The client's address, including the street name, building number, etc.  
FIELD_CLIENT_ADDRESS_STATE | 1057 | string | The client's region of residence.  
FIELD_CLIENT_ADDRESS_CITY | 1058 | string | The client's city of residence.  
FIELD_CLIENT_EXPERIENCE_FX | 1059 | uint | Client's Forex trading experience. Passed as a value of the [IMTDatasetField::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience) enumeration.  
FIELD_CLIENT_EXPERIENCE_CFD | 1060 | uint | Client's CFD trading experience. Passed as a value of the [IMTDatasetField::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience) enumeration.  
FIELD_CLIENT_EXPERIENCE_FUTURES | 1061 | uint | Client's Futures trading experience. Passed as a value of the [IMTDatasetField::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience) enumeration.  
FIELD_CLIENT_EXPERIENCE_STOCKS | 1062 | uint | Client's stock trading experience. Passed as a value of the [IMTDatasetField::EnTradingExperience (#entradingexperience)](Enumerations.md#entradingexperience) enumeration.  
FIELD_CLIENT_FIRST |  |  | Beginning of enumeration of client fields. Corresponds to FIELD_CLIENT_ID.  
FIELD_CLIENT_LAST |  |  | End of enumeration of client fields. Corresponds to FIELD_CLIENT_EXPERIENCE_STOCKS.  
Deal Fields  
FIELD_DEAL_DEAL | 2001 | uint | Deal ticket. Corresponds to [IMTDeal::Deal](../../../Database-Interfaces/Trade/Deals/IMTDeal/Deal.md).  
FIELD_DEAL_EXTERNAL_ID | 2002 | string | The ID of a deal in an external trading system. Corresponds to [IMTDeal::ExternalID](../../../Database-Interfaces/Trade/Deals/IMTDeal/ExternalID.md).  
FIELD_DEAL_LOGIN | 2003 | uint | The login of the client, to whom the deal belongs. Corresponds to [IMTDeal::Login](../../../Database-Interfaces/Trade/Deals/IMTDeal/Login.md).  
FIELD_DEAL_DEALER | 2004 | uint | The login of the dealer who processed the deal. Corresponds to [IMTDeal::Dealer](../../../Database-Interfaces/Trade/Deals/IMTDeal/Dealer.md).  
FIELD_DEAL_ORDER | 2005 | uint | The ticket of the order as a result of which the deal was executed. Corresponds to [IMTDeal::Order](../../../Database-Interfaces/Trade/Deals/IMTDeal/Order.md).  
FIELD_DEAL_ACTION | 2006 | uint | Type of action performed with the deal. Corresponds to [IMTDeal::Action](../../../Database-Interfaces/Trade/Deals/IMTDeal/Action.md).  
FIELD_DEAL_ENTRY | 2007 | uint | Deal direction. Corresponds to [IMTDeal::Entry](../../../Database-Interfaces/Trade/Deals/IMTDeal/Entry.md).  
FIELD_DEAL_DIGITS | 2008 | uint | Number of decimal places in the deal price. Corresponds to [IMTDeal::Digits](../../../Database-Interfaces/Trade/Deals/IMTDeal/Digits.md).  
FIELD_DEAL_DIGITS_CURRENCY | 2009 | uint | Number of decimal places in the deposit currency of the client who has executed the deal. Corresponds to [IMTDeal::DigitsCurrency](../../../Database-Interfaces/Trade/Deals/IMTDeal/DigitsCurrency.md).  
FIELD_DEAL_CONTRACT_SIZE | 2010 | double | Contract size of the symbol for which the deal was executed. Corresponds to [IMTDeal::ContractSize](../../../Database-Interfaces/Trade/Deals/IMTDeal/ContractSize.md).  
FIELD_DEAL_TIME | 2011 | int | Deal execution time. Corresponds to [IMTDeal::Time](../../../Database-Interfaces/Trade/Deals/IMTDeal/Time.md).  
FIELD_DEAL_SYMBOL | 2012 | string | The symbol, for which a deal is executed. Corresponds to [IMTDeal::Symbol](../../../Database-Interfaces/Trade/Deals/IMTDeal/Symbol.md).  
FIELD_DEAL_PRICE | 2013 | double | Deal execution price. Corresponds to [IMTDeal::Price](../../../Database-Interfaces/Trade/Deals/IMTDeal/Price.md).  
FIELD_DEAL_VOLUME_EXT | 2014 | uint | deal volume. Corresponds to [IMTDeal::VolumeExt](../../../Database-Interfaces/Trade/Deals/IMTDeal/VolumeExt.md).  
FIELD_DEAL_PROFIT | 2015 | double | Profit from a deal. Corresponds to [IMTDeal::Profit](../../../Database-Interfaces/Trade/Deals/IMTDeal/Profit.md).  
FIELD_DEAL_STORAGE | 2016 | double | Swap size for a deal. Corresponds to [IMTDeal::Storage](../../../Database-Interfaces/Trade/Deals/IMTDeal/Storage.md).  
FIELD_DEAL_COMMISSION | 2017 | double | Commission amount charged for a deal. Corresponds to [IMTDeal::Commission](../../../Database-Interfaces/Trade/Deals/IMTDeal/Commission.md).  
FIELD_DEAL_RATE_PROFIT | 2018 | double | The exchange rate for converting deal profit currency to the deposit currency of a client group. Corresponds to [IMTDeal::RateProfit](../../../Database-Interfaces/Trade/Deals/IMTDeal/RateProfit.md).  
FIELD_DEAL_RATE_MARGIN | 2019 | double | The exchange rate for converting deal margin currency to client deposit currency. Corresponds to [IMTDeal::RateMargin](../../../Database-Interfaces/Trade/Deals/IMTDeal/RateMargin.md).  
FIELD_DEAL_EXPERT_ID | 2020 | uint | The ID of the Expert Advisor which has executed the deal. Corresponds to [IMTDeal::ExpertID](../../../Database-Interfaces/Trade/Deals/IMTDeal/ExpertID.md).  
FIELD_DEAL_POSITION_ID | 2021 | uint | Position identifier (ticket) for the deal. Corresponds to [IMTDeal::PositionID](../../../Database-Interfaces/Trade/Deals/IMTDeal/PositionID.md).  
FIELD_DEAL_COMMENT | 2022 | string | Deal comment. Corresponds to [IMTDeal::Comment](../../../Database-Interfaces/Trade/Deals/IMTDeal/Comment.md).  
FIELD_DEAL_PROFIT_RAW | 2023 | double | Profit/loss gained as a result of performing a deal. Corresponds to [IMTDeal::ProfitRaw](../../../Database-Interfaces/Trade/Deals/IMTDeal/ProfitRaw.md).  
FIELD_DEAL_PRICE_POSITION | 2024 | double | The price of the position closed by this deal. Corresponds to [IMTDeal::PricePosition](../../../Database-Interfaces/Trade/Deals/IMTDeal/PricePosition.md).  
FIELD_DEAL_VOLUME_CLOSED_EXT | 2025 | uint | Position volume closed by the deal. Corresponds to [IMTDeal::VolumeClosedExt](../../../Database-Interfaces/Trade/Deals/IMTDeal/VolumeClosedExt.md).  
FIELD_DEAL_TICK_VALUE | 2026 | double | Tick price for the deal. Corresponds to [IMTDeal::TickValue](../../../Database-Interfaces/Trade/Deals/IMTDeal/TickValue.md).  
FIELD_DEAL_TICK_SIZE | 2027 | double | Tick value for the deal. Corresponds to [IMTDeal::TickSize](../../../Database-Interfaces/Trade/Deals/IMTDeal/TickSize.md).  
FIELD_DEAL_FLAGS | 2028 | uint | Common flags of a deal. Corresponds to [IMTDeal::Flags](../../../Database-Interfaces/Trade/Deals/IMTDeal/Flags.md).  
FIELD_DEAL_TIME_MSC | 2029 | int | Deal execution time in milliseconds. Corresponds to [IMTDeal::TimeMsc](../../../Database-Interfaces/Trade/Deals/IMTDeal/TimeMsc.md).  
FIELD_DEAL_REASON | 2030 | uint | Reason for the deal. corresponds to [IMTDeal::Reason](../../../Database-Interfaces/Trade/Deals/IMTDeal/Reason.md).  
FIELD_DEAL_GATEWAY | 2031 | string | ID of a gateway, through which the deal was executed Corresponds to [IMTDeal::Gateway](../../../Database-Interfaces/Trade/Deals/IMTDeal/Gateway.md).  
FIELD_DEAL_PRICE_GATEWAY | 2032 | double | The actual price of a deal conducted via a gateway in an external trading system, not taking into account the gateway price transformation settings. Corresponds to [IMTDeal::PriceGateway](../../../Database-Interfaces/Trade/Deals/IMTDeal/PriceGateway.md).  
FIELD_DEAL_MODIFICATION_FLAGS | 2033 | uint | Deal modification flags. Corresponds to [IMTDeal::ModificationFlags](../../../Database-Interfaces/Trade/Deals/IMTDeal/ModificationFlags.md).  
FIELD_DEAL_PRICE_SL | 2034 | double | Stop Loss level of the deal. Corresponds to [IMTDeal::PriceSL](../../../Database-Interfaces/Trade/Deals/IMTDeal/PriceSL.md).  
FIELD_DEAL_PRICE_TP | 2035 | double | Take Profit level of the deal. Corresponds to [IMTDeal::PriceTP](../../../Database-Interfaces/Trade/Deals/IMTDeal/PriceTP.md).  
FIELD_DEAL_FEE | 2036 | double | Fee amount per deal. Corresponds to [IMTDeal::Fee](../../../Database-Interfaces/Trade/Deals/IMTDeal/Fee.md).  
FIELD_DEAL_VALUE | 2037 | double | The deal execution value in the client's deposit currency. Corresponds to [IMTDeal::Value](../../../Database-Interfaces/Trade/Deals/IMTDeal/Value.md).  
FIELD_DEAL_MARKET_BID | 2038 | double | The market Bid price as at the time of deal execution by the server. Corresponds to [IMTDeal::MarketBid](../../../Database-Interfaces/Trade/Deals/IMTDeal/MarketBid.md).  
FIELD_DEAL_MARKET_ASK | 2039 | double | The market Ask price as at the time of deal execution by the server. Corresponds to [IMTDeal::MarketAsk](../../../Database-Interfaces/Trade/Deals/IMTDeal/MarketAsk.md).  
FIELD_DEAL_MARKET_LAST | 2040 | double | The market Last price as at the time of deal execution by the server. Corresponds to [IMTDeal::MarketLast](../../../Database-Interfaces/Trade/Deals/IMTDeal/MarketLast.md).  
FIELD_DEAL_FIRST |  |  | Beginning of enumeration of deal fields. Corresponds to FIELD_DEAL_DEAL.  
FIELD_DEAL_LAST |  |  | End of enumeration of deal fields. Corresponds to FIELD_DEAL_PRICE_TP.  
Order fields  
FIELD_ORDER_ORDER | 3001 | uint | Order ticket. Corresponds to[IMTOrder::Order](../../../Database-Interfaces/Trade/Orders/IMTOrder/Order.md).  
FIELD_ORDER_EXTERNAL_ID | 3002 | string | Order ID in external trading systems. Corresponds to [IMTOrder::ExternalID](../../../Database-Interfaces/Trade/Orders/IMTOrder/ExternalID.md).  
FIELD_ORDER_LOGIN | 3003 | uint | The login of the client, to whom the order belongs. Corresponds to [IMTOrder::Login](../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md).  
FIELD_ORDER_DEALER | 3004 | uint | The login of a dealer, who has processed an order. Corresponds to [IMTOrder::Dealer](../../../Database-Interfaces/Trade/Orders/IMTOrder/Dealer.md).  
FIELD_ORDER_SYMBOL | 3005 | string | Order symbol. Corresponds to [IMTOrder::Symbol](../../../Database-Interfaces/Trade/Orders/IMTOrder/Symbol.md).  
FIELD_ORDER_TIME_SETUP | 3006 | int | Order placing time. Corresponds to [IMTOrder::TimeSetup](../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeSetup.md).  
FIELD_ORDER_TIME_EXPIRATION | 3007 | int | Order expiration time. Corresponds to [IMTOrder::TimeExpiration](../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeExpiration.md).  
FIELD_ORDER_TIME_DONE | 3008 | int | Order execution time. Corresponds to [IMTOrder::TimeDone](../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDone.md).  
FIELD_ORDER_TYPE | 3009 | uint | Order type. Corresponds to [IMTOrder::Type](../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md).  
FIELD_ORDER_TYPE_FILL | 3010 | uint | Order filling type. Corresponds to [IMTOrder::TypeFill](../../../Database-Interfaces/Trade/Orders/IMTOrder/TypeFill.md).  
FIELD_ORDER_TYPE_TIME | 3011 | uint | Order expiration type. Corresponds to [IMTOrder::TypeTime](../../../Database-Interfaces/Trade/Orders/IMTOrder/TypeTime.md).  
FIELD_ORDER_TYPE_REASON | 3012 | uint | Reason for placing an order. Corresponds to [IMTOrder::Reason](../../../Database-Interfaces/Trade/Orders/IMTOrder/Reason.md).  
FIELD_ORDER_PRICE_ORDER | 3013 | double | Order price. Corresponds to [IMTOrder::PriceOrder](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md).  
FIELD_ORDER_PRICE_TRIGGER | 3014 | double | Price at which a limit order is placed upon triggering of a stop limit order. Corresponds to [IMTOrder::PriceTrigger](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceTrigger.md).  
FIELD_ORDER_PRICE_CURRENT | 3015 | double | The current price of the symbol, for which an order has been placed. Corresponds to [IMTOrder::PriceCurrent](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceCurrent.md).  
FIELD_ORDER_PRICE_SL | 3016 | double | The Stop Loss level of an order. Corresponds to [IMTOrder::PriceSL](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceSL.md).  
FIELD_ORDER_PRICE_TP | 3017 | double | The Take Profit level of an order. Corresponds to [IMTOrder::PriceTP](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceTP.md).  
FIELD_ORDER_VOLUME_INITIAL | 3018 | uint | Initial volume of the order. Corresponds to [IMTOrder::VolumeInitialExt](../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitialExt.md).  
FIELD_ORDER_VOLUME_CURRENT | 3019 | uint | The current unfilled volume of an order. Corresponds to [IMTOrder::VolumeCurrentExt](../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrentExt.md).  
FIELD_ORDER_STATE | 3020 | uint | Current order state. Corresponds to [IMTOrder::State](../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md).  
FIELD_ORDER_EXPERT_ID | 3021 | uint | The ID of the Expert Advisor that has placed the order. [IMTOrder::ExpertID](../../../Database-Interfaces/Trade/Orders/IMTOrder/ExpertID.md)  
FIELD_ORDER_POSITION_ID | 3022 | uint | The position ID (ticket) set in the order. Corresponds to [IMTOrder::PositionID](../../../Database-Interfaces/Trade/Orders/IMTOrder/PositionID.md).  
FIELD_ORDER_COMMENT | 3023 | string | Comment to an order. Corresponds to [IMTOrder::Comment](../../../Database-Interfaces/Trade/Orders/IMTOrder/Comment.md).  
FIELD_ORDER_CONTRACT_SIZE | 3024 | double | The contract size of the symbol, for which an order was placed. Corresponds to [IMTOrder::ContractSize](../../../Database-Interfaces/Trade/Orders/IMTOrder/ContractSize.md).  
FIELD_ORDER_DIGITS | 3025 | uint | The number of decimal places in the order price. Corresponds to [IMTOrder::Digits](../../../Database-Interfaces/Trade/Orders/IMTOrder/Digits.md).  
FIELD_ORDER_DIGITS_CURRENCY | 3026 | uint | The number of decimal places the deposit currency of the client who has placed the order. Corresponds to [IMTOrder::DigitsCurrency](../../../Database-Interfaces/Trade/Orders/IMTOrder/DigitsCurrency.md).  
FIELD_ORDER_POSITION_BY_ID | 3027 | uint | Position identifier (ticket) of the opposite position for the order. Corresponds to [IMTOrder::PositionByID](../../../Database-Interfaces/Trade/Orders/IMTOrder/PositionByID.md).  
FIELD_ORDER_MARGIN_RATE | 3028 | double | The exchange rate for converting the symbol margin currency to the client deposit currency used for calculating the margin for the order. Corresponds to [IMTOrder::RateMargin](../../../Database-Interfaces/Trade/Orders/IMTOrder/RateMargin.md).  
FIELD_ORDER_TIME_SETUP_MSC | 3029 | int | Order placing time in milliseconds. Corresponds to [IMTOrder::TimeSetupMsc](../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeSetupMsc.md).  
FIELD_ORDER_TIME_DONE_MSC | 3030 | int | Order execution time in milliseconds. Corresponds to [IMTOrder::TimeDoneMsc](../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDoneMsc.md).  
FIELD_ORDER_MODIFICATION_FLAGS | 3031 | uint | Order modification flags. Corresponds to [IMTOrder::ModificationFlags](../../../Database-Interfaces/Trade/Orders/IMTOrder/ModificationFlags.md).  
FIELD_ORDER_ACTIVATION_MODE | 3032 | uint | Order activation type. Corresponds to [IMTOrder::ActivationMode](../../../Database-Interfaces/Trade/Orders/IMTOrder/ActivationMode.md).  
FIELD_ORDER_ACTIVATION_TIME | 3033 | int | Order activation time. Corresponds to [IMTOrder::ActivationTime](../../../Database-Interfaces/Trade/Orders/IMTOrder/ActivationTime.md).  
FIELD_ORDER_ACTIVATION_PRICE | 3034 | double | The price, at which the order was activated. Corresponds to [IMTOrder::ActivationPrice](../../../Database-Interfaces/Trade/Orders/IMTOrder/ActivationPrice.md).  
FIELD_ORDER_ACTIVATION_FLAGS | 3035 | uint | Order activation flags. Corresponds to [IMTOrder::ActivationFlags](../../../Database-Interfaces/Trade/Orders/IMTOrder/ActivationFlags.md).  
FIELD_ORDER_GROUP | 3036 | string | The group of the client who has placed the order.  
FIELD_ORDER_FIRST |  |  | Beginning of enumeration of order fields. Corresponds to FIELD_ORDER_ORDER.  
FIELD_ORDER_LAST |  |  | End of enumeration of order fields. Corresponds to FIELD_ORDER_GROUP.  
Daily Report fields |  |  |   
FIELD_DAILY_DATE_TIME | 4001 | int | Daily report generation date and time. Corresponds to [IMTDaily::Datetime](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Datetime.md).  
FIELD_DAILY_DATE_TIME_PREV | 4002 | int | The date and time of the previous daily report generation. Corresponds to [IMTDaily::DatetimePrev](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DatetimePrev.md).  
FIELD_DAILY_LOGIN | 4003 | uint | The login of the client for whom the daily report is generated. Corresponds to [IMTDaily::Login](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Login.md).  
FIELD_DAILY_NAME | 4004 | string | The name of a client in a daily report. Corresponds to [IMTDaily::Name](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Name.md).  
FIELD_DAILY_GROUP | 4005 | string | Client group in a daily report. Corresponds to [IMTDaily::Group](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Group.md).  
FIELD_DAILY_CURRENCY | 4006 | string | Client's deposit currency in a daily report. Corresponds to [IMTDaily::Currency](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Currency.md).  
FIELD_DAILY_DIGITS_CURRENCY | 4007 | uint | The number of decimal places in the client's deposit currency in a daily report. Corresponds to [IMTDaily::CurrencyDigits](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/CurrencyDigits.md).  
FIELD_DAILY_COMPANY | 4008 | string | The company which manages the client group in a daily report. Corresponds to [IMTDaily::Company](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Company.md).  
FIELD_DAILY_EMAIL | 4009 | string | An email of a client in a daily report. Corresponds to [IMTDaily::EMail](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/EMail.md).  
FIELD_DAILY_BALANCE | 4010 | double | The client balance amount in a daily report. Corresponds to [IMTDaily::Balance](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Balance.md).  
FIELD_DAILY_CREDIT | 4011 | double | The amount of a client's credit funds in a daily report. Corresponds to [IMTDaily::Credit](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Credit.md).  
FIELD_DAILY_INTEREST_RATE | 4012 | double | The annual interest rate of a client in a daily report. Corresponds to [IMTDaily::InterestRate](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/InterestRate.md).  
FIELD_DAILY_COMMISSION_DAILY | 4013 | double | The amount of commissions charged from a client for a day in the report. Corresponds to [IMTDaily::CommissionDaily](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/CommissionDaily.md).  
FIELD_DAILY_COMMISSION_MONTHLY | 4014 | double | The total amount of commissions charged from a client for the current month in a report. Corresponds to [IMTDaily::CommissionMonthly](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/CommissionMonthly.md).  
FIELD_DAILY_AGENT_DAILY | 4015 | double | The size of agent commissions charged for a client's trading operations for a day. Corresponds to [IMTDaily::AgentDaily](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/AgentDaily.md).  
FIELD_DAILY_AGENT_MONTHLY | 4016 | double | The amount of agent commissions charged for a client's trading operations for the current month. Corresponds to [IMTDaily::AgentMonthly](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/AgentMonthly.md).  
FIELD_DAILY_BALANCE_PREV_DAY | 4017 | double | Client balance as of the end of the previous day. Corresponds to [IMTDaily::BalancePrevDay](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/BalancePrevDay.md).  
FIELD_DAILY_BALANCE_PREV_MONTH | 4018 | double | Client balance as of the end of the previous trading month. Corresponds to [IMTDaily::BalancePrevMonth](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/BalancePrevMonth.md).  
FIELD_DAILY_EQUITY_PREV_DAY | 4019 | double | Client equity as of the end of the previous day. Corresponds to [IMTDaily::EquityPrevDay](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/EquityPrevDay.md).  
FIELD_DAILY_EQUITY_PREV_MONTH | 4020 | double | Client equity amount as of the end of the previous trading month. Corresponds to [IMTDaily::EquityPrevMonth](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/EquityPrevMonth.md).  
FIELD_DAILY_MARGIN | 4021 | double | Client margin amount in a daily report. Corresponds to [IMTDaily::Margin](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Margin.md).  
FIELD_DAILY_MARGIN_FREE | 4022 | double | The amount of the client's free margin in a daily report. Corresponds to [IMTDaily::MarginFree](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/MarginFree.md).  
FIELD_DAILY_MARGIN_LEVEL | 4023 | double | The margin level of a client in the daily report. Corresponds to [IMTDaily::MarginLevel](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/MarginLevel.md).  
FIELD_DAILY_MARGIN_LEVERAGE | 4024 | uint | The margin leverage of a client in the daily report. Corresponds to [IMTDaily::MarginLeverage](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/MarginLeverage.md).  
FIELD_DAILY_PROFIT | 4025 | double | The size of the current profit for all open positions of a client in a daily report. Corresponds to [IMTDaily::Profit](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/Profit.md).  
FIELD_DAILY_PROFIT_STORAGE | 4026 | double | The current size of swaps charged for a client's open positions for a day, but not yet reflected in the balance. Corresponds to [IMTDaily::ProfitStorage](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/ProfitStorage.md).  
FIELD_DAILY_PROFIT_COMMISSION | 4027 | double | The current unfixed commission of a client in a daily report. Corresponds to [IMTDaily::ProfitCommission](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/ProfitCommission.md).  
FIELD_DAILY_PROFIT_EQUITY | 4028 | double | The amount of the current floating equity of a client in a daily report. Corresponds to [IMTDaily::ProfitEquity](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/ProfitEquity.md).  
FIELD_DAILY_DAILY_PROFIT | 4029 | double | The amount of a client's recorded daily profit. Corresponds to [IMTDaily::DailyProfit](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyProfit.md).  
FIELD_DAILY_DAILY_BALANCE | 4030 | double | The amount accrued to a client's balance during the reported day. Corresponds to [IMTDaily::DailyBalance](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyBalance.md).  
FIELD_DAILY_DAILY_CREDIT | 4031 | double | The amount of credit given to a client during the reported day. Corresponds to [IMTDaily::DailyCredit](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyCredit.md).  
FIELD_DAILY_DAILY_CHARGE | 4032 | double | The amount of other charges to the client's balance during the reported day. Corresponds to [IMTDaily::DailyCharge](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyCharge.md).  
FIELD_DAILY_DAILY_CORRECTION | 4033 | double | The amount of corrective balance operations for the reported day. Corresponds to [IMTDaily::DailyCorrection](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyCorrection.md).  
FIELD_DAILY_DAILY_BONUS | 4034 | double | The amount of bonuses transfered to the client's balance for the reported day. Corresponds to [IMTDaily::DailyBonus](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyBonus.md).  
FIELD_DAILY_DAILY_STORAGE | 4035 | double | The amount of swaps calculated for a client for a reported day. Corresponds to [IMTDaily::DailyStorage](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyStorage.md).  
FIELD_DAILY_DAILY_COMM_INSTANT | 4036 | double | The amount of client's instant commissions for the client during the reported day. Corresponds to [IMTDaily::DailyCommInstant](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyCommInstant.md).  
FIELD_DAILY_DAILY_COMM_ROUND | 4037 | double | The amount of client's turnover commissions for a reported day. Corresponds to [IMTDaily::DailyCommRound](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyCommRound.md).  
FIELD_DAILY_DAILY_AGENT | 4038 | double | The size of agent commissions charged for a client's trading operations for a reported day. Corresponds to [IMTDaily::DailyAgent](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyAgent.md).  
FIELD_DAILY_DAILY_INTEREST | 4039 | double | The amount accrued to a client as part of the annual interest rate for the reported day. Corresponds to [IMTDaily::DailyInterest](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/DailyInterest.md).  
FIELD_DAILY_PROFIT_ASSETS | 4040 | double | The current amount of a client's assets in a daily report. Corresponds to [IMTDaily::ProfitAssets](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/ProfitAssets.md).  
FIELD_DAILY_PROFIT_LIABILITIES | 4041 | double | The current amount of a client's liabilities in a daily report. Corresponds to [IMTDaily::ProfitLiabilities](../../../Database-Interfaces/Trade/Daily-Reports/IMTDaily/ProfitLiabilities.md).  
FIELD_DAILY_FIRST |  |  | Beginning of enumeration of the daily report fields. Corresponds to FIELD_DAILY_DATE_TIME.  
FIELD_DAILY_LAST |  |  | End of enumeration of the daily report fields. Corresponds to FIELD_DAILY_PROFIT_LIABILITIES.  
Position fields  
FIELD_POSITION_LOGIN | 5001 | uint | The login of the client, to whom the trade position belongs. Corresponds to [IMTPosition::Login](../../../Database-Interfaces/Trade/Positions/IMTPosition/Login.md).  
FIELD_POSITION_SYMBOL | 5002 | string | The symbol of the trading position. Corresponds to [IMTPosition::Symbol](../../../Database-Interfaces/Trade/Positions/IMTPosition/Symbol.md).  
FIELD_POSITION_ACTION | 5003 | uint | Position type. Corresponds to [IMTPosition::Action](../../../Database-Interfaces/Trade/Positions/IMTPosition/Action.md).  
FIELD_POSITION_DIGITS | 5004 | uint | The number of decimal places in the position price. Corresponds to [IMTPosition::Digits](../../../Database-Interfaces/Trade/Positions/IMTPosition/Digits.md).  
FIELD_POSITION_DIGITS_CURRENCY | 5005 | uint | The number of decimal places in the deposit currency of the client by whom the position was opened. Corresponds to [IMTPosition::DigitsCurrency](../../../Database-Interfaces/Trade/Positions/IMTPosition/DigitsCurrency.md).  
FIELD_POSITION_CONTRACT_SIZE | 5006 | double | The contract size of the symbol, for which the position is opened. Corresponds to [IMTPosition::ContractSize](../../../Database-Interfaces/Trade/Positions/IMTPosition/ContractSize.md).  
FIELD_POSITION_TIME_CREATE | 5007 | int | Position creation time. Corresponds to [IMTPosition::TimeCreate](../../../Database-Interfaces/Trade/Positions/IMTPosition/TimeCreate.md).  
FIELD_POSITION_TIME_UPDATE | 5008 | int | Last position modification time. Corresponds to [IMTPosition::TimeUpdate](../../../Database-Interfaces/Trade/Positions/IMTPosition/TimeUpdate.md).  
FIELD_POSITION_PRICE_OPEN | 5009 | double | The weighted average position open price. Corresponds to [IMTPosition::PriceOpen](../../../Database-Interfaces/Trade/Positions/IMTPosition/PriceOpen.md).  
FIELD_POSITION_PRICE_CURRENT | 5010 | double | The current price of the symbol, for which a trade position was opened. Corresponds to [IMTPosition::PriceCurrent](../../../Database-Interfaces/Trade/Positions/IMTPosition/PriceCurrent.md).  
FIELD_POSITION_PRICE_SL | 5011 | double | The position Stop Loss level. Corresponds to [IMTPosition::PriceSL](../../../Database-Interfaces/Trade/Positions/IMTPosition/PriceSL.md).  
FIELD_POSITION_PRICE_TP | 5012 | double | The position Take Profit level. Corresponds to [IMTPosition::PriceTP](../../../Database-Interfaces/Trade/Positions/IMTPosition/PriceTP.md).  
FIELD_POSITION_VOLUME | 5013 | uint | Trading position volume. Corresponds to [IMTPosition::Volume](../../../Database-Interfaces/Trade/Positions/IMTPosition/Volume.md).  
FIELD_POSITION_PROFIT | 5014 | double | Current profit/loss of a trading position. Corresponds to [IMTPosition::Profit](../../../Database-Interfaces/Trade/Positions/IMTPosition/Profit.md).  
FIELD_POSITION_STORAGE | 5015 | double | Position swap amount. Corresponds to [IMTPosition::Storage](../../../Database-Interfaces/Trade/Positions/IMTPosition/Storage.md).  
FIELD_POSITION_RATE_PROFIT | 5016 | double | The rate of conversion of the position profit currency to the client group deposit currency. Corresponds to [IMTPosition::RateProfit](../../../Database-Interfaces/Trade/Positions/IMTPosition/RateProfit.md).  
FIELD_POSITION_RATE_MARGIN | 5017 | double | The rate of conversion of the position margin currency to the client's deposit currency. Corresponds to [IMTPosition::RateMargin](../../../Database-Interfaces/Trade/Positions/IMTPosition/RateMargin.md).  
FIELD_POSITION_EXPERT_ID | 5018 | uint | The ID of the Expert Advisor which opened the position. Corresponds to [IMTPosition::ExpertID](../../../Database-Interfaces/Trade/Positions/IMTPosition/ExpertID.md).  
FIELD_POSITION_EXPERT_POSITION_ID | 5019 | uint | Position identifier. Corresponds to [IMTPosition::ExpertPositionID](../../../Database-Interfaces/Trade/Positions/IMTPosition/ExpertPositionID.md).  
FIELD_POSITION_COMMENT | 5020 | string | A comment to the position. Corresponds to [IMTPosition::Comment](../../../Database-Interfaces/Trade/Positions/IMTPosition/Comment.md).  
FIELD_POSITION_ACTIVATION_MODE | 5021 | uint | Position activation type. Corresponds to [IMTPosition::ActivationMode](../../../Database-Interfaces/Trade/Positions/IMTPosition/ActivationMode.md).  
FIELD_POSITION_ACTIVATION_TIME | 5022 | int | Position activation time. Corresponds to [IMTPosition::ActivationTime](../../../Database-Interfaces/Trade/Positions/IMTPosition/ActivationTime.md).  
FIELD_POSITION_ACTIVATION_PRICE | 5023 | double | Position activation price. Corresponds to [IMTPosition::ActivationPrice](../../../Database-Interfaces/Trade/Positions/IMTPosition/ActivationPrice.md).  
FIELD_POSITION_ACTIVATION_FLAGS | 5024 | uint | Position activation flag. Corresponds to [IMTPosition::ActivationFlags](../../../Database-Interfaces/Trade/Positions/IMTPosition/ActivationFlags.md).  
FIELD_POSITION_TIME_CREATE_MSC | 5025 | int | Position creation time in milliseconds. Corresponds to [IMTPosition::TimeCreateMsc](../../../Database-Interfaces/Trade/Positions/IMTPosition/TimeCreateMsc.md).  
FIELD_POSITION_TIME_UPDATE_MSC | 5026 | int | Last position modification time in milliseconds. Corresponds to [IMTPosition::TimeUpdateMsc](../../../Database-Interfaces/Trade/Positions/IMTPosition/TimeUpdateMsc.md).  
FIELD_POSITION_DEALER | 5027 | uint | The login of the dealer by whom the open position was processed. Corresponds to [IMTPosition::Dealer](../../../Database-Interfaces/Trade/Positions/IMTPosition/Dealer.md).  
FIELD_POSITION_POSITION | 5028 | uint | Trading position ticket (unique number) in the MetaTrader 5 platform. Corresponds to [IMTPosition::Position](../../../Database-Interfaces/Trade/Positions/IMTPosition/Position.md).  
FIELD_POSITION_EXTERNAL_ID | 5029 | uint | Position ticket (unique number) in the external trading system. Corresponds to [IMTPosition::ExternalID](../../../Database-Interfaces/Trade/Positions/IMTPosition/ExternalID.md).  
FIELD_POSITION_MODIFICATION_FLAGS | 5030 | uint | Position modification flag. Corresponds to [IMTPosition::ModificationFlags](../../../Database-Interfaces/Trade/Positions/IMTPosition/ModificationFlags.md).  
FIELD_POSITION_REASON | 5031 | uint | The reason for opening a position Corresponds to [IMTPosition::Reason](../../../Database-Interfaces/Trade/Positions/IMTPosition/Reason.md).  
FIELD_POSITION_VOLUME_EXT | 5032 | uint | Trading position volume with a high accuracy. Corresponds to [IMTPosition::VolumeExt](../../../Database-Interfaces/Trade/Positions/IMTPosition/VolumeExt.md).  
FIELD_POSITION_GROUP | 5033 | string | The group of the client who has opened the position.  
FIELD_POSITION_FIRST |  |  | Beginning of enumeration of position fields. Corresponds to FIELD_POSITION_LOGIN.  
FIELD_POSITION_LAST |  |  | End of enumeration of position fields. Corresponds to FIELD_POSITION_GROUP.  
Account trading state fields  
FIELD_ACCOUNT_LOGIN | 6001 | uint | The login of the client, to whom the trading account belongs. Corresponds to [IMTAccount::Login](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Login.md).  
FIELD_ACCOUNT_GROUP | 6002 | string | The group to which the account belongs.  
FIELD_ACCOUNT_CURRENCY_DIGITS | 6003 | uint | The number of decimal places in the account deposit currency. Corresponds to [IMTAccount::CurrencyDigits](../../../Database-Interfaces/Trade/Accounts/IMTAccount/CurrencyDigits.md).  
FIELD_ACCOUNT_BALANCE | 6004 | double | Trading account balance. Corresponds to [IMTAccount::Balance](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Balance.md).  
FIELD_ACCOUNT_CREDIT | 6005 | double | The current amount of credit given to an account. Corresponds to [IMTAccount::Credit](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Credit.md).  
FIELD_ACCOUNT_MARGIN | 6006 | double | The current value of the account margin. Corresponds to [IMTAccount::Margin](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Margin.md).  
FIELD_ACCOUNT_MARGIN_FREE | 6007 | double | The free margin of an account. Corresponds to [IMTAccount::MarginFree](../../../Database-Interfaces/Trade/Accounts/IMTAccount/MarginFree.md).  
FIELD_ACCOUNT_MARGIN_LEVEL | 6008 | double | Margin level as a percentage. Corresponds to [IMTAccount::MarginLevel](../../../Database-Interfaces/Trade/Accounts/IMTAccount/MarginLevel.md).  
FIELD_ACCOUNT_MARGIN_LEVERAGE | 6009 | uint | Leverage margin. Corresponds to [IMTAccount::MarginLeverage](../../../Database-Interfaces/Trade/Accounts/IMTAccount/MarginLeverage.md).  
FIELD_ACCOUNT_MARGIN_INITIAL | 6010 | double | The current size of the initial margin of positions on a trading account. Corresponds to [IMTAccount::MarginInitial](../../../Database-Interfaces/Trade/Accounts/IMTAccount/MarginInitial.md).  
FIELD_ACCOUNT_MARGIN_MAINTENANCE | 6011 | double | The current size of the maintenance margin of positions on a trading account. Corresponds to [IMTAccount::MarginMaintenance](../../../Database-Interfaces/Trade/Accounts/IMTAccount/MarginMaintenance.md).  
FIELD_ACCOUNT_PROFIT | 6012 | double | The size of the current profit for all open positions. Corresponds to [IMTAccount::Profit](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Profit.md).  
FIELD_ACCOUNT_STORAGE | 6013 | double | The size of swaps charged for open positions on the account. Corresponds to [IMTAccount::Storage](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Storage.md).  
FIELD_ACCOUNT_COMMISSION | 6014 | double | The size of commissions charged for all transactions on the account. Corresponds to [IMTAccount::Commission](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Commission.md).  
FIELD_ACCOUNT_FLOATING | 6015 | double | The size of floating profit/loss of open positions on the account. Corresponds to [IMTAccount::Floating](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Floating.md).  
FIELD_ACCOUNT_EQUITY | 6016 | double | The account equity. Corresponds to [IMTAccount::Equity](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Equity.md).  
FIELD_ACCOUNT_BLOCKED_COMMISSION | 6017 | double | The amount of the standard commission locked on the account, which has been accumulated during the day/month. Corresponds to [IMTAccount::BlockedCommission](../../../Database-Interfaces/Trade/Accounts/IMTAccount/BlockedCommission.md).  
FIELD_ACCOUNT_BLOCKED_PROFIT | 6018 | double | The amount of intraday profit blocked on the account. Corresponds to [IMTAccount::BlockedProfit](../../../Database-Interfaces/Trade/Accounts/IMTAccount/BlockedProfit.md).  
FIELD_ACCOUNT_ASSETS | 6019 | double | The current total amount of assets on a trading account. Corresponds to [IMTAccount::Assets](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Assets.md).  
FIELD_ACCOUNT_LIABILITIES | 6020 | double | The current total amount of liabilities on a trading account. Corresponds to [IMTAccount::Liabilities](../../../Database-Interfaces/Trade/Accounts/IMTAccount/Liabilities.md).  
FIELD_ACCOUNT_STOP_OUT_ACTIVATION | 6021 | uint | The account status as per the minimum amount of funds on the account required to maintain trading positions. Corresponds to [IMTAccount::SOActivation](../../../Database-Interfaces/Trade/Accounts/IMTAccount/SOActivation.md).  
FIELD_ACCOUNT_STOP_OUT_TIME | 6022 | int | The time when the Margin Call or Stop Out level was reached. Corresponds to [IMTAccount::SOTime](../../../Database-Interfaces/Trade/Accounts/IMTAccount/SOTime.md).  
FIELD_ACCOUNT_STOP_OUT_LEVEL | 6023 | double | The margin level of an account at the time it reached the Stop Out level. Corresponds to [IMTAccount::SOLevel](../../../Database-Interfaces/Trade/Accounts/IMTAccount/SOLevel.md).  
FIELD_ACCOUNT_STOP_OUT_EQUITY | 6024 | double | The account equity at the time the account reached the Stop Out level. Corresponds to [IMTAccount::SOEquity](../../../Database-Interfaces/Trade/Accounts/IMTAccount/SOEquity.md).  
FIELD_ACCOUNT_STOP_OUT_MARGIN | 6025 | double | The account margin volume at the time the account reached the Stop Out level. Corresponds to [IMTAccount::SOMargin](../../../Database-Interfaces/Trade/Accounts/IMTAccount/SOMargin.md).  
FIELD_ACCOUNT_FIRST |  |  | Beginning of enumeration of account trading state fields. Corresponds to FIELD_ACCOUNT_LOGIN.  
FIELD_ACCOUNT_LAST |  |  | End of enumeration of account trading state fields. Corresponds to FIELD_ACCOUNT_STOP_OUT_MARGIN.  
FIELD_FIRST |  |  | Enumeration beginning. Corresponds to FIELD_USER_LOGIN.  
FIELD_LAST |  |  | End of enumeration. Corresponds to FIELD_ACCOUNT_LAST.  
  
The enumeration is used in the [IMTDatasetField::Id](Id.md) method.

<a id="enfieldflags"></a>
## IMTDatasetField::EnFieldFlags (#enfieldflags)

Field flags are enumerated in IMTDatasetField::EnFieldFlags:

Identifier | Value | Description  
FLAG_NONE | 0x0000000 | No flags.  
FLAG_SELECT | 0x0000001 | The field is selected. If this flag is enabled, the corresponding field will be included in the resulting data set. Otherwise the field will only be used for filtering during data request.  
FLAG_DEFAULT |  | Default flags. Corresponds to enabling of FLAG_SELECT.  
FLAG_ALL |  | Enable all flags.  
  
The enumeration is used in the [IMTDatasetField::Flags](Flags.md) methods.

<a id="engender"></a>
## IMTDatasetField::EnGender (#engender)

IMTDatasetField::EnGender contains the values of the Gender property:

Identifier | Value | Description  
GENDER_UNSPECIFIED | 0 | Not specified.  
GENDER_MALE | 1 | Male.  
GENDER_FEMALE | 2 | Female.  
GENDER_FIRST |  | Beginning of enumeration. Corresponds to GENDER_UNSPECIFIED.  
GENDER_LAST |  | End of enumeration. Corresponds to GENDER_FEMALE.  
  
The enumeration is used for [IMTDatasetField::FIELD_CLIENT_PERSON_GENDER (#enfieldtype)](Enumerations.md#enfieldtype) fields.

<a id="enclienttype"></a>
## IMTDatasetField::EnClientType (#enclienttype)

IMTDatasetField::EnClientType contains client types:

Identifier | Value | Description  
CLIENT_TYPE_UNDEFINED | 0 | Not set.  
CLIENT_TYPE_INDIVIDUAL | 1 | Private.  
CLIENT_TYPE_CORPORATE | 2 | Corporate.  
CLIENT_TYPE_FUND | 3 | Fund.  
CLIENT_TYPE_FIRST |  | Beginning of enumeration. Corresponds to CLIENT_TYPE_UNDEFINED.  
CLIENT_TYPE_LAST |  | End of enumeration. Corresponds to CLIENT_TYPE_CORPORATE.  
  
The enumeration is used in the [IMTDatasetField::Type](Type.md) method.

<a id="enclientstatus"></a>
## IMTDatasetField::EnClientStatus (#enclientstatus)

Client statuses are enumerated in IMTDatasetField::EnClientStatus:

Identifier | Value | Description  
CLIENT_STATUS_UNREGISTERED | 0 | Not registered.  
CLIENT_STATUS_REGISTERED | 100 | Registered.  
CLIENT_STATUS_NOTINTERESTED | 200 | Not interested.  
CLIENT_STATUS_APPLICATION_INCOMPLETED | 300 | Not completed.  
CLIENT_STATUS_APPLICATION_COMPLETED | 400 | Completed.  
CLIENT_STATUS_APPLICATION_INFORMATION | 500 | Informed.  
CLIENT_STATUS_APPLICATION_REJECTED | 600 | Rejected.  
CLIENT_STATUS_APPROVED | 700 | Approved.  
CLIENT_STATUS_FUNDED | 800 | Funded.  
CLIENT_STATUS_ACTIVE | 900 | Active.  
CLIENT_STATUS_INACTIVE | 1000 | Inactive.  
CLIENT_STATUS_SUSPENDED | 1100 | Suspended.  
CLIENT_STATUS_CLOSED | 1200 | Closed.  
CLIENT_STATUS_TERMINATED | 1300 | Terminated.  
CLIENT_STATUS_FIRST |  | Beginning of enumeration. Corresponds to CLIENT_STATUS_UNREGISTERED.  
CLIENT_STATUS_LAST |  | End of enumeration. Corresponds to CLIENT_STATUS_TERMINATED.  
  
The enumeration is used for [IMTDatasetField::FIELD_CLIENT_STATUS (#enfieldtype)](Enumerations.md#enfieldtype) fields.

<a id="enemployment"></a>
## IMTDatasetField::EnEmployment (#enemployment)

IMTDatasetField::EnEmployment contains client types by employment:

Identifier | Value | Description  
EMPLOY_UNEMPLOYED | 0 | Unemployed.  
EMPLOY_EMPLOYED | 1 | Employed.  
EMPLOY_SELF_EMPLOYED | 2 | Entrepreneur or self-employed.  
EMPLOY_RETIRED | 3 | Retired.  
EMPLOY_STUDENT | 4 | Student.  
EMPLOY_OTHER | 5 | Other.  
EMPLOY_FIRST |  | Beginning of enumeration. Corresponds to EMPLOY_UNEMPLOYED.  
EMPLOY_LAST |  | End of enumeration. Corresponds to EMPLOY_OTHER.  
  
The enumeration is used for [IMTDatasetField::FIELD_CLIENT_PERSON_EMPLOYMENT (#enfieldtype)](Enumerations.md#enfieldtype) fields.

<a id="enemploymentindustry"></a>
## IMTDatasetField::EnEmploymentIndustry (#enemploymentindustry)

IMTDatasetField::EnEmploymentIndustry contains the enumeration of client employment areas:

Identifier | Value | Description  
INDUSTRY_NONE | 0 | None.  
INDUSTRY_AGRICULTURE | 1 | Agriculture, food and natural resources.  
INDUSTRY_CONSTRUCTION | 2 | Architecture and construction.  
INDUSTRY_MANAGEMENT | 3 | Administration and business management.  
INDUSTRY_COMMUNICATION | 4 | Art, audio/video technology and communication.  
INDUSTRY_EDUCATION | 5 | Education and training.  
INDUSTRY_GOVERNMENT | 6 | State and administrative management.  
INDUSTRY_HEALTHCARE | 7 | Health care.  
INDUSTRY_TOURISM | 8 | Tourism and hospitality.  
INDUSTRY_IT | 9 | Information technology.  
INDUSTRY_SECURITY | 10 | Legal and public safety, correction and protection services.  
INDUSTRY_MANUFACTURING | 11 | Production.  
INDUSTRY_MARKETING | 12 | Marketing and sales.  
INDUSTRY_SCIENCE | 13 | Science and technology.  
INDUSTRY_ENGINEERING | 14 | Engineering and mathematics.  
INDUSTRY_TRANSPORT | 15 | Transportation, distribution and logistics.  
INDUSTRY_OTHER | 16 | Other.  
INDUSTRY_FIRST |  | Beginning of enumeration. Corresponds to INDUSTRY_NONE.  
INDUSTRY_LAST |  | End of enumeration. Corresponds to INDUSTRY_OTHER.  
  
The enumeration is used for [IMTDatasetField::FIELD_CLIENT_PERSON_INDUSTRY (#enfieldtype)](Enumerations.md#enfieldtype) fields.

<a id="eneducationlevel"></a>
## IMTDatasetField::EnEducationLevel (#eneducationlevel)

IMTDatasetField::EnEducationLevel contains the enumeration of client education levels:

Identifier | Value | Description  
EDUCATION_LEVEL_NONE | 0 | None.  
EDUCATION_LEVEL_HIGH_SCHOOL | 1 | Secondary.  
EDUCATION_LEVEL_BACHELOR | 2 | Bachelor's degree or equivalent.  
EDUCATION_LEVEL_MASTER | 3 | Master's degree or equivalent.  
EDUCATION_LEVEL_PHD | 4 | PhD or equivalent.  
EDUCATION_LEVEL_OTHER | 5 | Other.  
EDUCATION_LEVEL_FIRST |  | Beginning of enumeration. Corresponds to EDUCATION_LEVEL_NONE.  
EDUCATION_LEVEL_LAST |  | End of enumeration. Corresponds to EDUCATION_LEVEL_OTHER.  
  
The enumeration is used for [IMTDatasetField::FIELD_CLIENT_PERSON_EDUCATION (#enfieldtype)](Enumerations.md#enfieldtype) fields.

<a id="enwealthsource"></a>
## IMTDatasetField::EnWealthSource (#enwealthsource)

IMTDatasetField::EnWealthSource contains the enumeration of client's income sources:

Identifier | Value | Description  
WEALTH_SOURCE_EMPLOYMENT | 0 | Employment/business  
WEALTH_SOURCE_SAVINGS | 1 | Savings or investments.  
WEALTH_SOURCE_INHERITANCE | 2 | Gift or inheritance.  
WEALTH_SOURCE_OTHER | 3 | Other.  
WEALTH_SOURCE_FIRST |  | Beginning of enumeration. Corresponds to WEALTH_SOURCE_EMPLOYMENT.  
WEALTH_SOURCE_LAST |  | End of enumeration. Corresponds to WEALTH_SOURCE_OTHER.  
  
The enumeration is used for [IMTDatasetField::FIELD_CLIENT_PERSON_WEALTH_SOURCE (#enfieldtype)](Enumerations.md#enfieldtype) fields.

<a id="enpreferredcommunication"></a>
## IMTDatasetField::EnPreferredCommunication (#enpreferredcommunication)

IMTDatasetField::EnPreferredCommunication contains the enumeration of preferred client contact methods:

Identifier | Value | Description  
PREFERRED_COMMUNICATION_UNDEFINED | 0 | Not specified.  
PREFERRED_COMMUNICATION_EMAIL | 1 | Email.  
PREFERRED_COMMUNICATION_PHONE | 2 | Phone.  
PREFERRED_COMMUNICATION_PHONE_SMS | 3 | SMS.  
PREFERRED_COMMUNICATION_MESSENGER | 4 | Instant messenger.  
PREFERRED_COMMUNICATION_FIRST |  | Beginning of enumeration. Corresponds to PREFERRED_COMMUNICATION_UNDEFINED.  
PREFERRED_COMMUNICATION_LAST |  | End of enumeration. Corresponds to PREFERRED_COMMUNICATION_MESSENGER.  
  
The enumeration is used for [IMTDatasetField::FIELD_CLIENT_CONTACT_PREFERRED (#enfieldtype)](Enumerations.md#enfieldtype) fields.

<a id="entradingexperience"></a>
## IMTDatasetField::EnTradingExperience (#entradingexperience)

IMTDatasetField::EnTradingExperience contains values describing clients' financial market trading experience:

Identifier | Value | Description  
EXPERIENCE_LESS_1_YEAR | 0 | < 1 year.  
EXPERIENCE_1_3_YEAR | 1 | 1 — 3 years.  
EXPERIENCE_ABOVE_3_YEAR | 2 | > 3 year.  
EXPERIENCE_FIRST |  | Beginning of enumeration. Corresponds to EXPERIENCE_LESS_1_YEAR.  
EXPERIENCE_LAST |  | End of enumeration. Corresponds to EXPERIENCE_ABOVE_3_YEAR.  
  
The enumeration is used for the following field types:

  * [IMTDatasetField::FIELD_CLIENT_EXPERIENCE_FX (#enfieldtype)](Enumerations.md#enfieldtype)
  * [IMTDatasetField::FIELD_CLIENT_EXPERIENCE_CFD (#enfieldtype)](Enumerations.md#enfieldtype)
  * [IMTDatasetField::FIELD_CLIENT_EXPERIENCE_FUTURES (#enfieldtype)](Enumerations.md#enfieldtype)
  * [IMTDatasetField::FIELD_CLIENT_EXPERIENCE_STOCKS (#enfieldtype)](Enumerations.md#enfieldtype)


