import pandas as pd
import streamlit as st
import extra_streamlit_components as stx
import streamlit.components.v1 as components
from streamlit.components.v1 import html

import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import html_result
import task1_result
@st.cache_resource(experimental_allow_widgets=True)
def display_result_task1():
    chosen_id = stx.tab_bar(data=[
    stx.TabBarItemData(id="tab1", title=" Section 1", description="Interactive graph"),
    stx.TabBarItemData(id="tab2", title="Section 2", description="Evaluation result")])
    placeholder = st.sidebar.container() 

    if chosen_id == "tab1":
        placeholder.markdown(f"## Welcome to the first section")
        placeholder.info(f"Choose the algorithm you want to see the result in the selection box below")
        option = placeholder.selectbox(f'## Select Graph',('Girvan-Newman algorithm','Louvain algorithm', 'Leiden algorithm','Fuzzy node clustering algorithm'))

        if option == 'Girvan-Newman algorithm':
            st.write("---")
            st.header("**Girvan-Newman algorithm graph**")
            HtmlFile = open("html_result\girvan_communities.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            components.html(source_code, height = 6000,width=1000)
            st.write("---")

        if option == 'Louvain algorithm':
            st.write("---")
            st.header("**Louvain algorithm graph**")
            HtmlFile = open("html_result\louvain_communities.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            components.html(source_code, height = 6000,width=1000)
            st.write("---")

        if option == 'Leiden algorithm':
            st.write("---")
            st.header("**Leiden algorithm graph**")
            HtmlFile = open("html_result\leiden_communities.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            components.html(source_code, height = 6000,width=1000)
            st.write("---")

        if option == 'Fuzzy node clustering algorithm':
            st.write("---")
            st.header("**Fuzzy node clustering algorithm graph**")
            HtmlFile = open("html_result\Fuzzy_communities.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            components.html(source_code, height = 6000,width=1000)
            st.write("---")
    if chosen_id == "tab2":
               
            # Define the NeoDash dashboard URL
               
               st.header("Welcome to second section")
               with st.expander("**Evaluation metrics explanation**"):
                 st.write(
                    ":blue[Triad Participation Ratio:] Fraction of community nodes that belong to a triad. \n"
                    "\n :blue[Flake-ODF]: Fraction of nodes in S that have fewer edges pointing inside than to the outside of the community \n"
                    "\n :blue[Average Transitivity:] Tells how well connected the neighborhood of the node is. If the neighborhood is fully connected, the clustering coefficient is 1 and a value close to 0 means that there are hardly any connections in the neighborhood \n"
                    "\n :blue[Fraction Over Median Degree:] Fraction of community nodes of having internal degree higher than the median degree value \n"
                    "\n :blue[Internal Edge Density:] measure the fraction of the edges (out of all possible edges) that appear between the nodes in S \n"
                    "\n :blue[Conductance:] measure the fraction of total edge volume that points outside the cluster"
                        )
          
               option_task2 = st.selectbox(f'**Select evaluation metric**',('Triad Participation Ratio','Flake-ODF', 'Average Transitivity','Fraction Over Median Degree','Internal Edge Density','Conductance'))
               if option_task2 == "Triad Participation Ratio":
                    triad_result = pd.read_csv("task1_data\Triad.csv")
                    st.header("Triad Participation Ratio result")
                    st.write(triad_result)
               if option_task2 == "Flake-ODF":
                    flake_odf_result = pd.read_csv("task1_data\Flake.csv")
                    st.header("Flake-ODF result")
                    st.write(flake_odf_result)
               if option_task2 == "Average Transitivity":
                    avg_trans_result = pd.read_csv("task1_data\Avg_trans.csv")
                    st.header("Average Transitivity result")
                    st.write(avg_trans_result)
               if option_task2 == "Fraction Over Median Degree":
                    frac_median_result = pd.read_csv("task1_data\Frac_median.csv")
                    st.header("Fraction Over Median Degree result")
                    st.write(frac_median_result)                                                      
               if option_task2 == "Internal Edge Density":
                    internal_edge_result = pd.read_csv("task1_data\Internal_edge.csv")
                    st.header("Internal Edge Density result")
                    st.write(internal_edge_result)    
               if option_task2 == "Conductance":
                    conductance_result = pd.read_csv("task1_data\conductance.csv")
                    st.header("Conductance result")
                    st.write(conductance_result)
               


