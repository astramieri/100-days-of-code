def length(string):
    """Return the number of chars in a string.
    This string can be multi-line."""
    def inner_length(inner_string):
        pass

    return len(string)

"""
TO AVOID!
This is a
multi-line
comment 
"""

# DO THIS INSTEAD
# FROR MULTI-LINE
# COMMENTS
length = length("Docstring")

print("The length = " + str(length))