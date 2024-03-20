from openai import OpenAI
from secret_key import open_api_key

client = OpenAI() #will get the secret key from the environmental variable I made

''' Role Types
system role - can help to setup model behavior and contect
user role - indicate end-user input prompt
assistant role - indicate message is a response from assistant (model), lets us save previous convo and send it again as prompt
'''
#Array to store messages
app_messages = [{"role" : "system", "content" : "You are a programmer with many years of experience. You have expertise with Java"}]

while True:
    user_message = input("User : ") #get message from user of API
    if user_message:
        app_messages.append({"role" : "user", "content" : user_message}) #store message in message array to preserve context
        #send request
        response = client.chat.completions.create(#create array of responses from chat
            model="gpt-3.5-turbo",
            messages=app_messages,
        )
        #print response
        reply = response.choices[0].message.content # access the 'content' attribute of the 'message' object
        print("ChatGPT : " + reply)
        app_messages.append({"role" : "assistant", "content" : reply})#add the reply to the message array



