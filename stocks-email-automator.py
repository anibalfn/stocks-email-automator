#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui
import pyperclip
import time
import yfinance

ticker = input("Digite o nome da ação: ")
data_time = input("Digite o período de tempo em dias: ")
data = yfinance.Ticker(ticker)
time_table = data.history(data_time+"d")
stock_closure = time_table.Close
max_value = stock_closure.max()
min_value = stock_closure.min()
current_value = stock_closure[-1]

print(max_value)
print(min_value)
print(current_value)

chart = time_table.plot()
chart


# In[ ]:


receiver = "anibalneto29@gmail.com"
subject = "Daily analisis of stocks"
message = f"""
Good day,
Below you encounter the analysis of the stock {ticker} from the last {data_time} days:
Max cotation: ${round(max_value,2)}
Min cotation: ${round(min_value,2)}
Current cotation: ${round(current_value,2)}


Yours sincerely,
Aníbal Figueiredo.
"""

print(receiver)
print(subject)
print(message)


# In[ ]:


pyautogui.PAUSE = 5

pyautogui.hotkey("ctrl", "t")

pyperclip.copy("https://gmail.com")

pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

pyautogui.click(x=93, y=218)

pyperclip.copy(receiver)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

pyperclip.copy(subject)
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

pyperclip.copy(message)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=842, y=729)

pyautogui.hotkey("ctrl", "f4")

print('E-mail sent successfully.')

