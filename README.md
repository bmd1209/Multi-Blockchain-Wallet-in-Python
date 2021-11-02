# Multi-Blockchain-Wallet-in-Python

### HOMEWORK background: 

Your new startup is focusing on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well! The problem is, there are so many coins out there! It's
a good thing you understand how HD wallets work, since you'll need to build out a system that can create them.
You're in a race to get to the market. There aren't as many tools available in Python for this sort of thing, yet.
Thankfully, you've found a command line tool, hd-wallet-derive that supports not only BIP32, BIP39, and BIP44, but
also supports non-standard derivation paths for the most popular wallets out there today! However, you need to integrate
the script into your backend with your dear old friend, Python.
Once you've integrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins, giving
you a serious edge against the competition.
In this assignment, however, you will only need to get 2 coins working: Ethereum and Bitcoin Testnet.
Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.


### 1. Project setup


I created a project directory called wallet and cd into it. I then cloned the hd-wallet-derive tool into this folder and installed it and crated a symlink called derive for the hd-wallet-derive/hd-wallet-derive.php script. This will clean up the command needed to run the script in our code, as we can call ./derive instead of ./hd-wallet-derive/hd-wallet-derive.php. I tested it using the following code to see if it works:./derive --key=xprv9zbB6Xchu2zRkf6jSEnH9vuy7tpBuq2njDRr9efSGBXSYr1QtN8QHRur28QLQvKRqFThCxopdS1UD61a5q6jGyuJPGLDV9XfYHQto72DAE8 --cols=path,address --coin=ZEC --numderive=3 -g

![image](https://user-images.githubusercontent.com/84600493/139745751-d3ee69c2-bba7-4351-b147-f6396c92759d.png)
