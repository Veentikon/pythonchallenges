"""
This is the first working solution for python challenge no. 4 on http://www.pythonchallenge.com/
The following code solves the problem of looping through a set of urls (400 in total).
Given url, the modification for the url can be found on the web page opened by previous url.
That modification is a set of integer, the next url is created by adding extracted set of integers to the end
of the original url, somewhere along those 400 iterations there should be a hint for the next challenge.

"""


from selenium import webdriver

# initiate web driver
wb = webdriver.Chrome()

# the first link to start following the chain
link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

# open the first link
wb.get(link + '12345')


# loop through the following links (loop through the chain)
count = 1
while count < 400:
    nxt = wb.find_element_by_tag_name('body').text
    # values printed can be checked to see the anomaly/next url/hint
    print(nxt)

    # isolate integer values from string 'next'
    filtered = filter(str.isdigit, nxt)
    # put all the integers together by iterating over filtered
    nxt = ''
    for i in filtered:
        nxt += i

    # open the next url by adding extracted from page number to link
    wb.get(link + nxt)
    count += 1

# close the page in the end
wb.close()

# the following improvement to the code could be made:
#   once irregular\hint is reached, break the loop and print what was found
