from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import subprocess

class ChatLLM(LLM):
    
    model_path: str
    
    @property
    def _llm_type(self) -> str:
        return "chat_exe"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        process = subprocess.Popen(["./chat.exe", "-m", self.model_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding="utf-8")
        stdout, _ = process.communicate(input=prompt)
        return stdout
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_path": self.model_path}
