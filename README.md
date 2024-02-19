# youtube-transcript-summarizer-openai

### YouTube Summarizer is a convenient Streamlit application designed to streamline the process of summarizing YouTube videos. Leveraging the power of OpenAI's Language Model, this tool generates transcripts from YouTube videos and condenses them into key points, providing users with a concise overview of the content.

### Features:

#### Summarized Transcripts: Enter a YouTube video URL and receive a summarized transcript, saving time and effort in digesting lengthy videos.

#### YouTube Transcript API Integration: Utilizes the YouTube Transcript API to seamlessly generate accurate video transcripts, ensuring reliable summarization.

#### OpenAI Language Model: Harnesses the advanced capabilities of OpenAI's Language Model to produce insightful summaries, highlighting the essential information within the video content.

### Installation:

Clone this repository:
```
git clone [[https://github.com/G12c4/ai-youtube-summarizer.git]
```

Navigate to the repository folder and install the required packages:
```
cd youtube-transcript-summarizer-openai
pip install -r requirements.txt
```

Replace your-api-key with your actual OpenAI API key in the following line of code:
```
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

Run the Streamlit app:
```
streamlit run app.py
```

Open the app in your browser at http://localhost:8501

### Usage:

### Input Video URL: Enter the YouTube video URL of interest into the designated text input field within the application.

#### Generate Summary: Click the "GO!" button to initiate the summarization process. The application will then generate a summarized transcript based on the provided video URL.

#### Review Summary: Evaluate the summarized transcript displayed on the screen, conveniently presenting the key points and essential information extracted from the video content.

#### YouTube Summarizer simplifies the task of extracting valuable insights from YouTube videos, empowering users to efficiently consume content and stay informed.
