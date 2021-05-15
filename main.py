import amino
import time

client = amino.Client()
client.login(email="ultimatehopee@gmail.com", password="Pikachu01")
subclient = amino.SubClient(comId="67", profile=client.profile)
oldComments = []
users = subclient.get_all_users()
for nickname, id in zip(users.profile.nickname, users.profile.userId):
    wallComments = subclient.get_wall_comments(str(id), sorting='top').content

    if "custom comment" not in wallComments:
        oldComments.append(str(id))
        subclient.comment("WELCOME", userId=str(id))
        print("Commented on", nickname, str(id))

    time.sleep(10.0)

def reconsocketloop():
    j = 0
    while True:
        if j >= 300:
            print("updapting socket...")
            client.socket.close()
            client.socket.start()
            print("updapted socket...")
            j = 0
        j += 1
        time.sleep(1)
reconsocketloop()