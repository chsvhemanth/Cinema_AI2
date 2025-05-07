import streamlit as st
from groq import Groq
GROQ_API_KEY = st.secrets["groq"]["API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

def generate_story(user_input):
    # Make the API call
    chat_completion = client.chat.completions.create(
        messages=[{
                    "role": "system",
                    "content": (
                        " You are a professional screenwriter with expertise in writing compelling scripts for film, television, and streaming platforms."
                        "You understand structure, pacing, dialogue, character development, and cinematic storytelling."
                        "Whenever a user gives you a story idea, genre, or character concept, respond in the format of a working screenwriter, developing:"
                        "1.A compelling logline along with A complete end to end script for the user to his future uses"
                        "2.A full beat sheet or story outline (based on 3-act structure or another appropriate format)"
                        "3.Character breakdowns including names, roles, motivations, flaws, and arcs"
                        "4.Scene-by-scene breakdowns with brief but cinematic descriptions"
                        "5.Actual screenplay scenes in industry-standard format when requested"
                        "6. Use professional screenwriting terminology (e.g., INT./EXT., VO, action lines, dialogue)"
                        " Your tone should be confident and imaginative but professional and concise, as if you're pitching or collaborating in a real writers' room." 
                        "If needed, you may reference classic screenwriting techniques (e.g., Save the Cat, The Hero’s Journey, etc.) to structure stories effectively."
                        "Always prioritize strong character motivation, emotional arcs, and visual storytelling."
                    )
                },
                {
                    "role": "user", 
                    "content": user_input
                }
                ],
        model="llama3-8b-8192",
    )
    
    # Return the response content
    return chat_completion.choices[0].message.content

# Streamlit app interface
st.title('THE STORY AKSHAYAPATRA')
st.write('Hello Thinker,Enter the basic concept of your amazing story :')

# User input for story content
user_input = st.text_area("Prompt:", "")

if st.button('Here is what you can create'):
    if user_input:
        # Generate the story based on the user's input
        response = generate_story(user_input)
        st.subheader("There you go:")
        st.write(response)
    else:
        st.warning("Please enter a valid prompt.")


 
 