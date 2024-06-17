import streamlit as st
import json
from PyPDF2 import PdfFileReader
from io import StringIO
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
from langchain_huggingface import HuggingFaceEndpoint
import os

# HuggingFace model details
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"


llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.5,
    huggingfacehub_api_token="Your Hugging Face Access Token ",
)


# Function to read PDF file
def read_pdf(file):
    pdf = PdfFileReader(file)
    text = ""
    for page_num in range(pdf.getNumPages()):
        page = pdf.getPage(page_num)
        text += page.extractText()
    return text

# Streamlit app
st.title('MCQ Quiz Generator')

with st.form(key='my_form'):
    uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=["pdf", "txt"])
    number = st.number_input('Number of Questions', min_value=1, value=5)
    subject = st.text_input('Subject', value='biology')
    tone = st.text_input('Tone', value='hard')
    submit_button = st.form_submit_button(label='Generate Quiz')

if submit_button:
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            TEXT = read_pdf(uploaded_file)
        elif uploaded_file.type == "text/plain":
            TEXT = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
        
        RESPONSE_JSON = {
            "1": {"mcq": "multiple choice question", "options": {"a": "choice here", "b": "choice here", "c": "choice here", "d": "choice here"}, "correct": "correct answer"},
            "2": {"mcq": "multiple choice question", "options": {"a": "choice here", "b": "choice here", "c": "choice here", "d": "choice here"}, "correct": "correct answer"},
            "3": {"mcq": "multiple choice question", "options": {"a": "choice here", "b": "choice here", "c": "choice here", "d": "choice here"}, "correct": "correct answer"},
        }
        
        TEMPLATE = """
        Text:{text}
        You are an expert MCQ maker. Given the above text, it is your job to \
        create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
        Make sure the questions are not repeated and check all the questions to be conforming the text as well.
        Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
        Ensure to make {number} MCQs
        ### RESPONSE_JSON
        {response_json}
        """
        
        quiz_generation_prompt = PromptTemplate(
            input_variables=["text", "number", "subject", "tone", "response_json"],
            template=TEMPLATE
        )
        
        quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)
        
        TEMPLATE2 = """
        You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
        You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
        if the quiz is not at per with the cognitive and analytical abilities of the students,\
        update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
        Quiz_MCQs:
        {quiz}

        Check from an expert English Writer of the above quiz:
        """
        
        quiz_evaluation_prompt = PromptTemplate(
            input_variables=["subject", "quiz"], 
            template=TEMPLATE2
        )
        
        review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)
        
        generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                                  output_variables=["quiz", "review"], verbose=True,)
        
        with get_openai_callback() as cb:
            response = generate_evaluate_chain(
                {
                    "text": TEXT,
                    "number": number,
                    "subject": subject,
                    "tone": tone,
                    "response_json": json.dumps(RESPONSE_JSON)
                }
            )
        
        quiz = response.get("quiz")
        
        json_str = quiz.replace('### RESPONSE_JSON\n', '')
        json_quiz_response = json.loads(json_str)
        
        st.subheader('Generated Quiz')
        st.json(json_quiz_response)
        
        review = response.get("review")
        st.subheader('Quiz Review')
        st.write(review)
