# Final Exam Question 6
import re
def statistics(filename):
    '''
    A text file, stored in the working directory, consists of sentences.
    A sentence consists of words, possibly directly followed by a comma,
    except for the last word which is directly followed by a full stop.
    Words are separated by spaces.

    >>> statistics('text_file_1.txt')
    There are 2 sentence(s).
    The shortest sentence has 31 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 9 character(s).
    >>> statistics('text_file_2.txt')
    There are 4 sentence(s).
    The shortest sentence has 6 word(s).
    The longest sentence has 34 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    >>> statistics('text_file_3.txt')
    There are 1 sentence(s).
    The shortest sentence has 30 word(s).
    The longest sentence has 30 word(s).
    The shortest word has 1 character(s).
    The longest word has 12 character(s).
    '''
    
    nb_of_sentences = None
    length_of_shortest_word = None
    length_of_longest_word = None
    min_nb_of_words_in_sentences = None
    max_nb_of_words_in_sentences = None
    nb_of_words = []
    length_of_word = []
    with open(filename) as file:
        all = file.read().strip()
        sentences = re.split(r"[\.\?:;!]",all)
        nb_of_sentences = all.count('.')
        for sentence in sentences:
            # 对于第一个进行初始化
            words = re.findall(r"\w+",sentence)
            nb_of_words.append(len(words))
            for word in words:
                length_of_word.append(len(word))
        length_of_shortest_word = min(length_of_word)
        length_of_longest_word = max(length_of_word)
        min_nb_of_words_in_sentences = min(nb_of_words)
        max_nb_of_words_in_sentences = max(nb_of_words)
        # REPLACE pass ABOVE WITH YOUR CODE
    
    print('There are', nb_of_sentences, 'sentence(s).')
    print('The shortest sentence has', min_nb_of_words_in_sentences, 'word(s).')
    print('The longest sentence has', max_nb_of_words_in_sentences, 'word(s).')
    print('The shortest word has', length_of_shortest_word, 'character(s).')
    print('The longest word has', length_of_longest_word, 'character(s).')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

