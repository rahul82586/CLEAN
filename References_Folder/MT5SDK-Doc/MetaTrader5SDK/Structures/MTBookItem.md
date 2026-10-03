[🏠 Document Start](../README.md) / [Structures](README.md) / MTBookItem

[Previous](MTChartBar.md) | [Next](MTBookMTBookDiff.md)

<a id="mtbookitem"></a>
# MTBookItem (#mtbookitem)

The MTBookItem describes an entry of the Depth of Market. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTBookItem
      {
       //--- Type of entry
       enum EnBookItem
         {
          ItemReset      =0,                                    // Reset an entry in the Depth of Market
          ItemSell       =1,                                    // Sell request
          ItemBuy        =2                                     // Buy request
          ItemSellMarket =3,                                    // Market sell request
          ItemBuyMarket  =4                                     // Market buy request
         };
       UINT              type;                                  // Type of entry
       double            price;                                 // Deal price
       INT64             volume;                                // Deal volume
       INT64             volume_ext;                            // deal volume with extended accuracy
       UINT              reserved[8];                           // A reserved field
      };
    #pragma pack(pop)

MTBookItem is used for filling the[MTBook/MTBookDiff](MTBookMTBookDiff.md) structure.

<a id="parameters"></a>
## Parameters (#parameters)

The structure contains the following parameters:

Field | Type | Description  
type | UINT | Type of entry that is passed using the EnBookItem enumeration.  
price | double | Deal price. All the symbol prices delivered into the platform are rounded in accordance with the [IMTConSymbol::Digits](../Configuration-Interfaces/Symbols/IMTConSymbol/Digits.md) parameter of the symbol. When broadcasting prices with higher accuracy, different levels can be combined into one rounded level. To avoid collisions, set the precision of the symbols in accordance with the precision of transmitted data.  
volume | INT64 | Deal volume. The volume is recorded in the same form as it is passed by a data provider. A data provider may pass volumes as amounts of contracts (in lots) or as amounts of money. On the trading platform side, this value is interpreted depending on the type of calculation of profit and margin set for a symbol ([IMTConSymbol::CalcMode](../Configuration-Interfaces/Symbols/IMTConSymbol/CalcMode.md)):

  * For the [IMTConSymbol::TRADE_MODE_FOREX (#encalcmode)](../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#encalcmode) type, the volume is interpreted as the amount of base currency units of a symbol.
  * For all the other types, the volume is interpreted as the amount of contracts (lots).

Unlike all other API methods and fields, in which the volume is specified as a fixed-precision value with 4 digits (where 10000 is 1 lot), the volume in this field is specified as is, with the precision of 0 digits. For example, for all financial instruments except Forex, the value of 1 means 1 lot. For operations with [extended-precision volumes (#volume)](../Development-Features/README.md#volume), use the 'volume_ext' field.

  * The 'volume_ext' value has a higher priority than 'volume'. The server will use this value if specified.
  * When returning volume values, the server fills both fields: with standard and extended precision.

  
volume_ext | INT64 | Deal volume with [extended precision (#volume)](../Development-Features/README.md#volume). It is similar to the 'volume' field, but the value is passed with the fixed number of decimal places (8).

  * The 'volume_ext' value has a higher priority than 'volume'. The server will use this value if specified.
  * When returning volume values, the server fills both fields: with standard and extended precision.

  
reserved | UINT | A reserved field for future use.  
  
<a id="enumerations"></a>
## Enumerations (#enumerations)

The structure contains one enumeration:

<a id="enbookitem"></a>
### EnBookItem (#enbookitem)

Types of entries of the Depth of Market are described in EnBookItem.

ID | Value | Description  
ItemReset | 0 | Reset an entry of the Depth of Market. This type is not used in Manager API.  
ItemSell | 1 | Sell request.  
ItemBuy | 2 | Buy request.  
ItemMarketSell | 3 | Used for displaying aggregated market sell requests.  
ItemMarketBuy | 4 | Used for displaying aggregated market buy requests.
