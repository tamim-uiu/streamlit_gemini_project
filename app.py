import streamlit as st

#import note_generator function(which will return the note) from api_calling
from api_calling import note_generator,audio_transcription,quiz_generator

from PIL import Image
#title
st.title("Note summery and quiz Generator")
st.markdown("Upload upto 3 images to generate note summery and quizes")
st.divider()




#use with st.sidebar so that all things like photo upload can be under sidebar

with st.sidebar:
    st.header("Controls")
    images=st.file_uploader(
        "upload the  photo of your note",
        type=['jpg','jpeg','png'],
        accept_multiple_files=True
    )

    pil_images =[]

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if images:
        if len(images)>3:
            st.error("upload at max 3 images")
        else:
            col=st.columns(len(images))

            st.subheader("Uploaded images")
# to show each img in column
            for i,img in enumerate(images):
              with col[i]:
               st.image(img)
    #difficulty of quiz           
    selected_option=st.selectbox(
       "Enter the difficulties of your quiz",
       ("Easy","Medium","Hard"),
       index=None
    )   
    if selected_option:
       st.markdown(f"you selected {selected_option}")
    else:
       st.error("You have to select a difficulty") 
    pressed=st.button("click to initiate Ai",type="primary")





#for frontend work like generate note & quiz
if pressed:
   if not images:
      st.error("You must upload 1 image")
   if not selected_option:
       st.error("You must select a difficulty")


       #create box for notes,audio,& quiz
   if images and selected_option:

      #note
      with st.container(border=True):
         st.subheader("your note")
         
         with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pil_images)
                st.markdown(generated_notes)

    
       #audio
      with st.container(border=True):
            st.subheader("Audio Transcription")

         #the portion below will be replaced by API Call 
            with st.spinner("AI is generating audio transcript for you"):
                #clearing the markdown

                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("-","")
                generated_notes = generated_notes.replace("`","")

                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)

    #quiz
      with st.container(border=True):
         st.subheader(f"Quiz ({selected_option}) Difficulty")

            #the portion below will be replaced by API Call 

         with st.spinner("AI is generating the quizzes"):
               quizzes = quiz_generator(pil_images,selected_option)
               st.markdown(quizzes)
         
