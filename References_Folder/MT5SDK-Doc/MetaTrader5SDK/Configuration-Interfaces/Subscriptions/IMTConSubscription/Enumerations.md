[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTConSubscription](../IMTConSubscription.md) / Enumerations

[Previous](../IMTConSubscription.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConSubscription](../IMTConSubscription.md) class contains the following enumerations:

  * [IMTConSubscription::EnLevel (#entype)](Enumerations.md#entype)
  * [IMTConSubscription::EnPeriod (#enperiod)](Enumerations.md#enperiod)
  * [IMTConSubscription::EnFreePeriod (#enfreeperiod)](Enumerations.md#enfreeperiod)
  * [IMTConSubscription::EnFlags (#enflags)](Enumerations.md#enflags)
  * [IMTConSubscription::EnControlMode (#encontrolmode)](Enumerations.md#encontrolmode)
  * [IMTConSubscription::EnImageType (#enimagetype)](Enumerations.md#enimagetype)



<a id="entype"></a>
## IMTConSubscription::EnType (#entype)

IMTConSubscription::EnType provides types of subscription objects.

ID | Value | Description  
TYPE_SUBSCRIPTION | 0 | The object is a subscription configuration.  
TYPE_FOLDER | 1 | The object is a subdirectory with subscription configurations. Accordingly, most of the [IMTConSubscription](../IMTConSubscription.md) properties are meaningless.  
LEVEL_FIRST |  | Enumeration beginning. Corresponds to TYPE_SUBSCRIPTION.  
LEVEL_LAST |  | End of enumeration. Corresponds to TYPE_FOLDER.  
  
The enumeration is used in the [IMTConSubscription::Type](Type.md) method.

<a id="enperiod"></a>
## IMTConSubscription::EnPeriod (#enperiod)

Subscription periods are enumerated in IMTConSubscription::EnPeriod.

ID | Value | Description  
PERIOD_ONCE | 0 | The subscription is billed once.  
PERIOD_DAILY | 1 | Daily subscription.  
PERIOD_WEEKLY | 2 | Weekly subscription.  
PERIOD_MONTHLY | 3 | Monthly subscription.  
PERIOD_QUARTERLY | 4 | Quarterly subscription.  
PERIOD_ANNUAL | 5 | One year subscription.  
PERIOD_CUSTOM | 100 | Custom period. If this option is selected, the period must be set by the [IMTConSubscription::PeriodCustom](PeriodCustom.md) method.  
PERIOD_FIRST |  | Enumeration beginning. Corresponds to PERIOD_ONCE.  
PERIOD_LAST |  | End of enumeration. Corresponds to PERIOD_CUSTOM.  
  
The enumeration is used in the [IMTConSubscription::PeriodMode](PeriodMode.md) method.

<a id="enfreeperiod"></a>
## IMTConSubscription::EnFreePeriod (#enfreeperiod)

The IMTConSubscription::EnFreePeriod enumeration contains subscription trial period variants.

ID | Value | Description  
FREE_PERIOD_NONE | 0 | No free period.  
FREE_PERIOD_DAY | 1 | One day.  
FREE_PERIOD_WEEK | 2 | One week.  
FREE_PERIOD_MONTH | 3 | One month.  
FREE_PERIOD_QUARTER | 4 | Three months.  
FREE_PERIOD_YEAR | 5 | One year.  
FREE_PERIOD_CUSTOM | 100 | Custom period. If this option is selected, the period must be set by the [IMTConSubscription::PeriodFreeCustom](PeriodFreeCustom.md) method.  
FREE_PERIOD_FIRST |  | Enumeration beginning. Corresponds to FREE_PERIOD_NONE.  
FREE_PERIOD_LAST |  | End of enumeration. Corresponds to FREE_PERIOD_NONE.  
  
The enumeration is used in the [IMTConSubscription::PeriodFreeMode](PeriodFreeMode.md) method.

<a id="enflags"></a>
## IMTConSubscription::EnFlags (#enflags)

IMTConSubscription::EnFlags is an enumeration of flags for additional subscription properties.

ID | Value | Description  
FREE_PERIOD_NONE | 0x00000000 | No flags.  
FLAG_ENABLE | 0x00000001 | Active subscription.  
FLAG_AUTO_PROLONG | 0x00000002 | The subscription is renewed automatically.  
FLAG_ALL |  | End of enumeration. It corresponds to enabling of all flags.  
  
The enumeration is used in the [IMTConSubscription::Flags](Flags.md) method.

<a id="encontrolmode"></a>
## IMTConSubscription::EnControlMode (#encontrolmode)

IMTConSubscription::EnControlMode enumerates subscription actions that can be performed in client terminals.

ID | Value | Description  
CONTROL_FULL | 0 | Any actions are allowed.  
CONTROL_UNSUBCRIBE | 1 | Only unsubscribing is allowed.  
CONTROL_VIEW | 2 | Only viewing subscription information is allowed.  
CONTROL_HIDDEN | 3 | The subscription is not displayed in the client terminals, so it cannot be purchased or canceled.  
CONTROL_FIRST |  | Enumeration beginning. Corresponds to CONTROL_FULL.  
CONTROL_LAST |  | End of enumeration. Corresponds to CONTROL_HIDDEN.  
  
The enumeration is used in the [IMTConSubscription::ControlMode](ControlMode.md) method.

<a id="enimagetype"></a>
## IMTConSubscription::EnImageType (#enimagetype)

IMTConSubscription::EnImageType is an enumeration of logos that can be used for subscriptions.

ID | Value | Description  
IMAGE_CUSTOM | 0 | Custom image. Currently not used.  
IMAGE_DEFAULT | 1 | Default image.  
IMAGE_STOCK_EXCHANGE | 2 | Exchange.  
IMAGE_AUDIT | 3 | Auditing service.  
IMAGE_REPORT | 4 | Report.  
IMAGE_PERSONAL_MANAGER | 5 | Personal manager.  
IMAGE_DOCUMENTS_DELIVERY | 6 | Delivery of documents.  
IMAGE_DOCUMENTS_STORING | 7 | Storage of documents.  
IMAGE_TRANSFER | 8 | Account transfer.  
IMAGE_CONVERSION | 9 | Currency conversion.  
Trading markets and instruments  
IMAGE_NASDAQ | 1000 | NASDAQ.  
IMAGE_TMX_GROUP | 1001 | TMX Group.  
IMAGE_CANADIAN_SECURITIES_EXCHANGE | 1002 | Canadian Securities Exchange.  
IMAGE_CBOE | 1003 | CBOE (Chicago Board Options Exchange).  
IMAGE_CBOE_FUTURES_EXCHANGE | 1004 | CBOE Futures Exchange.  
IMAGE_MEXICAN_DERIVATIVES | 1005 | Mexican Derivatives Exchange.  
IMAGE_FUND_SERV | 1006 | Fundserv.  
IMAGE_CME_CBOT | 1007 | Chicago Board of Trade.  
IMAGE_CME | 1008 | Chicago Mercantile Exchange.  
IMAGE_GLOBAL_OTC | 1009 | Global OTC.  
IMAGE_ICE_FUTURES | 1010 | ICE Futures (Intercontinental Exchange futures).  
IMAGE_IEX_GROUP | 1011 | IEX Group.  
IMAGE_ISE_OPTIONS | 1012 | ISE Options (International Securities Exchange options).  
IMAGE_NYSE | 1013 | NYSE (New York Stock Exchange).  
IMAGE_ONE_CHICAGO | 1014 | OneChicago.  
IMAGE_OTC_MARKETS | 1015 | OTC Markets.  
IMAGE_BOND_RATINGS | 1016 | Bond Ratings.  
IMAGE_US_REG_NMS | 1017 | US Regulation National Market System.  
IMAGE_BOVESPA | 1018 | Bovespa (Sao Paulo Stock Exchange).  
IMAGE_VIENNA_STOCK_EXCHANGE | 1019 | Vienna Stock Exchange.  
IMAGE_EURONEXT | 1020 | Euronext.  
IMAGE_GERMAN_ETFS | 1021 | German ETFs.  
IMAGE_BOLSA_DE_MADRID | 1022 | Bolsa De Madrid (Madrid Stock Exchange).  
IMAGE_STOXX | 1023 | STOXX.  
IMAGE_MEFF | 1024 | MEFF.  
IMAGE_BORSA_ITALIANA | 1025 | Borsa Italiana (Italian Stock Exchange).  
IMAGE_EUREX | 1025 | Eurex (European Exchange).  
IMAGE_MOSCOW_EXCHANGE | 1027 | Moscow Exchange.  
IMAGE_NORDIC_DERIVATIVES_EXCHANGE | 1028 | Nordic Derivatives Exchange.  
IMAGE_OSLO_STOCK_EXCHANGE | 1029 | Oslo Stock Exchange.  
IMAGE_PRAGUE_STOCK_EXCHANGE | 1030 | Prague Stock Exchange.  
IMAGE_SIX_GROUP | 1031 | SIX Group.  
IMAGE_XETRA | 1032 | Xetra.  
IMAGE_BOERSE_STUTTGART | 1033 | Börse Stuttgart (Stuttgart Stock Exchange).  
IMAGE_TURQUOISE | 1034 | Turquoise.  
IMAGE_LONDON_STOCK_EXCHANGE | 1035 | London Stock Exchange.  
IMAGE_WARSAW_STOCK_EXCHANGE | 1036 | Warsaw Stock Exchange.  
IMAGE_BUDAPEST_STOCK_EXCHANGE | 1037 | Budapest Stock Exchange.  
IMAGE_BATS_CHI_X_EUROPE | 1038 | BATS Chi-X Europe.  
IMAGE_LONDON_METAL_EXCHANGE | 1039 | London Metal Exchange.  
IMAGE_EUROPEAN_MUTUAL_FUNDS | 1040 | European mutual funds.  
IMAGE_TEL_AVIV_STOCK_EXCHANGE | 1041 | Tel Aviv Stock Exchange.  
IMAGE_JOHANNESBURG_STOCK_EXCHANGE | 1042 | Johannesburg Stock Exchange.  
IMAGE_HANG_SENG_BANK | 1043 | Hang Seng Bank.  
IMAGE_CHI_X_AUSTRALIA | 1044 | Chi-X Australia.  
IMAGE_HKEX | 1045 | Hong Kong Exchange.  
IMAGE_JPX | 1046 | Japan Exchange Group.  
IMAGE_SHANGHAI_STOCK_EXCHANGE | 1047 | Shanghai Stock Exchange.  
IMAGE_SHENZHEN_STOCK_EXCHANGE | 1048 | Shenzhen Stock Exchange.  
IMAGE_SINGAPORE_EXCHANGE | 1049 | Singapore Exchange.  
IMAGE_AUSTRALIAN_STOCK_EXCHANGE | 1050 | Australian Securities Exchange.  
IMAGE_KOREA_STOCK_EXCHANGE | 1051 | Korea Stock Exchange.  
IMAGE_A2X_MARKETS | 1052 | A2X Markets.  
IMAGE_ASCE | 1053 | Abuja Securities and Commodities Exchange.  
IMAGE_ALTX_EAST_AFRICA_EXCHANGE | 1054 | ALTX East Africa Exchange.  
IMAGE_AMMAN_STOCK_EXCHANGE | 1055 | Amman Stock Exchange.  
IMAGE_ARMENIA_SECURITIES_EXCHANGE | 1056 | Armenia Securities Exchange.  
IMAGE_ATHENS_STOCK_EXCHANGE | 1057 | Athens Stock Exchange.  
IMAGE_BAKU_STOCK_EXCHANGE | 1058 | Baku Stock Exchange.  
IMAGE_BANJA_LUKA_STOCK_EXCHANGE | 1059 | Banja Luka Stock Exchange.  
IMAGE_BERMUDA_STOCK_EXCHANGE | 1060 | Bermuda Stock Exchange.  
IMAGE_BOLIVIA_STOCK_EXCHANGE | 1061 | Bolivian Stock Exchange.  
IMAGE_BVRD | 1062 | Bolsa de Valores Republica Dominicana.  
IMAGE_BOLSAS_Y_MERCADOS_ESPANOLES | 1063 | Bolsas y Mercados Españoles.  
IMAGE_BOMBAY_STOCK_EXCHANGE | 1064 | Bombay Stock Exchange.  
IMAGE_BORSA_ISTANBUL | 1065 | Borsa İstanbul (Turkish Stock Exchange in Istanbul).  
IMAGE_BOTSWANA_STOCK_EXCHANGE | 1067 | Botswana Stock Exchange.  
IMAGE_BOURSA_KUWAIT | 1068 | Boursa Kuwait (Kuwait Stock Exchange).  
IMAGE_BVMAC | 1069 | Bourse des Valeurs Mobilieres de l Afrique Centrale.  
IMAGE_BOURSE_DE_TUNIS | 1070 | Bourse de Tunis.  
IMAGE_BRVM | 1071 | Bourse Regionale des Valeurs Mobilieres SA.  
IMAGE_BRAZIL_STOCK_EXCHANGE | 1072 | B3, Brazil Stock Exchange (Sao Paulo Stock Exchange, formerly known as Bovespa).  
IMAGE_BUCHAREST_STOCK_EXCHANGE | 1073 | Bucharest Stock Exchange.  
IMAGE_BUENOS_AIRES_STOCK_EXCHANGE | 1074 | Buenos Aires Stock Exchange.  
IMAGE_BULGARIAN_STOCK_EXCHANGE | 1075 | Bulgarian Stock Exchange.  
IMAGE_BURSA_MALAYSIA | 1076 | Bursa Malaysia (Malaysian Exchange).  
IMAGE_CALCUTTA_STOCK_EXCHANGE | 1077 | Calcutta Stock Exchange.  
IMAGE_CARACAS_STOCK_EXCHANGE | 1078 | Caracas Stock Exchange.  
IMAGE_CASABLANCA_STOCK_EXCHANGE | 1079 | Casablanca Stock Exchange.  
IMAGE_COLOMBIA_STOCK_EXCHANGE | 1080 | Colombia Stock Exchange.  
IMAGE_COLOMBO_STOCK_EXCHANGE | 1081 | Colombo Stock Exchange.  
IMAGE_CYPRUS_STOCK_EXCHANGE | 1082 | Cyprus Stock Exchange.  
IMAGE_DALIAN_COMMODITY_EXCHANGE | 1083 | Dalian Commodity Exchange.  
IMAGE_DAMASCUS_SECURITIES_EXCHANGE | 1084 | Damascus Securities Exchange.  
IMAGE_DAR_ES_SALAAM_STOCK_EXCHANGE | 1085 | The Dar es Salaam Stock Exchange.  
IMAGE_DEUTSCHE_BOERSE | 1086 | Deutsche Börse.  
IMAGE_DHAKA_STOCK_EXCHANGE | 1087 | Dhaka Stock Exchange.  
IMAGE_DOHA_SECURITIES_MARKET | 1088 | Doha Securities Market, Qatar Exchange.  
IMAGE_DOUALA_STOCK_EXCHANGE | 1089 | Douala Stock Exchange.  
IMAGE_DUBAI_FINANCIAL_MARKET | 1090 | Dubai Financial Market.  
IMAGE_DUTCH_CARIBBEAN_SECURITIES_EXCHANGE | 1091 | Dutch Caribbean Securities Exchange.  
IMAGE_EGYPTIAN_EXCHANGE | 1092 | Egyptian Exchange.  
IMAGE_ESWATINI_STOCK_MARKET | 1093 | Eswatini Stock Market.  
IMAGE_FRANKFURT_STOCK_EXCHANGE | 1094 | Frankfurt Stock Exchange.  
IMAGE_GEORGIAN_STOCK_EXCHANGE | 1095 | Georgian Stock Exchange.  
IMAGE_GHANA_STOCK_EXCHANGE | 1096 | Ghana Stock Exchange.  
IMAGE_INDONESIA_STOCK_EXCHANGE | 1097 | Indonesia Stock Exchange.  
IMAGE_IRAN_FARA_BOURSE | 1098 | Iran Fara Bourse (Iranian Stock Exchange).  
IMAGE_IRAN_MERCANTILE_EXCHANGE | 1099 | Iran Mercantile Exchange.  
IMAGE_ISLAMABAD_STOCK_EXCHANGE | 1100 | Islamabad Stock Exchange.  
IMAGE_JAMAICA_STOCK_EXCHANGE | 1101 | Jamaica Stock Exchange.  
IMAGE_KAZAKHSTAN_STOCK_EXCHANGE | 1102 | Kazakhstan Stock Exchange.  
IMAGE_KHARTOUM_STOCK_EXCHANGE | 1103 | Khartoum Stock Exchange.  
IMAGE_LAHORE_STOCK_EXCHANGE | 1104 | Lahore Stock Exchange.  
IMAGE_LIBYAN_STOCK_MARKET | 1105 | Libyan Stock Market.  
IMAGE_LJUBLJANA_STOCK_EXCHANGE | 1106 | Ljubljana Stock Exchange.  
IMAGE_LUSAKA_STOCK_EXCHANGE | 1107 | Lusaka Stock Exchange.  
IMAGE_LUXEMBOURG_STOCK_EXCHANGE | 1108 | Luxembourg Stock Exchange.  
IMAGE_MALAWI_STOCK_EXCHANGE | 1109 | Malawi Stock Exchange.  
IMAGE_MIAMI_INTERNATIONAL_SECURITIES_EXCHANGE | 1110 | Miami International Stock Exchange.  
IMAGE_MONGOLIAN_STOCK_EXCHANGE | 1111 | Mongolian Stock Exchange.  
IMAGE_MULTI_COMMODITY_EXCHANGE | 1112 | Multi Commodity Exchange.  
IMAGE_MUSCAT_SECURITIES_MARKET | 1113 | Muscat Securities Market.  
IMAGE_NAIROBI_SECURITIES_EXCHANGE | 1114 | Nairobi Securities Exchange.  
IMAGE_NCDEX | 1115 | National Commodity and Derivatives Exchange.  
IMAGE_NATIONAL_STOCK_EXCHANGE | 1116 | National Stock Exchange of India.  
IMAGE_NEO_EXCHANGE | 1117 | NEO Exchange (Toronto Stock Exchange).  
IMAGE_NEPAL_STOCK_EXCHANGE | 1118 | Nepal Stock Exchange.  
IMAGE_NEW_ZEALAND_EXCHANGE | 1119 | New Zealand Exchange.  
IMAGE_NIGERIAN_STOCK_EXCHANGE | 1120 | Nigerian Stock Exchange.  
IMAGE_NXCHANGE | 1121 | Nxchange (Dutch Stock Exchange).  
IMAGE_PAKISTAN_STOCK_EXCHANGE | 1122 | Pakistan Stock Exchange.  
IMAGE_PALESTINE_SECURITIES_EXCHANGE | 1123 | Palestine Securities Exchange.  
IMAGE_PFTS_UKRAINE_STOCK_EXCHANGE | 1124 | PFTS Ukraine Stock Exchange.  
IMAGE_PHILIPPINE_DEALING_EXCHANGE | 1125 | Philippine Dealing Exchange.  
IMAGE_PHILIPPINE_STOCK_EXCHANGE | 1126 | Philippine Stock Exchange.  
IMAGE_SAINT_PETERSBURG_STOCK_EXCHANGE | 1127 | Saint Petersburg Stock Exchange.  
IMAGE_SVGEX | 1128 | Saint Vincent and the Grenadines Securities Exchange.  
IMAGE_SANTIAGO_STOCK_EXCHANGE_MILA | 1129 | Mercado Integrado Latinoamericano (MILA, Integrated Latin American Market).  
IMAGE_STOCK_EXCHANGE_OF_MAURITIUS | 1130 | Stock Exchange of Mauritius.  
IMAGE_STOCK_EXCHANGE_OF_THAILAND | 1131 | Stock Exchange of Thailand.  
IMAGE_TADAWUL | 1132 | Tadawul (Saudi Stock Exchange).  
IMAGE_TAIWAN_STOCK_EXCHANGE | 1133 | Taiwan Stock Exchange.  
IMAGE_TEHRAN_STOCK_EXCHANGE | 1134 | Tehran Stock Exchange.  
IMAGE_TIRANA_STOCK_EXCHANGE | 1135 | Tirana Stock Exchange.  
IMAGE_TOKYO_STOCK_EXCHANGE | 1136 | Tokyo Stock Exchange.  
IMAGE_UGANDA_SECURITIES_EXCHANGE | 1137 | Uganda Securities Exchange.  
IMAGE_UKRAINIAN_EXCHANGE | 1138 | Ukrainian Exchange.  
IMAGE_ZAGREB_STOCK_EXCHANGE | 1139 | Zagreb Stock Exchange.  
IMAGE_ZIMBABWE_STOCK_EXCHANGE | 1140 | Zimbabwe Stock Exchange.  
IMAGE_BALTIC_EXCHANGE | 1141 | Baltic Exchange.  
IMAGE_FIRST |  | Enumeration beginning. Corresponds to IMAGE_CUSTOM.  
IMAGE_LAST |  | End of enumeration. Corresponds to IMAGE_BALTIC_EXCHANGE.  
  
The enumeration is used in the [IMTConSubscription::Image](Image.md) method.
