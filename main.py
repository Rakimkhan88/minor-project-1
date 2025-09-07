from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
# chatbot logic
def bot():
    # user input
    incoming_message = request.values.get('Body', '').lower()

    # creating object of MessagingResponse
    response = MessagingResponse()

    # If the user sends 'menu', show the options
    if 'menu' in incoming_message:
        menu_text = (
            "Welcome! How can I assist you today? Please choose one of the following options" 
            "by replying with the number:\n"
            "1. Exam Date Sheet\n"
            "2. Assignments\n"
            "3. Today's Classes\n"
            "4. Attendance\n"
            "5. Notice\n"
            "6. Result and Grade\n"
            "7. Admission Details\n"
            "8. Facility For Students\n"
            "9. Student Support\n"
            "10. Feedback\n"
            "Reply with the number of your choice (e.g., '1' for Exam Date Sheet)."
        )
        response.message(menu_text)

    # Handle different options
    elif '1' in incoming_message:
        response.message("The exam date sheet will be released next week. Please check the official website for updates.")
    elif '2' in incoming_message:
        response.message("Your assignments are due next Friday. Check your student portal for details.")
    elif '3' in incoming_message:
        response.message("Today's classes are:\n- 9:00 AM: Math\n- 11:00 AM: Computer Science\n- 2:00 PM: History")
    elif '4' in incoming_message:
        response.message("You have 75% attendance this semester. Keep it up,good work!")
    elif '5' in incoming_message:
        response.message("Tomorrow will be holiday and College will open on Next day") 
    elif '6' in incoming_message:
        response.message("Marks out of 100\n 1.Physics-90\n 2.Mathematics-85\n 3.Chemistry-95\n Congratulation,you got A+ grade")
    elif '7' in incoming_message:
        response.message(" 1.Bachelor Of Technology-130000/-\n2.Master Of Business Administration-100000/-\n3.Master Of Computer Application-96000/-")
    elif '8' in incoming_message:
        response.message("1.Library Service:-\n    A.Open Timing'10:00 AM To 5:00 PM'\n    B.Availability of all Latest Books\n    C.Peaceful Environment\n" 
         "2.Hostel Facility:-\n    A.Fees- 78000/-\n    B.Healthy Food\n    C.Gym Facility\n"
         "3.Transportation Convinience:-\n   "    "A.Routes and Chagres->\n   Mathura-25000/-\n   Agra-28000/-\n   Firozabad-34000/-")
    elif '9' in incoming_message:
        response.message("--Student can Contact to different Department--\n  "
        "1.Health Department- 9920558869\n  2.Anti-ragging Cell- 8899669666\n  3.Sport Cell- 8569694569\n  "
        "4.Admission Cell- 8856965620")
    elif '10' in incoming_message:
        response.message("Students can give Feedback to any Department of College,"
        "which help to improve") 
    else:
        response.message("Hello Sir,\n''Welcome To Hindustan College of Science and Technology.''\n\n" 
        "Please type ''menu'' to see available options.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)



