### Prediciting Physician Burnout with Causal Inference

Using causal inference to improve upon the results of previous physician burn out models with risk stratification

------------------------------------------------------------

#### Researchers:

| Hela Bahria, Sr. Data Scientist  | Joe Hoeller, Data Scientist I | Greg Chase, Sr. Data Scientist |
| ------------- | ------------- | ---------------- |
| M.S. in Engineering in statistics, Data Analysis & Physics  | Deep Learning & Software Engineer  | Acclerated GPU Computing Expert |
| hela@aktiver.io | joe@aktiver.io | greg@aktiver.io |


#### Data description
The following are the features that can be found in the dataset of physicians in the USA as well as the values they can take. This features will be generated later on respecting real life statistics in order to mimic real life cases. There exists correlation between the mentioned attributes, this correlation has to be implemented while generation data in order to guarantee the veracity of the output data.


##### Age: 4 age groups
As of 2018, the largest distribution of U.S. physicians was between the ages of 55 and 65 years old. At that time about 29 percent of physicians fell within this age group. With just 11.2 percent of all physicians, the smallest distribution of U.S. physicians was among those aged 35 years or younger.

 - 11.2% of population is age range from 25-35
 - 19.8% of population is age range from 36-45
 - 22.9% of population is age range 46-55
 - 29% of population is age range 56-65
 - 17% of population is age range 66-75
 ![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/active_physicians_by_age.PNG)
 
 ##### Gender
 Based on  the distribution of active physicians by age group (4 groups) for each gender in USA, we can generate successfuly the gender of physicians for this study.
 
 The graph shows the percentage of active physicians by age group for each gender in 2017.
 
 
 ![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/active_physicians_by_gender.PNG)
 
 
##### Specialities : There are 1.1 million (1 100 000) doctors in USA

Based on the description of U.S. Physicians Database which combines all of the individual state databases into one national database and covers every city and state with a registered physician, we can extract the distribution of active physicians by specialty (18 specialties).

 - Allergist / Immunologist: 4551, 0.45%
 - Anesthesiologist: 57300, 5.7%
 - Dermatologist: 15275, 1.52%
 - Emergency Doctor: 60090, 5.98%
 - Family Doctor: 140732, 14%
 - Internist: 260257, 25.9%
 - Neurological Surgeon: 7296, 0.73%
 - Obstetrician / Gynecologist: 51916, 5.17% 
 - Orthopedic Surgeon: 32777, 3.26%
 - Otolaryngologist: 12971, 1.29%
 - Pathologist: 21153, 2.1%
 - Pediatrician: 94900, 9.44%
 - Plastic Surgeons: 5399, 0.54%
 - Psychiatrist / Neurologist: 79721, 7.93%
 - Radiologist: 51685, 5.14%
 - Surgeons: 42585, 4.24%
 - Urologist: 13019, 1.29%
 - Optometrist: 56239, 5.6%
 
[Source:] https://doctordatabase.co/database/united-states-physicians/?gclid=Cj0KCQjwvIT5BRCqARIsAAwwD-TfZkr9UJ1cTGAZjmXqdE1IiX_PklVG9q5W6hDxeMcBlLdecIR4AswaAvMmEALw_wcB


##### Compensation 

Based on the average annual physicians compensation, we can generate the salary of physicians by gender for each specialties considering that women earned 30% less than men overall and a variance of 10% compared to the average salary of each gender.
The graph below shows the average annual physicians compensation by specialty reported in 2019.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/annual-compenstation.png)

##### Working hours spent on patient care

Based on the average number of hours per week spent by phyisicans seeing patients for each gender, we can generate the working hours per week spent seeing patients by gender considering a variance of 50% compared to the average number of each gender.

The graph below shows the average number of hours per week spent by phyisicans seeing patients by gender reported in 2019.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/work_hours_patient.PNG)

##### Self esteem by specialty

Based on the graph below that shows which specialties have the highest self esteem, we can generate a binary variable describing physicians self esteem as High or Low for each specialties.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/self_esteem_by_specialty.PNG)

#### Relevant burned out statistics observed in physicians, US

In 2020, 42% of physicians reported that they burned out down from 46% 5 years ago.

##### Which Generation is most burnout ?

During the burnout study, we will use 3 age groups of physicians:

- millenials(25-39 years old)
- Generation X(40-54 years old)
- baby boomers(55-73 years old)

Based on the graph below, the Generation X physicians report noticeably more burnout than other groups.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/burnout-by-age-range.png)
 
#####  Which gender is most burned out ?
Women have consistently reported higher percentages of burnout than men over the years.
The graph below shows the proportions of physicians burnout by gender in 2019.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/burnout-by-gender.png)

#####  Which specialties are most burned out ?
Specialties that were among the top in burnout in 2019:
- Urolgy
- Neurolgy
Following is a bar chart describing burnout cases per specialty during the year of 2019.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/burnout.png)

##### Where are physicians most burned Out?

Solo practice has been declining over the years and now comprises only about 15% of physicians.
The graph below shows where are physicians most burned out.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/burnout-by-specialty.png)

##### What contributes most to burnout?

There are several factors that have been contributing to physician burnout in US over years.
The graph below shows the contributor factors according to physcians who reported burnout knowing that a respondent could select more than one stressor.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/burnout-factors.png)

###### Bureaucratic task

Over half(55%) chose an excess of bureaucratic tasks as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20%
- Medium: 40%
- Low: 40%

###### long hours at work

More than one third noted(33%) too many hours at work as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%
###### Lack of respect from adminisrators, employers, colleagues or staff
32% of the physicians who reported burnout noted lack of respect from adminisrators, employers, colleagues or staff as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%

###### Increasing computerization of practice(EHRs)
30% of the physicians who reported burnout noted increasing computerization of practice(EHRs) as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%
###### Insufficient compensation,reimbursement
29% of the physicians who reported burnout noted insufficient compensation or reimbursement as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%
###### Lack of control, autonomy
24% of the physicians who reported burnout noted lack of control and autonomy as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%

###### Feeling like a cog in a wheel 
22% of the physicians who reported burnout noted Feeling like a cog in a wheel noted as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%
###### Decreasing reimbursements

19% of the physicians who reported burnout noted decreasing reimbursements as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%
###### Lack of respect from patients

17% of the physicians who reported burnout noted Lack of respect from patients as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%
###### Government regulations
16% of the physicians who reported burnout noted Government regulations as a stressor.
The severity of this stressor can be divided into three levels within this population as follows:
- High: 20% 
- Medium: 40%
- Low: 40%















