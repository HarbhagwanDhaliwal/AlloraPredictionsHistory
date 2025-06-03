````markdown
# 📈 AlloraPredictionsHistory ⏳

**AlloraPredictionsHistory** is a powerful Python utility thatfetches historical prediction data from the [Allora Network](https://allora.network/) blockchain.
It enables data scientists and researchers to analyze trends, backtest custom strategies, and export prediction data to Excel format effortlessly.

---

## 🌟 Features

- 📊 **Historical Data Collection** – Retrieve blockchain prediction data by topic ID.
- ⏱️ **Flexible Timeframes** – Choose from 1H, 1D, 1W, or 1M for tailored analysis.
- 🔁 **Resilient Architecture**
  - Supports **multiple RPC endpoints**
  - Built-in **automatic failover** and **retry logic**
- 📂 **Ready-to-Use Excel Output**
  - Clean tabular format
  - Includes timestamps and predicted values
- ⚠️ **Smart Error Handling**

---

## 🚀 Getting Started

### 🧰 Prerequisites

1. **Install Go (v1.20+)**
   ```bash
   wget https://go.dev/dl/go1.21.4.linux-amd64.tar.gz
   sudo tar -C /usr/local -xzf go1.21.4.linux-amd64.tar.gz
   export PATH=$PATH:/usr/local/go/bin
````

2. **Install Allora Chain**

   ```bash
   git clone https://github.com/allora-network/allora-chain
   cd allora-chain
   make install
   ```

3. **Create Python Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # or
   venv\Scripts\activate     # Windows
   ```

---

### 📦 Installation

```bash
git clone https://github.com/HarbhagwanDhaliwal/AlloraPredictionsHistory.git
cd AlloraPredictionsHistory
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Edit `config.py` to suit your needs:

```python
RPC_URLS = [
    "https://allora-rpc.testnet.allora.network",  # Primary
    "https://allora-testnet-rpc.polkachu.com",    # Backup
]

REQUEST_TIMEOUT = 15      # Request timeout (seconds)
MAX_RETRIES = 3           # Max retry attempts
ZERO_VALUE_COOLDOWN = 60  # Cooldown if zero value detected (seconds)
```

---

## 🖥️ Usage

Run the interactive script:

```bash
python main.py
```

You'll be prompted to:

1. 🔢 Enter a Topic ID (e.g., `58` for SOL/USD)
2. 🕒 Select a Timeframe (`1H`, `1D`, `1W`, or `1M`)
3. ⏳ View collection progress
4. 📁 Find your output Excel file in `data/allora_chain_data_topic_{ID}.xlsx`

---

## 📊 Output Format

The resulting Excel file includes:

| Column                   | Description                     | Example                     |
| ------------------------ | ------------------------------- | --------------------------- |
| `BLOCK_HEIGHT`           | Block number on the chain       | `4077213`                   |
| `BLOCK_TIMESTAMP`        | UTC timestamp (ISO 8601 format) | `2025-06-03T18:50:18+00:00` |
| `ALLORA_PREDICTED_VALUE` | Network consensus prediction    | `-0.0010625262224340856`    |

---

## 🤝 Contributing

We’d love your help! Here’s how you can contribute:

* 🐞 **Report Issues** – Found a bug? Open an issue.
* 💡 **Suggest Features** – Have an idea? Let’s discuss.
* 🔧 **Pull Requests** – Improve code, docs, or features.

---
