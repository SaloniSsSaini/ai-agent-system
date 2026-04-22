# 🧠 AI Cognitive Agent System

An intelligent, agent-based backend system that simulates autonomous decision-making using AI + fallback workflows.

---

## 🚀 Overview

This project is designed to mimic **modern AI agent systems** rather than traditional APIs.

Instead of blindly calling AI, the system:
- Makes decisions 🧠
- Handles failures ⚡
- Switches to fallback 🔁
- Ensures reliability ✅

---

## ❗ Problem Statement

Most AI applications fail silently when:
- API times out
- AI returns null
- Rate limits hit

This leads to poor user experience and unreliable systems.

---

## 🎯 Solution

A **Cognitive Agent Backend** that:
- Decides whether to call AI or not  
- Validates responses  
- Automatically triggers fallback  
- Ensures system resilience  

---

## 🧠 Architecture


User Input
↓
Agent Decision Layer 🧠
↓
AI Service Call 🤖
↓
Response Validation
↓
Fallback (if needed) 🔁
↓
Final Response ✅


---

## ⚙️ Tech Stack

- **Backend:** FastAPI (Python)
- **AI Layer:** Simulated AI / LLM-ready
- **Fallback System:** Rule-based response
- **Validation:** Error + timeout handling

---

## 🔑 Key Features

### 🧠 Intelligent Decision Engine
Chooses best execution path instead of blindly calling AI.

### ⚡ Failure Handling
Automatically detects and handles:
- Timeouts
- Null responses

### 🔁 Fallback Mechanism
Switches to backup logic when AI fails.

### 🧩 Modular Design
Each component acts like an independent agent.

---

## 🏗️ Project Structure


ai-agent-system/
│
├── app/
│ ├── main.py
│ ├── agent.py
│ ├── services/
│ │ ├── ai_service.py
│ │ ├── fallback_service.py
│ │
│ ├── models/
│ ├── request_model.py
│
├── requirements.txt
├── README.md


---

## ▶️ Getting Started

### 1. Clone Repo

```bash
git clone https://github.com/SaloniSsSaini/ai-agent-system.git
cd ai-agent-system
2. Install Dependencies
pip install -r requirements.txt
3. Run Server
uvicorn app.main:app --reload
4. Open API Docs

👉 http://127.0.0.1:8000/docs

🧪 Example API Request
POST /ask
{
  "query": "Hello AI"
}
🔄 Example Behavior
✅ Case 1: AI Success
AI Response: Hello AI
❌ Case 2: AI Failure
AI failed → fallback triggered
Fallback response for: Hello AI
🌟 Why This Project Matters

This project demonstrates:

Agent-based system design
Fault-tolerant architecture
Real-world AI reliability handling

It goes beyond simple API usage and focuses on:

Building systems that think, adapt, and recover

🚀 Future Improvements
Real OpenAI / LLM integration
Memory-based responses
Multi-agent workflows
Redis caching
Async task queues
👩‍💻 Author

Saloni Saini
