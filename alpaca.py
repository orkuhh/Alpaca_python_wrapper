from CustomLLM_test import ChatLLM
import time

llm = ChatLLM(model_path="ggml-alpaca-7b-native-q4.bin")
time.sleep(10)
response = llm("Hello, how are you?")
print(response)
