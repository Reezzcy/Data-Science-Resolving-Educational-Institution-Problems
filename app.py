import joblib
import numpy as np
import pandas as pd
import streamlit as st

boosting_model = joblib.load('model/Boosting_model.joblib')

pca = joblib.load('model/pca.joblib')

scaler_Course = joblib.load('model/scaler_Course.joblib')
scaler_DaytimeEveningAttendance = joblib.load('model/scaler_DaytimeEveningAttendance.joblib')
scaler_PreviousQualification = joblib.load('model/scaler_PreviousQualification.joblib')
scaler_PreviousQualificationGrade = joblib.load('model/scaler_PreviousQualificationGrade.joblib')
scaler_Nationality = joblib.load('model/scaler_Nationality.joblib')
scaler_AdmissionGrade = joblib.load('model/scaler_AdmissionGrade.joblib')
scaler_Displaced = joblib.load('model/scaler_Displaced.joblib')
scaler_EducationalSpecialNeeds = joblib.load('model/scaler_EducationalSpecialNeeds.joblib')
scaler_Debtor = joblib.load('model/scaler_Debtor.joblib')
scaler_TuitionFeesUpToDate = joblib.load('model/scaler_TuitionFeesUpToDate.joblib')
scaler_Gender = joblib.load('model/scaler_Gender.joblib')
scaler_ScholarshipHolder = joblib.load('model/scaler_ScholarshipHolder.joblib')
scaler_AgeAtEnrollment = joblib.load('model/scaler_AgeAtEnrollment.joblib')
scaler_International = joblib.load('model/scaler_International.joblib')
scaler_CurricularUnits1stSemCredited = joblib.load('model/scaler_CurricularUnits1stSemCredited.joblib')
scaler_CurricularUnits1stSemEnrolled = joblib.load('model/scaler_CurricularUnits1stSemEnrolled.joblib')
scaler_CurricularUnits1stSemEvaluations = joblib.load('model/scaler_CurricularUnits1stSemEvaluations.joblib')
scaler_CurricularUnits1stSemApproved = joblib.load('model/scaler_CurricularUnits1stSemApproved.joblib')
scaler_CurricularUnits1stSemGrade = joblib.load('model/scaler_CurricularUnits1stSemGrade.joblib')
scaler_CurricularUnits1stSemWithoutEvaluations = joblib.load('model/scaler_CurricularUnits1stSemWithoutEvaluations.joblib')
scaler_CurricularUnits2ndSemCredited = joblib.load('model/scaler_CurricularUnits2ndSemCredited.joblib')
scaler_CurricularUnits2ndSemEnrolled = joblib.load('model/scaler_CurricularUnits2ndSemEnrolled.joblib')
scaler_CurricularUnits2ndSemEvaluations = joblib.load('model/scaler_CurricularUnits2ndSemEvaluations.joblib')
scaler_CurricularUnits2ndSemApproved = joblib.load('model/scaler_CurricularUnits2ndSemApproved.joblib')
scaler_CurricularUnits2ndSemGrade = joblib.load('model/scaler_CurricularUnits2ndSemGrade.joblib')
scaler_CurricularUnits2ndSemWithoutEvaluations = joblib.load('model/scaler_CurricularUnits2ndSemWithoutEvaluations.joblib')

scaler_list = [
    scaler_Course, 
    scaler_DaytimeEveningAttendance, 
    scaler_PreviousQualification, 
    scaler_PreviousQualificationGrade,
    scaler_Nationality,
    scaler_AdmissionGrade,
    scaler_Displaced,
    scaler_EducationalSpecialNeeds,
    scaler_Debtor,
    scaler_TuitionFeesUpToDate,
    scaler_Gender,
    scaler_ScholarshipHolder,
    scaler_AgeAtEnrollment,
    scaler_International,
    scaler_CurricularUnits1stSemCredited,
    scaler_CurricularUnits1stSemEnrolled,
    scaler_CurricularUnits1stSemEvaluations,
    scaler_CurricularUnits1stSemApproved,
    scaler_CurricularUnits1stSemGrade,
    scaler_CurricularUnits1stSemWithoutEvaluations,
    scaler_CurricularUnits2ndSemCredited,
    scaler_CurricularUnits2ndSemEnrolled,
    scaler_CurricularUnits2ndSemEvaluations,
    scaler_CurricularUnits2ndSemApproved,
    scaler_CurricularUnits2ndSemGrade,
    scaler_CurricularUnits2ndSemWithoutEvaluations
]

scale_columns = [
    'Course',
    'DaytimeEveningAttendance',
    'PreviousQualification',
    'PreviousQualificationGrade',
    'Nationality',
    'AdmissionGrade',
    'Displaced', 
    'EducationalSpecialNeeds', 
    'Debtor', 
    'TuitionFeesUpToDate',
    'Gender', 
    'ScholarshipHolder', 
    'AgeAtEnrollment', 
    'International',
    'CurricularUnits1stSemCredited',
    'CurricularUnits1stSemEnrolled',
    'CurricularUnits1stSemEvaluations',
    'CurricularUnits1stSemApproved',
    'CurricularUnits1stSemGrade',
    'CurricularUnits1stSemWithoutEvaluations',
    'CurricularUnits2ndSemCredited',
    'CurricularUnits2ndSemEnrolled',
    'CurricularUnits2ndSemEvaluations',
    'CurricularUnits2ndSemApproved',
    'CurricularUnits2ndSemGrade',
    'CurricularUnits2ndSemWithoutEvaluations',
]

def preprocessing(data):
    data = data.copy()
    df = pd.DataFrame()

    for i in range(len(scale_columns)):
        try:
            data[scale_columns[i]] = scaler_list[i].transform(np.asarray(data[scale_columns[i]]).reshape(-1,1))[0]
        except Exception as e:
            print(scale_columns[i])

    df[['pc_1', 'pc_2', 'pc_3', 'pc_4', 'pc_5', 'pc_6', 'pc_7', 'pc_8', 'pc_9', 'pc_10']] = pca.transform(data[scale_columns]) 
    
    return df

def prediction(data):
    result = boosting_model.predict(data)
    return result

st.set_page_config(layout="wide")

st.header('Prototype for Predicting Students who will Dropout')

st.write('- Name: Nicolas Debrito')
st.write('- Email: nicolas.debrito66@gmail.com')
st.write('- Id Dicoding: reezzy')

data = pd.DataFrame()

st.header('Dropout Prediction (Prototype)')

st.subheader('Academic Information')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    course_dict = {
        'Biofuel Production Technologies': 33,
        'Animation and Multimedia Design': 171,
        'Social Service (evening attendance)': 8014,
        'Argonomy': 9003,
        'Communication Design': 9070,
        'Veterinary Nursing': 9085,
        'Informatics Engineering': 9119,
        'Equinculture': 9130,
        'Management': 9147,
        'Social Service': 9238,
        'Tourism': 9254,
        'Nursing': 9500,
        'Oral Hygiene': 9556,
        'Advertising and Marketing Management': 9670,
        'Journalism and Communication': 9773,
        'Basic Education': 9853,
        'Management (evening attendance)': 9991
    }

    course = st.selectbox(label='Course', options=course_dict.keys(), index=0)
    data['Course'] = [course_dict[course]]

with col2:

    attendance = st.selectbox(label='DaytimeEveningAttendance', options=['Daytime', 'Evening'], index=0)
    data['DaytimeEveningAttendance'] = [0 if attendance == 'Evening' else 1]

with col3:

    qualification_dict = {
    'Secondary education': 1,
    "Higher education - bachelor's degree": 2,
    'Higher education - degree': 3,
    "Higher education - master's": 4,
    'Higher education - doctorate': 5,
    'Frequency of higher education': 6,
    '12th year of schooling - not completed': 9,
    '11th year of schooling - not completed': 10,
    'Other - 11th year of schooling': 12,
    '10th year of schooling': 14,
    '10th year of schooling - not completed': 15,
    'Basic education 3rd cycle (9th/10th/11th year) or equiv.': 19,
    'Basic education 2nd cycle (6th/7th/8th year) or equiv.': 38,
    'Technological specialization course': 39,
    'Higher education - degree (1st cycle)': 40,
    'Professional higher technical course': 42,
    'Higher education - master (2nd cycle)': 43
    }

    previousQualification = st.selectbox(label='PreviousQualification', options=qualification_dict.keys(), index=0)
    data['PreviousQualification'] = [qualification_dict[previousQualification]]

with col4:

    previousQualificationGrade = float(st.number_input(label='PreviousQualificationGrade', value=0.0))
    data['PreviousQualificationGrade'] = [previousQualificationGrade]

with col5:

    admissionGrade = float(st.number_input(label='AdmissionGrade', value=0.0))
    data['AdmissionGrade'] = [admissionGrade]

st.subheader('Demographic Information')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    age = int(st.number_input(label='AgeAtEnrollment', value=20))
    data['AgeAtEnrollment'] = [age]

with col2:

    gender = st.selectbox(label='Gender', options=['Male', 'Female'], index=0)
    data['Gender'] = [1 if gender == 'Male' else 0]

with col3:

    international = st.selectbox(label='International', options=['Yes', 'No'], index=1)
    data['International'] = [0 if international == 'No' else 1]

with col4:

    nationality_dict = {
        'Portuguese': 1,
        'German': 2,
        'Spanish': 6,
        'Italian': 11,
        'Dutch': 13,
        'English': 14,
        'Lithuanian': 17,
        'Angolan': 21,
        'Cape Verdean': 22,
        'Guinean': 24,
        'Mozambican': 25,
        'Santomean': 26,
        'Turkish': 32,
        'Brazilian': 41,
        'Romanian': 62,
        'Moldova (Republic of)': 100,
        'Mexican': 101,
        'Ukrainian': 103,
        'Russian': 105,
        'Cuban': 108,
        'Colombian': 109
    }

    nationality = st.selectbox(label='Nationality', options=nationality_dict.keys(), index=0)
    data['Nationality'] = [nationality_dict[nationality]]

st.subheader('Social & Economic Information')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    displaced = st.selectbox(label='Displaced', options=['Yes', 'No'], index=1)
    data['Displaced'] = [0 if displaced == 'No' else 1]

with col2:

    educationalSpecialNeeds = st.selectbox(label='EducationalSpecialNeeds', options=['Yes', 'No'], index=1)
    data['EducationalSpecialNeeds'] = [0 if educationalSpecialNeeds == 'No' else 1]

with col3:

    debtor = st.selectbox(label='Debtor', options=['Yes', 'No'], index=1)
    data['Debtor'] = [0 if debtor == 'No' else 1]

with col4:

    tuitionFeesUpToDate = st.selectbox(label='TuitionFeesUpToDate', options=['Yes', 'No'], index=1)
    data['TuitionFeesUpToDate'] = [0 if tuitionFeesUpToDate == 'No' else 1]

with col5:

    scholarshipHolder = st.selectbox(label='ScholarshipHolder', options=['Yes', 'No'], index=1)
    data['ScholarshipHolder'] = [0 if scholarshipHolder == 'No' else 1]

st.subheader('Transkrip Nilai')

st.write('1st Semester')

col1, col2, col3 = st.columns(3)

with col1:

    curricularUnits1stSemCredited = int(st.number_input(label='CurricularUnits1stSemCredited', value=0))
    data['CurricularUnits1stSemCredited'] = [curricularUnits1stSemCredited]

with col2:

    curricularUnits1stSemEnrolled = int(st.number_input(label='CurricularUnits1stSemEnrolled', value=0))
    data['CurricularUnits1stSemEnrolled'] = [curricularUnits1stSemEnrolled]

with col3:
    
    curricularUnits1stSemEvaluations = int(st.number_input(label='CurricularUnits1stSemEvaluations', value=0))
    data['CurricularUnits1stSemEvaluations'] = [curricularUnits1stSemEvaluations]

col1, col2, col3 = st.columns(3)

with col1:

    curricularUnits1stSemApproved = int(st.number_input(label='CurricularUnits1stSemApproved', value=0))
    data['CurricularUnits1stSemApproved'] = [curricularUnits1stSemApproved]

with col2:

    curricularUnits1stSemGrade = float(st.number_input(label='CurricularUnits1stSemGrade', value=0.0))
    data['CurricularUnits1stSemGrade'] = [curricularUnits1stSemGrade]

with col3:

    curricularUnits1stSemWithoutEvaluations = int(st.number_input(label='CurricularUnits1stSemWithoutEvaluations', value=0))
    data['CurricularUnits1stSemWithoutEvaluations'] = [curricularUnits1stSemWithoutEvaluations]

st.write('2nd Semester')

col1, col2, col3 = st.columns(3)

with col1:

    curricularUnits2ndSemCredited = int(st.number_input(label='CurricularUnits2ndSemCredited', value=0))
    data['CurricularUnits2ndSemCredited'] = [curricularUnits2ndSemCredited]

with col2:

    curricularUnits2ndSemEnrolled = int(st.number_input(label='CurricularUnits2ndSemEnrolled', value=0))
    data['CurricularUnits2ndSemEnrolled'] = [curricularUnits2ndSemEnrolled]

with col3:
    
    curricularUnits2ndSemEvaluations = int(st.number_input(label='CurricularUnits2ndSemEvaluations', value=0))
    data['CurricularUnits2ndSemEvaluations'] = [curricularUnits2ndSemEvaluations]

col1, col2, col3 = st.columns(3)

with col1:

    curricularUnits2ndSemApproved = int(st.number_input(label='CurricularUnits2ndSemApproved', value=0))
    data['CurricularUnits2ndSemApproved'] = [curricularUnits2ndSemApproved]

with col2:

    curricularUnits2ndSemGrade = float(st.number_input(label='CurricularUnits2ndSemGrade', value=0.0))
    data['CurricularUnits2ndSemGrade'] = [curricularUnits2ndSemGrade]

with col3:

    curricularUnits2ndSemWithoutEvaluations = int(st.number_input(label='CurricularUnits2ndSemWithoutEvaluations', value=0))
    data['CurricularUnits2ndSemWithoutEvaluations'] = [curricularUnits2ndSemWithoutEvaluations]

with st.expander("View the Raw Data"):

    st.dataframe(data=data, width=1500, height=10)

if st.button('Predict'):

    new_data = preprocessing(data=data)

    with st.expander("View the Preprocessed Data"):

        st.dataframe(data=new_data, width=1500, height=10)

    st.write(f'Prediction: {prediction(new_data)[0]}')
