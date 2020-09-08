def isurl(my_url):

    if my_url[0:4] == "http":
        print(my_url, " is valid URL")
    elif my_url[0:5] == "https":
        print(my_url, " is valid URL")
    elif my_url[-4:] == ".com":
        print(my_url, "is valid and ends with .com")

    else: 
        print(my_url, " is not valid URL")

isurl("httpsgfd")
