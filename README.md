# Instagram_Bot
An Instagram Bot to watch stories and give likes in pictures **built with Python and Selenium Webdriver.


How to get started?

Step 1:

Download Selenium Webdriver for Chrome. Save the driver and don't forget to change the location of the driver inside the file essentials.py located at Essentials folder.

Step 2:

Go to Credentials folder and replace the variables values by your instagram and facebook credentials, check credentials.py file. 

Step 3:

You can generate a list of tags manually or dynamically or both.

To do it MANUALLY: Go inside Tags folder and add as many tags as you'd like inside tags.txt file. Each tag must be in a single line.

To do it DYNAMICALLY: Go to file trending_searches.py and edit the LIST type variable "tags_to_search" with the tags you'd like to build a list. Save it and run the file. This will automatically add 10 different tags per tag in "tags_to_search" list variable. These tags are retrieved from the website https://best-hashtags.com/. So, if you add 20 tags in the "tags_to_search" you will end up building a list with 200 tags. That means 200 different urls for selenium to visit. Play safe with this in order to fly under instagram filters.

Step 4: This program is built with the use of Stories. Each Story is a scene. By default you should start your program with "Scene_0()" - this scene will attempt to perform login by Instagram, and if unsuccesful it will attempt to login via Facebook. That's why you should add your Facebook credentials.

Explaining Scenes: Each Scene is a Story performed by the bot.

Scene_1()

Scan for the 7 most recent people that you follow who published a story and visits each story of them for building impact.

Scene_2() Visits the stories of all tags in tags.txt file

Scene_3() Likes 1 pic per tag

Scene_4() Likes 2 pics per tag

Scene_5() Likes 6 pics per tag

Movie_1() Composed of Scenes 0,2 and 5

Movie_2() Composed of Scenes 0,1 and 5

You can create your own Movie using the pre-built scenes. Remember to start the Scenes with Scene_0 **ALWAYS**.

To check how Each Scene was made go to: scenes.py file inside Scenes folder. 
To check how which function works, go to: functions.py file inside Functions folder.
You are free to change this and use it as you wish. You can also hire me to write you scripts like this. 
