import os
import re
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import TokenTextSplitter

os.environ["OPENAI_API_KEY"] = "your-api-key"

llm = OpenAI(temperature=0)

def get_transcript(video_id):
    # retrieve the available transcripts
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    result = [transcript.translate('en').fetch()[0]["text"]
            for transcript in transcript_list]
    # join the transcripts into one string
    script = ''.join(result)

    return script
    
def summarize(input):
    text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=20)
    texts = text_splitter.split_text(input)
    # print(texts)
    docs = [Document(page_content=t) for t in texts[:3]]
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain.run(docs)

def main():
    st.title("Youtube Summarization App")

    url = st.text_input("Enter a URL:", value="")
    go_button = st.button("GO!")

    if go_button:
        if url:
            # Show a loading indicator while waiting to display the text
            with st.spinner('Loading...'):
                url_id = re.search("v=(.*)", url).group(1)
                script = get_transcript(url_id)
                sum_res = summarize(script)
                st.write(sum_res)
        else:
            st.error("Please enter a valid URL.")

if _name_ == "_main_":
    main()
