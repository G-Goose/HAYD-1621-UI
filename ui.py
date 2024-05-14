import streamlit as st
import requests
import json
import time

def app():
    # Set session_state to not done
    if 'picture' not in st.session_state:
        st.session_state['picture']='not done'

<<<<<<< HEAD

    st.title(f'HOW ARE YOU DOING TODAY ?')

    st.write(f"### :orange[&#x2600; TIME TO CHECK YOUR EMOTIONS] ")

    col1,col2 = st.columns([0.65,0.35])
=======
    # creating to columns with 0.3/0.7 relation
    st.title(f'HOW ARE YOU DOING TODAY ?')

    st.write(f"### :orange[&#x2600; TIME TO CHECK YOUR EMOTIONS] ")

    col1,col2 = st.columns([0.99,0.01])
    # Create tabs with two options
    tab1, tab2, = st.tabs(["Upload a Picture ⬆️", "Take a Picture 📸"])
>>>>>>> d50de2edd8b6b92afbffb5fe89d848d078a4ab50

    # function to track changes on the session_state
    def change_picture_state():
        st.session_state['picture']='done'

    ### changing the input method
    picture = None
    picture_upload = None
    picture_camera = None

<<<<<<< HEAD
    picture_upload = col1.file_uploader("Upload a picture", on_change=change_picture_state)
    picture_camera = col1.camera_input("Please take a picture", on_change=change_picture_state)
=======
    picture_upload = tab1.file_uploader("Please upload a picture", on_change=change_picture_state)
    picture_camera = tab2.camera_input("Please take a picture 🤳", on_change=change_picture_state)
>>>>>>> d50de2edd8b6b92afbffb5fe89d848d078a4ab50


    # url = 'https://hayd1621-docker-v2-lempkfijgq-uc.a.run.app/upload_your_nice_face'
    url = 'http://127.0.0.1:8000/upload_your_nice_face'

    if picture_upload is not None:
        picture = picture_upload
    elif picture_camera is not None:
        picture = picture_camera
    if picture is not None:
        # The key 'img' is the name of the form field for the file upload
        files = {'img': picture}
        # Send the POST request with the image file
        response = requests.post(url, files=files)

        print('* * * picture taken * * *')

        #response.content
        data = response.content
        ### Decode the bytes object into a string
        data_str = data.decode('utf-8')
        ### Convert to a dict
        data_dict = json.loads(data_str)

        emotion_list = []
        # for-loop to get the keys and values
        for key, value in data_dict.items():
            result = f"{key} : {round(value,2)}%"
            emotion_list.append(result)

        if st.session_state['picture'] == 'done':
            progress_bar = col1.progress(0)

            for percentage in range(100):
                time.sleep(0.02)
                progress_bar.progress(percentage+1)

<<<<<<< HEAD

            col2.success("Picture uploaded successfully!")
=======
            col1.success("Picture uploaded successfully!")
>>>>>>> d50de2edd8b6b92afbffb5fe89d848d078a4ab50

            #with st.expander("See your results:"):
            if len(emotion_list) == 1:
                st.write(f'### Your top detected emotions are:')
                st.write(f'### :blue[{emotion_list[0]}]')
            else:
                st.write(f'### Your detected emotions are:')
                st.write(f'### :blue[{emotion_list[0]}]')
                st.write(f'### :blue[{emotion_list[1]}]')

            top_mood = next(iter(data_dict))
            mood_list = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
            mood_int = int(mood_list.index(top_mood))


        st.write(f"If you're satisfied with the result, update your mood board!")
        st.write(f"Othewise, take another picture.")
        # bq_url = 'https://hayd1621-docker-v2-lempkfijgq-uc.a.run.app/save_to_bq'
        bq_url = 'http://127.0.0.1:8000/save_to_bq'

        if st.button('Save to mood board!'):
            bq_response = requests.get(bq_url, params={'val': mood_int})
            if bq_response.status_code == 200:
                st.success('Data successfully saved to BigQuery!')
            else:
                st.error('Failed to save data to BigQuery.')
