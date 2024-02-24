#!/usr/bin/env python
# coding: utf-8

# # Financial Assets

# Financial asset
# : A liquid asset that gets its value from a contractual right or ownership claim.
# : No physical form.
# : e.g. cash, stocks, bonds, mutual funds and bank deposits.

# Financial assets are featured by:
# - Liquidity
# - Rate of return
# - Risk

# Liquidity
# : Ease of converting an asset or security into cash, with cash itself being the most liquid asset of all.
# : Cash and deposits are the most liquid assets. Bonds and stocks follow.<br>
# <br>
# Rate of return
# : Net gain or loss of an investment over a specified time period, expressed as a percentage of the investment's initial cost.
# : <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi>R</mi>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <msub>
#         <mi>V</mi>
#         <mi>f</mi>
#       </msub>
#       <mo>&#x2212;<!-- − --></mo>
#       <msub>
#         <mi>V</mi>
#         <mi>i</mi>
#       </msub>
#     </mrow>
#     <msub>
#       <mi>V</mi>
#       <mi>i</mi>
#     </msub>
#   </mfrac>
#   <mo>&#x00D7;<!-- × --></mo>
#   <mn>100</mn>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
# </math>

# Example<br>
# The house was bought for 1 million in 2018 and sold for 1.5 million in 2023. So, the rate of return was 50%.

# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi>R</mi>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mn>1.5</mn>
#       <mo>&#x2212;<!-- − --></mo>
#       <mn>1</mn>
#     </mrow>
#     <mn>1</mn>
#   </mfrac>
#   <mo>=</mo>
#   <mn>50</mn>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
# </math>

# Financial risks are uncertainties about future outcomes that involve financial losses and gains, including:
# - Market risk<br>Movement in prices of financial instrument.
# - Credit risk<br>One fails to fulfill their obligations towards their counterparties, such as default on the mortgage repayments.
# - Operational risk<br> Mismanagement or technical failures, such as fraud Risk and model Risk.
# - Legal risk<br>Risk to be involved in a lawsuit.

# The figure below shows the financial assets at the corresponding risk levels. **The greater the risk, the higher the rate of return to compensate the investors taking additional risks.**

# <img src='../pic/unit041_risk.png' alt='risk' width='600'/>

# ```{admonition} Equity vs. Bond
# Bond
# : Paid a fixed interest rate (coupon) to debtholders.
# : e.g. treasury bonds, corporate bonds.
# <br><br>
# Equity
# : Value that would be returned to a company’s shareholders if all of the assets were liquidated and all of the company's debts were paid off.
# ```

# ## Relationship between Bond Price and Interest Rate

# > For example, there is a corporate bond with a face value of \$100, a coupon rate of 5% and a duration of 1 year. This means that investors can pay \$100 for this bond today. Next year, the investor can get \$105 (\$100 as the face value and \$5 as the interest).<br><br>
# > Will this bond be worth more if the interest rate is higher or lower?

# Method 1:
# - If the interest rate is 3%, this bond will have a higher value. If you deposit \$100 in your bank account, you will get \$103 next year. The corporate bond pays more and more people will want to buy this bond. So, the bond price will increase.
# - If the interest rate is 7%, this bond will have a higher value. If you deposit \$100 in your bank account, you will get \$107 next year. The corporate bond pays less and less people will want to buy this bond. So, the bond price will decrease.

# Method 2:
# 
# **(1+r)PV = FV**, where PV is the present value (money paid today), FV is the future value (money get back next year), and r is the interest rate.<br>
# 
# Hence, price paid today = PV = FV/(1+r).
# - If the interest rate increases, the price will decrease.
# - If the interest rate decreases, the price will increase.

# ```{important}
# The price of bonds and interest rates on bonds are inversely related.<br>
# 
# The opportunity cost of holding money is the interest.
# ```
