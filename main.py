import playsound
status = input("Do you want to start | yes | no | : ")
while(status=="yes"):
    vod = input("Enter the song you want to play : ")
    playsound.playsound(vod, True)
    status = input("Do you want to start another song or the same song again ? | yes | no | : ")


