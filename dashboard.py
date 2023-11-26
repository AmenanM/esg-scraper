# Initial page config
import streamlit as st
import pandas as pd
import yfinance as yfin


st.set_page_config(
     page_title='esg dashboard',
     layout="wide",
     initial_sidebar_state="expanded",
)
# read datasets
map=pd.read_csv('mapping.csv')
df=map.head(12)
#Header
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True) #reduce white space on top of page
st.markdown("<h1 style='text-align: left;color:#2c9451'>ESG <span style='color:#080808'>Dashboard</h1>", unsafe_allow_html=True)
# st.markdown('<p style="color:#fc0000;background-color:#404040">Text Color Yellow <span style="color:#ffffff">Text Color White</span></p>', unsafe_allow_html=True)


# st.markdown("<h5 style='text-align: left;'>An individual's personal budget and their list of transactions. Analysis of these data in detail.</h1>", unsafe_allow_html=True)
st.write('')
st.markdown("<h6 style='text-align: left;'>A few of the top 500 companies ESG score metrics</h6>", unsafe_allow_html=True)
st.write('')

#Write company names

def name_ticker(x):
    try:
        name=yfin.Ticker(x).info['longName']
    except:
        name=x
    return name

df['name']=df['Ticker'].apply(lambda x :name_ticker(x))

#selection
select_name=st.selectbox('', list(df['name'].unique()))

col1,col2,col3,col4,col5,col6=st.columns(6)

with col1:
    st.write('')
    st.markdown("<h3 style='text-align: left;'>Total ESG Score</h1>", unsafe_allow_html=True)
with col2:
    value_score=df.loc[df['name'] == select_name, 'Total ESG Score'].iloc[0]
    st.markdown(f"""<h2 style='text-align: left;color:#692c94'>{value_score}</h1>""", unsafe_allow_html=True)
with col3:
    st.write('')
    st.markdown("<h3 style='text-align: left;'>Controvercy score</h1>", unsafe_allow_html=True)
with col4:
    value_score=df.loc[df['name'] == select_name, 'Controversy Score'].iloc[0]
    st.markdown(f"""<h2 style='text-align: left;color:#692c94'>{value_score}</h1>""", unsafe_allow_html=True)
st.write('---')
col1,col2,col3=st.columns(3)
with col1:
    st.metric('Environment', df.loc[df['name'] == select_name, 'Environment'].iloc[0], delta=None, delta_color="normal", help=None, label_visibility="visible")

with col2:
    st.metric('Social', df.loc[df['name'] == select_name, 'Social'].iloc[0], delta=None, delta_color="normal", help=None, label_visibility="visible")
with col3:
    st.metric('Governance', df.loc[df['name'] == select_name, 'Governance'].iloc[0], delta=None, delta_color="normal", help=None, label_visibility="visible")
col1,col2,col3=st.columns(3)
with col1:
    st.subheader('Company info')
    value_sector=df.loc[df['name'] == select_name, 'Sector'].iloc[0]
    st.markdown(f"""<h6 style='text-align: left;font-weight:bold'>Sector: <span style='color:#080808'>{value_sector}</span></p>""", unsafe_allow_html=True)
    value_hq=df.loc[df['name'] == select_name, 'Headquarter'].iloc[0]
    st.markdown(f"""<h6 style='text-align: left;font-weight:bold'>Headquarter: <span style='color:#080808'>{value_hq}</span></p>""", unsafe_allow_html=True)
    # Industry	Headquarter	Total ESG Score	Environment	Social	Governance	Controversy Score	City	State	Country
    value_loc=df.loc[df['name'] == select_name, 'City'].iloc[0]
    valuee_loc=df.loc[df['name'] == select_name, 'Country'].iloc[0]
    st.markdown(f"""<h6 style='text-align: left;font-weight:bold'>Country: <span style='color:#080808'>{valuee_loc}</span></p>""", unsafe_allow_html=True)
with col2:
    st.subheader('Financials')
    company_ticker = yfin.Ticker(df.loc[df['name'] == select_name, 'Ticker'].iloc[0])
    df_name=pd.DataFrame(company_ticker.income_stmt)
    st.dataframe(df_name)

with col3:
    company_ticker = yfin.Ticker(df.loc[df['name'] == select_name, 'Ticker'].iloc[0])
