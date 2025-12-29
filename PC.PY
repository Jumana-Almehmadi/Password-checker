import hashlib

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score+=1
    else:
        feedback.append('1- Lentgh less than 8')

    if any(char.isupper() for char in password):
        score+=1
    else:
        feedback.append('2- No uppercase letter')

    if any(char.islower() for char in password):
        score+=1
    else:
        feedback.append('3- No lowercase letter')

    if any(char.isdigit() for char in password):
        score+=1
    else:
        feedback.append('4- No digits')
    
    if any(char in "!@#$%^&*-()_+=?/~" for char in password):
        score +=1
    else:
        feedback.append('5- 11-No symbol')

    if score <= 2:
        strength = 'Weak password'
    elif score <= 4:
        strength = ' You can protect better !'
    else:
        strength = "strong password"
        
    return strength, feedback

def hash(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

password = input("Enter your password ?")

strength, feedback = check_password(password)
hash = hash(password)

print("Result : ")
print("Strength : ", strength)

if feedback:
    print("Notes :")
    for note in feedback:
        print(note)

print("Hash value (sha-256)")
print(hash)