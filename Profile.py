import streamlit as st 
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.graph_objs as go
import pickle
import plotly.express as px

data = pd.read_csv("C:/Users/HP/Documents/hackathon/cleaned_data (1).csv.xls")

def run_website():
    with st.sidebar:
        selected = option_menu('Vental Capital Analysis Website',
                            
                            ['Analytics Dashboard',
                             'Categorical ranking',
                            'Predicting success probability',
                            'Implement own dataset'],
                            default_index=0)
        
        
    if(selected == 'Analytics Dashboard'):

        st.write("To be coded")

        fig = go.Figure(data=go.Scatter(x=data["incorporated_date_c"], y=data["total_funding_c"], mode='markers'))
        # Add axis labels and title
        fig.update_layout(xaxis_title="Incorporation Date", yaxis_title="Total Funding Amount", title="Company Funding")

        # Show plot
        st.plotly_chart(fig)


        # Create a slider to select the year
        year = st.slider("Select year", min_value=int(data["incorporated_date_c"].min()), max_value=int(data["incorporated_date_c"].max()))

        # Filter the data based on the selected year
        data_filtered = data[data["incorporated_date_c"] == year]

        # Create the plot using Plotly Express
        fig = px.scatter(data_filtered, x="incorporated_date_c", y="total_funding_c",color="category")

        # Display the plot
        st.plotly_chart(fig)

    if(selected == 'Categorical ranking'):

        st.title('Categorical Ranking')
        num_var_display = ['Total Funding','Last Valuation','last funding amount','Latest year revenue','Revenue growth','Earnings before Interest and Tax','Employee growth past 6 months','Employee growth past 12 months','Number of founders','Number of funding rounds','Number of shareholders','Minimum share','Median share','Max Share']
        num_var = ['total_funding_c','last_valuation_c','last_round_size_c','revenue_c','revenue_growth(%)','EBIT_c','employee_growth_6(%)','employee_growth_12(%)','num_founders','num_funding_rounds','num_shareholders','min_share','median_share','max_share']
        feature = st.selectbox('Select a feature',options = num_var)

        sorted = data.sort_values(feature, ascending = True)

        # Get the top 10 and bottom 10 companies based on the selected feature
        top_10 = sorted.head(10)
        bottom_10 = sorted.tail(10)

        st.write("Top 10")
        st.write(top_10)
        st.write("Bottom 10")
        st.write(bottom_10)
        
        
        #Create a list of other features to plot
        other_features = [f for f in num_var if f != feature]

        # Plot double line graph for each feature
        for f in other_features:
            fig = go.Figure()

            # Add top 10 line
            fig.add_trace(go.Scatter(x=top_10[feature], y=top_10[f], mode='lines', name='Top 10'))

            # Add bottom 10 line
            fig.add_trace(go.Scatter(x=bottom_10[feature], y=bottom_10[f], mode='lines', name='Bottom 10'))

            # Add axis labels and title
            fig.update_layout(xaxis_title=feature, yaxis_title=num_var_display[num_var.index(f)], title=f"{num_var_display[num_var.index(f)]} vs {feature}")

            # Display the plot
            st.plotly_chart(fig)

  

    if(selected == 'Predicting success probability'):

        st.title('Predicting success probability')
        col1, col2, col3 = st.columns(3)


    if(selected == 'Implement own dataset'):

        st.title('Implement your dataset')
        file = st.file_uploader("Upload Your Dataset")
        if file:
            df = pd.read_csv(file,index_col = None)
            df.to_csv('dataset.csv', index = None)

run_website()