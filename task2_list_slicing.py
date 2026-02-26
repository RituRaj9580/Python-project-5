def main():
    # 1. Create a list of numbers from 1 to 10
    original_list = list(range(1, 11))

    # 2. Extract the first five elements from the list
    extracted_elements = original_list[:5]

    # 3. Reverse these extracted elements
    # [::-1] is the Pythonic way to slice a list in reverse
    reversed_elements = extracted_elements[::-1]

    # 4. Print the lists as per the expected output
    print(f"Original list: {original_list}")
    print(f"Extracted first five elements: {extracted_elements}")
    print(f"Reversed extracted elements: {reversed_elements}")

if __name__ == "__main__":
    main()
