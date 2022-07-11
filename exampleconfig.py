from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 9365736
    API_HASH = "3fa1b478ca72a73d267e10188556cc34"
    # the name to display in your alive message
    ALIVE_NAME = "هادي"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://hbifpcsx:H1KGLnvFlLPFs5u9g6tjhNb9bbdA8zmc@salt.db.elephantsql.com/hbifpcsx"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1BJWap1wBu3AnKuJGX5y4xXdDiRBeQ-kN9jLxw-i-7LWnUTF1a5OeV3px8lXKnVC5OWsIwdyymr5_944SAgCrTWKxVr7CHVeHZrLv04V4IE8C73yma3VMAdeaHpaZnFDiktg2kmY0KaHq9KAhIGdRWyvtwDtZ8pmCUY5uulHbpb7iuS5zVsy0_DlyqnFho984V0JrKn6-oRuVjfwP33alvSRaEyFenFf-wQE6eb1opYpRImf1bDAIJLNomHy0NECjeiaHljithlZm-1Qw8TeskITBdqjdST1pjby0APxMYxDZd3m29xrQxDjWauayARW9ph1PrCbH9noWQpCb1aSFZE4Ss3ET7a4="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "5111897157:AAGKx8QRGetJKugii06AwtLoHqE51AyYMbs"
    TG_BOT_USERNAME = "Q71bot"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001659591037
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = [5049024596]
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
