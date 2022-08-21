Free upcoming Earning API
example usage:

To return one symbol:
https://ab.tradeui.com/api/earnings.php?symbol=ACST

To return symbols that start with letter: 
(up to 3 letters wild card)

https://ab.tradeui.com/api/earnings.php?symbolstart=A
https://ab.tradeui.com/api/earnings.php?symbolstart=BA
https://ab.tradeui.com/api/earnings.php?symbolstart=BAC


Result is in JSON:
[
{
"symbol": "AACG",
"earning_time": "2",
"earning_date": "2022-08-11",
"MarketCap": "82156300",
"optionable": "0",
"last_updated": "2022-08-21 19:03:18"
}
]

Condition to use the API is to insert a link in your site footer back to <a href="https://tradeui.com">TradeUI.com</a>