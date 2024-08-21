from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="meta/llama3-70b-instruct",
  messages=[{"role":"user","content":"hello"}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

