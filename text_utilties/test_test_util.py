from text_util import TextUtil

tutil = TextUtil()

def test_word_count():
    assert tutil.count_words("Hello World") == 2

def test_unique_words():
    assert tutil.unique_words("Hello World Hello World Bye Bye") == "Hello World Bye"

def test_rev_string():
    assert tutil.rev_string("Hello World") == "dlroW olleH"

def test_edge_word_count():
    assert tutil.count_words("$ @ @") == 3
    assert tutil.count_words("hello") == 1

def test_edge_unique_words():
    assert tutil.unique_words("hello") == "hello"
    assert tutil.unique_words("$$ 2@@ 3jfd#") == "$$ 2@@ 3jfd#"

def test_edge_rev_string():
    assert tutil.rev_string("hello world") == "dlrow olleh"