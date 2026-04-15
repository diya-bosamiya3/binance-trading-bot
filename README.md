# Binance Futures Trading Bot (Mock Implementation)

A command-line trading bot that simulates placing Market and Limit orders on Binance Futures (USDT-M), designed with clean architecture, validation, and logging.

---

## 📌 Overview

This project demonstrates a structured trading bot system with:

- CLI-based order execution
- Input validation
- Logging of requests and responses
- Error handling
- Modular and reusable code design

Due to API access restrictions (KYC requirements), the bot uses **mock responses** that closely resemble real Binance Futures API behavior.

---

## 📁 Project Structure


trading_bot/
├── bot/
│ ├── init.py
│ ├── orders.py # Mock order execution logic
│ ├── validators.py # Input validation
│ └── logging_config.py # Logging setup
├── cli.py # CLI entry point
├── trading_bot.log # Log file (generated after running)
├── requirements.txt
└── README.md


---

## ⚙️ Features

- ✅ Market Order support
- ✅ Limit Order support
- ✅ BUY / SELL sides
- ✅ CLI-based input handling
- ✅ Input validation with error messages
- ✅ Logging of orders and responses
- ✅ Clean modular structure

---

## 🚀 How to Run

### 1. Install dependencies


pip install -r requirements.txt


---

### 2. Run Market Order


python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01


---

### 3. Run Limit Order


python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000


---

## 📄 Example Output


📌 Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.01

✅ Order Successful!
Order ID: 123456
Status: FILLED
Executed Qty: 0.01
Avg Price: 65000


---

## 📊 Logging

All order activity is logged in:


trading_bot.log


Logs include:
- Order requests
- Order responses
- Errors (if any)

---

## ⚠️ Notes

- This project uses **mock responses** instead of real Binance API calls.
- Designed to replicate real-world trading system architecture.
- Can be easily extended to integrate real APIs.

---

## 🧠 Design Decisions

- Separation of concerns (CLI, validation, logic)
- Reusable and scalable structure
- Logging for traceability and debugging
- Mock layer to simulate real API behavior

---

## 📌 Assumptions

- User provides valid symbol format (e.g., BTCUSDT)
- Internet/API not required (mock mode)

---

## 🔮 Future Improvements

- Add Stop-Limit order support
- Integrate real Binance API
- Add interactive CLI menu
- Add simple UI

---

## 📬 Submission Note

This implementation fulfills all core requirements including:
- Order placement logic (mocked)
- CLI input handling
- Validation
- Logging
- Clean project structure