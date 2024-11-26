import speech_recognition as sr
import picar_4wd as fc

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def get_voice_command():
    with microphone as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return None

def execute_command(command):
    if 'forward' in command:
        fc.forward(50)
    elif 'backward' in command:
        fc.backward(50)
    elif 'left' in command:
        fc.turn_left(50)
    elif 'right' in command:
        fc.turn_right(50)
    elif 'stop' in command:
        fc.stop()
    else:
        print("Command not recognized")

if __name__ == "__main__":
        try:
            while True:
                command = get_voice_command()
                if command:
                    execute_command(command)
                if command == 'quit':
                    break
        finally:
            fc.stop()
