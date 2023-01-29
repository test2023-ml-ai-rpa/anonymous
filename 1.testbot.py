import aiml
kernel = aiml.Kernel()

kernel.learn("/Users/neosoft/PROJECTS/python/ai/1/std-startup.xml")
kernel.learn("/Users/neosoft/PROJECTS/python/ai/1/basic_chat.aiml")
kernel.respond("LOAD")
# Press CTRL-C to break this loop
while True:
    print( kernel.respond(input("Enter your message >> ")))