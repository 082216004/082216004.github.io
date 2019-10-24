s="TypeError: not enough arguments for format string"

print("a occurs %d times" % s.count("a"))

print("The first five characters are '%s'" % s[:5])

print("The next five character are '%s'" % s[5:10])

print("The thirteeth character is '%s'" % s[12])

print("The characters with odd index are '%s'"% s[1::2])

print("The last five characters are '%s'"% s[-5:])

print("String in uppercase: %s"% s.upper())