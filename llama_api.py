import requests

def call_llama_api(prompt, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(
        "https://api.meta.com/llama/completions",  # Replace with actual endpoint
        headers=headers,
        json={"prompt": prompt, "max_tokens": 200}
    )
    return response.json().get("text")