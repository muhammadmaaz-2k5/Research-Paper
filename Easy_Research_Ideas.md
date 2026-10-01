# 🚀 Easy, Implementable Research Proposal Ideas (USTC)
### Tailored to the 2024–2026 Publications of Prof. Nikolaos M. Freris & Prof. Junxue Zhang
**Candidate**: Muhammad Maaz (Full-Stack Engineer, UET Peshawar Graduate)

---

## 🎯 Strategic Objective
These two proposals are specifically designed to be:
1. **Grounded in their exact 2024–2026 papers**: Instantly demonstrates that you follow their latest work.
2. **Easy to understand and explain**: No esoteric pure math; intuitive systems engineering logic.
3. **Easy for YOU to implement on your laptop**: Built with Python, PyTorch, Docker, Redis, and WebSockets—technologies you already use daily.
4. **Strong defense for a 2.5 CGPA**: Shows practical engineering competence that theoretical students lack.

---

# Proposal 1: For Prof. Nikolaos M. Freris (USTC)

### 📚 Direct Paper Reference:
- *Huang & Freris*, **"Reinforcement-learning-based layer-wise aggregation for personalized federated learning"**, *IEEE Internet of Things Journal*, 12(7), 8614-8625, **2024**.
- *Yi & Freris*, **"Communication efficient quasi-Newton distributed optimization"**, *arXiv:2409.04049*, **2024**.

---

### 📌 Title:
```text
Communication-Efficient Federated Learning with Selective Layer Caching for Resource-Constrained Edge Networks
```

### 💡 The 30-Second Intuition:
In Federated Learning, IoT edge devices (cameras, phones) train local models and send all model weights back to a server. Sending full weights over wireless networks burns battery and causes latency spikes. Building directly upon Prof. Freris's 2024 IEEE IoT-J paper on **layer-wise aggregation**, your idea is: **Edge devices only send layers whose weights have changed significantly ($\Delta W > \theta$), while the central server caches the rest in Redis.**

### 🛠️ Why It Is Easy for You to Implement:
- **Core Technology**: Python + PyTorch + WebSockets (or gRPC) + Docker.
- **Your Advantage**: You built *PakChess* using real-time WebSockets. Client-server Federated Learning is essentially WebSocket message passing between client scripts and a server script!

### 🧪 1-Week Implementation Blueprint:
1. **Server (`server.py`)**: A Python WebSocket server maintaining the global model and a Redis cache of layer states.
2. **Clients (`client.py`)**: 3–5 lightweight Python containers running MobileNet/ResNet on CIFAR-10 data.
3. **Selective Layer Logic**: After 1 epoch of local training, calculate the L2 norm of weight changes per layer:
   $$\Delta W_l = ||W_l^{(t)} - W_l^{(t-1)}||_2$$
   Only transmit layers where $\Delta W_l$ exceeds a dynamic threshold; skip transmitting static layers.
4. **Benchmark**: Record bandwidth savings (e.g., 60%+ reduction in network payload with negligible loss in convergence accuracy).

### 🎤 1-Minute Presentation Script:
> *"Prof. Freris, I thoroughly studied your 2024 IEEE IoT Journal paper on layer-wise aggregation for personalized federated learning. In practical edge computing, bandwidth and battery limits prevent low-power devices from uploading full model checkpoints every round.*
> 
> *Building on your layer-wise aggregation concept, I propose an adaptive client-side layer caching framework: edge nodes dynamically evaluate weight divergence and only transmit volatile layers over WebSockets, while the server maintains cached states of stable layers.*
> 
> *With my 4+ years of hands-on experience in real-time WebSocket architectures and containerized systems, I can quickly set up a multi-client Docker testbed in your lab and implement this communication-efficient protocol immediately."*

---

# Proposal 2: For Prof. Junxue Zhang (USTC)

### 📚 Direct Paper Reference:
- *Wang, Chen, Zhang et al.*, **"Towards Efficient Serving of Network-intensive LLM Inferences"**, *Proceedings of the 10th Asia-Pacific Workshop on Networking (APNet)*, 260-266, **2026**.
- *Liu, Huang, Zhang et al.*, **"CEIO: A Cache-Efficient Network I/O Architecture for NIC-CPU Data Paths"**, *Proceedings of ACM SIGCOMM 2025*, 381-394, **2025**.
- *Tian, Wang, Zhang et al.*, **"{PolicyCache}: Intra-flow Learning in Congestion Control"**, *USENIX NSDI 2026*.

---

### 📌 Title:
```text
Network-Aware Prefix Caching and Dynamic Request Batching for High-Throughput Distributed LLM Serving
```

### 💡 The 30-Second Intuition:
When multiple users interact with LLM systems (e.g., Notion AI or customer support agents), their queries share **identical system instructions and historical conversation prefixes**. As highlighted in Prof. Zhang's APNet 2026 paper, sending these repetitive tokens across the network creates severe bandwidth waste and GPU idle time. Your idea is: **An intelligent API Gateway that detects shared prompt prefixes, stores their precomputed Key-Value (KV) attention states in a high-speed Redis cache, and routes requests to GPUs without resending redundant tokens across the network.**

### 🛠️ Why It Is Easy for You to Implement:
- **Core Technology**: Python (FastAPI) + Redis + Docker + vLLM or Ollama (Llama-3 / Mistral).
- **Your Advantage**: You already built a *Notion AI Clone* and have professional experience with Redis caching, REST API gateways, and microservices.

### 🧪 1-Week Implementation Blueprint:
1. **Inference Worker**: Run an open-source LLM (e.g., Llama-3-8B or Mistral-7B) using **vLLM** inside Docker.
2. **Intelligent Gateway (`gateway.py`)**: A lightweight FastAPI reverse proxy that hashes incoming prompt prefixes.
3. **Prefix KV-Cache Layer**: Store common prefix hashes in Redis. If a prefix hit occurs, the gateway instructs vLLM to utilize the cached attention block directly rather than parsing the entire prompt from scratch.
4. **Benchmark**: Use Locust or Apache Bench (`ab`) to simulate 100 concurrent requests with identical system prompts; measure Time-to-First-Token (TTFT) and data transfer volume.

### 🎤 1-Minute Presentation Script:
> *"Prof. Zhang, I was inspired by your APNet 2026 paper on 'Towards Efficient Serving of Network-intensive LLM Inferences' and your SIGCOMM work on cache-efficient I/O.*
> 
> *In production multi-tenant LLM applications, redundant transfer of identical prompt prefixes clogs cluster fabrics and delays first-token response times. I propose an intelligent API-level prefix-caching and batching gateway that detects recurrent prompt prefixes, stores their KV-cache references in a distributed cache, and eliminates redundant token transfers across the cluster network.*
> 
> *Having already engineered full-stack AI-integrated applications and high-throughput Redis caching layers, I can implement and benchmark this serving gateway over containerized vLLM instances in your group from day one."*

---

## 🏆 Recommendation: Which to Pitch First?

1. **If you want the highest probability with 2.5 CGPA**: Start with **Prof. Nikolaos M. Freris**.
   - International European professor; English-speaking group.
   - Evaluates coding demos and GitHub projects over academic transcripts.
2. **If you want the hottest AI systems topic**: Pitch **Prof. Junxue Zhang**.
   - LLM infrastructure is the most well-funded, top-tier research area today.
   - Mentioning his 2026 APNet and SIGCOMM papers will immediately separate you from 99% of other applicants.
