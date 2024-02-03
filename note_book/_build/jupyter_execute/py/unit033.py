#!/usr/bin/env python
# coding: utf-8

# # Short-Run Aggregate Supply (SRAS)

# Aggregate supply/AS
# : Amount of goods and services (real GDP) that firms will produce in an economy at different price levels. The supply for everything by all firms.
# : AS differentiates between short run and long-run and has two different curves.<br><br>
# 
# Short-Run aggregate supply/SRAS
# : Wages and resource prices are sticky and will not change as price levels change.<br><br>
# 
# Long-Run aggregate supply/LRAS
# : Wages and resource prices are flexible and will change as price levels change.

# > Similar to AD, the y-axis is price level and the x-axis is real GDP. The figure below shows a SRAS curve.

# In[1]:


import pandas as pd
import altair as alt


# In[2]:


df = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[4, 3, 2, 1]})

fig1 = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity', title='Real GDP', scale=alt.Scale(domain=[0,5])),
    alt.Y('price', title='Price Level', scale=alt.Scale(domain=[0,3])),
).properties(title='Short-Run Aggregate Supply')

text1 = alt.Chart({'values':[{'x': 4.35, 'y': 2.6}]}).mark_text(
    text='SRAS',
    fontSize=15
).encode(x='x:Q', y='y:Q')


# In[3]:


fig1 + text1


# ```{admonition} SRAS is upward sloping
# - If the price level increases (inflation), then real GDP supplied increases.
# 
# - If the price level decreases (deflation), then real GDP supplied decreases.
# 
# 
# Reasons why AD is downward sloping:<br>
# Suppliers have incentive to bring more to market if the price level rises because they can get more for their finished products while wages remain unchanged.
# ```

# ## Factors shifting SRAS

# ```{admonition} Factors shift SRAS
# - Change in the amount of resources in the economy
# - Change in production technology
# - Change in expected future prices
# - Change in prices of land, labor, or capital
# - Change in actions of the government (tax or subsidy)
# 
# The figure below shows the shifts of SRAS.
# ```

# In[4]:


df2 = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity0':[7,6,5,4], 
                         'quantity1':[9,8,7,6],
                         'quantity2':[5,4,3,2]}
                  )

fig2 = alt.Chart(df2).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity0', title='Real GDP', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price Level', scale=alt.Scale(domain=[0,3])),
).properties(title='Short-Run Aggregate Supply')

fig3 = alt.Chart(df2).mark_line(color='green', point=alt.OverlayMarkDef(filled=False, fill='white', color='green')).encode(
    alt.X('quantity1', title='Real GDP', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price Level', scale=alt.Scale(domain=[0,3])))

fig4 = alt.Chart(df2).mark_line(color='red', point=alt.OverlayMarkDef(filled=False, fill='white', color='red')).encode(
    alt.X('quantity2', title='Real GDP', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price Level', scale=alt.Scale(domain=[0,3])))

text1 = alt.Chart({'values':[{'x': 7.5, 'y': 2.6}]}).mark_text(
    text='SRAS0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9.5, 'y': 2.6}]}).mark_text(
    text='SRAS1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 5.5, 'y': 2.6}]}).mark_text(
    text='SRAS2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 7.5, 'y': 2.2}]}).mark_text(
    text='➟',
    fontSize=40
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 5.5, 'y': 2.227}]}).mark_text(
    text='➟',
    fontSize=40,
    angle=180
).encode(x='x:Q', y='y:Q')


fig2 + fig3 + fig4 + text1 + text2 + text3 + text4 + text5

