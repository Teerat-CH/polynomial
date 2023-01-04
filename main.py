import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

n = st.slider('Enter number count', 1, 10, 1)

lst = [i for i in range(1,n+1)]

list_of_sequence = []

x = 1

for i in range(n):
    x = x+1
    list_of_sequence.append(st.number_input('Insert a number', step=1, key=x))

p = st.slider('Maximum power', 1, 8, 1)

coefficients = np.polyfit(lst, list_of_sequence, p)

poly = np.poly1d(coefficients)

new_x = np.linspace(lst[0], lst[-1])

new_y = poly(new_x)

y = st.number_input('predict N', step=1)
answer = poly(y).round(5)

st.write(answer)

fig, ax = plt.subplots()
ax.plot(lst, list_of_sequence, "o", new_x, new_y, y, answer, "o")

st.pyplot(fig)