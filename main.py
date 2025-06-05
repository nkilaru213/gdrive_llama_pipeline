from gdrive_auth import authenticate_gdrive
from text_extraction import download_and_extract_text
from embedding_store import create_index, get_top_k_matches
from llama_api import call_llama_api

def main():
    drive_service = authenticate_gdrive()

    results = drive_service.files().list(pageSize=10, fields="files(id, name)").execute()
    texts = []
    for file in results.get('files', []):
        print(f"Downloading: {file['name']}")
        text = download_and_extract_text(file['id'], drive_service)
        texts.append(text)

    model, index, text_map = create_index(texts)

    question = input("Enter your question: ")
    context_snippets = get_top_k_matches(question, model, index, text_map)
    prompt = f"""Context:\n{'\n---\n'.join(context_snippets)}\n\nQuestion: {question}\nAnswer:"""

    answer = call_llama_api(prompt, api_key="LL-your-key")
    print("Answer:", answer)

if __name__ == "__main__":
    main()