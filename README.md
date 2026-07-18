
# LinkedIn Post Generator using LLM

## Overview

LinkedIn Post Generator is an AI-powered web application that generates professional LinkedIn posts from user input using Large Language Models (LLMs).

The application leverages LangChain for prompt orchestration, Groq API for inference, and Streamlit to deliver an interactive user interface. A few-shot prompting strategy is used to maintain consistent formatting and writing style.

---

## Features

- AI-generated LinkedIn posts
- Few-shot prompting
- Customizable post length
- Topic selection
- Language selection
- Interactive Streamlit interface
- Fast inference using Groq API

---

## Technology Stack

### Frontend

- Streamlit

### Backend

- Python

### AI Framework

- LangChain

### Language Model

- LLaMA 3

### API

- Groq API

---

## Workflow

User Input

↓

Prompt Template

↓

Few-Shot Examples

↓

LangChain

↓

Groq API

↓

LLaMA Model

↓

Generated LinkedIn Post

---

## Project Structure

```
LinkedIn-Post-Generator
│
├── app.py
├── main.py
├── chains.py
├── few_shot.py
├── post_generator.py
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/linkedin-post-generator.git
```

Navigate to the project

```bash
cd linkedin-post-generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## How It Works

1. User selects the topic.
2. User specifies the preferred language.
3. User chooses the post length.
4. LangChain constructs the prompt.
5. Few-shot examples guide the model.
6. Groq API generates the response.
7. The generated LinkedIn post is displayed.

---

## Example Use Cases

- Personal branding
- Technical content creation
- Career updates
- Project showcases
- Thought leadership
- Industry insights

---

## Future Enhancements

- Tone customization
- AI-generated hashtags
- Image suggestions
- Content scheduling
- Multi-platform support
- Export to PDF
- Save post history

---

## Live Demo

https://linkedin-post-genrator-fxeetpdvpfmkhisisdgtkj.streamlit.app/

---

## License

This project is developed for educational and portfolio purposes.

---

## License

This project is developed for educational and portfolio purposes.
