import subprocess
import time
from typing import Optional, List, Mapping, Any
from langchain.llms.base import LLM


class AlpacaLLM(LLM):
    
    model_path: str

        
    @property
    def _llm_type(self) -> str:
        return "alpaca"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        command = f'.\\chat.exe -m "{self.model_path}"'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        print("Starting Alpaca process...")

        # Wait until the model is ready to receive input
        while True:
            output = process.stderr.readline()
            if b"== Running in chat mode. ==" in output:
                time.sleep(7)  # import time
                print("Alpaca process is ready.")
                break

        input_text = f"{prompt}\n"
        process.stdin.write(input_text.encode())
        process.stdin.flush()

        output, errors = process.communicate()

        print("Alpaca process has finished.")
        
        if errors:
            print(f"Errors: {errors.decode()}")

        return output.decode()
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_path": self.model_path}



