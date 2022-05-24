import os


def make_text(message, id):
    word = message.text
    list_word = list(word)
    middle_char_index = round(len(list_word) / 2)
    num_chars = len(word)
    try:
        os.mkdir(f"users/{message.chat.id}")
    except FileExistsError:
        pass
    with open(f"users/{message.chat.id}/text1.txt", "w") as word_data:
        # 1 10times write word
        for _ in range(20):
            word_data.write(f"{word}\n")

        # 2 add spaces and deleting them before word 2 times
        for _ in range(2):
            list1 = list_word
            add_spaces(list1, word_data)
            delete_spaces(list1, word_data)

    with open(f"users/{message.chat.id}/text2.txt", "w") as word_data:
        # 3 move one character to the right
        list3 = list_word
        num = 1
        for _ in range(num_chars-1):
            for _ in range(2):
                list3.insert(-num, " ")
                word_data.write(f"{''.join(list3)}\n")
            num += 3

        # 4 delete spaces between chars
        num = 2
        for _ in range(num_chars-1):
            for _ in range(2):
                del list3[-num]
                list3.insert(0, " ")
                word_data.write(f"{''.join(list3)}\n")
            num += 1

        word_data.write(f"{''.join(list3)}\n")
        word_data.write(f"{''.join(list3)}\n")

        # 5 back to begin
        num = 0
        for _ in range(num_chars):
            for _ in range(2):
                del list3[0]
                list3.insert(-num_chars+num, " ")
                word_data.write(f"{''.join(list3)}\n")
            num += 1

        # 6 delete spaces between chars
        num = 1
        for _ in range(num_chars):
            try:
                for _ in range(2):
                    del list3[num]
                    word_data.write(f"{''.join(list3)}\n")
            except IndexError:
                break

            num += 1

    with open(f"users/{message.chat.id}/text3.txt", "w") as word_data:
        # 7 Middle letter dance
        list7 = list_word
        add_spaces_short(list7, word_data)
        index = -middle_char_index

        if list7[index] == " ":
            index -= 1

        num = 1
        for _ in range(10):
            list7.insert(index+1, " ")
            list7.insert(index-num, " ")
            del list7[0]
            num += 1
            word_data.write(f"{''.join(list7)}\n")

        index_middle = index-10
        if list7[index_middle] == " ":
            index_middle -= 1

        num = 0
        middle_char = list7[index_middle]
        for _ in range(3):
            list7[index_middle-num-1] = middle_char
            list7[index_middle-num] = " "
            num += 1
            word_data.write(f"{''.join(list7)}\n")

        for _ in range(6):
            list7[index_middle-num+1] = middle_char
            list7[index_middle-num] = " "
            num -= 1
            word_data.write(f"{''.join(list7)}\n")

        for _ in range(6):
            list7[index_middle-num-1] = middle_char
            list7[index_middle-num] = " "
            num += 1
            word_data.write(f"{''.join(list7)}\n")

        for _ in range(3):
            list7[index_middle-num+1] = middle_char
            list7[index_middle-num] = " "
            num -= 1
            word_data.write(f"{''.join(list7)}\n")

        # 8 delete spaces after dance
        num = 1
        for _ in range(10):
            del list7[index_middle + num]
            del list7[index_middle + num - 1]
            list7.insert(0, " ")
            num += 1
            word_data.write(f"{''.join(list7)}\n")
        delete_spaces(list7, word_data)

    # 9 move letters from start and back
    with open(f"users/{message.chat.id}/text4.txt", "w") as word_data:
        for _ in range(10):
            list7.insert(0, " ")
            word_data.write(f"{''.join(list7)}\n")

        start_index = 10

        for _ in range(len(list7)):
            index = start_index
            try:
                if list7[index] != " ":
                    for _ in range(10):
                        char = list7[index]
                        list7[index - 1] = char
                        list7[index] = " "
                        index -= 1
                        word_data.write(f"{''.join(list7)}\n")
            except IndexError:
                break
            start_index += 1

    # 10 first char to last
    with open(f"users/{message.chat.id}/text5.txt", "w") as word_data:
        word_data.write(f"{''.join(list7)}\n")
        word_data.write(f"{''.join(list7)}\n")

        list7 = list7[:-3]

        for _ in range(len(list7) * 3):
            list10 = list7
            list7.append(list10[0])
            del list7[0]
            word_data.write(f"{''.join(list7)}\n")

    # 11 adding spaces and splitting half
    with open(f"users/{message.chat.id}/text6.txt", "w") as word_data:
        add_spaces(list7, word_data)

        index = -middle_char_index
        for _ in range(10):
            list7.insert(index, " ")
            list7.insert(index, " ")
            del list7[0]
            word_data.write(f"{''.join(list7)}\n")

        for _ in range(10):
            del list7[index - 1]
            del list7[index - 1]
            list7.insert(0, " ")
            word_data.write(f"{''.join(list7)}\n")

        for _ in range(10):
            list7.insert(index, " ")
            list7.insert(index, " ")
            del list7[0]
            word_data.write(f"{''.join(list7)}\n")

        for _ in range(10):
            del list7[index - 1]
            del list7[index - 1]
            list7.insert(0, " ")
            word_data.write(f"{''.join(list7)}\n")

        for _ in range(20):
            del list7[0]
            word_data.write(f"{''.join(list7)}\n")

        for _ in range(20):
            word_data.write(f"{word}\n")


def add_spaces(list_word, word_txt):
    for _ in range(20):
        list_word.insert(0, " ")
        word_txt.write(f"{''.join(list_word)}\n")


def delete_spaces(list_word, word_txt):
    for _ in range(20):
        del list_word[0]
        word_txt.write(f"{''.join(list_word)}\n")


def add_spaces_short(list_word, word_txt):
    for _ in range(10):
        list_word.insert(0, " ")
        list_word.insert(0, " ")
        word_txt.write(f"{''.join(list_word)}\n")


def delete_spaces_short(list_word, word_txt):
    for _ in range(10):
        del list_word[0]
        del list_word[0]
        word_txt.write(f"{''.join(list_word)}\n")
