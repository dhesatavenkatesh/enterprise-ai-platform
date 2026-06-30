from datetime import datetime

def log_request(user, ip, endpoint, method, status):
    print("========== AUDIT LOG ==========")
    print("Timestamp :", datetime.now())
    print("User      :", user)
    print("IP        :", ip)
    print("Endpoint  :", endpoint)
    print("Method    :", method)
    print("Status    :", status)
    print("===============================")