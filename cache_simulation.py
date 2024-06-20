
#Creating global empty lists
cache = []
requests = []

#Defining function for FIFO
def fifo():
    for integer in requests:
        if integer in cache:
            print("Hit")
        else:
            print("Miss")
            #Remove oldest integer if cache is full
            if len(cache) == 8:
                cache.pop(0)
            cache.append(integer)

    print(cache)
    cache.clear()
    requests.clear()

#Defining function for LFU
def lfu():
    #Dict to store page frequency
    page_freq = {}
    def freq_of_page(page):
        return page_freq[page], page
    for page in requests:
        page_freq[page] = page_freq.get(page, 0) + 1
        if page in cache:
            print("Hit")
        else:
            print("Miss")
            #Check if cache is full
            if len(cache) == 8:
                #Page with least frequency
                removed_int = min(cache, key = freq_of_page)
                cache.remove(removed_int)
            cache.append(page)

    print(cache)
    cache.clear()
    requests.clear()


def program():
    #Display menu options to the user
    print("Select an option: ")
    print("Select 1 for FIFO")
    print("Select 2 for LFU")
    print("Select Q to quit")

    #Get input from user
    choice = input()
    #Match case for user's choice
    match choice:
        case '1':
            #Call the fifo() function
            fifo() 
        case '2':
            #Call the lfu() function
            lfu()
        case "Q":
            #Exit the loop if the user chooses to quit
            quit()
        case _:
            print("Please choose again, incorrect choice.")


while True:
    # Request page input from user
    integer = int(input())
    if integer == 0:
        program()
    else:
        requests.append(integer)
