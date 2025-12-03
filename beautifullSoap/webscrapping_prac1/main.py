from bs4 import BeautifulSoup
with open("index.html", "r") as html_file:
    content=html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    # course_tags = soup.find_all('h2')
    # for course in course_tags:
    #     print(course.text)
    article_tags = soup.find_all('article')
    for article in article_tags:
        name = article.h2.text
        price = article.a.text
        print(name)
        print(price)