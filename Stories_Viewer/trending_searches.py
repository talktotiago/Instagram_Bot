from Essentials.essentials import *


tag_to_search = [
    'Market', 
    'Ecommerce', 
    'ForSale', 
    'Neymar', 
    'Photography', 
    'PicOfTheDay', 
    'Instadog', 
    'Georgia',
    'Tblisi',
    'Kiev',
    'Madagascar',
    ]

url = 'https://best-hashtags.com/hashtag/'


def Trending_Hashtags():
    print(url)
    tags = []
    xpaths = []
    for i in range (0,len(tag_to_search)):
        time.sleep(5)
        driver.get(url+tag_to_search[i])
        #Generate xpaths "...h3[1]/a","...h3[2]/a", "...h3[3]/a" ---- t0 h3[10]/a
        print("Generating Xpaths to find the text from url")
        for i in range (1,11):
            #Find Element and append them to tags list
            find_xpaths = '/html/body/div[1]/div[4]/div[1]/div/div[1]/div/div/div[3]/div[1]/h3['+repr(i)+']/a'
            xpaths.insert(0,find_xpaths)
        print(xpaths)
        #Retrieve Text from Selenium    
        for i in range (0,10):
            try:
                tags.append(driver.find_element_by_xpath(xpaths[i]).text)
            except:
                print('error getting text from xpath ' + xpaths[i])
        #append them to tags variable and print
        for i in range (0,len(tags)):
            print(tags[i])
        
        #Remove Hashtag from text
        for idx, ele in enumerate(tags): 
            tags[idx] = ele.replace('#', '') 
        # printing result 
        print("The list after removal of character : " + str(tags))
    #Save them to a text file
    file_to_save_tags = open(r'./Tags/automatic_tags.txt', 'a+')
    file_to_save_tags_2 = open(r'./Tags/tags.txt', 'a+')
    for i in range (0, len(tags)):
        file_to_save_tags.write(tags[i]+'\n')
        file_to_save_tags_2.write(tags[i]+'\n')
    file_to_save_tags.close()
    driver.quit()


