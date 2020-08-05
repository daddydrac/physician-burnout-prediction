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
 
[Source:](https://github.com/facebook/react/wiki/Sites-Using-React)

4) States:  (54 possible values)


5) Gender 
Professionally Active Physicians by Gender
Gender distribution by speciality


6)   Working place: (8 possible values)
Describing the nature of their workplace which could be a hospital, a clinic, etc..

7)  Physicians compensation:
by speciality :
Orthopedics and Cardiology have been among the top-earning specialties
in the survey every year for the past 5 years.Pediatrics, family medicine, and diabetes and endocrinology have been among the lowest.



By gender:


BY race:
Caucasian/white physicians earn more than physicians of other races.



7)  Job performance satisfaction :
It an ordinal categorical variable that describes how the physician rates their satisfaction with their job on a scale 0-4.

8) Lifestyle & Happiness:
We have multiples measure with which we can calculate a lifestyle and happiness index.
E.g. Generation, specialty, health and wellness, vacation, work hours, marriage, exercice, etc..
This index would logically correlate with our target variable (burnout). You can find more details in the reference attached to this report.    







 
Study of burned out statistics observed in physicians, US.
During this study, we will go over the correlation of the features we have discussed in the previous section with our target feature: burnout. This is an important part as it define the generation of the burnout labels. 
E. g. if we notice that physicians in some specialities show more tendencies to burnout then we’ll generate data that mirrors that but attributing the positive label for the burnout variable more to individuals in those specialties. 

In 2020, 42% of physicians reported that they burned out down from 46% 5 years ago.

Which Specialties are most burnout ?
Specialties that have been among the top in burnout over past 5 years (ordered):
Critical care
Emergency medicine
Family medicine
Neurolgy
Urolgy

Following is a bar chart describing burnout cases per specialty during the year of 2019.












2. Which Generation is most burnout ?

  Generation X physicians report noticeably more burnout than other groups.
   
3. Which gender is most burned out ?

Women have consistently reported higher percentages of burnout than
men over the years.
In 2015, a greater proportion of women(51%) than men (43%) said they were burned out.




4. What Contributes most to Burnout ?

Top causes of burnout over years:
Long hours
Overwhelming workload
Lack of support

5. Where Are physicians Most Burned Out?

Solo practice has been declining over the years and now comprises only about 15% of physicians.









Does your workplace offer a program to reduce stress and/or burnout?

A little more than a quarter (28%) of physicians say their workplaces offer stress reduction programs, while half say their workplaces don't. 



Are physicians depressed?
Burnout may lead to depression.


References:
https://www.medscape.com/slideshow/2020-lifestyle-happiness-6012424
https://www.medscape.com/slideshow/2020-lifestyle-burnout-6012460
https://www.medscape.com/slideshow/2019-compensation-overview-6011286
