[🏠 Document Start](..\README.md) / [Trading Platform](README.md) / Push Ticks

# Push Ticks

Overview
The Push Ticks component allows pushing prices manually as a Maker into Taker Feeds in the event of stale prices.
This functionality has several uses and is mainly used for B Book execution, allowing to settle B Book Positions at a certain close price
such as Risk Account Adjustment, Position Adjustments, and Expired Future Symbol.
Symbol Selection
To select the Symbol into which the ticks will be pushed
1. Click the dropdown button “Toggle here to add/remove Symbol”.
2. Fill it in with the relevant information. You may refer to the field descriptions hereafter.
3. Click the “Add / Remove Symbol” button to submit the changes.
Push Ticks Manually
To push the ticks manually
Once you have selected the desired parameter, you will be presented will a panel pertaining to the selected Symbol through which you can
push the ticks manually.
1. Fill in the Bid and Ask volumes and prices as highlighted below. You may refer to the field descriptions hereafter.
2. Click the “Submit” button to push the tick.
Makers Select a Maker into which the Orders will be executed.
Taker Feed Select a Taker Feed into which the ticks will be pushed.
Symbol Select a Symbol into which the ticks will be pushed. By doing this, you are pushing ticks to that specific symbol only.
Field Description

Symbol The selected Symbol.
Makers The selected Maker.
Bid The Bid Price to be pushed.
Ask The Ask Price to be pushed.
LTP Price The Last Traded Price to be pushed.
Bid Volume The Bid Volume to be pushed along with the Bid Price which defines the available liquidity for order execution.
Ask
Volume
The Ask Volume to be pushed along with the Ask Price which defines the available liquidity for order execution.
LTP
Volume
The Last Traded Price Volume to be pushed along with the LTP Price which defines the available liquidity for order
execution.
Field Description

