import json
import time
import argparse
from selenium import webdriver

doc_path = "question.txt"
doc_path_trans = "question_trans.txt"
driver_path = './chromedriver.exe'
url='https://translate.google.co.kr/?hl=ko'
chromedriver = driver_path
driver = webdriver.Chrome(chromedriver)
driver.get(url)
time.sleep(1)
with open(doc_path) as f:
    txt_data = f.readlines()
#문장들을 5000자 제한에 맞춰 sents에 저장함
sents = []
sent = ''
for i in range(len(txt_data)):
    sent += txt_data[i]
    if len(sent) >= 4500: #5,000자 제한
        #print(sent)
        sents.append(sent)
        sent = ''
    #time.sleep(0.5)
sents.append(sent)
i = 0
for sent in sents:
    i += 1
    text_box = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea')
    text_box.send_keys(sent)
    time.sleep(8)
    result = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div').text
    driver.get(url)
    time.sleep(1)
    print(str(i) + '/212 완료')
    with open(doc_path_trans, 'a') as f:
        f.write(result+'\n')
    f.close()
driver.quit()

#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--doc_path', type=str, default='./v2_Questions_Train_mscoco/v2_OpenEnded_mscoco_train2014_questions.json', help='English document path(JSON)')
#     parser.add_argument('--out_path', type=str, default='./', help='output document path')
#     parser.add_argument('--driver_path', type=str, default='./chromedriver.exe', help='Chrome driver path')
#     parser.add_argument('--url', type=str, default='https://translate.google.co.kr/?hl=ko', help='Crawling URL')
#     opt = parser.parse_args()
#     translate(opt.doc_path, opt.out_path, opt.driver_path, opt.url)
#
#
