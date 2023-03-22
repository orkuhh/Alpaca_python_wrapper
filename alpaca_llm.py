from langchain.llms.base import LLM
import subprocess
from typing import Optional, List, Mapping, Any

class AlpacaLLM(LLM):
    
    model_path: str
        
    @property
    def _llm_type(self) -> str:
        return "alpaca"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        cmd = f".\\chat.exe -m {self.model_path}"
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        output, _ = proc.communicate(input=prompt.encode())
        return output.decode()
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_path": self.model_path}
