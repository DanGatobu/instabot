import pymongo
from pymongo import MongoClient

from functions import follow,unfollow,login,postpicture
import os


client=MongoClient()
db=client['pyinsta']



def final_follow(driver,main_username):
    #get follow accounts related to main username
    password=db['growaccounts'].find_one({'main_username':main_username})
    password=password['password']
    login(driver,main_username,password)
    follow_profile=db['followaccounts'].find({'main_username':main_username})
    limit=db['followlimit'].find_one({'main_username':main_username})['limit']
    len_fp=len(list(follow_profile))
    if len_fp==0:
        print('No follow accounts found')
    else:
        followcounter=db['followcounter'].find_one({'main_username':main_username})
        count_num=followcounter['count']
        if count_num>=len_fp:
            #reset count in db
            db['followcounter'].update_one({'main_username':main_username},{'$set':{'count':0}})
            count_num=0
        
        
        for k,i in enumerate(follow_profile):
            if k==count_num:
                profile=i['username']
                follow(driver,profile,int(limit))
    
def final_unfollow(driver,username):
    password=db['growaccounts'].find_one({'main_username':username})
    password=password['password']
    limit=db['unfollowlimit'].find_one({'main_username':username})['limit']
    login(driver,username,password)
    unfollow(driver,int(limit),username)
    
def final_postpicture(driver,username):
    password=db['growaccounts'].find_one({'main_username':username})
    password=password['password']
    login(driver,username,password)
    sent_imagelinks=db['imagetracker'].find({'main_username':username})
    image_directory = r"{}".format(db['imagefolder'].find_one({'main_username':username})['foldername'])
    caption=list(db['captions'].find({'main_username':username})['caption'])
    
    if len(caption)==0:
        caption=['Amazing','Wow']

    # open image directory and loop through images
    
    images=os.listdir(image_directory)
    for image in images:
        if image not in list(sent_imagelinks):
            path=os.path.join(image_directory,image)
            postpicture(driver,path,caption)
            db['imagetracker'].insert_one({'main_username':username,'imagelink':image})
            break
    
    
    
def all_actions(driver,main_username):
    password=db['growaccounts'].find_one({'main_username':main_username})
    password=password['password']
    login(driver,main_username,password)
    follow_profile=db['followaccounts'].find({'main_username':main_username})
    limit=db['followlimit'].find_one({'main_username':main_username})['limit']
    len_fp=len(list(follow_profile))
    if len_fp==0:
        print('No follow accounts found')
    else:
        followcounter=db['followcounter'].find_one({'main_username':main_username})
        count_num=followcounter['count']
        if count_num>=len_fp:
            #reset count in db
            db['followcounter'].update_one({'main_username':main_username},{'$set':{'count':0}})
            count_num=0
        
        
        for k,i in enumerate(follow_profile):
            if k==count_num:
                profile=i['username']
                follow(driver,profile,int(limit))
                
    uflimit=db['unfollowlimit'].find_one({'main_username':main_username})['limit']
    unfollow(driver,int(uflimit),main_username)
    sent_imagelinks=db['imagetracker'].find({'main_username':main_username})
    image_directory = r"{}".format(db['imagefolder'].find_one({'main_username':main_username})['foldername'])
    caption=list(db['captions'].find({'main_username':main_username})['caption'])
    
    if len(caption)==0:
        caption=['Amazing','Wow']

    # open image directory and loop through images
    
    images=os.listdir(image_directory)
    for image in images:
        if image not in list(sent_imagelinks):
            path=os.path.join(image_directory,image)
            postpicture(driver,path,caption)
            db['imagetracker'].insert_one({'main_username':main_username,'imagelink':image})
            break
    
                
    
    
    
