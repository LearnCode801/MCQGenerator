# AI-Powered Multiple Choice Question (MCQ) Generator

**[🎥 Demo Video](https://drive.google.com/file/d/1arv9te6pJimE-x0ugjEt8ddtDfl76fA1/view?usp=sharing)**

## 🚀 Overview

This project is an intelligent MCQ generator that uses Mistral AI's language model to automatically create multiple choice questions from any given text. The system features a dual-chain approach with question generation and quality evaluation, making it perfect for educators, content creators, and assessment designers.

## ✨ Key Features

- **Automated MCQ Generation**: Creates high-quality multiple choice questions from any input text
- **Dual-Chain Processing**: Two-stage process with generation and evaluation chains
- **Customizable Parameters**: Adjustable difficulty levels, subject areas, and question count
- **Quality Assessment**: Built-in evaluation system to ensure question quality and appropriateness
- **JSON Output Format**: Structured, easily parseable output format
- **Real-time Processing**: Interactive generation with immediate results

## 🛠️ Technical Stack

- **Language Model**: Mistral-7B-Instruct-v0.3 via Hugging Face
- **Framework**: LangChain for chain management
- **Libraries**: 
  - `langchain`
  - `langchain_huggingface`
  - `transformers`
  - `json`

## 📋 Prerequisites

Before running the project, ensure you have:

- Python 3.7+
- Hugging Face API token
- Required Python packages (see installation section)

## 🔧 Installation

```bash
# Install required packages
pip install langchain
pip install langchain_huggingface
pip install transformers
```

## ⚙️ Configuration

1. **Set up Hugging Face Token**:
   ```python
   huggingfacehub_api_token = "your_hugging_face_token_here"
   ```

2. **Configure Model Parameters**:
   ```python
   repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
   temperature = 0.5  # Adjust for creativity vs consistency
   ```

## 🎯 Usage

### Basic Usage

```python
# Define your input parameters
TEXT = "Your educational content here..."
NUMBER = 5  # Number of questions to generate
SUBJECT = "biology"  # Subject area
TONE = "hard"  # Difficulty level: easy, medium, hard

# Generate MCQs
response = generate_evaluate_chain({
    "text": TEXT,
    "number": NUMBER,
    "subject": SUBJECT,
    "tone": TONE,
    "response_json": json.dumps(RESPONSE_JSON)
})
```

### Customization Options

- **Subject Areas**: Any academic subject (biology, chemistry, history, etc.)
- **Difficulty Levels**: Easy, Medium, Hard
- **Question Count**: 1-20 questions per generation
- **Content Types**: Text passages, articles, educational material

## 🔄 System Architecture

The system operates through a **Sequential Chain** with two main components:

### 1. Quiz Generation Chain
- **Input**: Text content, parameters (number, subject, tone)
- **Process**: Analyzes text and generates MCQs
- **Output**: Structured JSON with questions, options, and correct answers

### 2. Quality Evaluation Chain
- **Input**: Generated quiz questions
- **Process**: Evaluates complexity, grammar, and appropriateness
- **Output**: Quality assessment and improvement suggestions

## 📊 Output Format

```json
{
  "1": {
    "mcq": "What is the scientific study of life?",
    "options": {
      "a": "Physics",
      "b": "Chemistry", 
      "c": "Biology",
      "d": "Mathematics"
    },
    "correct": "c"
  },
  "2": {
    "mcq": "What major theme explains unity and diversity of life?",
    "options": {
      "a": "Evolution",
      "b": "Cell division",
      "c": "Photosynthesis", 
      "d": "DNA replication"
    },
    "correct": "a"
  }
}
```

## 🎓 Example Implementation

The project includes a complete biology example that demonstrates:

1. **Text Analysis**: Processing a biology passage about life sciences
2. **Question Generation**: Creating 5 hard-level biology questions
3. **Quality Evaluation**: Assessing question complexity and suggesting improvements
4. **Result Processing**: Parsing JSON output and displaying questions

## 🔍 Quality Assurance Features

- **Content Relevance**: Ensures questions directly relate to input text
- **Difficulty Calibration**: Matches question complexity to specified tone
- **Grammar Checking**: Validates language quality and clarity
- **Uniqueness Verification**: Prevents duplicate questions
- **Educational Alignment**: Ensures questions match cognitive abilities

## 📈 Performance Insights

The system provides detailed chain execution logs showing:
- Prompt formatting and processing
- Token usage and model interactions
- Chain execution flow
- Quality evaluation results

## 🎯 Use Cases

- **Educational Assessment**: Create quizzes for students
- **Content Validation**: Test comprehension of educational material  
- **Training Programs**: Generate questions for corporate training
- **Study Materials**: Create practice tests from textbooks
- **Online Courses**: Automated quiz generation for e-learning platforms

## 🔧 Advanced Configuration

### Custom Prompt Templates
```python
TEMPLATE = """
Text: {text}
Create {number} {tone} difficulty questions for {subject} students.
Format: {response_json}
"""
```

### Chain Customization
```python
# Modify generation parameters
quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt)
review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt)
```

## 🚦 Getting Started

1. **Clone the repository**
2. **Install dependencies**
3. **Set up Hugging Face credentials**
4. **Run the example notebook**
5. **Customize for your content and requirements**

## 📝 Notes

- Ensure proper Hugging Face API authentication
- Model responses may vary based on temperature settings
- Quality evaluation provides suggestions for improvement
- JSON parsing handles the structured output format
- Token usage is tracked for cost management

## 🤝 Contributing

Feel free to contribute by:
- Adding new subject templates
- Improving evaluation criteria
- Enhancing output formatting
- Adding new language models

---

**Ready to transform your educational content into engaging assessments? Start generating intelligent MCQs today!** 🚀
