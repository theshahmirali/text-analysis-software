def preprocess(filename):
    """
    Algorithm:
    Open the file and then convert the lines to strings, start a for loop to check the characters are between "a" and "z" so that punctuations are eliminated and the word is concatenated to mystr and after every character either a space, newline or tab
    is checked and if the the condition meets and a word is formed then the word is checked for if it is in the list of auxiliary verbs and then the word is appended to the final list and returned and then the string is again emptied and re-initialised
    for the new word.

    :param filename: the file that is passed for the function
    precondition: a text file
    post-condition: a list of word strings
    Time Complexity: O(NM) in worst case where the N are the words and M is the maximum length of the list.
    Space Complexity: O(NM)
    :return: a list of word strings
    """
    with open(filename, 'r') as myFile:  # opening the file using a "with" command so the file gets automatically closed
        test = myFile.read()  # reading the file
        aux_words = ["a", "an", "the", "am", "is", "are", "was", "were", "has", "have", "had", "been", "will", "shall",
                     "may", "can", "would", "should", "might", "could"]  # initialised a list of auxiliary verbs

    mych = ''  # empty string
    for line in test:  # (O(N))
        mych += line  # concatenating the lines of the file

    mystr = ''  # initialising an empty string
    finallist = []

    for i in range(len(mych)):  # looping through the mych string #(O(NM))
        if 97 <= ord(mych[i]) <= 122:  # check only a to z characters using ascii code
            mystr += mych[i]  # concatenating those characters in to mystr
        if ord(mych[i]) == 32 or ord(mych[i]) == 10 or ord(
                mych[i]) == 9:  # check for space, newline, tab and a full stop using ascii code
            if mystr not in aux_words:  # searching if my str not in aux verbs  (O(1)) because the aux_words list is constant
                finallist.append(mystr)  # appending into finallist
            mystr = ''  # emptying the mystr again for the next word to be appended
    if len(mystr) != 0:               # to append the last word in the list if my str is not empty
        finallist.append(mystr)
    return finallist


def wordSort(arraywords):
    """
    Algorithm:
    At first the length of the longest word is checked in the array and returned. A frequency_table is created to store the word according to the current index which is achieved by getting the ascii of the current character, then the remaining words
    with length lower are placed into the list of ignore table and then the loop goes on until all the words are added to the frequency table and the ignore table. Then the main array is re-initialised to array of type string and then the words
    in the ignore table are appended back to the main array. Then the word in the frequency table is appended to the main array. This goes on until the bucket stores all the words according to the index of the character which goes on a decrement level
    from the length of the longest word to 0, and then it returns a final list of sorted words.

    :param arraywords: a list of words
    precondition: a list of unsorted array
    post-condition: a list of sorted array
    Time Complexity: Worst Case = O(NM), where N is number of strings in input stringArray, and M is the maximum length of string.
    Space Complexity: O(NM) since O(NM), where N are the words and M is the longest word in the file. A frequency table of size 26 is created for the alphabets a to z using ascii.
    :return: a list of sorted array
    """

    def maxlength(arraywords):  # function to find the length of the word for the maximum array
        length = 0
        for word in arraywords:  # for the word in the array if the length is greater it makes length of that word as the longest length.
            if len(word) > length:
                length = len(word)
        return length

    freq_table = [[] for _ in range(26)]  # initialise frequency table which is list of lists
    ignore_table = []  # initialising an ignore table

    for number in range(maxlength(arraywords) - 1, -1,
                        -1):  # M start a decrementing loop from the rightmost index (O(M))
        for words in arraywords:  # (O(N))
            if len(words) > number:  # comparing the length of the word
                index = (ord(words[number]) - 97)  # using ascii for the current index character
                freq_table[index].append(words)  # append to the frequency table.
            else:
                ignore_table.append(words)  # append the remaining ignore words in the table

        arraywords = [""] * len(ignore_table)  # re-initialising array of type string

        for i in range(len(ignore_table)):  # lop through the ignore table (O(N))
            item = ignore_table.pop()
            arraywords[i] = item  # set the item to the main array index

        for bucket in freq_table:  # (O(N))
            for item in bucket:
                arraywords.append(item)  # append the word in the frequency table

        freq_table = [[] for _ in range(27)]  # re-initialise frequency table

    return arraywords


def wordCount(sortedlist):
    """
    Algorithm:
    The algorithm uses two pointers, the first pointer is at 0 and the second at 1. To append the last word as well, I used a check where if in the end both i and j pointers are the same because of decrementing j when it reaches the last word.
    Then it appends the last word and its count and appends to the main list and the function stops. In the normal loop when the pointer has not reached the last word, the pointer at i and j compares the word and if they are the same the word
    gets appended to the temp list and the count is 2, and the flag is false, else the words are not the same, then it checks if there is any word currently stored in the temp list, if yes then it appends it to the main list and then empties
    the temp list and since the words were not the same the i pointer becomes the j pointer and j pointer is incremented by one to the next value. Then the loop again begins and in the same order the entire count is found and returned.
    The function stops when the i and j pointers are the same value as I decrement j as mentioned above and the final word is appended with its count to the list.

    precondition: a list of sorted words
    post-condition: a list with two values, total number of words and a list of word count
    Time Complexity: O(NM), where N is number of strings in input stringArray, and M is the maximum length of string.
    Space Complexity: O(NM)
    :param sortedlist: a list of sorted words
    :return: a list with two values, total number of words and a list of word count


    """

    mainList = [] + [len(sortedlist)]
    tempList = []
    i = 0
    j = 1
    flag = True
    while j < len(sortedlist):

        if sortedlist[i] == sortedlist[j] and i == j:  # if the last word is the same
            tempList.append(sortedlist[i])  # then append to temp list
            tempList.append(1)  # and set count to 1
            mainList.append(tempList)  # append temp list to main list
            break
        if sortedlist[i] == sortedlist[j]:  # if the two words are the same
            if flag:
                tempList.append(sortedlist[i])  # append the word in temp list
                tempList.append(2)  # and add 2 as the occurrence of that word for the first time
                flag = False
            else:
                tempList[
                    1] += 1  # this increments the count for the word if it occurs more than twice while the flag is false
            j += 1  # increments j to the next word
        else:
            if len(tempList) != 0:  # this checks that when the two words are not equal and there is a word in temp list
                mainList.append(tempList)  # appends the current word and count in main list
                tempList = []  # re-initialises the temp list
                i = j  # makes the current j value as the new i because the word now is new
                j += 1  # and j points to the next word
                flag = True
            else:
                tempList.append(sortedlist[i])  # now the temp list is empty and the current word gets appended
                tempList.append(1)  # now the counter gets incremented
                i += 1
                j += 1
                mainList.append(tempList)  # appends the words to the main list
                tempList = []  # re-initialises the temp list to 0

        if j == len(sortedlist) and i < len(sortedlist):  # if the j pointer equals to the length of the sorted array
            j -= 1  # then decrement j pointer

    return mainList


if __name__ == "__main__":

    filename = preprocess("Writing.txt")

    if len(filename) == 0:  # condition for the empty file
        print("Unable to continue: \n 1. Writing.txt is empty or \n 2. There is no word remaining after preprocessing.")

    else:  # when the file is not empty execute this

        print("Words are preprocessed...")

        sortedWords = wordSort(filename)
        countSortedWords = wordCount(sortedWords)

        yes = "Y"
        no = "N"

        userInput = input("Do I need to display the remaining words: ")  # user input 1
        print()

        if userInput == yes:  # loop to print all the words unsorted
            for word in filename:
                print(word)

            print("The remaining words are sorted in alphabetical order")

            userInputTwo = input("Do you want to see: ")    # user input 2
            print()

            if userInputTwo == yes:     # if the user chooses yes then execute this else end the program

                for words in sortedWords:       # for loop to print the sorted words
                    print(words)

                print("The total number of words in the writing: " + str(len(filename)))    # printing the total number of words in the file

                print("The frequencies of each word: ")

                for freq in countSortedWords[1:]:              # loop to to print the frequencies of each word starting from index 1 to eliminate the count of the words
                    print("{} : {}".format(freq[0], freq[1]))  # changing the format according to the output required

            elif userInputTwo == no:                           # when the user inputs no then end the program
                print("End of Program")

        else:
            print("End of Program")
