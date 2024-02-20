from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Create a two-column CSV of top science fiction movies along with the year of release."
    }
  ],
  temperature=0.5,
  max_tokens=64,
  top_p=1
)