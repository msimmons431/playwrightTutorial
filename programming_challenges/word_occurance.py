import re

sentance = (
    "This is a bogus sentence, that will be used in this bogus challenge. this used"
)
wordpat = re.compile(r"\w+")
results = re.findall(wordpat, sentance)
# print(results)
wordcount_dict = {}
for word in results:
    wordCount = results.count(word)
    wordcount_dict[word] = wordCount
print(wordcount_dict)
