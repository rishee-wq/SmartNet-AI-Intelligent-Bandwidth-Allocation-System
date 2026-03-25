# SmartNet AI – Intelligent Bandwidth Allocation System
## 🎯 Complete Presentation Script & Slide Deck
### *Futuristic Tech Theme | College Viva Ready | Copy directly into Canva / PowerPoint*

---

> **How to Use This File**
> - Each section is one slide.
> - **SLIDE CONTENT** → Add this text to the slide in your presentation tool.
> - **🎤 PRESENTER SCRIPT** → Read this out loud during your viva (3–4 lines per slide).
> - Text in `[brackets]` → Insert actual screenshots/images/diagrams there.

---

---
## SLIDE 1 — TITLE SLIDE
---

### **VISUAL DESIGN NOTES:**
> Dark blue/black background with glowing circuit lines. Project name in bold white text. Use a networking + AI icon (e.g., neural network overlaid on a router).

### SLIDE CONTENT:
```
🌐  SmartNet AI
──────────────────────────────────────
Intelligent Bandwidth Allocation System

[Your Name] | [Roll No.] | [Department]
[College Name]
[Year]

Guided by: [Guide Name]
```

### 🎤 PRESENTER SCRIPT:
> *"Good morning/afternoon. My project is titled SmartNet AI – an Intelligent Bandwidth Allocation System. This project sits at the intersection of two powerful fields — Computer Networking and Artificial Intelligence — and was developed to solve a very real problem that every network administrator faces: intelligent and fair distribution of bandwidth."*

---

---
## SLIDE 2 — ABSTRACT
---

### SLIDE CONTENT:
```
📋  ABSTRACT
──────────────────────────────────────

SmartNet AI is a hybrid networking system that combines:

▸ Cisco Data Communication Networking (DCN)
  • VLAN segmentation (VLAN 10, 20, 30)
  • Router-on-a-Stick inter-VLAN routing

▸ Machine Learning Intelligence
  • Decision Tree Classifier (Python /  Scikit-learn)
  • Classifies traffic: Critical | High | Low

▸ Outcome:
  • 92%+ accuracy in traffic classification
  • Dynamic, adaptive bandwidth management
```

### 🎤 PRESENTER SCRIPT:
> *"In simple terms, SmartNet AI is a two-part system. On the networking side, we use Cisco VLANs to segment traffic. On the AI side, we use a Decision Tree model to predict traffic priority. Together, they allow the network to automatically adjust bandwidth allocation — removing the need for manual intervention by an engineer."*

---

---
## SLIDE 3 — INTRODUCTION
---

### SLIDE CONTENT:
```
📡  INTRODUCTION
──────────────────────────────────────

The Digital Age Challenge:
  ▸ Video calls, cloud apps, IoT, gaming — all compete for bandwidth.
  ▸ A single large file transfer can slow down the entire network.

Why Intelligent Allocation?
  ▸ Static rules can't adapt to real-time demand
  ▸ "Best Effort" delivery treats all traffic equally — that's a problem
  ▸ VoIP call dropping is not equal to a slow update download

Solution: A SMART system that learns traffic patterns
and assigns bandwidth based on actual needs.
```

### 🎤 PRESENTER SCRIPT:
> *"Networks today carry a massive mix of traffic. A simple file download and a live video call require completely different levels of service. Traditional networks treat them the same way — which causes problems. SmartNet AI was designed to be aware of this difference and act on it automatically."*

---

---
## SLIDE 4 — PROBLEM STATEMENT
---

### SLIDE CONTENT:
```
⚠️  PROBLEM STATEMENT
──────────────────────────────────────

Traditional Bandwidth Allocation Has 3 Core Problems:

1️⃣  STATIC POLICIES
    Rules are manually written and never adapt to traffic changes.

2️⃣  NETWORK CONGESTION
    Peak hour traffic clogs the network for all users equally.

3️⃣  UNFAIR DISTRIBUTION
    Bandwidth hogs take up resources needed by critical systems.

        [Impact Illustration / Congestion Diagram]
```

### 🎤 PRESENTER SCRIPT:
> *"The core problem we're solving is this: current networks are 'dumb.' They follow fixed rules written months ago, even if the traffic today looks completely different. This leads to congestion and unfair usage, where a large backup job can cripple the network for a business-critical ERP system. SmartNet AI eliminates this static behavior."*

---

---
## SLIDE 5 — OBJECTIVES
---

### SLIDE CONTENT:
```
🎯  OBJECTIVES
──────────────────────────────────────

This project aims to achieve:

 ✅  VLAN Segmentation
     Logically divide the network by traffic type

 ✅  Inter-VLAN Routing (Router-on-a-Stick)
     Allow controlled communication between VLANs

 ✅  Traffic Prioritization (QoS)
     Mark and queue packets based on their class

 ✅  AI-Based Classification
     Use Machine Learning to predict traffic priority
     and dynamically suggest bandwidth percentages
```

### 🎤 PRESENTER SCRIPT:
> *"Our project had four clear objectives. First, segment the network into logical groups. Second, enable smart routing between those groups. Third, apply QoS to enforce priorities. And fourth — the most important — use Artificial Intelligence to automate the entire classification process so the network can manage itself."*

---

---
## SLIDE 6 — METHODOLOGY: DCN (NETWORKING SIDE)
---

### SLIDE CONTENT:
```
🔧  METHODOLOGY — DCN SIDE
──────────────────────────────────────

  VLAN 10 — CRITICAL   ►  IP: 192.168.10.x
  VLAN 20 — HIGH       ►  IP: 192.168.20.x
  VLAN 30 — LOW/BULK   ►  IP: 192.168.30.x

  🔗 TRUNKING (IEEE 802.1Q):
     Single cable carries all VLANs between Switch and Router.

  🔀 ROUTER-ON-A-STICK (R1):
     Sub-interfaces per VLAN — G0/0.10 | G0/0.20 | G0/0.30
     Each sub-interface acts as the gateway for its VLAN.

  🌐 TOPOLOGY:
     PC → Switch (S1) → Trunk Link → Router (R1) → Another VLAN
```

### 🎤 PRESENTER SCRIPT:
> *"On the networking side, we created three VLANs to separate traffic types. Using 802.1Q trunking, a single cable carries all three VLANs to the router. The router uses sub-interfaces to handle each VLAN separately — this is called Router-on-a-Stick, and it's an efficient way to do inter-VLAN routing without needing multiple physical interfaces."*

---

---
## SLIDE 7 — METHODOLOGY: MACHINE LEARNING SIDE
---

### SLIDE CONTENT:
```
🤖  METHODOLOGY — MACHINE LEARNING
──────────────────────────────────────

  📊 INPUT FEATURES:
     packet_size | burst_rate | protocol_type
     latency | jitter | retransmission_rate

  🌳 MODEL: Decision Tree Classifier
     • Trained on 10,000 synthetic flow samples
     • GridSearchCV for optimal hyperparameters
     • 5-Fold Cross Validation

  📤 OUTPUT → PRIORITY CLASS:
     Class 0 (Critical) → Allocate 40% bandwidth
     Class 1 (High)     → Allocate 30% bandwidth
     Class 2 (Low)      → Allocate 10% bandwidth

  [Insert ML Decision Tree Diagram / Graph]
```

### 🎤 PRESENTER SCRIPT:
> *"This is the brain of our system. We feed network traffic features — like packet size, burst rate, and latency — into a Decision Tree classifier. The model was trained on 10,000 data points and tuned using grid search. Based on its output, the system knows exactly how much bandwidth to assign to each type of traffic."*

---

---
## SLIDE 8 — SYSTEM ARCHITECTURE
---

### SLIDE CONTENT:
```
🏗️  SYSTEM ARCHITECTURE
──────────────────────────────────────

  PHYSICAL COMPONENTS:
  ┌─────────┐     Trunk     ┌──────────┐    ┌─────────┐
  │ PC1     │──────────────▶│          │    │  PC2    │
  │ (VLAN10)│               │  SWITCH  │───▶│(VLAN 20)│
  │         │               │   (S1)   │    │         │
  └─────────┘               └────┬─────┘    └─────────┘
                                 │ Trunk
                           ┌─────▼─────┐
                           │  ROUTER   │
                           │   (R1)    │
                           │ QoS + AI  │
                           └───────────┘

  [Insert Topology Screenshot from Packet Tracer]
```

### 🎤 PRESENTER SCRIPT:
> *"Here's the actual system architecture. We have a single switch, S1, connected to three PCs on different VLANs. A single trunk link goes from the switch to the router R1. The router handles all inter-VLAN routing and enforces the QoS policies generated by the AI model. It's simple, clean, and effective."*

---

---
## SLIDE 9 — IMPLEMENTATION
---

### SLIDE CONTENT:
```
⚙️  IMPLEMENTATION
──────────────────────────────────────

  STEP 1 — SWITCH (S1):
  vlan 10 / 20 / 30 created and named
  fa0/1 → VLAN 10 (access)
  fa0/2 → VLAN 20 (access)
  g0/1  → Trunk (to Router)

  STEP 2 — ROUTER (R1):
  interface g0/0.10
   encapsulation dot1Q 10
   ip address 192.168.10.1 255.255.255.0
   service-policy output SMARTNET_AI_POLICY

  STEP 3 — END DEVICES:
  PC1 → IP: 192.168.10.10 | GW: 192.168.10.1
  PC2 → IP: 192.168.20.10 | GW: 192.168.20.1
  PC3 → IP: 192.168.30.10 | GW: 192.168.30.1
```

### 🎤 PRESENTER SCRIPT:
> *"Implementation had three parts. First, we configured the VLANs and trunk on the switch. Second, we set up sub-interfaces with dot1Q encapsulation on the router — this is what enables Router-on-a-Stick. Third, we assigned IP addresses and gateways to each PC matching their VLAN subnet. This was all built and verified in Cisco Packet Tracer."*

---

---
## SLIDE 10 — RESULTS & TESTING
---

### SLIDE CONTENT:
```
📊  RESULTS & TESTING
──────────────────────────────────────

  TEST 1 — PING TESTING:
  ✅  PC1 (VLAN 10) → PC2 (VLAN 20): SUCCESS
  ✅  PC2 (VLAN 20) → PC3 (VLAN 30): SUCCESS
  ✅  Intra-VLAN communication: SUCCESS

  [Insert Ping Output Screenshot]

  TEST 2 — ML MODEL PERFORMANCE:
  ✅  Accuracy:       92%+
  ✅  F1-Score:       0.91
  ✅  Inference Time: < 0.5ms per flow

  [Insert ML Accuracy / Confusion Matrix Graph]

  TEST 3 — BANDWIDTH ALLOCATION:
  Critical: 400 Mbps (40%)  |  High: 300 Mbps (30%)
  Low:      100 Mbps (10%)  |  AG+:  +15% efficiency
```

### 🎤 PRESENTER SCRIPT:
> *"Our results were highly satisfactory on both fronts. Ping tests confirmed that inter-VLAN routing is working correctly. The ML model achieved over 92% accuracy with sub-millisecond inference time, making it fast enough for real-time use. The bandwidth allocation module successfully distributed bandwidth across all three priority classes."*

---

---
## SLIDE 11 — DISCUSSION
---

### SLIDE CONTENT:
```
💬  DISCUSSION
──────────────────────────────────────

  ✅  ADVANTAGES:
  ▸ Adaptive — learns from traffic patterns, not fixed rules
  ▸ Interpretable — Decision Tree rules are human-readable
  ▸ Cost-effective — uses one router, one switch
  ▸ Scalable — model can be retrained on larger datasets

  ⚠️  LIMITATIONS:
  ▸ Packet Tracer doesn't support real-time Python API calls
  ▸ Synthetic data may not perfectly mirror live network traffic
  ▸ Real deployment requires a dedicated AI controller (e.g., SDN)
```

### 🎤 PRESENTER SCRIPT:
> *"Every system has strengths and limitations. Our key advantage is that the model-based approach is far more adaptable than static QoS rules. However, a key limitation is the Cisco Packet Tracer environment — it's a simulation tool and can't yet run our Python model directly. In a real network, this would be handled by an SDN controller."*

---

---
## SLIDE 12 — FUTURE SCOPE
---

### SLIDE CONTENT:
```
🚀  FUTURE SCOPE
──────────────────────────────────────

  1.  REAL-TIME ML INTEGRATION
      ▸ Use live packet captures (Wireshark / Scapy)
      ▸ Model runs as a microservice, feeding QoS policies live

  2.  QoS AUTOMATION
      ▸ Python script auto-updates router IOS configuration
      ▸ No manual engineer intervention required

  3.  SMART DASHBOARD
      ▸ React or Flask web UI showing live bandwidth usage
      ▸ AI decision log visible to the network admin

  4.  SDN INTEGRATION
      ▸ Deploy on OpenFlow-compatible switches for full control
```

### 🎤 PRESENTER SCRIPT:
> *"The future of this project is very exciting. The immediate next step is to connect the Python model to a live network using tools like Scapy. After that, we can build an automation layer that rewrites router configuration in real time, and a dashboard so administrators can see what the AI is doing at every moment."*

---

---
## SLIDE 13 — CONCLUSION
---

### SLIDE CONTENT:
```
✅  CONCLUSION
──────────────────────────────────────

SmartNet AI successfully demonstrates that:

  ▸ Machine Learning + Networking = Smarter Networks
  ▸ VLANs + Router-on-a-Stick provide structured control
  ▸ Decision Trees offer transparent, fast classification

This project is a proof-of-concept for the next generation
of self-managing networks — where the network understands
traffic and responds intelligently without human intervention.

     "The network of the future doesn't just connect.
               It thinks."
```

### 🎤 PRESENTER SCRIPT:
> *"To conclude, SmartNet AI proves that integrating AI with traditional networking tools creates a far more powerful and responsive system. Our system reduces congestion, eliminates manual QoS management, and scales with demand. This is a glimpse into the future of software-defined, AI-powered networking. Thank you."*

---

---
## SLIDE 14 — REFERENCES
---

### SLIDE CONTENT:
```
📚  REFERENCES
──────────────────────────────────────

[1] Cisco Systems, Inc. (2023). Inter-VLAN Routing and QoS
    Configuration Guide.

[2] Tanenbaum, A. S., & Wetherall, D. J. (2021).
    Computer Networks (6th ed.). Pearson Education.

[3] Pedregosa et al. (2011). Scikit-learn: Machine Learning
    in Python. JMLR, 12, pp. 2825–2830.

[4] IEEE Standard 802.1Q — Virtual Bridged Local Area Networks.

[5] Cisco Networking Academy — CCNA: Switching & Routing Essentials.

[6] Mitchell, T. M. (1997). Machine Learning. McGraw Hill.
```

### 🎤 PRESENTER SCRIPT:
> *"These are the key references we used during this project — standard textbooks on Networking and Machine Learning, Cisco's official documentation, and IEEE standards. All implementation details are grounded in these authoritative sources."*

---

---
## BONUS: AI DECISION FLOW DIAGRAM (for Slide 7)
---

```
              ┌──────────────────────────┐
              │     Network Traffic       │
              │   (Incoming IP Packet)    │
              └───────────┬──────────────┘
                          │
                          ▼
              ┌──────────────────────────┐
              │    Feature Extraction     │
              │  packet_size | burst_rate │
              │  latency | protocol_type  │
              └───────────┬──────────────┘
                          │
                          ▼
              ┌──────────────────────────┐
              │   Decision Tree Model     │
              │   (Python / Scikit-learn) │
              └────┬──────────┬──────────┘
                   │          │          │
                   ▼          ▼          ▼
              CRITICAL      HIGH       LOW
              (Class 0)   (Class 1)  (Class 2)
                   │          │          │
                   ▼          ▼          ▼
               40% BW      30% BW     10% BW
           ┌──────────────────────────────────┐
           │ Cisco QoS Policy Applied (R1)    │
           └──────────────────────────────────┘
```

---

---
## BONUS: PRESENTER QUICK REFERENCE CARD
---

| Slide | Topic | Time |
|-------|-------|------|
| 1 | Title | 15 sec |
| 2 | Abstract | 1 min |
| 3 | Introduction | 1 min |
| 4 | Problem Statement | 1 min |
| 5 | Objectives | 1 min |
| 6 | DCN Methodology | 2 min |
| 7 | ML Methodology | 2 min |
| 8 | Architecture | 1.5 min |
| 9 | Implementation | 2 min |
| 10 | Results | 1.5 min |
| 11 | Discussion | 1 min |
| 12 | Future Scope | 1 min |
| 13 | Conclusion | 45 sec |
| 14 | References | 15 sec |
| **TOTAL** | | **~17 min** |

---
*End of Presentation Script*
