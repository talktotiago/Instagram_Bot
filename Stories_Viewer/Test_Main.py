from Essentials.essentials import *
from Classes.classes import *
from Xpaths.xpaths import *
from Elements.elements import *
from Credentials.credentials import *
from Functions.functions import *
from Elements.elements import *
from selenium.webdriver.common.keys import Keys
from Setup.setup import *
from Scenes.scenes import *
from trending_searches import *
#Start a dynamic list built with the trending_searches.py document
try:
    print("Attempting to build an automated list")
    #Trending_Hashtags()
except:
    print("Some error occurred - check tags.txt file in Tags folder")
#################

url = "http://www.instagram.com"
driver.get(url)
time.sleep(4)

""" Generate_Tags_From_Txt_File_2()
time.sleep(5)

print(tags)
 """
try:
    Scene_0()
except:
    print("Error during Log In - Scene_0 failed")

try:
    print("Starting to Watch People I follow Stories")
    #Scene_1()
except:
    print("Error while trying to watch stories from people I follow - Some Error with Scene_1() - going to next Scene")
#try:
print("Starting Scene_5() - Liking 6 posts per tag")
Liking_6_Posts_Per_Tag()
#except:
print("Some error happened while trying to like posts from tags - Scene_5() failed")
