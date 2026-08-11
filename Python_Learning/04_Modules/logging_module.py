import logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


username = input("Enter a username: ")
password = input("Enter a password: ")

if username == 'admin' and password == '1234':
    print("Login Successful.")
    logging.info("User logging Successfully")

elif username != 'admin':
    print("Username is incorrect.")
    logging.warning("Wrong username Entered")
else:
    print("Password is incorrect.")
    logging.error("Password is incorrect.")


