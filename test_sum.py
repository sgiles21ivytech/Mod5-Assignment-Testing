def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
    #assert sum([1, 1, 1]) == 6, "Should be 6" # returns AssertionError: Should be 6

if __name__ == "__main__":
    test_sum()
    print("Everything passed")