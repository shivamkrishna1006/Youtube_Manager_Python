
import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            test=json.load(file)
            print(test)
            return test
    except FileNotFoundError:
            return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)



def list_all_videos(videos):
    print("\n")
    print("*"*70)
    print
    for i, vid in enumerate(videos, start=1):
        print(f"{i}. {vid['name']}, Duration: {vid['time']}")
    print("\n")
    print("*"*70)

def Add_videos(videos):
    name= input("Enter the name of the video : ")
    time= input("Enter the time of the video : ")
    videos.append({'name' : name  , 'time' :time})
    save_data_helper(videos)



def update_videos(videos):
    pass
def delete_videos(videos):
    pass

def main():
    
 videos=load_data()
 while True:
    print("\n Youtube Manager | choose an option ")
    print("1. list favourite videos")
    print("2. Add a youtube video")
    print("3. update a youtube video details ")
    print("4. delete a youtube video")
    print("5. Exit the app")
    choice= input("Enter the choice")
   # print(videos)

    match choice:
        case '1':
            list_all_videos(videos)
        case '2':
            Add_videos(videos)  
        case '3':
            update_videos(videos)
        case '4':
            delete_videos(videos)
        case '5':
            break
        case _:
            print("Invalid choice")

if __name__ == "__main__":
    main()





