from alpaca_llm import AlpacaLLM

llm = AlpacaLLM(model_path="./ggml-alpaca-7b-native-q4.bin")

output = llm("Hello, how are you?")
print(output)

