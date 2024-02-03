#!/usr/bin/env python
# coding: utf-8

# # Aggregate Demand (AD)

# Aggregate demand/AD
# : Amount of goods and services demanded by households, business, governments, and foreigners.
# : Demand for all final goods and services by everyone.
# : The x-axis is output (not quantity), which is easured in **dollars**.
# : **AD = C + I + G + (X - M)**
# : e.g. demand for everything by everyone in the US.

# > Similar to the demand curve in microeconomics, AD is also **downward sloping**.<br>
# > Recall that we learned that output can be measured by **real GDP**.<br>
# > So, there is an inverse relationship between **price level** and **real GDP demanded** as shown in the figure below.

# In[1]:


import pandas as pd
import altair as alt


# In[2]:


df = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[1,2,3,4]})

fig1 = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity', title='Real GDP', scale=alt.Scale(domain=[0,5])),
    alt.Y('price', title='Price Level', scale=alt.Scale(domain=[0,3])),
).properties(title='Aggregate Demand')

text1 = alt.Chart({'values':[{'x': 4.25, 'y': 1}]}).mark_text(
    text='AD',
    fontSize=15
).encode(x='x:Q', y='y:Q')


# In[3]:


fig1 + text1


# ```{admonition} AD is downward sloping
# - If the price level increases (inflation), then real GDP demanded falls.
# 
# - If the price level decreases (deflation), then real GDP demanded increases.
# 
# Reasons why AD is downward sloping:
# - Foreign purchases effect<br>Foreigners demand less when domestic prices rise because their incomes have not risen; and domestic consumers prefer more imports since domestic prices are up.
# 
# - Wealth effect<br>Financial wealth is eroded when prices rise; this cause consumers to save more and spend less.
# 
# - Interest rate effect<br>When the price level increases, lenders need to charge higher interest rates to get a real return on their loans. Higher interest rates discourage consumer spending and business investment. 
# ```

# > Note that the reason used (substitution effect, income effect) in microeconomics cannot explain a downward sloping AD. When prices in general rise, this is inflation which does not erode overall income in the economy.

# ## Factors shifting AD
# 
# ```{admonition} Factors shift AD
# **AD = C + I + G + (X-M)**<br>
# 
# According to the formula, factors shifting AD are
# - Change in consumer confidence
# - Changes in taxes
# - Changes in business confidence
# - Changes in the money supply
# - Changes in foreign demand due to preferences or income
# - Changes in government spending
# ```

# In[4]:


df2 = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity0':[4,5,6,7], 
                         'quantity1':[6,7,8,9],
                         'quantity2':[2,3,4,5]}
                  )

fig2 = alt.Chart(df2).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity0', title='Real GDP', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price Level', scale=alt.Scale(domain=[0,3])),
).properties(title='Aggregate Demand')

fig3 = alt.Chart(df2).mark_line(color='green', point=alt.OverlayMarkDef(filled=False, fill='white', color='green')).encode(
    alt.X('quantity1', title='Real GDP', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price Level', scale=alt.Scale(domain=[0,3])))

fig4 = alt.Chart(df2).mark_line(color='red', point=alt.OverlayMarkDef(filled=False, fill='white', color='red')).encode(
    alt.X('quantity2', title='Real GDP', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price Level', scale=alt.Scale(domain=[0,3])))

text1 = alt.Chart({'values':[{'x': 7.5, 'y': 0.85}]}).mark_text(
    text='AD0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9.5, 'y': 0.85}]}).mark_text(
    text='AD1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 5.5, 'y': 0.85}]}).mark_text(
    text='AD2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 7.5, 'y': 1.2}]}).mark_text(
    text='➟',
    fontSize=40
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 5.5, 'y': 1.227}]}).mark_text(
    text='➟',
    fontSize=40,
    angle=180
).encode(x='x:Q', y='y:Q')


fig2 + fig3 + fig4 + text1 + text2 + text3 + text4 + text5


# **Change in consumer confidence**<br>
# If households become more confident about their future job security or pay raises, they will spend more, shifting AD to right, *vice versa*.
# 
# <br>
# 
# **Changes in taxes**<br>
# A reduction in income taxes gives households more after-tax income, boosting their spending. AD shifts to right, *vice versa*.
# 
# <br>
# 
# **Changes in business confidence**<br>
# If business become more confident in their future sales, they will spend on plant and equipment in order to gear up. AD shifts to right, *vice versa*.
# 
# <br>
# 
# **Changes in the money supply**<br>
# An increase in the money supply lowers interest rates, stimulating firms to borrow and spend. Households also borrow and spend more. AD shifts to right, *vice versa*.
# 
# <br>
# 
# **Changes in foreign demand due to preferences or income**<br>
# If foreigners develop a taste for the products, AD will shift to right, *vice versa*.
# 
# <br>
# 
# 
# **Changes in government spending**<br>
# If the government spend more on buying goods and services, AD will shift to right, *vice versa*.

# ```{importance}
# Similar to the demand-supply model, points move along the AD curve when there is only the price level change, *ceteris paribus*. If those factors change, the entire AD curve will shift right or left.
# ```
