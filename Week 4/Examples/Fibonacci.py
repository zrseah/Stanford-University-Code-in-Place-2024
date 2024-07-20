"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""
max_value = 10000
def main():
    current_num = 0
    next_num = 1
    while current_num <= 10000:
        print(current_num)
        num_after_next = current_num + next_num
        current_num = next_num
        next_num = num_after_next

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()