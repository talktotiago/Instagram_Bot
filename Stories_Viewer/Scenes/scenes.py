from Functions.functions import *

def Scene_0():
    Log_In_Intelligent()
    Generate_Tags_From_Txt_File_2()
    Collect_Ids()
    
def Scene_1():
    Scene_Visit_Most_Recent_Stories()

def Scene_2():
    Visit_Recent_Stories_Tags_I_Follow()

def Scene_3():
    print("In Scene 3 - we will like 1 post per tag")
    Like_1_Post_Per_Tag()

def Scene_4():
    print("In Scene 4 - We will like 2 posts per tag")
    Liking_2_Posts_Per_Tag()

def Scene_5():
    print("In Scene 5 - the likes are done dynamically - 6 likes per topic")
    Liking_6_Posts_Per_Tag()



def Movie_1():
    try:
        print('Starting Scene 0')
        Scene_0()
    except:
        print('Log In Failed')
        driver.quit()

    try:
        print('Starting Scene 2')
        Scene_2()
    except:
        print("Failed")
    try:
        print("Starting Scene 5")
        Scene_5()
    except:
        print("Scene 5 failed")
        for i in range (0,5):
            time.sleep(1)
            print("Closing Browser in "[5-i])


def Movie_2():
    try:
        print('Starting Scene 0')
        Scene_0()
    except:
        print('Log In Failed')
        driver.quit()

    try:
        print('Starting Scene 1')
        Scene_1()
    except:
        print("Failed")
    try:
        print("Starting Scene 5")
        Scene_5()
    except:
        print("Scene 5 failed")
    for i in range (0,5):
        time.sleep(1)
        print("Closing Browser in "[5-i])








def End_Movie():
    for i in range(0,5):
        print("Closing in "+repr(5-i))
        time.sleep()
    driver.quit()
    print("Bye - and I regret Nothing")