

---

# Pros & Cons Decision Assistant with LangGraph and OpenAI

This project is a simple command-line assistant that helps you evaluate decisions by generating a table of pros and cons using OpenAI's GPT-3.5 and LangGraph.

## Features

- Accepts any decision input from the user.
- Uses GPT-3.5 Turbo to generate a concise pros & cons table.
- Built using the [LangGraph](https://github.com/langchain-ai/langgraph) framework.
- Clean, interactive command-line interface.


## Technologies Used

Python

LangGraph

OpenAI Python SDK

## Example

```bash
$ python main.py
Enter your decision (e.g., Should I buy an electric car?):
> Should I move to a new city?

=== Pros & Cons Analysis ===
Your Decision: Should I move to a new city?
----------------------------
Pros:
- New opportunities for career and personal growth.
- Chance to explore a different lifestyle and culture.

Cons:
- Potential cost and stress of relocation.
- Leaving behind familiar people and places.

Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/pros-cons-assistant.git
cd pros-cons-assistant

2. Install Dependencies

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required packages:

pip install openai langgraph

3. Set Your OpenAI API Key

You can set your OpenAI API key in the script or via environment variable.

Option 1: Set directly in the script Edit main.py:

openai.api_key = "your-openai-api-key"

Option 2: Set as an environment variable

export OPENAI_API_KEY=your-openai-api-key  # Linux/macOS
set OPENAI_API_KEY=your-openai-api-key     # Windows

And modify the code to use:

import os
openai.api_key = os.getenv("OPENAI_API_KEY")

4. Run the Assistant

python main.py



---
.

