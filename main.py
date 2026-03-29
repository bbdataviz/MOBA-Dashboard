import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="MoBa Pregnancy and Child Growth Dashboard",
    layout="wide",
    initial_sidebar_state="expanded")


### Load data subset
# length (box)
source4_1 = pd.read_csv('data/subdata/CC388_len_1.csv', encoding='utf-8')
source5_1 = pd.read_csv('data/subdata/CC389_len_1.csv', encoding='utf-8')
source6_1 = pd.read_csv('data/subdata/CC390_len_1.csv', encoding='utf-8')
source7_1 = pd.read_csv('data/subdata/CC391_len_1.csv', encoding='utf-8')
source8_1 = pd.read_csv('data/subdata/CC392_len_1.csv', encoding='utf-8')
source4_2 = pd.read_csv('data/subdata/CC388_len_2.csv', encoding='utf-8')
source5_2 = pd.read_csv('data/subdata/CC389_len_2.csv', encoding='utf-8')
source6_2 = pd.read_csv('data/subdata/CC390_len_2.csv', encoding='utf-8')
source7_2 = pd.read_csv('data/subdata/CC391_len_2.csv', encoding='utf-8')
source8_2 = pd.read_csv('data/subdata/CC392_len_2.csv', encoding='utf-8')
source4_3 = pd.read_csv('data/subdata/CC141_len_3.csv', encoding='utf-8')
source5_3 = pd.read_csv('data/subdata/CC142_len_3.csv', encoding='utf-8')
source6_3 = pd.read_csv('data/subdata/CC143_len_3.csv', encoding='utf-8')
source7_3 = pd.read_csv('data/subdata/CC144_len_3.csv', encoding='utf-8')
source8_3 = pd.read_csv('data/subdata/CC145_len_3.csv', encoding='utf-8')
# weight (box)
source4_1w = pd.read_csv('data/subdata/CC388_wei_1.csv', encoding='utf-8')
source5_1w = pd.read_csv('data/subdata/CC389_wei_1.csv', encoding='utf-8')
source6_1w = pd.read_csv('data/subdata/CC390_wei_1.csv', encoding='utf-8')
source7_1w = pd.read_csv('data/subdata/CC391_wei_1.csv', encoding='utf-8')
source8_1w = pd.read_csv('data/subdata/CC392_wei_1.csv', encoding='utf-8')
source4_2w = pd.read_csv('data/subdata/CC388_wei_2.csv', encoding='utf-8')
source5_2w = pd.read_csv('data/subdata/CC389_wei_2.csv', encoding='utf-8')
source6_2w = pd.read_csv('data/subdata/CC390_wei_2.csv', encoding='utf-8')
source7_2w = pd.read_csv('data/subdata/CC391_wei_2.csv', encoding='utf-8')
source8_2w = pd.read_csv('data/subdata/CC392_wei_2.csv', encoding='utf-8')
source4_3w = pd.read_csv('data/subdata/CC141_wei_3.csv', encoding='utf-8')
source5_3w = pd.read_csv('data/subdata/CC142_wei_3.csv', encoding='utf-8')
source6_3w = pd.read_csv('data/subdata/CC143_wei_3.csv', encoding='utf-8')
source7_3w = pd.read_csv('data/subdata/CC144_wei_3.csv', encoding='utf-8')
source8_3w = pd.read_csv('data/subdata/CC145_wei_3.csv', encoding='utf-8')
# length (histo)
source4_1h = pd.read_csv('data/subdata/CC388_len_1h.csv', encoding='utf-8')
source5_1h = pd.read_csv('data/subdata/CC389_len_1h.csv', encoding='utf-8')
source6_1h = pd.read_csv('data/subdata/CC390_len_1h.csv', encoding='utf-8')
source7_1h = pd.read_csv('data/subdata/CC391_len_1h.csv', encoding='utf-8')
source8_1h = pd.read_csv('data/subdata/CC392_len_1h.csv', encoding='utf-8')
source4_2h = pd.read_csv('data/subdata/CC388_len_2h.csv', encoding='utf-8')
source5_2h = pd.read_csv('data/subdata/CC389_len_2h.csv', encoding='utf-8')
source6_2h = pd.read_csv('data/subdata/CC390_len_2h.csv', encoding='utf-8')
source7_2h = pd.read_csv('data/subdata/CC391_len_2h.csv', encoding='utf-8')
source8_2h = pd.read_csv('data/subdata/CC392_len_2h.csv', encoding='utf-8')
source4_3h = pd.read_csv('data/subdata/CC141_len_3h.csv', encoding='utf-8')
source5_3h = pd.read_csv('data/subdata/CC142_len_3h.csv', encoding='utf-8')
source6_3h = pd.read_csv('data/subdata/CC143_len_3h.csv', encoding='utf-8')
source7_3h = pd.read_csv('data/subdata/CC144_len_3h.csv', encoding='utf-8')
source8_3h = pd.read_csv('data/subdata/CC145_len_3h.csv', encoding='utf-8')
# weigth (histo)
source4_1wh = pd.read_csv('data/subdata/CC388_wei_1h.csv', encoding='utf-8')
source5_1wh = pd.read_csv('data/subdata/CC389_wei_1h.csv', encoding='utf-8')
source6_1wh = pd.read_csv('data/subdata/CC390_wei_1h.csv', encoding='utf-8')
source7_1wh = pd.read_csv('data/subdata/CC391_wei_1h.csv', encoding='utf-8')
source8_1wh = pd.read_csv('data/subdata/CC392_wei_1h.csv', encoding='utf-8')
source4_2wh = pd.read_csv('data/subdata/CC388_wei_2h.csv', encoding='utf-8')
source5_2wh = pd.read_csv('data/subdata/CC389_wei_2h.csv', encoding='utf-8')
source6_2wh = pd.read_csv('data/subdata/CC390_wei_2h.csv', encoding='utf-8')
source7_2wh = pd.read_csv('data/subdata/CC391_wei_2h.csv', encoding='utf-8')
source8_2wh = pd.read_csv('data/subdata/CC392_wei_2h.csv', encoding='utf-8')
source4_3wh = pd.read_csv('data/subdata/CC141_wei_3h.csv', encoding='utf-8')
source5_3wh = pd.read_csv('data/subdata/CC142_wei_3h.csv', encoding='utf-8')
source6_3wh = pd.read_csv('data/subdata/CC143_wei_3h.csv', encoding='utf-8')
source7_3wh = pd.read_csv('data/subdata/CC144_wei_3h.csv', encoding='utf-8')
source8_3wh = pd.read_csv('data/subdata/CC145_wei_3h.csv', encoding='utf-8')
# Sex
source_sex = pd.read_csv('data/subdata/girls_boys.csv', encoding='utf-8')


#######################
### Plots
## Box plot

def create_boxplot(source, color_code, title_txt):
    boxplot = alt.Chart(source).mark_boxplot(color= color_code).encode(
        alt.Y('outcome_level:Q', scale=alt.Scale(domain=[5, 75]), title='Length [cm]')
    ).properties(
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17
    }
    ).configure_axis(
    labelFontSize=13,
    titleFontSize=15
    ).interactive()
    return boxplot

def create_boxplot_w(source, color_code, title_txt):
    #title = alt.TitleParams(text="No NVP (n=33040)")
    boxplot = alt.Chart(source).mark_boxplot(color= color_code).encode(
    alt.Y('outcome_level:Q', scale=alt.Scale(domain=[0, 10000]), title='Weight [g]')
    ).properties(
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17
    }
    ).configure_axis(
    labelFontSize=13,
    titleFontSize=15
    ).interactive() 
    return boxplot

## Histogram
def create_histo(source, color_code, title_txt):
    histo = alt.Chart(source).mark_bar(color= color_code).encode( 
        alt.X('outcome_level:Q', bin=alt.Bin(extent=[0, 70], step=2),  title='Length [cm]'),
        alt.Y('n:Q'),  
    ).properties(
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17
    }
    ).configure_axis( 
    labelFontSize=13,
    titleFontSize=15
    ).interactive(bind_y=False)
    return histo  


def create_histo_w(source, color_code, title_txt):
    histo = alt.Chart(source).mark_bar(color= color_code).encode(  
        alt.X('outcome_level:Q', bin=alt.Bin(extent=[0, 10000], step=200),  title='Weight [g]'),
        alt.Y('n:Q'),   
    ).properties(
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17
    }
    ).configure_axis(
    labelFontSize=13,
    titleFontSize=15
    ).interactive(bind_y=False)  
    return histo


def create_barchart_sex(source, color_code, title_txt):
        
    barchart = alt.Chart(source).mark_bar(color=color_code).encode(
        alt.X('outcome_level:N', title='Sex'),
        alt.Y('n:Q', title='n'),
        
    ).properties(
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17
    }).configure_axis( 
        labelFontSize=13,
        titleFontSize=15
    )
    # (1 = Girls, 2 = Boys, 3 = Missing)
    return barchart 

#######################
## Layout
col1, col2, col3, col4 = st.columns([1,1,1,1])

# Define colors for patient groups
color1="#038d93"    # turquoise "#0097a7"
color2="#5443aa"    # violett 
color3="#882255"    # dark red
color4="#88ccee"    # light blue


sub_sex_any = source_sex.loc[(source_sex.category == 'any').reset_index(drop=True)]
# No NVP
sub_sex_4_1 = source_sex.loc[(source_sex.category == 'CC388').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_5_1 = source_sex.loc[(source_sex.category == 'CC389').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_6_1 = source_sex.loc[(source_sex.category == 'CC390').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_7_1 = source_sex.loc[(source_sex.category == 'CC391').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_8_1 = source_sex.loc[(source_sex.category == 'CC392').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
# NVP
sub_sex_4_2 = source_sex.loc[(source_sex.category == 'CC388').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_5_2 = source_sex.loc[(source_sex.category == 'CC389').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_6_2 = source_sex.loc[(source_sex.category == 'CC390').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_7_2 = source_sex.loc[(source_sex.category == 'CC391').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_8_2 = source_sex.loc[(source_sex.category == 'CC392').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
# Hospital
sub_sex_4_3 = source_sex.loc[(source_sex.category == 'CC141').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_5_3 = source_sex.loc[(source_sex.category == 'CC142').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_6_3 = source_sex.loc[(source_sex.category == 'CC143').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_7_3 = source_sex.loc[(source_sex.category == 'CC144').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_8_3 = source_sex.loc[(source_sex.category == 'CC145').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]

# calculate sums for n
sum_any = source_sex.loc[(source_sex['category'] == 'any').reset_index(drop=True) & (source_sex['level'] == 'any').reset_index(drop=True), 'n'].sum()
sum4_1 = source_sex.loc[(source_sex['category'] == 'CC388').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() # 80960 
sum4_2 = source_sex.loc[(source_sex['category'] == 'CC388').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum5_1 = source_sex.loc[(source_sex['category'] == 'CC389').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() 
sum5_2 = source_sex.loc[(source_sex['category'] == 'CC389').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum6_1 = source_sex.loc[(source_sex['category'] == 'CC390').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() 
sum6_2 = source_sex.loc[(source_sex['category'] == 'CC390').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum7_1 = source_sex.loc[(source_sex['category'] == 'CC391').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() 
sum7_2 = source_sex.loc[(source_sex['category'] == 'CC391').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum8_1 = source_sex.loc[(source_sex['category'] == 'CC392').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() 
sum8_2 = source_sex.loc[(source_sex['category'] == 'CC392').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 

sum4_3 = source_sex.loc[(source_sex['category'] == 'CC141').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum5_3 = source_sex.loc[(source_sex['category'] == 'CC142').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum()
sum6_3 = source_sex.loc[(source_sex['category'] == 'CC143').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum()
sum7_3 = source_sex.loc[(source_sex['category'] == 'CC144').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum()
sum8_3 = source_sex.loc[(source_sex['category'] == 'CC145').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum()

with col1:
    #### No NVP
    ### BIRTH LENGTH
    
    boks4_1 = create_boxplot(source4_1, color1, "No NVP (n=" + str(sum4_1) + ")")
    st.altair_chart(boks4_1, use_container_width=True)

    histo4_1 = create_histo(source4_1h, color1, "No NVP (n=" + str(sum4_1) + ")")
    st.altair_chart(histo4_1, use_container_width=True)
   
    boks5_1 = create_boxplot(source5_1, color1, "No NVP (n=" + str(sum5_1) + ")")
    st.altair_chart(boks5_1, use_container_width=True)
    histo5_1 = create_histo(source5_1h, color1, "No NVP (n=" + str(sum5_1) + ")")
    st.altair_chart(histo5_1, use_container_width=True)
    
    boks6_1 = create_boxplot(source6_1, color1, "No NVP (n=" + str(sum6_1) + ")")
    st.altair_chart(boks6_1, use_container_width=True)
    histo6_1 = create_histo(source6_1h, color1, "No NVP (n=" + str(sum6_1) + ")")
    st.altair_chart(histo6_1, use_container_width=True)
   
    boks7_1 = create_boxplot(source7_1, color1, "No NVP (n=" + str(sum7_1) + ")")
    st.altair_chart(boks7_1, use_container_width=True)
    histo7_1 = create_histo(source7_1h, color1, "No NVP (n=" + str(sum7_1) + ")")
    st.altair_chart(histo7_1, use_container_width=True)
    
    boks8_1 = create_boxplot(source8_1, color1, "No NVP (n=" + str(sum8_1) + ")")
    st.altair_chart(boks8_1, use_container_width=True)
    histo8_1 = create_histo(source8_1h, color1, "No NVP (n=" + str(sum8_1) + ")")
    st.altair_chart(histo8_1, use_container_width=True)
    
    ### BIRTH WEIGHT
    
    boks4_1 = create_boxplot_w(source4_1w, color1, "No NVP (n=" + str(sum4_1) + ")")
    st.altair_chart(boks4_1, use_container_width=True)
    histo4_1 = create_histo_w(source4_1wh, color1, "No NVP (n=" + str(sum4_1) + ")")
    st.altair_chart(histo4_1, use_container_width=True)

    boks5_1w = create_boxplot_w(source5_1w, color1, "No NVP (n=" + str(sum5_1) + ")")
    st.altair_chart(boks5_1w, use_container_width=True)
    histo5_1 = create_histo_w(source5_1wh, color1, "No NVP (n=" + str(sum5_1) + ")")
    st.altair_chart(histo5_1, use_container_width=True)
  
    boks6_1 = create_boxplot_w(source6_1w, color1, "No NVP (n=" + str(sum6_1) + ")")
    st.altair_chart(boks6_1, use_container_width=True)
    histo6_1 = create_histo_w(source6_1wh, color1, "No NVP (n=" + str(sum6_1) + ")")
    st.altair_chart(histo6_1, use_container_width=True)

    boks7_1 = create_boxplot_w(source7_1w, color1, "No NVP (n=" + str(sum7_1) + ")")
    st.altair_chart(boks7_1, use_container_width=True)
    histo7_1 = create_histo_w(source7_1wh, color1, "No NVP (n=" + str(sum7_1) + ")")
    st.altair_chart(histo7_1, use_container_width=True)

    boks8_1 = create_boxplot_w(source8_1w, color1, "No NVP (n=" + str(sum8_1) + ")")
    st.altair_chart(boks8_1, use_container_width=True)
    histo8_1 = create_histo_w(source8_1wh, color1, "No NVP (n=" + str(sum8_1) + ")")
    st.altair_chart(histo8_1, use_container_width=True)

with col2:
    #### pNVP
    ### BIRTH LENGTH

    boks4_2 = create_boxplot(source4_2, color2, "NVP (n=" + str(sum4_2) + ")")
    st.altair_chart(boks4_2, use_container_width=True)
    histo4_2 = create_histo(source4_2h, color2, "NVP (n=" + str(sum4_2) + ")")
    st.altair_chart(histo4_2, use_container_width=True)

    boks5_2 = create_boxplot(source5_2, color2, "NVP (n=" + str(sum5_2) + ")")
    st.altair_chart(boks5_2, use_container_width=True)
    histo5_2 = create_histo(source5_2h, color2, "NVP (n=" + str(sum5_2) + ")")
    st.altair_chart(histo5_2, use_container_width=True)
   
    boks6_2 = create_boxplot(source6_2, color2, "NVP (n=" + str(sum6_2) + ")")
    st.altair_chart(boks6_2, use_container_width=True)
    histo6_2 = create_histo(source6_2h, color2, "NVP (n=" + str(sum6_2) + ")")
    st.altair_chart(histo6_2, use_container_width=True)
   
    boks7_2 = create_boxplot(source7_2, color2, "NVP (n=" + str(sum7_2) + ")")
    st.altair_chart(boks7_2, use_container_width=True)
    histo7_2 = create_histo(source7_2h, color2, "NVP (n=" + str(sum7_2) + ")")
    st.altair_chart(histo7_2, use_container_width=True)

    boks8_2 = create_boxplot(source8_2, color2, "NVP (n=" + str(sum8_2) + ")")
    st.altair_chart(boks8_2, use_container_width=True)
    histo8_2 = create_histo(source8_2h, color2, "NVP (n=" + str(sum8_2) + ")")
    st.altair_chart(histo8_2, use_container_width=True)

    ### BIRTH WEIGHT
 
    boks4_2 = create_boxplot_w(source4_2w, color2, "NVP (n=" + str(sum4_2) + ")")
    st.altair_chart(boks4_2, use_container_width=True)
    histo4_2 = create_histo_w(source4_2wh, color2, "NVP (n=" + str(sum4_2) + ")")
    st.altair_chart(histo4_2, use_container_width=True)

    boks5_2 = create_boxplot_w(source5_2w, color2, "NVP (n=" + str(sum5_2) + ")")
    st.altair_chart(boks5_2, use_container_width=True)
    histo5_2 = create_histo_w(source5_2wh, color2, "NVP (n=" + str(sum5_2) + ")")
    st.altair_chart(histo5_2, use_container_width=True)

    boks6_2 = create_boxplot_w(source6_2w, color2, "NVP (n=" + str(sum6_2) + ")")
    st.altair_chart(boks6_2, use_container_width=True)
    histo6_2 = create_histo_w(source6_2wh, color2, "NVP (n=" + str(sum6_2) + ")")
    st.altair_chart(histo6_2, use_container_width=True)
 
    boks7_2 = create_boxplot_w(source7_2w, color2, "NVP (n=" + str(sum7_2) + ")")
    st.altair_chart(boks7_2, use_container_width=True)
    histo7_2 = create_histo_w(source7_2wh, color2, "NVP (n=" + str(sum7_2) + ")")
    st.altair_chart(histo7_2, use_container_width=True)
  
    boks8_2 = create_boxplot_w(source8_2w, color2, "NVP (n=" + str(sum8_2) + ")")
    st.altair_chart(boks8_2, use_container_width=True)
    histo8_2 = create_histo_w(source8_2wh, color2, "NVP (n=" + str(sum8_2) + ")")
    st.altair_chart(histo8_2, use_container_width=True)

with col3:
    ### Hospitalized
    # LENGTH
    boks4_3 = create_boxplot(source4_3, color3, "Hospitalized (n=" + str(sum4_3) + ")")
    st.altair_chart(boks4_3, use_container_width=True)
    histo4_3 = create_histo(source4_3h, color3, "Hospitalized (n=" + str(sum4_3) + ")")
    st.altair_chart(histo4_3, use_container_width=True)
 
    boks5_3 = create_boxplot(source5_3, color3, "Hospitalized (n=" + str(sum5_3) + ")")
    st.altair_chart(boks5_3, use_container_width=True)
    histo5_3 = create_histo(source5_3h, color3, "Hospitalized (n=" + str(sum5_3) + ")")
    st.altair_chart(histo5_3, use_container_width=True)
 
    boks6_3 = create_boxplot(source6_3, color3, "Hospitalized (n=" + str(sum6_3) + ")")
    st.altair_chart(boks6_3, use_container_width=True)
    histo6_3 = create_histo(source6_3h, color3, "Hospitalized (n=" + str(sum6_3) + ")")
    st.altair_chart(histo6_3, use_container_width=True)
   
    boks7_3 = create_boxplot(source7_3, color3, "Hospitalized (n=" + str(sum7_3) + ")")
    st.altair_chart(boks7_3, use_container_width=True)
    histo7_3 = create_histo(source7_3h, color3, "Hospitalized (n=" + str(sum7_3) + ")")
    st.altair_chart(histo7_3, use_container_width=True)
  
    boks8_3 = create_boxplot(source8_3, color3, "Hospitalized (n=" + str(sum8_3) + ")")
    st.altair_chart(boks8_3, use_container_width=True)
    histo8_3 = create_histo(source8_3h, color3, "Hospitalized (n=" + str(sum8_3) + ")")
    st.altair_chart(histo8_3, use_container_width=True)
    
    ### BIRTH WEIGHT

    boks4_3 = create_boxplot_w(source4_3w, color3, "Hospitalized (n=" + str(sum4_3) + ")")
    st.altair_chart(boks4_3, use_container_width=True)
    histo4_3 = create_histo_w(source4_3wh, color3, "Hospitalized (n=" + str(sum4_3) + ")")
    st.altair_chart(histo4_3, use_container_width=True)
    
    boks5_3 = create_boxplot_w(source5_3w, color3, "Hospitalized (n=" + str(sum5_3) + ")")
    st.altair_chart(boks5_3, use_container_width=True)
    histo5_3 = create_histo_w(source5_3wh, color3, "Hospitalized (n=" + str(sum5_3) + ")")
    st.altair_chart(histo5_3, use_container_width=True)
   
    boks6_3 = create_boxplot_w(source6_3w, color3, "Hospitalized (n=" + str(sum6_3) + ")")
    st.altair_chart(boks6_3, use_container_width=True)
    histo6_3 = create_histo_w(source6_3wh, color3, "Hospitalized (n=" + str(sum6_3) + ")")
    st.altair_chart(histo6_3, use_container_width=True)
   
    boks7_3 = create_boxplot_w(source7_3w, color3, "Hospitalized (n=" + str(sum7_3) + ")")
    st.altair_chart(boks7_3, use_container_width=True)
    histo7_3 = create_histo_w(source7_3wh, color3, "Hospitalized (n=" + str(sum7_3) + ")")
    st.altair_chart(histo7_3, use_container_width=True)

    boks8_3 = create_boxplot_w(source8_3w, color3, "Hospitalized (n=" + str(sum8_3) + ")")
    st.altair_chart(boks8_3, use_container_width=True)
    histo8_3 = create_histo_w(source8_3wh, color3, "Hospitalized (n=" + str(sum8_3) + ")")
    st.altair_chart(histo8_3, use_container_width=True)


with col4:

    all = create_barchart_sex(sub_sex_any, color4, "Any (n=" + str(sum_any) + ")") 
    st.altair_chart(all, use_container_width=True)

    bar4_1 = create_barchart_sex(sub_sex_4_1, color1, "No NVP (n=" + str(sum4_1) + ")")
    st.altair_chart(bar4_1, use_container_width=True)
    bar4_2 = create_barchart_sex(sub_sex_4_2, color2, "NVP (n=" + str(sum4_2) + ")")
    st.altair_chart(bar4_2, use_container_width=True)
    bar4_3 = create_barchart_sex(sub_sex_4_3, color3, "Hospitalized (n=" + str(sum4_3) + ")")
    st.altair_chart(bar4_3, use_container_width=True)

    bar5_1 = create_barchart_sex(sub_sex_5_1, color1, "No NVP (n=" + str(sum5_1) + ")")
    st.altair_chart(bar5_1, use_container_width=True)
    bar5_2 = create_barchart_sex(sub_sex_5_2, color2, "NVP (n=" + str(sum5_2) + ")")
    st.altair_chart(bar5_2, use_container_width=True)
    bar5_3 = create_barchart_sex(sub_sex_5_3, color3, "Hospitalized (n=" + str(sum5_3) + ")")
    st.altair_chart(bar5_3, use_container_width=True)

    bar6_1 = create_barchart_sex(sub_sex_6_1, color1, "No NVP (n=" + str(sum6_1) + ")")
    st.altair_chart(bar6_1, use_container_width=True)
    bar6_2 = create_barchart_sex(sub_sex_6_2, color2, "NVP (n=" + str(sum6_2) + ")")
    st.altair_chart(bar6_2, use_container_width=True)
    bar6_3 = create_barchart_sex(sub_sex_6_3, color3, "Hospitalized (n=" + str(sum6_3) + ")")
    st.altair_chart(bar6_3, use_container_width=True)

    bar7_1 = create_barchart_sex(sub_sex_7_1, color1, "No NVP (n=" + str(sum7_1) + ")")
    st.altair_chart(bar7_1, use_container_width=True)
    bar7_2 = create_barchart_sex(sub_sex_7_2, color2, "NVP (n=" + str(sum7_2) + ")")
    st.altair_chart(bar7_2, use_container_width=True)
    bar7_3 = create_barchart_sex(sub_sex_7_3, color3, "Hospitalized (n=" + str(sum7_3) + ")")
    st.altair_chart(bar7_3, use_container_width=True)

    bar8_1 = create_barchart_sex(sub_sex_8_1, color1, "No NVP (n=" + str(sum8_1) + ")")
    st.altair_chart(bar8_1, use_container_width=True)
    bar8_2 = create_barchart_sex(sub_sex_8_2, color2, "NVP (n=" + str(sum8_2) + ")")
    st.altair_chart(bar8_2, use_container_width=True)
    bar8_3 = create_barchart_sex(sub_sex_8_3, color3, "Hospitalized (n=" + str(sum8_3) + ")")
    st.altair_chart(bar8_3, use_container_width=True)
    
    
#######################

# Load data set
data = pd.read_csv('data/data-5-box.csv', encoding='utf-8')

##### Filter data (subdata sets) 
### DD14 = birth length
# No NVP
sub_CC388_len_1 = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC388_len_1.to_csv('data/subdata/CC388_len_1.csv', index=False, encoding='utf-8') 
sub_CC389_len_1 = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC389_len_1.to_csv('data/subdata/CC389_len_1.csv', index=False, encoding='utf-8') 
sub_CC390_len_1 = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC390_len_1.to_csv('data/subdata/CC390_len_1.csv', index=False, encoding='utf-8') 
sub_CC391_len_1 = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC391_len_1.to_csv('data/subdata/CC391_len_1.csv', index=False, encoding='utf-8') 
sub_CC392_len_1 = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC392_len_1.to_csv('data/subdata/CC392_len_1.csv', index=False, encoding='utf-8')
# PNVP
sub_CC388_len_2 = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC388_len_2.to_csv('data/subdata/CC388_len_2.csv', index=False, encoding='utf-8') 
sub_CC389_len_2 = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC389_len_2.to_csv('data/subdata/CC389_len_2.csv', index=False, encoding='utf-8') 
sub_CC390_len_2 = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC390_len_2.to_csv('data/subdata/CC390_len_2.csv', index=False, encoding='utf-8') 
sub_CC391_len_2 = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC391_len_2.to_csv('data/subdata/CC391_len_2.csv', index=False, encoding='utf-8') 
sub_CC392_len_2 = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC392_len_2.to_csv('data/subdata/CC392_len_2.csv', index=False, encoding='utf-8')
# hospitalized due to PNVP 
sub_CC141_len_3 = data.loc[(data.category == 'CC141').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC141_len_3.to_csv('data/subdata/CC141_len_3.csv', index=False, encoding='utf-8') 
sub_CC142_len_3 = data.loc[(data.category == 'CC142').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)] 
sub_CC142_len_3.to_csv('data/subdata/CC142_len_3.csv', index=False, encoding='utf-8') 
sub_CC143_len_3 = data.loc[(data.category == 'CC143').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC143_len_3.to_csv('data/subdata/CC143_len_3.csv', index=False, encoding='utf-8') 
sub_CC144_len_3 = data.loc[(data.category == 'CC144').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC144_len_3.to_csv('data/subdata/CC144_len_3.csv', index=False, encoding='utf-8') 
sub_CC145_len_3 = data.loc[(data.category == 'CC145').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC145_len_3.to_csv('data/subdata/CC145_len_3.csv', index=False, encoding='utf-8')
### DD13 = birth weight
# No NVP
sub_CC388_wei_1 = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC388_wei_1.to_csv('data/subdata/CC388_wei_1.csv', index=False, encoding='utf-8') 
sub_CC389_wei_1 = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC389_wei_1.to_csv('data/subdata/CC389_wei_1.csv', index=False, encoding='utf-8') 
sub_CC390_wei_1 = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC390_wei_1.to_csv('data/subdata/CC390_wei_1.csv', index=False, encoding='utf-8') 
sub_CC391_wei_1 = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC391_wei_1.to_csv('data/subdata/CC391_wei_1.csv', index=False, encoding='utf-8') 
sub_CC392_wei_1 = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
sub_CC392_wei_1.to_csv('data/subdata/CC392_wei_1.csv', index=False, encoding='utf-8') 
# NVP
sub_CC388_wei_2 = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC388_wei_2.to_csv('data/subdata/CC388_wei_2.csv', index=False, encoding='utf-8') 
sub_CC389_wei_2 = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC389_wei_2.to_csv('data/subdata/CC389_wei_2.csv', index=False, encoding='utf-8') 
sub_CC390_wei_2 = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC390_wei_2.to_csv('data/subdata/CC390_wei_2.csv', index=False, encoding='utf-8') 
sub_CC391_wei_2 = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC391_wei_2.to_csv('data/subdata/CC391_wei_2.csv', index=False, encoding='utf-8') 
sub_CC392_wei_2 = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
sub_CC392_wei_2.to_csv('data/subdata/CC392_wei_2.csv', index=False, encoding='utf-8') 
# hospitalized due to PNVP
sub_CC141_wei_3 = data.loc[(data.category == 'CC141').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC141_wei_3.to_csv('data/subdata/CC141_wei_3.csv', index=False, encoding='utf-8') 
sub_CC142_wei_3 = data.loc[(data.category == 'CC142').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC142_wei_3.to_csv('data/subdata/CC142_wei_3.csv', index=False, encoding='utf-8') 
sub_CC143_wei_3 = data.loc[(data.category == 'CC143').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC143_wei_3.to_csv('data/subdata/CC143_wei_3.csv', index=False, encoding='utf-8') 
sub_CC144_wei_3 = data.loc[(data.category == 'CC144').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC144_wei_3.to_csv('data/subdata/CC144_wei_3.csv', index=False, encoding='utf-8') 
sub_CC145_wei_3 = data.loc[(data.category == 'CC145').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
sub_CC145_wei_3.to_csv('data/subdata/CC145_wei_3.csv', index=False, encoding='utf-8') 

data_h = pd.read_csv('data/data-5-histo.csv', encoding='utf-8')
#### Filter data (subdata sets) 
## DD14 = birth length
# No NVP
sub_CC388_len_1h = data_h.loc[(data_h.category == 'CC388').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC388_len_1h.to_csv('data/subdata/CC388_len_1h.csv', index=False, encoding='utf-8') 
sub_CC389_len_1h = data_h.loc[(data_h.category == 'CC389').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC389_len_1h.to_csv('data/subdata/CC389_len_1h.csv', index=False, encoding='utf-8') 
sub_CC390_len_1h = data_h.loc[(data_h.category == 'CC390').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC390_len_1h.to_csv('data/subdata/CC390_len_1h.csv', index=False, encoding='utf-8') 
sub_CC391_len_1h = data_h.loc[(data_h.category == 'CC391').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC391_len_1h.to_csv('data/subdata/CC391_len_1h.csv', index=False, encoding='utf-8') 
sub_CC392_len_1h = data_h.loc[(data_h.category == 'CC392').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC392_len_1h.to_csv('data/subdata/CC392_len_1h.csv', index=False, encoding='utf-8')
# PNVP
sub_CC388_len_2h = data_h.loc[(data_h.category == 'CC388').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC388_len_2h.to_csv('data/subdata/CC388_len_2h.csv', index=False, encoding='utf-8') 
sub_CC389_len_2h = data_h.loc[(data_h.category == 'CC389').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC389_len_2h.to_csv('data/subdata/CC389_len_2h.csv', index=False, encoding='utf-8') 
sub_CC390_len_2h = data_h.loc[(data_h.category == 'CC390').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC390_len_2h.to_csv('data/subdata/CC390_len_2h.csv', index=False, encoding='utf-8') 
sub_CC391_len_2h = data_h.loc[(data_h.category == 'CC391').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC391_len_2h.to_csv('data/subdata/CC391_len_2h.csv', index=False, encoding='utf-8') 
sub_CC392_len_2h = data_h.loc[(data_h.category == 'CC392').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC392_len_2h.to_csv('data/subdata/CC392_len_2h.csv', index=False, encoding='utf-8')
# hospitalized due to PNVP 
sub_CC141_len_3h = data_h.loc[(data_h.category == 'CC141').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC141_len_3h.to_csv('data/subdata/CC141_len_3h.csv', index=False, encoding='utf-8') 
sub_CC142_len_3h = data_h.loc[(data_h.category == 'CC142').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)] 
sub_CC142_len_3h.to_csv('data/subdata/CC142_len_3h.csv', index=False, encoding='utf-8') 
sub_CC143_len_3h = data_h.loc[(data_h.category == 'CC143').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC143_len_3h.to_csv('data/subdata/CC143_len_3h.csv', index=False, encoding='utf-8') 
sub_CC144_len_3h = data_h.loc[(data_h.category == 'CC144').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC144_len_3h.to_csv('data/subdata/CC144_len_3h.csv', index=False, encoding='utf-8') 
sub_CC145_len_3h = data_h.loc[(data_h.category == 'CC145').reset_index(drop=True) & (data_h.outcome == 'DD14').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC145_len_3h.to_csv('data/subdata/CC145_len_3h.csv', index=False, encoding='utf-8')
### DD13 = birth weight
# No NVP
sub_CC388_wei_1h = data_h.loc[(data_h.category == 'CC388').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC388_wei_1h.to_csv('data/subdata/CC388_wei_1h.csv', index=False, encoding='utf-8') 
sub_CC389_wei_1h = data_h.loc[(data_h.category == 'CC389').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC389_wei_1h.to_csv('data/subdata/CC389_wei_1h.csv', index=False, encoding='utf-8') 
sub_CC390_wei_1h = data_h.loc[(data_h.category == 'CC390').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC390_wei_1h.to_csv('data/subdata/CC390_wei_1h.csv', index=False, encoding='utf-8') 
sub_CC391_wei_1h = data_h.loc[(data_h.category == 'CC391').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC391_wei_1h.to_csv('data/subdata/CC391_wei_1h.csv', index=False, encoding='utf-8') 
sub_CC392_wei_1h = data_h.loc[(data_h.category == 'CC392').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '0').reset_index(drop=True)]
sub_CC392_wei_1h.to_csv('data/subdata/CC392_wei_1h.csv', index=False, encoding='utf-8') 
# NVP
sub_CC388_wei_2h = data_h.loc[(data_h.category == 'CC388').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC388_wei_2h.to_csv('data/subdata/CC388_wei_2h.csv', index=False, encoding='utf-8') 
sub_CC389_wei_2h = data_h.loc[(data_h.category == 'CC389').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC389_wei_2h.to_csv('data/subdata/CC389_wei_2h.csv', index=False, encoding='utf-8') 
sub_CC390_wei_2h = data_h.loc[(data_h.category == 'CC390').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC390_wei_2h.to_csv('data/subdata/CC390_wei_2h.csv', index=False, encoding='utf-8') 
sub_CC391_wei_2h = data_h.loc[(data_h.category == 'CC391').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC391_wei_2h.to_csv('data/subdata/CC391_wei_2h.csv', index=False, encoding='utf-8') 
sub_CC392_wei_2h = data_h.loc[(data_h.category == 'CC392').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == '1').reset_index(drop=True)]
sub_CC392_wei_2h.to_csv('data/subdata/CC392_wei_2h.csv', index=False, encoding='utf-8') 
# hospitalized due to PNVP
sub_CC141_wei_3h = data_h.loc[(data_h.category == 'CC141').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC141_wei_3h.to_csv('data/subdata/CC141_wei_3h.csv', index=False, encoding='utf-8') 
sub_CC142_wei_3h = data_h.loc[(data_h.category == 'CC142').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC142_wei_3h.to_csv('data/subdata/CC142_wei_3h.csv', index=False, encoding='utf-8') 
sub_CC143_wei_3h = data_h.loc[(data_h.category == 'CC143').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC143_wei_3h.to_csv('data/subdata/CC143_wei_3h.csv', index=False, encoding='utf-8') 
sub_CC144_wei_3h = data_h.loc[(data_h.category == 'CC144').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC144_wei_3h.to_csv('data/subdata/CC144_wei_3h.csv', index=False, encoding='utf-8') 
sub_CC145_wei_3h = data_h.loc[(data_h.category == 'CC145').reset_index(drop=True) & (data_h.outcome == 'DD13').reset_index(drop=True) & (data_h.level == 1).reset_index(drop=True)]
sub_CC145_wei_3h.to_csv('data/subdata/CC145_wei_3h.csv', index=False, encoding='utf-8') 

