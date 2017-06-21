# countdown.py
#
# A simple generator function

# def countdown(n):
#     print('Counting down from', n)
#     while n > 0:
#         yield n
#         n -= 1
#     print('Done counting down')
#
# # Example use
# if __name__ == '__main__':
#     for i in countdown(10):
#         print(i)

# grep.py
#
# A very simple coroutine

def grep(pattern):
    print('Counting down from', pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line),

# Example use
if __name__ == '__main__':
    g = grep("python")
    g.next()
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")