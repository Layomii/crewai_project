import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from summarize_tool import summarize  # Assuming summarize_tool.py is in the same directory

load_dotenv()

os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
os.environ["ANTHROPIC_MODEL_NAME"] = os.getenv("ANTHROPIC_MODEL_NAME")

print('##Welcome to your History Task!##')
history_input = input("Please enter your history task: ")

history_agent = Agent(
    role="History Agent",
    goal="To search for any history-related tasks",
    backstory="You are a history expert with extensive knowledge of historical events, figures, and contexts.",
    tools=["summarize"]
)

task1 = Task(
    description=f'{history_input}',
    expected_output="Provide a detailed itemized summary of the historical event or figure.",
    agent=history_agent,
)

crew = Crew(
    agent=history_agent,
    tasks=[task1],
    Process=Process.sequential,  # Sequential processing of tasks
)

result = crew.run()
print("##Task Completed!##")