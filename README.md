# 🔒 Free Fire Ban Checker API

Check if a Free Fire UID is banned — fast, free, and reliable.
  
Powered by Flask & hosted effortlessly on [Vercel](https://vercel.com).

---

## 🚀 Features

- ⚡ Instant ban status check
- 📦 Lightweight Flask API (zero overhead)
- ☁️ Vercel-ready (deploy in seconds)
- 🤖 Developer-friendly JSON response
- 💖 Open-source & free to use

---

## 🔍 How It Works

This API connects to Garena's Free Fire **anti-hack check** system using a UID.  
It returns whether the player is currently banned and for how long.

---

## 📥 API Usage

### 🧾 Endpoint

```
GET /bancheck?uid={uid} 
```
```
https://your.vercel.app/bancheck?uid={uid} 
```
---

### ✅ Example Request

```
https://sumibancheck.vercel.app/bancheck?uid=123456789
```

---

### 📤 Example JSON Response

```json
{
  "credits": "@dear_sumi",
  "free repo": "https://github.com/bisug/FF-Ban-Check-api",
  "status": "BANNED",
  "ban_period": 6,
  "uid": "123456789",
  "is_banned": true
}
```

---

## ⚠️ Error Responses

| Message                    | Reason                          |
|----------------------------|---------------------------------|
| `"Player ID is required"`  | Missing `uid` parameter         |
| `"Failed to fetch data"`   | Garena server error             |
| `status_code: 500`         | Invalid UID / server timeout    |

---

## 🧑‍💻 Local Development

```bash
git clone https://github.com/bisug/FF-Ban-Check-api
cd FF-Ban-Check-api
pip install -r requirements.txt
python index.py

```
## ▲ 1-Click Deploy to Vercel

You can deploy this API to your own Vercel account in seconds:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/bisug/FF-Ban-Check-api)

---

## 🧩 Project Structure

```
.
├── index.py      # Main Flask API
├── requirements.txt
├── vercel.json     # Vercel deployment config
└── README.md       # API documentation
```

-
---

## 🙌 Credits

- 👑 Author: [@dear_sumi](https://t.me/dear_sumi)
- 📂 GitHub Repo: [bisug/FF-Ban-Check-api](https://github.com/bisug/FF-Ban-Check-api)
- 💡 Powered by: Garena’s Anti-Hack API (unofficial)

---

## 📄 License

This project is licensed under the MIT License — use it freely with credit.

---

Feel free to reach out via [@dear_sumi](https://t.me/dear_sumi)! 
