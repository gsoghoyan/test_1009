def isurl(my_url):

    if my_url[0:4] == "http":
        print(my_url, " is valid URL")
    else: 
        print(my_url, " is not valid URL")

isurl("httgfd")
