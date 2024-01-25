## Stocks E-mail Automator
### Create an automation of a e-mail returning the price of a stock in a period of time.

This application access to the Yahoo! Finance DB and returns informations of a stock indicated by the user, returning the price of this stock in a certain period of time.
<br/>
After that, the automation creates a new tab, access Gmail, create a new email, fill the destination, subject and message body and sends the email.
<br/>
Currently the application have Linux support, but soon will have support to Windows. The code was made with <b>Python</b> and <b>Jupyter Notebook.</b>

---
#### Template of message:


"Good day,
<br/>
Below you encounter the analysis of the stock XXXX from the last 90 days:
<br/>
Max cotation: $XXX.XX
<br/>
Min cotation: $YYY.YY
<br/>
Current cotation: $ZZZ.ZZ
<br/>

<br/>
<br/>
Yours sincerely,
Anibal Figueiredo."
