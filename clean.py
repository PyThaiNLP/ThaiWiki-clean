def clean_text(text):
    return text.strip().replace('()','').replace('( )','').replace('(; ;)','').replace('(; ; )','').replace('(; )','').replace('(, )','')

with open('wiki_20210620.txt', 'r', encoding='utf-8-sig') as f:
    data = clean_text(f.read())

with open('wiki_20210620_clean.txt', 'w', encoding='utf-8') as f:
    f.write(data)