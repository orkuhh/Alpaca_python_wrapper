import os
from CustomLLM import AlpacaLLM

model_path = os.path.join(".", "ggml-alpaca-7b-native-q4.bin")
llm = AlpacaLLM(model_path=model_path)

output = llm("Hello, how are you?")
print(output)
