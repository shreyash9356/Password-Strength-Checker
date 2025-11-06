# Password-Strength-Checker

A modern Flask web application that analyzes and visualizes the strength of passwords in real time. Built with Python and Flask, it helps users create stronger passwords by checking for length, character diversity, entropy, and common weaknesses — all through a clean, responsive web interface.

## ✨ Features

- **Real-time Password Analysis** - Instant feedback as you type
- **Visual Strength Indicator** - Color-coded progress bar showing password strength
- **Detailed Requirements Checklist** - See which password requirements are met
- **Show/Hide Password Toggle** - Easy password visibility control
- **Strength Percentage Score** - 0-100% strength rating
- **Common Password Detection** - Warns against weak/common passwords
- **Responsive Design** - Works beautifully on all devices
- **Modern UI** - Dark theme with smooth animations

## 🚀 Quick Start

1) Create/activate a virtual environment (recommended).

```bash
python -m venv .venv
# Windows PowerShell
. .venv\Scripts\Activate.ps1
```

2) Install dependencies:

```bash
pip install -r requirements.txt
```

3) Run the app:

```bash
python app.py
```

4) Open in your browser:

- http://127.0.0.1:5000/

## 📡 API

- **POST `/check`**
  - Request: `{ "password": "..." }`
  - Response: 
    ```json
    {
      "strength": "Very Weak|Weak|Medium|Strong|Very Strong",
      "strength_class": "very-weak|weak|medium|strong|very-strong",
      "score": 0-7,
      "percentage": 0-100,
      "feedback": ["suggestion1", "suggestion2", ...],
      "checks": {
        "length": true/false,
        "length_optimal": true/false,
        "has_upper": true/false,
        "has_lower": true/false,
        "has_digit": true/false,
        "has_special": true/false,
        "not_common": true/false
      }
    }
    ```

The browser UI uses this endpoint via `fetch()` for real-time password checking.

## 🛠️ Technologies Used

- **Flask** - Web framework
- **Python** - Backend logic
- **HTML/CSS/JavaScript** - Frontend interface
- **Modern CSS** - Animations, gradients, responsive design

## 📝 Password Requirements

The checker evaluates passwords based on:
- Minimum 8 characters (12+ recommended)
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Numbers (0-9)
- Special characters (!@#$%...)
- Not a common password

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests!
