from flask import Flask, render_template, request, jsonify
from langchain_community.llms import Ollama

app = Flask(__name__)

# Local Ollama model
llm = Ollama(model="granite3-dense:2b")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"]

    prompt = f"""
    Give short definition:
    Question: {question}
    """

    answer = llm.invoke(prompt)

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
