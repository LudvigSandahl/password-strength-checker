import re
import string

COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]

def check_length(password):
    length = len(password)
    if length < 8:
        return 0, "Too short — aim for at least 8 characters"
    elif length < 12:
        return 1, None
    elif length < 16:
        return 2, None
    return 3, None

def check_password(password):
    if password.lower() in COMMON_PASSWORDS:
        return "Weak", 0, ["Pick something less obvious."]

    score = 0
    feedback = []

    length_score, length_tip = check_length(password)
    score += length_score
    if length_tip:
        feedback.append(length_tip)

    # Character checks
    checks = [
        (any(c.isupper() for c in password), "Add an uppercase letter"),
        (any(c.islower() for c in password), "Add a lowercase letter"),
        (any(c.isdigit() for c in password), "Add a number"),
        (any(c in string.punctuation for c in password), "Add a special character (!@#$ etc)"),
    ]

    for passed, tip in checks:
        if passed:
            score += 1
        else:
            feedback.append(tip)

    # Check for repeated characters
    if re.search(r'(.)\1{2,}', password):
        feedback.append("Avoid repeating characters like 'aaa' or '111'")
    else:
        score += 1

    strengths = ["Weak", "Weak", "Moderate", "Moderate", "Strong", "Strong", "Very Strong", "Very Strong"]
    strength = strengths[min(score, len(strengths) - 1)]

    return strength, score, feedback


def main():
    print("Password Strength Checker\n")

    while True:
        password = input("Enter a password (or 'q' to quit): ")

        if password.lower() == "q":
            break

        strength, score, feedback = check_password(password)
        print(f"\nResult: {strength} ({score}/8)")

        if feedback:
            print("Tips:")
            for tip in feedback:
                print(f"  - {tip}")
        print()

if __name__ == "__main__":
    main()