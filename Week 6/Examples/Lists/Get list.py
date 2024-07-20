"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
def user_input():
    lst = []
    user_value = input("Enter a value: ")
    while user_value != "":
        lst.append(user_value)
        user_value = input("Enter a value: ")
    return lst  
def print_list(lst):
    print ("Here's the list:", lst)

def main():
    lst = user_input()
    print_list(lst)
    
 


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
