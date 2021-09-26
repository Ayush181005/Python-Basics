userInput = input(">")
a = userInput.split()
emojis = {
    ':)': '😀',
    ':(': '☹ 🙁 😞 😟',
}
output = ''

for words in a:
    output += emojis.get(words, words) + ' '
print(output)