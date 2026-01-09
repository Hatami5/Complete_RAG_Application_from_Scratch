<h1 align="center">🤖 Enterprise GenAI Knowledge Assistant</h1>

<p align="center">
  <b>Ask questions. Get grounded answers. Powered by Generative AI.</b><br>
  Built and maintained by <a href="https://github.com/Hatami5">Hassan Hatami</a> • AI/ML Engineer @ SageMind Tech Services
</p>

---

<h2>📌 Overview</h2>

<p>
<b>Enterprise GenAI Knowledge Assistant</b> is an AI-powered interactive web application that allows users to upload documents and ask natural language questions.  
The system uses <b>Retrieval-Augmented Generation (RAG)</b> to ensure responses are accurate, grounded, and based strictly on the provided content.
</p>

<blockquote>
Designed for enterprises, researchers, and AI practitioners who need reliable, explainable, and production-ready GenAI solutions.
</blockquote>

---

<h2>🚀 Key Features</h2>

<ul>
  <li>📄 <b>Document Ingestion</b> — Upload and process text-based documents.</li>
  <li>🔍 <b>Semantic Search (RAG)</b> — Retrieves relevant context using vector embeddings.</li>
  <li>💬 <b>Natural Language Q&A</b> — Ask questions in plain English.</li>
  <li>🧠 <b>LLM-Powered Answers</b> — Uses Large Language Models for intelligent responses.</li>
  <li>🛡️ <b>Hallucination Reduction</b> — Agent-based validation ensures grounded answers.</li>
  <li>🌐 <b>Interactive Web UI</b> — Built with Streamlit for fast and clean user interaction.</li>
  <li>⚡ <b>Local Vector Store</b> — FAISS enables fast semantic retrieval.</li>
</ul>

---

<h2>🧰 Tech Stack</h2>

<table>
  <tr>
    <th>Tool / Framework</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><b>Python 3.9+</b></td>
    <td>Core programming language</td>
  </tr>
  <tr>
    <td><b>Streamlit</b></td>
    <td>Interactive web application UI</td>
  </tr>
  <tr>
    <td><b>OpenAI / OpenRouter</b></td>
    <td>LLM-based text generation</td>
  </tr>
  <tr>
    <td><b>SentenceTransformers</b></td>
    <td>Text embeddings generation</td>
  </tr>
  <tr>
    <td><b>FAISS</b></td>
    <td>Vector similarity search</td>
  </tr>
  <tr>
    <td><b>dotenv</b></td>
    <td>Secure environment variable management</td>
  </tr>
</table>

---

<h2>⚙️ Setup Instructions</h2>

<h3>1️⃣ Clone the Repository</h3>

```bash
git clone https://github.com/Hatami5/enterprise-genai-assistant.git
cd enterprise-genai-assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt





