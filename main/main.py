import openai
from dotenv import load_dotenv
import os

# .env에서 apikey 가져오기
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# gpt 프롬프트 설정
prompt = "You are a very scary computer teacher"

messages = [{"role": "system", "content": prompt}]

# 대화를 기록할 파일 설정
log_file = "chat_log.txt"

# 지정한 파일에 대화 기록
def log_message(user_message, gpt_response):
    with open(log_file, "a") as file:
        file.write(f"User: {user_message}\n")
        file.write(f"GPT: {gpt_response}\n")
        file.write("-" * 50 + "\n")

# 대화 구현
while True:
    user_input = input("User: ")
    
    # exit 입력하면 종료
    if user_input.lower() == "exit":
        print("대화를 종료합니다")
        break
    
    messages.append({"role": "user", "content": user_input})

    # 답변 생성
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_reply = response['choices'][0]['message']['content']

    # 답변 출력
    print(f"GPT: {assistant_reply}\n")

    messages.append({"role": "assistant", "content": assistant_reply})
    
    # chat_log 파일에 대화 기록
    log_message(user_input, assistant_reply)