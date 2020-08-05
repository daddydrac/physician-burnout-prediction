### Prediciting Physician Burnout with Causal Inference

Using causal inference to improve upon the results of previous physician burn out models with risk stratification

------------------------------------------------------------

#### Researchers:

| Hela Bahria, Sr. Data Scientist  | Joe Hoeller, Data Scientist I | Greg Chase, Sr. Data Scientist |
| ------------- | ------------- | ---------------- |
| M.S. in Engineering in statistics, Data Analysis & Physics  | Deep Learning & Software Engineer  | Acclerated GPU Computing Expert |
| hela@aktiver.io | joe@aktiver.io | greg@aktiver.io |


#### Data description:
The following are the features that can be found in the dataset of physicians in the USA as well as the values they can take. This features will be generated later on respecting real life statistics in order to mimic real life cases. There exists correlation between the mentioned attributes, this correlation has to be implemented while generation data in order to guarantee the veracity of the output data.


#### Age: 4 age groups
As of 2018, the largest distribution of U.S. physicians was between the ages of 55 and 65 years old. At that time about 29 percent of physicians fell within this age group. With just 11.2 percent of all physicians, the smallest distribution of U.S. physicians was among those aged 35 years or younger.

 - 11.2% of population is age range from 25-35
 - 19.8% of population is age range from 36-45
 - 22.9% of population is age range 46-55
 - 29% of population is age range 56-65
 - 17% of population is age range 66-75
 ![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/active_physicians_by_age.PNG)
 
 #### Gender: 
 Based on  the distribution of active physicians by age group (4 groups) for each gender in USA, we can generate successfuly the gender of physicians for this study.
 
 The graph shows the percentage of active physicians by age group for each gender in 2017.
 
 
 ![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/active_physicians_by_gender.PNG)
 
 
#### Specialities : There are 1.1 million (1 100 000) doctors in USA

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


#### Compensation : 

Based on the average annual physicians compensation, we can generate the salary of physicians by gender for each specialties considering that women earned 30% less than men overall and a variance of 10% compared to the average salary of each gender.
The graph below shows the average annual physicians compensation by specialty reported in 2019.

![Alt text](https://github.com/joehoeller/physician-burnout-prediction/blob/feature/stressors/misc/annual-compenstation.png)













