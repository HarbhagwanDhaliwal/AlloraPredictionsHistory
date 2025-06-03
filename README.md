````markdown
# AlloraPredictionsHistory

**AlloraPredictionsHistory** is a Python utility designed to fetch historical prediction data from the [Allora](https://allora.network/) blockchain. This tool allows data scientists and researchers to export structured prediction data into Excel format, enabling them to analyze trends and backtest their own custom strategies.

![Sample Output](https://github.com/HarbhagwanDhaliwal/AlloraPredictionsHistory/blob/4dd343bd7e03712e72bfbbb45e4a272068fa7c70/excel_sheet.png)

---

## 🚀 Features

- 📊 Fetch historical prediction data from the Allora chain  
- 📁 Export data to Excel for seamless analysis and integration  
- 🕒 Support for multiple timeframes: 1 hour, 1 day, 1 week, 1 month  
- 🌐 Multiple RPC endpoints for reliable data fetching  
- ⚙️ Automatically handles missing values and RPC timeouts  

---

## 🔧 Prerequisites

Before you get started, ensure the following are installed on your system:

1. **Go (required to build and run the Allora chain CLI)**  
   👉 [Download Go](https://go.dev/dl/)

2. **Allora Chain Binary (`allorad`)**
   ```bash
   git clone https://github.com/allora-network/allora-chain
   cd allora-chain
   make install
````

---

## 📦 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/HarbhagwanDhaliwal/AlloraPredictionsHistory.git
   cd AlloraPredictionsHistory
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## 🛠️ Usage

Run the script using:

```bash
python main.py
```

* You'll be prompted to enter a topic ID and select a timeframe.
* The script will retrieve prediction data from the allora network chain.
* The results will be saved to an Excel file (`data\allora_chain_data_topic_{topic_id}.xlsx`) in the project folder.

---

## 📁 Output

The generated Excel sheet includes:

* Block Height
* Timestamp
* Allora Predicted Value

---

## 📬 Contact

If you have any suggestions, issues, or want to contribute, feel free to open an issue or pull request.

---
