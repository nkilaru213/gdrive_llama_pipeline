from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_index(texts):
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    text_map = {i: texts[i] for i in range(len(texts))}
    return model, index, text_map

def get_top_k_matches(question, model, index, text_map, k=3):
    q_embedding = model.encode([question])
    D, I = index.search(np.array(q_embedding), k)
    return [text_map[i] for i in I[0]]