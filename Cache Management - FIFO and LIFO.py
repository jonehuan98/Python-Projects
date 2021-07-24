# Jone Huan Chong , 201533109

cacheSize = 8 #define the cache maximum size

def getRequest(): #function to get user input for requests 
    global requests
    requests = [] #intialises an empty list of requests for each loop
    while True: #try and except used to repeatedly obtain int values only
        try:
            requestInput = int(input("Enter your request as an integer, and enter 0 to finish the request: "))
            if requestInput == 0 : 
                break #while loop breaks when 0 is entered
            else:
                requests.append(requestInput)
        except Exception as e:
            print(e)

    print("Requests: ",requests)
    selectMethod() #calls the method selection function

def selectMethod(): #function to get user input for method selection
    method = input("Press '1' for fifo, '2' for lfu, or 'Q' to quit the program: ")
    if method == "Q": #quits program
        print("Program quit")
        quit
    elif method == "1": #calls fifo function
        fifo()
    elif method == "2": #calls lfu function
        lfu() 
    else:
        print("Enter a valid selection") 
        selectMethod() #runs the function again if user input is not valid

def fifo():
    global cache
    cache = [] #intialises an empty cache list, and clears the cache if a method of fifo or lfu is used previously
    for i in requests:
        if i in cache: #if a page already exists, hit is printed and the cache is not changed, moves on to next request
            print(i,": hit")
        else:
            if cacheSize == len(cache): #if cache is at capacity, the first page in the cache is removed
                del cache[0]
            print(i,": miss") 
            cache.append(i) #if cache is not at capacity, the page is added into the cache
    print("Cache: ", cache)
    cache = [] #clear cache
    getRequest() #goes to main menu
    
        
def lfu():
    global cache
    cache = {} #intialises an empty cache dictionary, and clears the cache if a method of fifo or lfu is used previously

    for i in requests: #iterates through each request
        if i in cache:
            cache[i] += 1 #iterates through cache and updates the frequency of the page/key already present
            print(i,": hit")
        else:
            if cacheSize == len(cache): #when cache size is at its limit
                lowestFreq = [k for k, v in cache.items() if v == min(cache.values())] #creates a list of all pages with the lowest frequency of hits
                smallestInt = min(lowestFreq) #define the lowest integer page among the lowest hits
                del cache[smallestInt] #remove page from dictionary

            cache[i] = 1 #inserts a new page with the default frequency of 1
            print(i, ": miss")

    print("Cache: ",list(cache.keys())) #prints the keys of the cache dictionary as a list
    cache = {} #clear cache
    getRequest() #goes to main menu
                
getRequest()
