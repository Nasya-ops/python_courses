# Math operations
a = 29
b = 40

print(
    f"\nAddition: {a + b}\n",
    f"Subtraction {a - b}:",
    f"Multiplication: {a * b}\n",
    f"Exponantion: {a ** 2}\n",
    f"Division: {a / b}\n",
    f"Integer division: {a // b}\n",
    f"\nModule division {a % b}\n",
    f"Move_left: {b << 2}\n",
    f"Move right: {a >> 1}\n",
    f"&: {a & b}\n",
    f"|: {a | b}\n",
    f"Except OR: {a ^ b}\n",
    f"NOT(~): {~a}\n",
    f"Comparison: {a < b}, {a > b}, {a <= b}\n",
    f"EqualObjects:{a == b}, {a != b}\n",
    f"not: {not b}\n",
    f"and: {a and b}\n",
    f"or: {a or b}\n",
)
# Converting the string with the name to the correct format
s = "вишневецька Rнастасія DdD"
numR = s.find("R")
d = s.index("D")
myName = s[:d].replace(s[numR], "A").title()
print(myName)
# String methods using
str = "нас"
S = "s\np\ta\x00m"
print(S)
block = "'Big 'text' block'"
print(block)
S1 = b"spam"
print(
    "a{0} parrot".format(S1),
    len(S1),
    s.encode("latin-1", "ignore"),
    "ишн" in s,
    map(ord, s),
    s.find(str),
    s.split(" "),
    s.isalpha(),
    s.isalnum(),
    s.islower(),
    "\n",
    s.isspace(),
    s.startswith(str),
    s.join("^^"),
)
# for i in s:
# print(i),print([c*2 for c in s])
full_name = " вишневецька Rнастасія DdD"
print(f"{full_name} -> {full_name.strip().lower().replace('r', 'А').replace('ddd', 'Володимирівна').title()}",)
