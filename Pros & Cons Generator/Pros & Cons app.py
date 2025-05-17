import openai
from langgraph.graph import StateGraph
from typing import TypedDict
from openai import OpenAI

# Set your OpenAI API key here or via environment variable
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual key

# Define the state
class ProsConsState(TypedDict):
    decision: str
    result: str

# Node function to call GPT-3.5
def generate_pros_cons(state: ProsConsState) -> ProsConsState:
    decision = state["decision"]

    prompt = f"""
    Help me decide the following:
    Decision: {decision}

    Please provide a concise table of pros and cons for this decision.
    Format the response as:
    Pros:
    - ...
    - ...
    
    Cons:
    - ...
    - ...
    """

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    response = completion.choices[0].message.content
    return {"decision": decision, "result": response}

# Build the LangGraph
def create_graph():
    builder = StateGraph(ProsConsState)
    builder.add_node("generate", generate_pros_cons)
    builder.set_entry_point("generate")
    builder.set_finish_point("generate")
    return builder.compile()

# Main function
def main():
    graph = create_graph()
    user_decision = input("Enter your decision (e.g., Should I buy an electric car?):\n> ")

    if not user_decision.strip():
        print("Please enter a valid decision.")
        return

    # Run the graph
    result_state = graph.invoke({"decision": user_decision})
    print("\n=== Pros & Cons Analysis ===")
    print(f"Your Decision: {result_state['decision']}")
    print("----------------------------")
    print(result_state["result"])

if __name__ == "__main__":
    main()