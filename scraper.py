import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

def get_title():
    response = requests.get("https://crawlingstudy-dd3c9.web.app/01/")
    soup = bs(response.text, "lxml")
    title_tag = soup.select_one("title")
    return title_tag.text
    if __name__ == "__main__":
        title = get_title()

print(f"페이지 제목: {title}")

def get_table_data():
    soup = bs(requests.get(URL).text, "lxml")
    table = soup.select_one("table")
    # 헤더(th) 추출
    headers = [th.text for th in table.select("th")]
    # 데이터(tbody tr) 추출
    data = []
    for row in table.select("tbody tr"):
        tds = row.select("td")
        data.append({headers[0]: tds[0].text})
        return headers, data


def save_to_file(title, paragraphs, headers, data):
    """추출한 모든 데이터를 파일로 저장"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("crawling_result.txt", "w", encoding="utf-8") as f:
        f.write(f"크롤링 결과 - {now}\\n")
        f.write(f"페이지 제목: {title}\\n")
        f.write(f"p태그 개수: {len(paragraphs)}개\\n")
        for row in data:
            f.write(f"이름: {row['이름']}, 나이: {row['나이']}\\n")
print("✅ crawling_result.txt 저장 완료!")
            
def get_paragraphs():
    """모든 p태그 텍스트 추출"""
    response = requests.get("https://crawlingstudy-dd3c9.web.app/01/")
    soup = bs(response.text, "lxml")
    # select: 모든 p태그를 리스트로 반환
    p_tags = soup.select("p")
    result = []
    for p in p_tags:
        result.append(p.text.strip())
        return result