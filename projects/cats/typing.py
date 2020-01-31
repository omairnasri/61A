"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # store valid paragraphs
    valid_ps = [paragraphs[i] for i in range(len(paragraphs)) if select(paragraphs[i])]
    return '' if k >= len(valid_ps) else valid_ps[k]

def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def is_topic_in_p(paragraph):
        """
        PARAGRAPH - string
        P_ARR - list of words in PARAGRAPH (string)
        """
        # Convert paragraph to string --> clean words/elements
        p_arr = split(paragraph)
        p_arr = [lower(i) for i in p_arr]
        p_arr = [remove_punctuation(i) for i in p_arr]

        # List of whether each word from PARAGRAPH is a topic
        res = [i in topic for i in p_arr]
        return True in res
    return is_topic_in_p


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    """
    reference_words ['Cute', 'Dog.']
    typed_words ['Cute']
    """
    typed_words = split(typed)
    reference_words = split(reference)
    total = correct = 0.0
    min_len = min(len(reference_words), len(typed_words))
    if len(typed_words) == 0:
        return 0.0
    if len(typed_words) > len(reference_words): 
        total = len(typed_words) - len(reference_words)
    i = 0
    while i < min_len:
        if typed_words[i] == reference_words[i]:
            correct += 1
        i += 1
    total += min_len
    return correct / total * 100

def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return (len(typed) / 5) / (elapsed / 60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        differences = [diff_function(user_word, v, limit) for v in valid_words]
        difference = min(differences)
        index = differences.index(difference)
        return user_word if difference > limit else valid_words[index] 
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def inner(start, goal, differences):
        if len(start) == 0 or len(goal) == 0:
            return differences
        if differences > limit:
            return limit + 1
        if start[0] != goal[0]: 
            return inner(start[1:], goal[1:], differences + 1)
        else:
            return inner(start[1:], goal[1:], differences)
    differences = inner(start, goal, 0)
    return differences if differences == limit + 1 else differences + abs(len(start) - len(goal))
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    if limit < 0:
        return 1
    if start == goal: 
        return 0
    if len(start) == 0 or len(goal) == 0:
        return abs(len(goal) - len(start))
    else:
        add_diff = edit_diff(start, goal[1:], limit - 1)
        remove_diff = edit_diff(start[1:], goal, limit - 1)
        substitute_diff = edit_diff(start[1:], goal[1:], limit - 1)
        if start[0] == goal[0]:
            return edit_diff(start[1:], goal[1:], limit)
        else:
            return 1 + min(add_diff, remove_diff, substitute_diff)

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'

###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    i = 0
    while i < min(len(typed), len(prompt)):
        if typed[i] != prompt[i]:
            break
        else:
            i += 1
    progress = i / len(prompt)
    send({'id': id, 'progress': progress})
    return progress

def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0

    def time_spent_typing_word(i, player): 
        """ Args: word I, player WORD_TIME list Return: Time for player to type word i """
        return elapsed_time(player[i]) - elapsed_time(player[i - 1])

    def fastest_time_for_word(i): 
        """ Get fastest time for word I between all players | Return minimum time for word I"""
        times_for_word_i = []
        for j in word_times:
            times_for_word_i.append(elapsed_time(j[i]) - elapsed_time(j[i-1]))
        return min(times_for_word_i)

    solution, word_index, player = [[] for i in range(n_players)], 1, 0
    while word_index <= n_words:
        player = 0
        fastest = fastest_time_for_word(word_index) # Fastest time for word 1 -> n_words
        while player < n_players:
            time_spent_word_i = time_spent_typing_word(word_index, word_times[player])
            if time_spent_word_i <= fastest + margin:
                solution[player].append(word(word_times[player][word_index]))
            else:
                pass
            player += 1
        word_index += 1
    return solution


def word_time(word, elapsed_time):
    """A data abstraction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]

enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)