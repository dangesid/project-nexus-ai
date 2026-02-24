from dotenv import load_dotenv
import os 
import requests

load_dotenv()

class LLMClient:
    """
    Central LLM wrapper for all agents 
    Agents will call this class to interact with the LLMs 
    """

    def __init__(self, model="mistralai/Mistral-7B-Instruct-v0.2"):
        self.model = model
        self.api_url = f"https://api-inference.huggingface.co/models/{model}"
        self.headers={
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
        }

    def run(self,prompt: str) -> str:
        """
        Run a prompt on Huggingface inference API and returned generated text.
        """

        payload = {
            "inputs": f"<s>[INST]{prompt} [/INST]",
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.7,
                "return_full_text": False
            }
        }

        response = requests.post(self.api_url, headers=self.headers, json=payload)

        # ---- Error Handling ----
        if response.status_code != 200:
            return f"LLM Error: {response.text}"
        
        output = response.json()

        # ----- HF Output parsing -------
        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"]
        
        #fallback
        return str(output)