from Essentials.essentials import *
from Credentials.credentials import *
from Xpaths.xpaths import *
from Classes.classes import *
from Setup.setup import *
from Elements.elements import *
from Essentials.variables import *

def Login_By_FB():
    try:
        print('Clicking at Facebook Login Option Btn')
        try:
            print('FB Option Btn - looking xpath')
            driver.find_element_by_xpath(login_option_btn_xpath).click()
            print('Success!')
            time.sleep(2)
        except:
            print('1st Attempt failed - ATTEMPT 2: going by class name')
            driver.find_element_by_class_name(login_option_btn_fb_class).click()    
            print('Success')
            time.sleep(2)
        try:
            print('passing username - attempting by xpath')
            driver.find_element_by_xpath(username_field_fb_xpath).send_keys(username_fb)
            print('Success!')
        except:
            print('error - attempting by class name to insert username')
            driver.find_element_by_class_name(username_field_fb_class).send_keys(username_fb)
            print('Success!')
        try:
            print('trying to insert password via xpath')
            driver.find_element_by_xpath(password_field_fb_xpath).send_keys(password_fb)
            print('Success')
        except:
            print('Error - attempting by class name')
            driver.find_elements_by_class_name(password_field_fb_class).send_keys(password_fb)
            print('Success!!')
        try:
            print('Clicking at Log In Button')
            driver.find_element_by_xpath(login_btn_fb_xpath).click()
            print('Success!')
        except:
            print('Error - attempting via class name')
            driver.find_elements_by_class_name(login_btn_fb_class).click()
            print('Success! We are in!')
    except:
        print('Error to Log In with FB')

def Login_By_IG():
    try:
        Username_Field_IG()
    except:
        print('Some error occurred while passing the username in the username field - trying in 3 seconds again')
        for i in range(0,3):
            print("Seconds "+repr(3-i))
        Username_Field_IG()
    try:
        Password_Field_IG()
    except:
        print('Some error occurred while passing the password in the password field - trying in 3 seconds again')
        for i in range(0,3):
            print("Seconds "+repr(3-i))
        Password_Field_IG()
    try:
        print('Clicking at Login Btn')
        Login_Btn_IG()
    except:
        print('Some error occurred while passing the password in the password field - trying in 3 seconds again')
        for i in range(0,3):
            print("Seconds "+repr(3-i))
        Login_Btn_IG()

def Count_Recent_Stories():
    try:
        print('looking for recent stories by class name - attempt 1')    
        recent_stories = driver.find_elements_by_class_name(recent_stories_class)
        ######
        #river.find_element_by_class_name(recent_stories_class).text
        ####
        last_time_count_recent_stories.insert(0,repr(len(recent_stories)))
        print('success - found: '+repr(last_time_count_recent_stories)+' recent stories')
    except:
        print('some error occurred - trying again')
        print(repr(last_time_count_recent_stories))
        last_time_count_recent_stories.insert(0,repr(len(recent_stories)))
        print('success - stories found: '+repr(last_time_count_recent_stories))

def Arrow_Btn_Right_Recent_Stories():
    try:
        print('Click in arrow btn right')
        driver.find_element(arrow_btn_right_class).click()
        print('Success!')
    except:
        print('failed in first attempt - click in arrow btn right - attempt 2')
        driver.find_element_by_xpath(arrow_btn_right_xpath).click()
        print('Success')

def Arrow_Btn_Left_Recent_Stories():
    try:
        print('Click in arrow btn left')
        driver.find_element_by_class_name(arrow_btn_right_class).click()
        print('Success!')
    except:
        print('failed in first attempt - click in arrow btn left- attempt 2')
        driver.find_element_by_xpath(arrow_btn_right_xpath).click()
        print('Success!')

def Click_Left_and_Right_Recent_Stories():

    try:
        for i in range (0,nr_of_clicks_to_tap):
            Arrow_Btn_Right_Recent_Stories()
            time.sleep(0.15)
    except:
        print('Button disappeared. Click left')
        try:
            time.sleep(0.25)
            for i in range (0,nr_of_clicks_to_tap):
                Arrow_Btn_Left_Recent_Stories()
                time.sleep(0.15)
            Count_Recent_Stories()
        except:
            try:
                print('End of line - Error occured by button disappearence - Counting Recent Stories')
                Count_Recent_Stories()
            except:
                print('MAJOR ERROR - GOING BACK TO HOME PAGE')
                driver.get(url)
                time.sleep(2)
                print('Back to '+url+ ' due to error in Click_Left_and_Right_Function')

def Log_In_Intelligent():
    try:
        Login_By_IG()
        time.sleep(3)
        print('Instagram Logo click')
        Logo_Instagram()
        time.sleep(2)
        Not_Now_Btn()
    except:
        Login_By_FB()
        time.sleep(3)
        #Logo_Instagram()
        time.sleep(2)
        Not_Now_Btn()
        time.sleep(3)

def Check_Recent_Stories_From_People_I_Follow():
    print('Name of The first publisher')
    buttons = driver.find_elements_by_class_name('Ckrof')
    print(len(buttons))
    for i in range (0,len(buttons)):
        print('Story '+repr(i)+' of '+repr(len(buttons)-i))
        try:
            print(buttons[i].text)
        except:
            print('some error occurred')

def Visit_Recent_Stories_People_I_Follow():
    url = 'https://www.instagram.com'
    for i in range (0,len(collect_ids)):
        driver.get(url+'/'+collect_ids[i])
        time.sleep(1)
        driver.find_element_by_class_name(profile_story_btn_class).click()
        time.sleep(2)
        Jump_Stories()

def Jump_Stories():
    count_stories_in_profile = driver.find_elements_by_class_name('_7zQEa')
    print('This profile has: ' +repr(len(count_stories_in_profile)))
    for i in range (0,len(count_stories_in_profile)):
        try:
            time.sleep(0.2)
            driver.find_element_by_class_name(next_story_btn_class).click()
            time.sleep(0.2)
        except:
            print("Go to Next")
            try:
                print(collect_ids)
                print(url+'/'+collect_ids[i+1])
                driver.get(url+'/'+collect_ids[i+1])
            except:
                print("ERROR - Out of Range?")
                print("ERROR ####### ERROR ##### QUITTING DRIVER ####")
                driver.quit()



def Collect_Ids():
    buttons = driver.find_elements_by_class_name('Ckrof')
    for i in range (0,len(buttons)):
        try:
            collect_ids.append(buttons[i].text)
        except:
            print('ignore error')
        
def Generate_Tags_From_Txt_File():
    file1 = open(r'./Stories_Viewer/Tags/tags.txt', 'r+') 
    count = 0
  
    for line in file1: 
        count += 1
        tags.append(line.strip())
        print("Line{}: {}".format(count, line.strip()))
    print(tags)
    # Closing files 
    file1.close()

def Visit_Recent_Stories_Tags_I_Follow():
    url = 'https://www.instagram.com'
    for i in range (0,len(tags)):
        driver.get(url+'/explore/tags/'+tags[i])
        time.sleep(3)
        print('clicking '+url+'/explore/tags/'+tags[i])
        try:
            driver.find_element_by_class_name('fZC9e').click()
            time.sleep(2)
            Jump_Stories()
        except:
            try:
                print('Failed at '+tag[i])
                print('Reloading to next tag in line' + tag[i+1])
                driver.get(url+'/explore/tags/'+tags[i+1])
                time.sleep(3)
                print('clicking '+url+'/explore/tags/'+tags[i+1])
                try:
                    driver.find_element_by_class_name('fZC9e').click()
                    time.sleep(2)
                    Jump_Stories()
                except:
                    print('Failed - Trying again with new tag')
                    print('clicking '+url+'/explore/tags/'+tags[i+2])
                    time.sleep(3)
                    driver.find_element_by_class_name('fZC9e').click()
                    time.sleep(2)
                    Jump_Stories()
            except:
                print('Several attempts were made - check source code for reasons')

def Scene_Visit_Most_Recent_Stories():
    Collect_Ids()
    print(collect_ids)
    Visit_Recent_Stories_People_I_Follow()
    driver.quit()

def Like_1_Post_Per_Tag():
    for i in range (0,len(tags)):
        driver.get(url+"/explore/tags/"+tags[i])
    try:
        click_post = driver.find_element_by_xpath(click_post_xpath).click()
        time.sleep(1)
        like_post = driver.find_element_by_xpath(like_post_xpath)
        like_post.click()
        close_post = driver.find_element_by_xpath(close_post_xpath)
        time.sleep(0.0029)
        close_post.click()
        time.sleep(1)
    except:
        print('Page Unavailable or some other error at '+ url+"/explore/tags/"+tags[i])


def Scene_3():
        for i in range (0,len(tags)):
            driver.get(url+'/explore/tags/'+tags[i])
            time.sleep(3)
            print('clicking '+url+'/explore/tags/'+tags[i])
            first_post_open = driver.find_element_by_xpath(first_post_tag_xpath).click()
        try:
            first_post_open = driver.find_element_by_xpath(first_post_tag_xpath).click()
            time.sleep(1)
            like_this_post = driver.find_element_by_xpath(like_post_xpath).click()
            time.sleep(0.5)
            close_this_post = driver.find_element_by_xpath(close_post_xpath).click()
        except:
            print("Error Clicking at First Post")
        try:
            second_post_open = driver.find_element_by_xpath(second_post_tag_xpath).click()
            time.sleep(1)
            like_this_post = driver.find_element_by_xpath(like_post_xpath).click()
            time.sleep(0.5)
            close_this_post = driver.find_element_by_xpath(close_post_xpath).click()
        except:
            print("Error Clicking at Second Post")
        try:
            third_post_open = driver.find_element_by_xpath(third_post_open).click()
            time.sleep(1)
            like_this_post = driver.find_element_by_xpath(like_post_xpath).click()
            time.sleep(0.5)
            close_this_post = driver.find_element_by_xpath(close_post_xpath).click()
        except:
            print("Error Clicking at Third Post")
        try:
            fourt_post_open = driver.find_element_by_xpath(second_post_tag_xpath).click()
            time.sleep(1)
            like_this_post = driver.find_element_by_xpath(like_post_xpath).click()
            time.sleep(0.5)
            close_this_post = driver.find_element_by_xpath(close_post_xpath).click()
        except:
            print("Error Clicking at Second Post")


def Like_1_Post_Per_Tag():
    for i in range (0,len(tags)):
        driver.get(url+'/explore/tags/'+tags[i])
        time.sleep(3)
        print('clicking '+url+'/explore/tags/'+tags[i])
        try:
            first_post_open = driver.find_element_by_xpath(first_post_tag_xpath).click()
            print('First Post Click')
            time.sleep(1)
            print('Liking Post')
            like_this_post = driver.find_element_by_xpath(like_post_xpath).click()
            time.sleep(0.2)
            print('Liked This Post')
            time.sleep(0.5)
            close_this_post = driver.find_element_by_xpath(close_post_xpath).click()
            print('Closing this Post')
        except:
            print('Error Liking Post at tag'+tags[i])



def Liking_2_Posts_Per_Tag():
    for i in range (0,len(tags)):
        driver.get(url+'/explore/tags/'+tags[i])
        time.sleep(3)
        print('clicking '+url+'/explore/tags/'+tags[i])
        try:
            first_post_open = driver.find_element_by_xpath(first_post_tag_xpath).click()
            print('First Post Click')
            time.sleep(1)
            print('Liking Post')
            like_this_post = driver.find_element_by_xpath(like_post_xpath).click()
            time.sleep(0.2)
            print('Liked This Post')
            time.sleep(0.5)
            close_this_post = driver.find_element_by_xpath(close_post_xpath).click()
            print('Closing this Post')
        except:
            print('Error Liking Post at tag'+tags[i])
        try:
            second_post_open = driver.find_element_by_xpath(second_post_tag_xpath).click()
            print('Second Post Click')
            time.sleep(1)
            print('Liking Post')
            like_this_post = driver.find_element_by_xpath(like_post_xpath).click()
            time.sleep(0.2)
            print('Liked This Post')
            time.sleep(0.5)
            close_this_post = driver.find_element_by_xpath(close_post_xpath).click()
            print('Closing this Post')
        except:
            print('Error Liking Post at tag'+tags[i])

def Generate_Dynamic_Xpaths():
    for i in range (0,6):
        dynamic_link_to_post = '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div['+repr(i+1)+']'
        dynamic_xpaths.insert(0,dynamic_link_to_post)
    print("Generating Dynamic Xpaths")
    print(dynamic_xpaths)


def Dynamic_Likes():
    Generate_Dynamic_Xpaths()
    print("Xpaths Generated")
    print(dynamic_xpaths)
    for i in range (0,len(tags)):
        driver.get(url+'/explore/tags/'+tags[i])
        time.sleep(3)
        try:
            print('Link '+ url+'/explore/tags/'+tags[i])
            for i in range(0,len(dynamic_xpaths)):
                try:
                    open_story = driver.find_element_by_xpath(dynamic_xpaths[i+3]).click()
                    print('Success! - Opening the Story '+repr(i+3))
                    time.sleep(2)
                    like_story = driver.find_element_by_xpath(like_post_xpath).click()
                    print('Liked for Sure!')
                    close_story = driver.find_element_by_xpath(close_post_xpath).click()
                    print('Successfully Closed Story')
                    time.sleep(2)
                except:
                    print("error clicking this story")

        except:
            print('error liking dynamic generated likes')      


def Visit_Recent_Stories_People_I_Follow_Directly():
    for i in range (0,len(collect_ids)):
        driver.get(url+'/stories/'+collect_ids[i])
        time.sleep(1)
        print("playing video")
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/button').click()
        print("success")
        time.sleep(2)
        Jump_Stories_2()


def Jump_Stories_2():
    count_stories_in_profile = driver.find_elements_by_class_name('_7zQEa')
    print('This profile has: ' +repr(len(count_stories_in_profile)))
    for i in range (0,len(count_stories_in_profile)):
        try:
            print("playing video")
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/button').click()
            print("success")
            time.sleep(0.2)
            driver.find_element_by_class_name(next_story_btn_class).click()
            time.sleep(0.2)
        except:
            print("Go to Next")
            try:
                print(collect_ids)
                print(url+'/stories/'+collect_ids[i+1])
                driver.get(url+'/stories/'+collect_ids[i+1])
                print("playing video")
                driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/button').click()
                print("success")
                time.sleep(0.2)
                driver.find_element_by_class_name(next_story_btn_class).click()
                time.sleep(0.2)
            except:
                print("ERROR - Out of Range?")
                print("ERROR ####### ERROR ##### QUITTING DRIVER ####")
                driver.quit()


def Visit_Recent_Stories_People_I_Follow_2():
    url = 'https://www.instagram.com'
    for i in range (0,len(collect_ids)):
        driver.get(url+'/stories/'+collect_ids[i])
        time.sleep(1)
        print(url+'/stories/'+collect_ids[i])
        #driver.find_element_by_class_name(profile_story_btn_class).click()
        time.sleep(2)
        Unfreeze_and_Jump_Stories()

def Unfreeze_and_Jump_Stories():
    count_stories_in_profile = driver.find_elements_by_class_name('_7zQEa')
    print('This profile has: ' +repr(len(count_stories_in_profile)))
    for i in range (0,len(count_stories_in_profile)):
        try:
            time.sleep(0.2)
            print("Unfreezing")
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/section/div[2]/div[1]/div/div/button').click()
            print("Playing")
            time.sleep(0.5)
            print("Click Next Story")
            driver.find_element_by_class_name(next_story_btn_class).click()
            print("Clicked")
            time.sleep(0.2)
        except:
            print("Go to Next")
        try:
            print(collect_ids)
            print(url+'/stories/'+collect_ids[i+1])
            driver.get(url+'/stories/'+collect_ids[i+1])
        except:
            print("ERROR - Out of Range?")
            print("ERROR ####### ERROR ##### QUITTING DRIVER ####")
            driver.quit()


def Generate_Tags_From_Txt_File_2():
    file1 = open(r'./Tags/tags.txt', 'r')
    file2 = open(r'./Tags/tags_2.txt', 'r+')
    file_log = open(r'./Tags/tags_already_used.txt', 'r+') 
    count = 0
  
    for line in file1: 
        count += 1
        tags.append(line.strip())
        tags_log.append(line.strip())
        file_log.write(line.strip()+"\n")
        print("Line{}: {}".format(count, line.strip()))
    for line in file2: 
        count += 1
        tags_1.append(line.strip())
        tags_log.append(line.strip())
        file_log.write(line.strip()+"\n")
        print("Line{}: {}".format(count, line.strip()))
    print(tags_log)
    # Closing files 
    file1.close()
    file2.close()
    file_log.close()

def Liking_6_Posts_Per_Tag():
    url = 'https:www.instagram.com'
    print("Starting Function")
    for i in range (0,3):
        time.sleep(1)
        print('in '+repr(i))
    Generate_Tags_From_Txt_File_2()
    print(tags)
    print("total of tags " +repr(len(tags)))

    for i in range (0,len(tags)):
        driver.get(url+'/explore/tags/'+tags[i])
        time.sleep(3)
        print('clicking '+url+'/explore/tags/'+tags[i])
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        try:
            for i in range(0,6):
                first_post_open = driver.find_element_by_xpath(xpaths[i]).click()
                print('Post '+repr(i)+' Click')
                #print(first_post_open)
                time.sleep(1)
                print('Liking Post')
                like_this_post = driver.find_element_by_xpath(like_post_xpath).click()
                time.sleep(0.2)
                print('Liked This Post')
                time.sleep(0.5)
                close_this_post = driver.find_element_by_xpath(close_post_xpath).click()
                print('Closing this Post')
        except:
            print("Failed at "+xpaths[i])
            print('Error Liking 6 posts at tag '+tags[i])
    for i in range (0,len(xpaths)):
        print(xpaths[i])