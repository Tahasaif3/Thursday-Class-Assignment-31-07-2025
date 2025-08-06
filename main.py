import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dynamic_instructions import dynamic_instructions
from math_tool import plus_tool , subtract_tool , multiplication_tool , division_tool
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=provider
)

agents = Agent(
    name = "Role Based Agent",
    instructions=dynamic_instructions,
    model=model,
    tools=[plus_tool, subtract_tool , multiplication_tool , division_tool]
)

# Run Agent as Student
# result = Runner.run_sync(
#      starting_agent= agents,
#      input="What is web development?",
#      context={"name": "Ali", "role": "student"}
#     )
# print("As Student:", result.final_output)

# Run Agent as Teacher
# result2 = Runner.run_sync(
#     starting_agent= agents,
#     input="What is web development?",
#     context={"name": "Sir Taha", "role": "teacher"}
#     )
# print("As Teacher:", result2.final_output)

async def main():
    result = Runner.run_streamed(
     starting_agent= agents,
     input="What is web development?",
     context={"name": "Ali", "role": "teacher"}
    )
    print("As Student:", result.final_output)

    async for event in result.stream_events():
         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
             print(event.data.delta, end="", flush=True) 

asyncio.run(main())
