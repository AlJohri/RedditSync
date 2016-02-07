from redditblogger import get_google_service

def create_post(blog_id, title, text="", url="", image_url=""):

    image_html = "<img style='width: 100%; height: auto;' src='{image_url}'></img><br/>".format(image_url=image_url) if image_url else ""
    text_html = "<p>" + text + "</p>" + "<br/>" if text else ""
    url_html = "<a href='{url}'>Check it out!</a>".format(url=url) if url else ""
    content = image_html + text_html + url_html

    body = {
        "blog": {
            "id": blog_id
        },
        "kind": "blogger#post",
        "author": {
            "id": "self"
        },
        "title": title,
        "content": content
    }

    service = get_google_service()
    request = service.posts().insert(blogId=blog_id, body=body, isDraft=False, fetchImages=True, fetchBody=True)
    response = request.execute()

if __name__ == "__main__":
    create_post(
        blog_id=8891791559553249304,
        title="This is a test post",
        text="blahblahblah",
        url="http://www.google.com",
        image_url="http://ichef.bbci.co.uk/news/976/media/images/83351000/jpg/_83351965_explorer273lincolnshirewoldssouthpicturebynicholassilkstone.jpg"
    )
