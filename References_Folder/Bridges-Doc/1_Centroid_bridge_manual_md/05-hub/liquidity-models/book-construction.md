[🏠 Document Start](..\..\README.md) / [Synthetic Symbols](..\README.md) / [Liquidity Models](README.md) / Book Construction

# Book Construction

Overview
The Book Construction feature is an essential component of the Liquidity Model module, and its configuration takes place at the individual
Symbol level through the dedicated Book Construction field. This feature facilitates the creation of a virtual liquidity book, enabling users to
tailor a multi-layered Liquidity Book according to their specific preferences. Additionally, it provides the capability to incorporate markups at
various levels within the constructed Liquidity Book. This means users have the flexibility to customize and enhance the liquidity
representation based on their unique requirements, introducing personalized adjustments and markups at different tiers of the constructed
Liquidity Book. When constructing a Book, the Centroid Bridge always takes the Top of the Book that is available to the Centroid Bridge
Constructing an Artificial Book
To construct an artificial book
1. Click on Hub > Liquidity Model > Desired Liquidity Model > Symbol > Book Construction > Add.
2. . Select your preferred book construction mode as follows:
Normal: The book is constructed using TOB Bid and TOB Ask Price from the maker.
Midpoint: The book is constructed using the Midpoint price of the TOB Bid and Ask Price from the maker.
3. Configure the required values, You may refer to the field descriptions hereafter.


4. Click the “Save” button to save your configured values.
How pricing works when using the Book Construction
When constructing a Book, the Centroid Bridge always takes the Top of the Book that is available on the Centroid Bridge whenever a new
price update comes in. The Book is constructed using the artificial Volumes specified at each level in addition to the Top of the Book price
to which the markup specified at each level is added. Volume can be randomized (using a range), fixed, or derived from the real Volume at
the Top of the Book.
Mode Normal, Midpoint Normal: The book is constructed using TOB Bid and TOB Ask Price from the maker.
Midpoint: The book is constructed using the Midpoint price of the TOB Bid and Ask Price from
the maker.
Bid Vol From 1000,15000 Clients can specify starting volume in the "Vol From" for Bid side
Bid Vol To 1000,1500 Clients can input the same volume in "Vol From" for a fixed range, or a different volume to
establish a variable volume range for the Bid layer.
Markup 0,10,15 Markups can be added on each layer in points for Bid Volume
Ask Vol From 1000,15000 Clients can specify starting volume in the "Vol From" for Ask side
Ask Vol To 1000,1500 Clients can input the same volume in "Vol From" for a fixed range, or a different volume to
establish a variable volume range for the Ask layer.
Field Possible Values Description

Note: If you are creating a virtual book of 3 layers without any markup then it will be merged and streamed as one layer only. So to
achieve a multi-layered virtual book, you need to add markups on each layer along with the volume.
How execution works when using the Book Construction
When it comes to execution, we differentiate A Book from B Book as follows
Modes Of Book Construction

Normal Mode:
When creating a book using the Normal mode for Book Construction, the system utilizes the TOB Bid Price and TOB Ask Price provided
by the maker(s) in the liquidity model or pool, in conjunction with the volumes you specified in the book construction process. This
approach ensures that the book is constructed based on the most recent bid and ask prices available.
Example:
Raw Book from the Maker ( 1.1 )
Markup 0,10,15 Markups can be added on each layer in points for Ask Volume
A Book The entire Order will be sent to the Makers at the Top of the Book irrespective of the Volumes at the
constructed Book.
B Book Orders will be filled based on the constructed Book by sweeping the Book from top to bottom until the Order
is fully or partially filled. It’s the same way the Centroid Bridge would execute any Order based on a real
Liquidity Book.
Book Execution Type Execution Mode


Summary:
In the process of constructing the book using normal mode, we initially referenced the raw TOB Bid and Ask Prices (see Image 1.1).
We then performed the requisite markup adjustments and incorporated the volume data, as outlined in Image 1.2.
The resultant prices and volumes, as shown in Image 1.3, confirm that the final output meets our anticipated criteria.
Midpoint Mode:
When using the Midpoint mode for Book Construction, the system calculates the book values based on the midpoint between the TOB Bid
Price and TOB Ask Price provided by the maker(s) in the liquidity model or pool. Additionally, any markups you apply are incorporated
along with the volumes you specify during the construction process. This approach ensures that the book accurately reflects the adjusted
pricing and the volumes you have entered.
Example:
Raw Book from the Maker ( 2.1 )
1 1.05567 2000 1.05571 1500
2 1.05566 3000 1.05572 2500
3 1.05565 4000 1.05573 4500
Number of Layers Bid Prices Bid Volumes Ask Prices Ask Volumes
Market Watch Raw Book from the
Maker ( 1.1 )
Constructed Artificial Book ( 1.2 )
Market Watch Utilizing the Book
Construction ( 1.3 )
1 1.05567 1000 1.05571 1500
2 1.05566 2000 1.05572 2500
3 1.05565 4000 1.05573 4500
Number of Layers Bid Prices Bid Volumes Ask Prices Ask Volumes
Market Watch Raw Book from the
Maker ( 2.1 )
Constructed Artificial Book ( 2.2 )Market Watch Utilizing the Book
Construction ( 2.3 )

Summary:
During the book construction using midpoint mode, we first used the raw TOB Bid and Ask Prices to determine the Midpoint (Average)
(refer to Image 2.1).
After calculating the average from the TOB Bid and Ask Prices, we applied the necessary markup adjustments and incorporated the
volume data, as detailed in Image 2.2.
The resulting prices and volumes, illustrated in Image 2.3, verify that the final output aligns with our expected criteria.
VWAP Mode:
In VWAP Mode for Book Construction, the system considers the pricing from all layers provided by the maker(s) in the liquidity model or
pool, as well as the volumes the maker(s) is streaming. The book is constructed based on the volumes you specify. If necessary, the
system will use pricing and volumes from two layers provided by the maker to build one layer of your artificial book. The construction of the
second layer will begin where the first layer concluded. Further details will be provided with an example. The price displayed for the book
will be the Volume-Weighted Average Price (VWAP).
Example:
Raw Book from the Maker ( 3.1 )
Summary:
In constructing the book using VWAP mode, we utilized the Raw Bid Prices and Volumes and Raw Ask Prices and Volumes from all
layers (see Image 3.1) to create the artificial book.
1 1.05567 1000 1.05571 1000
2 1.05566 1500 1.05572 1500
3 1.05565 1500 1.05573 1500
Number of Layers Bid Prices Bid Volumes Ask Prices Ask Volumes
Market Watch Raw Book from the
Maker ( 3.1 )
Constructed Artificial Book ( 3.2 )
Market Watch Utilizing the Book
Construction ( 3.3 )


We then applied any necessary markup adjustments and integrated the volume data, as described in Image 3.2. This process involved
sweeping the Raw Book from top to bottom.
The final prices and volumes, shown in Image 3.3, confirm that the output meets our anticipated criteria. Price for Artificial Book is
calculated as
VWAP is calculated using the formula: VWAP=∑(Price×Quantity)/∑Quantity, where each raw price and quantity pair is considered
until the final value meets the expected criteria.
VWAP Cumulative Mode:
In VWAP Cumulative Mode for Book Construction, the system incorporates the pricing from all layers provided by the maker(s) in the
liquidity model or pool, as well as the volumes the maker(s) is streaming. The book is constructed based on the volumes you specify. If
necessary, the system will use pricing and volumes from two layers provided by the maker to build one layer of your artificial book. The
construction of the second layer will start from the very top again. Further details will be provided with an example. The displayed price for
the book will be the Volume-Weighted Average Price (VWAP).
Example:
Raw Book from the Maker ( 4.1 )
Summary:
In constructing the book using VWAP Cumulative Mode, we utilized the Raw Bid Prices and Volumes and Raw Ask Prices and Volumes
from all layers (see Image 4.1) to create the artificial book.
We then applied any necessary markup adjustments and integrated the volume data, as described in Image 4.2. This process involved
sweeping the Raw Book from top to bottom, restarting from the top for each subsequent layer.
The final prices and volumes, shown in Image 4.3, confirm that the output meets our anticipated criteria. Price for the Artificial Book is
calculated as
VWAP is calculated using the formula: VWAP = ∑(Price × Quantity) / ∑Quantity, where each raw price and quantity pair is considered
until the final value meets the specified volume requirements.
1 1.05567 500 1.05571 500
2 1.05566 1500 1.05572 1500
3 1.05565 5000 1.05573 5000
Number of Layers Bid Prices Bid Volumes Ask Prices Ask Volumes
Market Watch Raw Book from the
Maker ( 4.1 )
Constructed Artificial Book ( 4.2 )
Market Watch Utilizing the Book
Construction ( 4.3 )


Cumulative Mode:
In Cumulative Mode for Book Construction, the system takes into account the pricing from all layers provided by the maker(s) in the
liquidity model or pool, as well as the volumes the maker(s) is streaming. The book is constructed based on the volumes you specify. If
necessary, the system will use pricing and volumes from two layers provided by the maker to build one layer of your artificial book. The
construction of the second layer will start from the very top again. In Cumulative Mode, the displayed price will always reflect the price of
the last consumed layer. Further details will be provided with an example.
Example:
Raw Book from the Maker ( 5.1 )
Summary:
In constructing the book using Cumulative Mode, we utilized the Raw Bid Prices and Volumes and Raw Ask Prices and Volumes from
all layers (see Image 5.1) to create the artificial book.
We applied the necessary markup adjustments and integrated the volume data, as detailed in Image 5.2. In Cumulative Mode, the
process involved sweeping the Raw Book from top to bottom and restarting from the top for each new layer. Notably, if a layer was
touched, its full volume was utilized rather than the Book Construction Volume.
The final prices and volumes, shown in Image 5.3, confirm that the output meets our anticipated criteria. Price for the Artificial Book is
derived from the last consumed layer.


1 1.05567 1500 1.05571 1500
2 1.05566 2250 1.05572 2250
3 1.05565 7250 1.05573 7250
Number of Layers Bid Prices Bid Volumes Ask Prices Ask Volumes
Market Watch Raw Book from the
Maker ( 5.1 )
Constructed Artificial Book ( 5.2 )
Market Watch Utilizing the Book
Construction ( 5.3 )



