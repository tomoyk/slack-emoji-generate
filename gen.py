import random
from urllib import request, parse


def get_emoji(text: str, text_color: str):
    req_url = 'https://emoji-gen.ninja/emoji?text={}&font=rounded-x-mplus-1p-black&color={}&back_color=ffffffff&size_fixed=false&align=center&stretch=true&locale=ja'.format(
        parse.quote(text),
        text_color)
    print(req_url)
    req_method = 'GET'
    req_header = {
        'Content-Type': 'application/json',
    }
    req = request.Request(req_url, method=req_method, headers=req_header)
    try:
        res_body = request.urlopen(req).read()
        with open('assets/' + text + ".png", mode="wb") as f:
            f.write(res_body)
            print("保存しました")
    except Exception as e:
        print(e)


def get_random_color():
    return ''.join([format(random.randrange(10), 'x') for _ in range(6)]) + 'ff'


def main():
    with open('list') as f:
        file_content = f.readlines()
    for fc in file_content:
        get_emoji(fc.strip(), get_random_color())


if __name__ == '__main__':
    main()
