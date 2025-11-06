from flask import Flask, render_template, request, jsonify
import string


app = Flask(__name__)

# Common weak passwords
COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123", 
    "password1", "admin", "letmein", "welcome", "monkey"
]


def check_password_strength(password: str) -> dict:
    """Returns detailed password strength analysis"""
    if not password:
        return {
            "strength": "None",
            "score": 0,
            "percentage": 0,
            "feedback": [],
            "checks": {
                "length": False,
                "has_upper": False,
                "has_lower": False,
                "has_digit": False,
                "has_special": False,
                "not_common": True
            }
        }
    
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    not_common = password.lower() not in COMMON_PASSWORDS
    
    # Calculate score
    checks_passed = sum([has_upper, has_lower, has_digit, has_special, not_common])
    
    # Length scoring
    length_score = 0
    if length >= 12:
        length_score = 2
    elif length >= 8:
        length_score = 1
    
    # Total score out of 7 (4 char types + 1 common + 2 length)
    total_score = checks_passed + length_score
    
    # Calculate percentage
    percentage = int((total_score / 7) * 100)
    
    # Determine strength level
    if length < 8:
        strength = "Very Weak"
        strength_class = "very-weak"
    elif total_score <= 2:
        strength = "Weak"
        strength_class = "weak"
    elif total_score <= 4:
        strength = "Medium"
        strength_class = "medium"
    elif total_score <= 5:
        strength = "Strong"
        strength_class = "strong"
    else:
        strength = "Very Strong"
        strength_class = "very-strong"
    
    # Generate feedback
    feedback = []
    if length < 8:
        feedback.append("Password should be at least 8 characters")
    elif length < 12:
        feedback.append("Consider using 12+ characters for better security")
    
    if not has_upper:
        feedback.append("Add uppercase letters")
    if not has_lower:
        feedback.append("Add lowercase letters")
    if not has_digit:
        feedback.append("Add numbers")
    if not has_special:
        feedback.append("Add special characters (!@#$%...)")
    if not not_common:
        feedback.append("Avoid common passwords")
    
    if not feedback:
        feedback.append("Excellent password! ✓")
    
    return {
        "strength": strength,
        "strength_class": strength_class,
        "score": total_score,
        "percentage": percentage,
        "feedback": feedback,
        "checks": {
            "length": length >= 8,
            "length_optimal": length >= 12,
            "has_upper": has_upper,
            "has_lower": has_lower,
            "has_digit": has_digit,
            "has_special": has_special,
            "not_common": not_common
        }
    }


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/check")
def check():
    if request.is_json:
        data = request.get_json(silent=True) or {}
        password = data.get("password", "")
        result = check_password_strength(password)
        return jsonify(result)

    password = request.form.get("password", "")
    result = check_password_strength(password) if password else {}
    return render_template("index.html", result=result, prev_password=password)


if __name__ == "__main__":
    app.run(debug=True)


