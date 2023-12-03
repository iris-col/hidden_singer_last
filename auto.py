import sys

def wrap_in_paragraphs(text):
    paragraphs = [f'<p>{line}</p>' for line in text.split('\n')]
    return '\n'.join(paragraphs)

lst = ["Stay With Me", "Say Goodbye", "새사랑","행복해","겨울비","함부로 다정하게","이 노래 (This song)","너를 보는게 지친 하루에","처음처럼","사랑이라 쓰고 이별이라 읽어"]

top = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <style>
            body{
                -ms-overflow-style: none;
            }

            ::-webkit-scrollbar {
                display: none;
            }
            p {
                color: #666;
                font-size: 15px;
                /* padding-top: 30px; */
                text-align: left;
            }
            hr {
                color: #333;
                border: 1px solid #333;
            }
            h3 {
                color: #333;
                padding:15px 0;
                margin:0;
                text-align: center;
            }
        </style>
    </head>
    <body>
"""
bottom = """
    </body>
</html>
"""
for i in lst:
    # 예제 텍스트
    input_text = text = sys.stdin.read()

    # 각 줄을 <p> 태그로 감싸기
    output_html = wrap_in_paragraphs(input_text)

    file_path = f"./가사/송하예/{i}.html"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(top)
        file.write(f"<h3>{i}</h3>\n")
        file.write("<hr>\n")
        file.write(output_html)
        file.write(bottom)

    print(f"HTML file created at: {file_path}")
