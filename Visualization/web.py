import streamlit as st
import plotly as py
import plotly_express as px
import pandas as pd
# import plotly.graph_objects as go
import altair as alt

# Title
st.set_page_config(page_title='Income-Expense', page_icon='💲', layout='wide', initial_sidebar_state='auto')
st.subheader('Income - Expense Visualzation')

#Read the Dataset
df = pd.read_csv('Inc_Exp_Data.csv')

#-----Columns-----#
col1, col2 = st.columns(2)

#Show Dataframe
st.dataframe(df)


# -------SIDEBAR-------
st.sidebar.subheader('Select the parameters')
member = st.sidebar.multiselect('Select the Qualified Member', options = df['Highest_Qualified_Member'].unique())

#filter the data
df_selection = df.query('Highest_Qualified_Member == @member')



# -------MAIN-------

# avg_popularity = df['Popularity'].mean()
# st.write('Average Popularity:', round(avg_popularity, 2))

# -------PLOTLY-------
values = df['Annual_HH_Income']     #values for pie chart
names = df['Highest_Qualified_Member']  #labels for pie chart
fig = px.pie(df, values=values, names=names, title='Income Distribution') #create pie chart

#update traces
fig.update_traces(textposition='inside', textinfo='percent+label')  #show labels inside pie chart

#update layout
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')  #hide labels that don't fit inside slices


#altair
st.subheader('Monthy income-Expense of different Households')   #title
chart = alt.Chart(df).mark_circle().encode(     #create chart
    x='Mthly_HH_Income',                            #x-axis
    y='Mthly_HH_Expense',                           #y-axis
    color='Highest_Qualified_Member',           #color
).interactive()                                 #enable zoom

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])  #create tabs

#display piechart
st.subheader('Annual Income Distribution')  #title
st.plotly_chart(fig)    #display chart

with col1:      #display altair chart
    with tab1:  #display altair chart with streamlit theme
        # Use the Streamlit theme.
        # This is the default. So you can also omit the theme argument.
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        # Use the native Altair theme.
        st.altair_chart(chart, theme=None, use_container_width=True)
    

#barchart not showing
chart_data = pd.DataFrame(df['Highest_Qualified_Member'],columns=['Mthly_HH_Income','Mthly_HH_Expense'])

st.bar_chart(chart_data)

with col1:
    st.subheader('Average Income')
    st.write('Average Income', df['Annual_HH_Income'].mean())   #average income

    st.subheader('What is the Monthly Expense for most of the Households?') #title
    mth_exp_tmp = pd.crosstab(index=df["Mthly_HH_Expense"], columns="count")    #count the number of times each value appears
    mth_exp_tmp.reset_index(inplace=True)   #reset index
    mth_exp_tmp[mth_exp_tmp['count'] == df.Mthly_HH_Expense.value_counts().max()]   #find the value that appears the most

    st.subheader('Calculate IQR(difference between 75% and 25% quartile)')
    df.plot(x="Mthly_HH_Income", y="Mthly_HH_Expense")  #plot the scatter plot
    IQR=df["Mthly_HH_Expense"].quantile(0.75)-df["Mthly_HH_Expense"].quantile(0.25) #calculate IQR
    st.write('IQR', IQR)    #display IQR
    line_chart = alt.Chart(df).mark_line().encode(      #create line chart
        y= 'Mthly_HH_Expense',      #y-axis
        x=  'Mthly_HH_Income',      #x-axis
    ) 
    st.altair_chart(line_chart, use_container_width=True)       #display line chart


#Plot the Histogram to count the Highest qualified member
with col2:
    st.subheader('What is the Highest Qualified Member?')
    st.bar_chart(df["Highest_Qualified_Member"].value_counts()) #display bar chart

    # df["No_of_Earning_Members"].value_counts().plot(kind="bar")
    #No. of earning members
    st.bar_chart(df["No_of_Earning_Members"].value_counts())    #display bar chart






# fig = go.Figure(
#     data=[go.Bar(x=df['Annual_HH_Income'], y=df['Highest_Qualified_Member'])],
#     layout_title_text="A Figure Displayed with fig.show()")
# st.plotly_chart(fig)

# st.checkbox("Use container width", value=False, key="use_container_width")


