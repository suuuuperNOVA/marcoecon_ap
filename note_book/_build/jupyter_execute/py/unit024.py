#!/usr/bin/env python
# coding: utf-8

# # Price Indices and Inflation

# ## Inflation
# 
# Inflation
# : Sustained increase in most prices in the economy.
# : Reduce the purchasing power of money.<br><br>
# 
# Deflation
# : Decrease in general prices or a negative inflation rate.<br><br>
# 
# Disinflation
# : A temporary slowing of the pace of price inflation.
# : Occasions when the inflation rate has reduced marginally over the short term.

# - Governments always want to achieve a slight inflation because a slight inflation can stimulate consumption.
# - A high inflation is bad because banks don’t lend and people don’t save. This decreases investment and GDP.
# - Deflation is bad because people will hoard money and assets. This decreases consumer spending and GDP.

# ## Measuring Inflation
# 
# > The government tracks the prices of specific market baskets that included the same goods and services. 
# 
# ### Consumer Price Index/CPI
# Price indices
# : Index numbers assigned to each year that show how prices have changed relative to a specific base year.
# : e.g. Consumer Price Index/CPI<br><br>
# 
# Consumer Price Index/CPI
# : Measures the overall change in consumer prices based on a representative basket of goods and services over time.
# : <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi>C</mi>
#   <mi>P</mi>
#   <mi>I</mi>
#   <mo>=</mo>
#   <mfrac>
#     <mtext>Total Cost This Period</mtext>
#     <mtext>Total Cost Base Period</mtext>
#   </mfrac>
# </math>
# 
# Inflation rate
# : Percent change in prices from year to year.
# : <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mtext>Inflation Rate</mtext>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mi>C</mi>
#       <mi>P</mi>
#       <msub>
#         <mi>I</mi>
#         <mi>t</mi>
#       </msub>
#       <mo>&#x2212;<!-- − --></mo>
#       <mi>C</mi>
#       <mi>P</mi>
#       <msub>
#         <mi>I</mi>
#         <mrow class="MJX-TeXAtom-ORD">
#           <mi>t</mi>
#           <mo>&#x2212;<!-- − --></mo>
#           <mn>1</mn>
#         </mrow>
#       </msub>
#     </mrow>
#     <mrow>
#       <mi>C</mi>
#       <mi>P</mi>
#       <msub>
#         <mi>I</mi>
#         <mrow class="MJX-TeXAtom-ORD">
#           <mi>t</mi>
#           <mo>&#x2212;<!-- − --></mo>
#           <mn>1</mn>
#         </mrow>
#       </msub>
#     </mrow>
#   </mfrac>
#   <mo>&#x00D7;<!-- × --></mo>
#   <mn>100</mn>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
# </math>

# The table below shows how the CPI and inflation rates are calculated.
# 
# |Year|Item in Basket|Price (\$)|Amount|Cost (\$)|CPI|Inflation Rate|
# |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
# |2020|Cheese<br>Crackers|2.00<br>1.25|5<br>8|20.00|20/20=100||
# |2021|Cheese<br>Crackers|2.25<br>1.50|5<br>8|23.25|23.25/20=116.25|(116.25-100)/100 = 16.25%|
# |2022|Cheese<br>Crackers|2.35<br>1.60|5<br>8|24.55|24.55/20=122.75|(122.75-116.25)/116.25 = 5.59%|

# The inflation rate between 2020 and 2022 can also be calculated:<br>
# 
# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mtext>Inflation Rate</mtext>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mn>122.75</mn>
#       <mo>&#x2212;<!-- − --></mo>
#       <mn>100</mn>
#     </mrow>
#     <mn>100</mn>
#   </mfrac>
#   <mo>&#x00D7;<!-- × --></mo>
#   <mn>100</mn>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mo>=</mo>
#   <mn>22.75</mn>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
# </math>

# ### Problems with CPI
# 
# - Substitution bias<br>As prices increase for the fixed market basket, consumers buy less of these products and more substitutes that may not be part of the market basket.
#     - CPI may be higher than what consumers are really paying.
# - New product<br>CPI market basket may not include the newest consumer products.
#     - CPI measures prices but not the increase in choices.
# - Product quality<br>CPI ignores both improvements and decline in product quality, e.g. IPhone 15 vs. IPhone 4.
#     - CPI may suggest that prices stay the same though the economic well being has improved significantly.
