import streamlit as st
import pandas as pd
#import altair as alt
import matplotlib.pyplot as plt


st.set_option('deprecation.showPyplotGlobalUse', False)


def app():
    #Header
    st.write("Training data used")


    #Reading the data
    training_sample_subset=pd.read_csv("training_sample_subset.csv")


    #display the data as a table
    st.write(training_sample_subset.head(30))


    #header
    st.write("Distribution of Orders (Dependent variable)")


    #bar plot
    temp=training_sample_subset["ordered"].value_counts()
    fig, ax = plt.subplots()
    ax.bar(["Not ordered","Ordered"],temp,color ='maroon',width = 0.4)
    plt.xlabel("Order status")
    plt.ylabel("No. of customers")
    st.pyplot()