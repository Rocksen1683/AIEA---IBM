import json
import sys
from ibm_watson import ApiException
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Authentication for watson

authenticator = IAMAuthenticator('KBb1g0YqmaC5ytYzG1reO-H07A1JbxO1q-KoBadZCf-K')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator)
visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/9d84264f-b813-48e5-8627-c3febd52beeb')

# Function that classifies images as accident or not taking path as parameter

def watson(st):
    with open(st, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file=images_file,
            threshold='0.6',
        classifier_ids='Finalting_540897173').get_result()

    # prints result
    
    info = classes['images'][0]['classifiers'][0]['classes']
    print(info[0]['class'], ' --- ', info[0]['score'])
    try:
        print(info[1]['class'], ' --- ', info[1]['score'])
    except:
        pass

    # if it is an accident, returns true. Otherwise, false.
    
    if info[0]['class'] == 'accident':
        return True
    else:
        return False
