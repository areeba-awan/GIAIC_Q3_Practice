
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
_: bool = load_dotenv()

GEMINI_API_KEY = os.environ.get("GOOGLE_API_KEY")

external_client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)
external_model= OpenAIChatCompletionsModel(
    model = "gemini-2.5-flash",
    openai_client = external_client
)
config = RunConfig(
    model = external_model,
    model_provider = external_client,
    tracing_disabled = True
)

Testing_Agent = Agent(
    name = "My Assistant",
    instructions = "You are a Helpful Assitant!"
)
result = Runner.run_sync(Testing_Agent, input = "Give me 2 names of famous English novel based on Success", run_config = config)

print("\nCalling My Agent ✨", result.final_output)