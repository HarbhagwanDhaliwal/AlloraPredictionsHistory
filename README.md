```markdown
# AlloraPredictionsHistory 📈⏳

**AlloraPredictionsHistory** is a Python utility designed to fetch historical prediction data from the [Allora](https://allora.network/) blockchain. This tool allows data scientists and researchers to export structured prediction data into Excel format, enabling them to analyze trends and backtest their own custom strategies.

![Sample Output](https://raw.githubusercontent.com/HarbhagwanDhaliwal/AlloraPredictionsHistory/1804b914a6e593b32d367d6180c0091165e12811/excel_sheet.png)


## 🌟 Key Features

- **Historical Data Collection**: Fetch prediction data directly from Allora chain
- **Multiple Timeframes**: 1H, 1D, 1W, and 1M historical windows
- **Reliable Architecture**: 
  - Multiple RPC endpoint support
  - Automatic failover and retry logic
- **Analysis-Ready Output**: 
  - Clean Excel format with proper formatting
  - Includes timestamps and predicted values
- **Smart Error Handling**:
  - Zero-value detection
  - Timeout management

## 🚀 Quick Start

### Prerequisites

1. **Install Go** (v1.20+ required):
   ```bash
   # Linux/macOS
   wget https://go.dev/dl/go1.21.4.linux-amd64.tar.gz
   sudo tar -C /usr/local -xzf go1.21.4.linux-amd64.tar.gz
   export PATH=$PATH:/usr/local/go/bin
   ```

2. **Install Allora Chain**:
   ```bash
   git clone https://github.com/allora-network/allora-chain
   cd allora-chain
   make install
   ```

3. **Set Up Python Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # OR
   venv\Scripts\activate    # Windows
   ```

### Installation

```bash
git clone https://github.com/HarbhagwanDhaliwal/AlloraPredictionsHistory.git
cd AlloraPredictionsHistory
pip install -r requirements.txt
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
RPC_URLS = [
    "https://allora-rpc.testnet.allora.network",  # Primary endpoint
    "https://allora-testnet-rpc.polkachu.com",   # Secondary endpoint
    # Add your private nodes here
]

# Advanced Settings
REQUEST_TIMEOUT = 15      # seconds per request
MAX_RETRIES = 3           # retry attempts
ZERO_VALUE_COOLDOWN = 60   # seconds to wait after zero values
```

## 🖥️ Basic Usage

Run the interactive collector:

```bash
python main.py
```

Follow the prompts:
1. Enter Topic ID (e.g., `58` for SOL/USD predictions)
2. Select Timeframe (1H/1D/1W/1M)
3. View real-time collection progress
4. Find your data in `data/allora_chain_data_topic_{ID}.xlsx`

## 📊 Output Format

The Excel output contains:

| Column             | Description                          | Example Value              |
|--------------------|--------------------------------------|----------------------------|
| BLOCK_HEIGHT       | Blockchain block number              | 4077213                    |
| BLOCK_TIMESTAMP    | ISO-formatted UTC timestamp          | 2025-06-03T18:50:18+00:00  |
| ALLORA_PREDICTED_VALUE | Network consensus prediction    | -0.0010625262224340856     |

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Report Issues**: Found a bug? Open an issue
2. **Suggest Features**: Have an idea? Start a discussion
3. **Submit Pull Requests**
```

Remember to:
1. Ensure the screenshot path is correct
2. Verify all links work
3. Update contact email
4. Keep the LICENSE file updated
5. Maintain consistency with your actual project structure
