from pp_17_decode_a_web_page import nyt_titles

f = open("nyt_titles.txt","w+")

for element in nyt_titles:
    f.write(element.text + "\n")

f.close()
print(nyt_titles)
