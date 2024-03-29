import streamlit as st
import pandas as pd
import numpy as np



def main ():
    x = st.slider("Select a value")
    st.write(x, "squared is", x * x)

    df=pd.DataFrame({
                        'first column': [1, 2, 3, 4],
                        'second column': [10, 20, 30, 40]
                    })

    st.write(df)

    
    st.write("I LIKE THIS")

    dataframe = pd.DataFrame(
                        np.random.randn(10, 20),
                        columns=('col %d' % i for i in range(20)))

    st.dataframe(dataframe.style.highlight_max(axis=0))

    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

        chart_data

    add_selectbox = st.sidebar.selectbox(
            'How would you like to be contacted?',
            ('Email', 'Home phone', 'Mobile phone')
        )

# Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )

    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)
    



if __name__== "__main__":

    main()
   