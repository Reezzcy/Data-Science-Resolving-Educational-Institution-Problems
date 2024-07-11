# Final Project: Solving Human Resources Problems

## Business Understanding

Jaya Jaya Maju is a multinational company that has been established since 2000. It has more than 1000 employees spread across the country.

### Business Problems

Despite being a fairly large company, Jaya Jaya Maju was still struggling to manage its employees. This resulted in a high attrition rate (the ratio of the number of employees who left to the total number of employees) of more than 10%. This attrition rate will cause various problems for the company. Problems such as decreased productivity, increased recruitment and training costs, and loss of knowledge from experienced employees. To solve this problem, data scientists must identify the factors that affect the attrition rate.

### Project Scope

This project aims to reduce employee turnover (attrition rate) in Jaya Jaya Maju by visualising the factors that make employees affected by attrition and developing a clustering system to divide employees who have a high potential for attrition. The output will be a visualisation dashboard and a prediction program that predicts whether an employee will potentially experience attrition or not.

### Preparation

Data source: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Running the Dashboard:

1. Make sure Docker is installed, then run metabase.db.mv.db

2. Open a browser and run localhost:3000/setup

3. Enter email: xxxzuppasoupxxx@gmail.com password: 45464748

Setup environment:

1. Install pipenv
```
pip install pipenv
```

2. Create an environment 
```
pipenv install
```

3. Running predict
```
Input the data of the examined employee in the data dictionary
```

```
python prediction.py
```

## Business Dashboard

The Business Dashboard is created using Metabase, the display contains customer satisfaction score metrics with this the level of employee satisfaction can be measured. The pie chart shows the name of the job position (JobRole) that has a lot of attrition. The first bar chart shows the average salary of each job position (JobRole) of employees who are attrition. The second bar chart shows the average years of service (YearsAtCompany) of employees in each job position (JobRole). And the Line chart Shows the number of employees at each percentage increase in salary who made attrition.

## Conclusion

Based on the data analysis that has been conducted, there are several key factors that affect the attrition rate at Jaya Jaya Maju. The overall employee satisfaction score is below average, indicating that many employees are dissatisfied with their jobs. Some job positions have high turnover, indicating a potential problem. In addition, there is a high gap in average salary between job positions. Average tenure also varies between job positions, with Research Directors having the longest tenure of 26.5 years on average, and Sales Representatives having the shortest tenure of 2.04 years on average. Employees who received small salary increases were the largest group to leave the company, suggesting that the lack of significant salary increases may contribute to an employee's decision to leave.

Characteristics of Employees experiencing Attrition:
- Employees who are dissatisfied with their job (satisfaction score below 3).
- Employees who work as a Laboratory Technician, Sales Executive, or Research Scientist have a higher turnover rate.
- Employees who receive lower salaries, especially in Sales Representative positions.
- Employees with shorter tenure, especially in positions with the shortest average tenure such as Sales Representative.
- Employees who only received small salary increases (11%, 12%, and 13%).

### Recommended Action Items

- Increase employee satisfaction by considering factors such as work environment, work/life balance, and job engagement. Improvements can be made by ensuring the work environment has good facilities and cleanliness. Implement a more flexible work policy while still considering the company's operational needs. Provide work that is interesting but also fulfils the needs of the company.
- Identify the reasons why Laboratory Technician, Sales Executive, and Research Scientist often attrition. Identification can be done by conducting surveys and interviews to identify the specific reasons behind their decisions. Organise discussion sessions to understand the challenges and issues faced in the workplace.
- Adjust the salary of each position to avoid discrepancies and unfairness. Conduct studies to determine competitive salary levels for each position and implement clear and transparent compensation to set compensation that considers work experience, education level, and performance factors.
- Enhance tenure and career development by providing job position rotation opportunities. Rotation of positions is done to allow employees to gain experience from across positions which helps employees' interest in developing careers in the long term.
- Evaluate performance-based salary increase policies to incentivise high-performing employees. Analyse performance data to measure the performance of employees, benchmarks that can be used can be productivity, quality and efficiency of work results. 
