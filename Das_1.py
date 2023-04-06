import streamlit as st
import pandas as pd
import numpy as np


def main ():
    x = st.slider("Select a value")
    st.write(x, "squared is", x * x)

    st.write(pd.DataFrame({
                        'first column': [1, 2, 3, 4],
                        'second column': [10, 20, 30, 40]
                    }))

    
    st.write("I LIKE THIS")

    dataframe = pd.DataFrame(
                        np.random.randn(10, 20),
                        columns=('col %d' % i for i in range(20)))

    st.dataframe(dataframe.style.highlight_max(axis=0))



if __name__== "__main__":

    main()