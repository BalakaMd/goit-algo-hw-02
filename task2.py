from collections import deque


def is_palindrome(input_str):
    final_string = input_str.lower().replace(" ", "")

    char_deque = deque(final_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))
