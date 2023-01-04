#Import Library
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

#amount of number in the sequence
n = st.slider('Enter the number of terms in the sequence', 1, 10, 1)

#domain list
domain_list = [i for i in range(1,n+1)]

range_list = []

#loop's input's key
x = 1

#range input
for i in range(n):
    x = x+1
    range_list.append(st.number_input('Enter a number', step=1, key=x))

#define highest polynomial degree
highest_polynomial_degree = st.slider('Enter highest polynomial degree', 1, 8, 1)

coefficients = np.polyfit(domain_list, range_list, highest_polynomial_degree)
poly = np.poly1d(coefficients)
new_x = np.linspace(domain_list[0], domain_list[-1])
new_y = poly(new_x)

#predict next term
next_term_answer = poly(n+1).round(5)
st.write("""
##### The answer equal : 
""",next_term_answer)

#plot the sequence with best fit line
fig, ax = plt.subplots()
ax.plot(domain_list, range_list, "o", new_x, new_y, n+1, next_term_answer, "o")
st.pyplot(fig)

#print coefficient
st.write("""
##### Coefficients equal : 
""",poly)

#predict n term
y = st.number_input('predict n term', step=1)
n_term_answer = poly(y).round(5)
st.write("""
##### The answer equal : 
""",n_term_answer)

st.write("""


### Code
""")

code = '''
#Import Library
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

#amount of number in the sequence
n = st.slider('Enter the number of terms in the sequence', 1, 10, 1)

#domain list
domain_list = [i for i in range(1,n+1)]

range_list = []

#loop's input's key
x = 1

#range input
for i in range(n):
    x = x+1
    range_list.append(st.number_input('Enter a number', step=1, key=x))

#define highest polynomial degree
highest_polynomial_degree = st.slider('Enter highest polynomial degree', 1, 8, 1)

coefficients = np.polyfit(domain_list, range_list, highest_polynomial_degree)
poly = np.poly1d(coefficients)
new_x = np.linspace(domain_list[0], domain_list[-1])
new_y = poly(new_x)

#predict next term
next_term_answer = poly(n+1).round(5)
st.write("""
##### The answer equal : 
""",next_term_answer)

#plot the sequence with best fit line
fig, ax = plt.subplots()
ax.plot(domain_list, range_list, "o", new_x, new_y, n+1, next_term_answer, "o")
st.pyplot(fig)

#print coefficient
st.write("""
##### Coefficients equal : 
""",poly)

#predict n term
y = st.number_input('predict n term', step=1)
n_term_answer = poly(y).round(5)
st.write("""
##### The answer equal : 
""",n_term_answer)
'''

st.code(code, language='python')