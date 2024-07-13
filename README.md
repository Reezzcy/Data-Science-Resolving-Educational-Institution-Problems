# Final Project: Solving Educational Institution Problems

## Business Understanding
Jaya Jaya Institut is one of the college educational institutions that has been established since 2000. Until now it has produced many graduates with an excellent reputation. However, there are also many students who do not complete their education, aka dropouts.

### Business Issues
This high number of dropouts is certainly one of the big problems for an educational institution. The high student dropout rate at Jaya Jaya Institute threatens the quality of education and the sustainability of the institution. This phenomenon not only affects the individual dropouts, but also has a broad impact on the quality of education, the reputation of the institution, as well as the financial and operational aspects of the institution. Therefore, Jaya Jaya Institut wants to detect as soon as possible students who might dropout so that they can be given specialised guidance. 

### Project Scope
This project aims to detect students who are at high risk of dropout as early as possible and provide appropriate interventions to help them complete their education at Jaya Jaya Institut. The end result is a visualisation dashboard to monitor student performance and a prototype to predict whether students will potentially dropout.

### Preparation

Data source: https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success

Setup environment:

1. Install pipenv
```
pip install pipenv
```

2. Create an environment 
```
pipenv install
```

3. Install dependencies
```
pipenv install -r requirements.txt
```

Running the Dashboard:

1. Make sure Docker is installed, then run metabase.db.mv.db

2. Open a browser and run localhost:3000/setup

3. Enter email: xxxzuppasoupxxx@gmail.com password: 45464748

## Business Dashboard
The business dashboard was created using Metabase, the dashboard contains metrics from the average of each grade from the student transcript in semester 1 & 2. Furthermore, in the diagram section, there is a piechart that shows the percentage of courses taken by students. The second chart contains a comparison of the number of students who take day or night classes. Thirdly, there is the average of the PreviousQualificationGrade. Fourthly there is a barchart for the education level before entry (PreviousQualification). Fifth there is a barchart for the gender of the students. Sixth there is a comparison piechart of international and local students. Finally, there is a barchart to see the nationality of the students.

## Running the Machine Learning System
The prototype can be run through the cmd/powershell terminal via the project directory.

Running the Prototype:

1. Run locally
```
streamlit run app.py
```
2. Access via deploy streamlit
```
https://data-science-solving-educational-institution-problems.streamlit.app/
```

## Conclusion

When comparing the dashboard showing all targets and dropout targets, there are two main signs that indicate students who are potential dropouts. Firstly, a significant drop in academic grades. Students who dropped out showed a significantly lower drop in grades compared to those who did not drop out. This indicates that the student may have difficulty following the curriculum or understanding the material being taught. Secondly, gender also plays an important role in dropout rates. The data shows that male students have a higher dropout rate compared to female students.

Characteristics of Students Experiencing Dropout:
- Students have low average academic grades.
- Male students tend to drop out more often.

### Recommended Action Items

- Students may have difficulty in following the curriculum or understanding the material being taught. To address this issue, institutions can implement specialised academic tutoring programmes as well as real-time grade monitoring systems to detect declines in academic performance earlier.
- Identify the reasons why male students drop out more often, identification can be done through interviews or surveys on male students to ascertain whether there are specific reasons for students to drop out. Furthermore, to overcome the problem, have a joint discussion to understand and be able to fix the problem.