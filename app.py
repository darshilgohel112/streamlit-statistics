import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

st.title("Central Limit Theorem Demo")

dist = st.selectbox("Distribution", ["Exponential", "Uniform", "Bernoulli"])
n = st.slider("Sample size", 1, 500, 30)
sims = st.slider("Number of simulations", 100, 5000, 1000)

if dist == "Exponential":
    data = np.random.exponential(size=(sims, n))
elif dist == "Uniform":
    data = np.random.uniform(size=(sims, n))
else:
    data = np.random.binomial(1, 0.5, size=(sims, n))

means = data.mean(axis=1)

fig, ax = plt.subplots()
ax.hist(means, bins=30, density=True, alpha=0.7)
mu, sigma = means.mean(), means.std()
x = np.linspace(means.min(), means.max(), 200)
ax.plot(x, norm.pdf(x, mu, sigma))
ax.set_title("Sampling Distribution of the Mean")

st.pyplot(fig)
