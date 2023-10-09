import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
 
#####################
# Header 
st.markdown('''
# Swetha  Bsc(cs)
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=160)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- As a recent graduate with a strong foundation in data science principles and a passion for problem-solving, I am excited to embark on a career in data science. 
- My education and practical experiences have equipped me with valuable skills and knowledge that make me a promising candidate in the field.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Internship-experience">Internship Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a):
    col1, col2 = st.columns([4, 1])
    with col1:
      st.markdown(a)

#####################
st.markdown('''
## Education
''')

txt('**Bachelors of Science** (Computer Science ), *University of  XYZ College*, Chennai',
'2019-2023')
st.markdown('''
- GPA: `80`
- Mention your major or concentration if applicable (e.g., "Major in Artificial Intelligence").
- Thesis awarded `1st` Prize by the National Research Council of XYZ.
''')

#####################
st.markdown('''
## Internship Experience
''')

txt('**Tech Private Limited**,Faculty of Datascience Technology',
'Jun 2021-Aug 2021')

st.markdown('''
- Conducted data analysis and data cleaning on real-world datasets using Python and Pandas.
- Built predictive models for [mention specific tasks or projects].
- Presented findings and insights to team members and management.
- Gained proficiency in [mention specific tools or techniques relevant to your internship].
''')

#####################
st.markdown('''
## Projects
''')

st.markdown('''
#### Natural Language Processing for Sentiment Analysis
''')

txt4('- Conducted sentiment analysis on customer reviews using Python NLTK TextBlob')
txt4('- Created a sentiment classification model achieving an accuracy of 86%.')
txt4('- Provided actionable insights to the marketing team, resulting in a 15% increase in customer satisfaction.')
txt4('- Tools and Skills: Python, NLTK, TextBlob, data preprocessing, text analysis.')


#####################
st.markdown('''
## Core Competencies
''')
txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/XYZ')
txt2('Twitter', 'https://twitter.com/XYZ')
txt2('GitHub', 'https://github.com/XYZ/')

