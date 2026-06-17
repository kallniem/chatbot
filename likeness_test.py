from openai import OpenAI
import numpy as np

EMBEDDING_MODEL = "embeddinggemma-300M-Q8_0.gguf"
SIMILARITY_THRESHOLD = 0.45

KEYWORDS = ["endless", "dull", "manipulative", "beautiful", "pristine"]
SENTENCE = "She will lie, cheat and do anything in her power to deceive you."

client = OpenAI(
    base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
    api_key = "sk-no-key-required"
)




def get_embedding(text: str) -> np.ndarray:
    """
    Get embedding vector for text.
    """
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    return np.array(response.data[0].embedding)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Compute cosine similarity between two vectors.
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))




def find_semantic_matches(sentence, keywords, threshold=0.45):
    sentence_embedding = get_embedding(sentence)

    matches = []

    for keyword in keywords:
        keyword_embedding = get_embedding(keyword)

        similarity = cosine_similarity(
            sentence_embedding,
            keyword_embedding
        )
        print(f"{keyword}: {similarity:.3f}")

        if similarity >= threshold:
            matches.append({
                "keyword": keyword,
                "similarity": round(float(similarity), 3)
            })

    # Sort by best match first
    matches.sort(key=lambda x: x["similarity"], reverse=True)

    return matches




if __name__ == "__main__":
    results = find_semantic_matches(
        SENTENCE,
        KEYWORDS,
        SIMILARITY_THRESHOLD
    )

    print(f"\nSentence:\n{SENTENCE}\n")

    if results:
        print("Semantic matches found:\n")

        for result in results:
            print(
                f"- {result['keyword']} "
                f"(similarity: {result['similarity']})"
            )
    else:
        print("No semantic matches found.")