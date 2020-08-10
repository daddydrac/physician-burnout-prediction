import random
import pydash as _
def stressor_a(_idx, _data):
    _scope = {
        "stressor_a": None,
         "severity_a": None
         }
    # stressor_a refers to "too many bureaucrtic tasks"
    #stressor_a: (0,1) present/absent
    # 42% of physicians reported burnout , 55% of this population is living under stressor_a: 0.42*0.55=23% live under stressor_a
    _scope["stressor_a"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.77, 0.23],k=1)))
    #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_a"]==1:
        _scope["severity_a"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_a"]=0
    result = _.assign(_data[_idx], {"stressor_a": _scope["stressor_a"]},{"severity_a":_scope["severity_a"]})
    return result

def stressor_b(_idx, _data):
    _scope = {
        "stressor_b": None,
         "severity_b": None
         }
    # stressor_b refers to "spending too many hours at work"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 33% of this population is living under stressor_b: 0.42*0.33=10% live under stressor_a
    _scope["stressor_b"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.87, 0.13],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_b"]==1:
        _scope["severity_b"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_b"]=0
    result = _.assign(_data[_idx], {"stressor_b": _scope["stressor_b"]},{"severity_b":_scope["severity_b"]})
    return result

def stressor_c(_idx, _data):
    _scope = {
        "stressor_c": None,
         "severity_c": None
         }
    # stressor_b refers to "Lack of respect from administrators,employers,colleagues,or staff"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 32% of this population is living under stressor_b: 0.42*0.32=13% live under stressor_a
    _scope["stressor_c"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.87, 0.13],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_c"]==1:
        _scope["severity_c"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_c"]=0
    result = _.assign(_data[_idx], {"stressor_c": _scope["stressor_c"]},{"severity_c":_scope["severity_c"]})
    return result

def stressor_d(_idx, _data):
    _scope = {
        "stressor_d": None,
         "severity_d": None
         }
    # stressor_b refers to "Increasing computerization of practice (EHRs)"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 30% of this population is living under stressor_b: 0.42*0.3=12% live under stressor_a
    _scope["stressor_d"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.88, 0.12],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_d"]==1:
        _scope["severity_d"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_d"]=0
    result = _.assign(_data[_idx], {"stressor_d": _scope["stressor_d"]},{"severity_d":_scope["severity_d"]})
    return result

def stressor_e(_idx, _data):
    _scope = {
        "stressor_e": None,
         "severity_e": None
         }
    # stressor_b refers to "Insufficient compensation, reimbursement"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 29% of this population is living under stressor_b: 0.42*0.29=12% live under stressor_a
    _scope["stressor_e"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.88, 0.12],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_e"]==1:
        _scope["severity_e"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_e"]=0
    result = _.assign(_data[_idx], {"stressor_e": _scope["stressor_e"]},{"severity_e":_scope["severity_e"]})
    return result

def stressor_f(_idx, _data):
    _scope = {
        "stressor_f": None,
         "severity_f": None
         }
    # stressor_b refers to "Lack of control, autonomy"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 24% of this population is living under stressor_b: 0.42*0.24=10 live under stressor_a
    _scope["stressor_f"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.9, 0.1],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_f"]==1:
        _scope["severity_f"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_f"]=0
    result = _.assign(_data[_idx], {"stressor_f": _scope["stressor_f"]},{"severity_f":_scope["severity_f"]})
    return result

def stressor_g(_idx, _data):
    _scope = {
        "stressor_g": None,
         "severity_g": None
         }
    # stressor_b refers to "Feeling like a cog in a wheel"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 22% of this population is living under stressor_b: 0.42*0.22=9% live under stressor_a
    _scope["stressor_g"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.91, 0.08],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_g"]==1:
        _scope["severity_g"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_g"]=0
    result = _.assign(_data[_idx], {"stressor_g": _scope["stressor_g"]},{"severity_g":_scope["severity_g"]})
    return result

def stressor_h(_idx, _data):
    _scope = {
        "stressor_h": None,
         "severity_h": None
         }
    # stressor_b refers to "Decreasing reimbursements"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 19% of this population is living under stressor_b: 0.42*0.19=8% live under stressor_a
    _scope["stressor_h"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.92, 0.08],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_h"]==1:
        _scope["severity_h"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_h"]=0
    result = _.assign(_data[_idx], {"stressor_h": _scope["stressor_h"]},{"severity_h":_scope["severity_h"]})
    return result

def stressor_i(_idx, _data):
    _scope = {
        "stressor_i": None,
         "severity_i": None
         }
    # stressor_b refers to "Lack of respect from patient"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 17% of this population is living under stressor_b: 0.42*0.17=7% live under stressor_a
    _scope["stressor_i"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.93, 0.07],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_i"]==1:
        _scope["severity_i"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_i"]=0
    result = _.assign(_data[_idx], {"stressor_i": _scope["stressor_i"]},{"severity_i":_scope["severity_i"]})
    return result

def stressor_j(_idx, _data):
    _scope = {
        "stressor_j": None,
         "severity_i": None
         }
    # stressor_b refers to "Government regulations"
    #stressor_b: (0,1) present/absent
    # 42% of physicians reported burnout , 16% of this population is living under stressor_b: 0.42*0.16=6% live under stressor_a
    _scope["stressor_j"]= int(''.join(str(i) for i in random.choices(population=(0,1),weights=[0.84, 0.06],k=1)))
     #sverety of a stressor takes 4 levels :0 absent, 1 low 40%,2 medium 40%, 3 high 20%
    if _scope["stressor_j"]==1:
        _scope["severity_j"]= int(''.join(str(i) for i in random.choices(population=(1,2,3),weights=[0.4, 0.4,0.2],k=1)))
    else: 
         _scope["severity_j"]=0
    result = _.assign(_data[_idx], {"stressor_j": _scope["stressor_j"]},{"severity_j":_scope["severity_j"]})
    return result

def work_hours_patient(_idx, _data):

    _scope = {
        "work_hours_patient": None
       }
    #hours per week spent on seeing patients by gender
    if _data[_idx]["gender"] == 0:
        _scope["work_hours_patient"]=random.randrange(20, 60, 1)
    else:
        _scope["work_hours_patient"]=random.randrange(18, 54, 1)
        
    result = _.assign(_data[_idx], {"work_hours_patient": _scope["work_hours_patient"]})
    return result

def employment_status(_idx, _data):
    _scope = {
        "employment_status": None
    }

    # owner:  45.9% of a population of 8000 =3672
    if _idx in range(0, 3672, 1):
        _scope["employment_status"] = (1, "owner")

    # Employee: 47.4% of a population of 8000=3792
    elif _idx in range(3673, 7465, 1):
        _scope["employment_status"] = (2, "employee")

    else:
        _scope["employment_status"] = (3, "Independent contractor")

    result = _.assign(_data[_idx], {"employment_status": _scope["employment_status"]})

    return result


def antistress_program(_idx, _data):

    _scope = {
        "antistress_program": None
    }

    # 1: Yes : workplace offers a program to reduce stress 30% of a population of 8000=2400
    if _idx in range(0, 2400, 1):
        _scope["antistress_program"] = 1

    # 2: No : 48% of a population of 8000=3840
    if _idx in range(2401, 6241, 1):
        _scope["antistress_program"] = 2
    # 3: unspecified : 22% of a population of 8000
    else:
        _scope["antistress_program"] = 3

    result = _.assign(_data[_idx], {"anti_stress_program": _scope["antistress_program"]})

    return result

def self_esteem(_idx, _data):

    _scope = {
        "self_esteem": None
    }

    #self_esteem: ordinal variable 3: high, 2:  medium,3: low 
    # Allergist / Immunologist: range(0, 36, 1)
    if _idx in range(0, 36) :
        if _idx in range(0, 21): #59% have the highest self_esteem
            _scope["self_esteem"]=3
        elif  _idx in range(22, 29):#20% have medium self_esteem
            _scope["self_esteem"]=2
            
        else:  # 20% the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1
            
    # Anesthesiologist:  (36, 492, 1)      
      
    elif _idx in range(36, 493, 1):
        if _idx in range(36, 282): #54% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(282, 387):  #23% have medium self_esteem
            _scope["self_esteem"]=2
        else: # 23% the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1
            
    # Dermatologist: range(492, 614)
    
    elif _idx in range(492, 612):
        if _idx in range(492, 560):# 56% have the highest self_esteem
            _scope["self_esteem"]=3
        elif  _idx in range(560,584):#20% have medium self_esteem
            _scope["self_esteem"]=2
            
        else:  # 20% the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1    
              
    # Emergency Doctor: range(614,1092)
    elif _idx in range(614,1092):
        if _idx in range(614, 891):#58% have the highest self_esteem
            _scope["self_esteem"]=3 
        elif _idx in range(891, 991):#21% have medium self_esteem
            _scope["self_esteem"]=2 
        else:   #21% the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1
            
    # Family Doctor: range(1092,2212)  
    elif _idx in range(1092,2212):
        if _idx in range(1092, 1663):# 51% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(1663,1943):#25%have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1
    
   # Internist:  range(2212,4284)
    elif _idx in range(2212,4284):
        if _idx in range(2212,3248):#50% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(3248,3767):#25%have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1
                
    # Neurological Surgeon: range(4284,4343)
    elif _idx in range(4284,4343):
        if _idx in range(4284, 4316):# 55% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(4316,4330):# 23% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1 
            
    # Obstetrician / Gynecologist:range(4343,4757)
    elif _idx in range(4343,4757):
        if _idx in range(4343, 4571):# 55% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(4571,4667):# 23% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1 
            
   # Orthopedic Surgeon: range(4757,5018)
    elif _idx in range(4757,5018):
        if _idx in range(4757, 4929):# 66% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(4929,4973):# 17% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1 
                
  # Otolaryngologist: range(5018,5121)
    elif _idx in range(5018,5121):
        if _idx in range(5018, 5087):# 67% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(5087,5105):# 17% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1
            
  # Pathologist: range(5121,5289)
    elif _idx in range(5121,5289):
        if _idx in range(5121, 5207):# 51% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(5207,5250):# 25% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1 
                
    # Pediatrician: range(5289,6044)    
    elif _idx in range(5289,6044):
        if _idx in range(5289, 5689):# 53% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(5689,5871):# 24% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1 
            
   # Plastic Surgeons: range(6044,6087)    
    elif _idx in range(6044,6087):
        if _idx in range(6044, 6075):# 73%  have the highest self_esteem
             _scope["self_esteem"]=3
        elif _idx in range(6075,6081):# 14% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1 
            
     # Psychiatrist/Neurologist: range(6087,6722)
    elif _idx in range(6087,6722):
        if _idx in range(6087, 6424):#53% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(6424,6577):# 24% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1 
                
   # Radiologist: range(6722,7133)   
    elif _idx in range(6722,7133):
        if _idx in range(6722, 6956):#57% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(6956,7043):# 22% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1 
            
  # Surgeons:  range(7133,7473)
    elif _idx in range(7133,7473):
        if _idx in range(7133, 7347):#63% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(7347,7412):# 19% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1
               
   # Urologist: range(7473,7576)
    elif _idx in range(7473,7576):
        if _idx in range(7473, 7543):#68% have the highest self_esteem
            _scope["self_esteem"]=3
        elif _idx in range(7543,7560):# 16% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1

    #Optometrist: (7576,8000)
    
    else:
        if _idx in range(7576, 7876):#67% have the highest self_esteem
            _scope["self_esteem"]=1
        
        elif _idx in range(7876,7953):# 17% have medium self_esteem
            _scope["self_esteem"]=2
        else: #the population that remains have the lowest self_esteem
            _scope["self_esteem"]=1


    result = _.assign(_data[_idx], {"self_esteem":_scope["self_esteem"]})
    return result

def specialties(_idx, _data):

    _scope = {
        "speciality": None,
        "salary": None
    
    }

    # Allergist / Immunologist: 0.45% of a population of 8000 =36 
    if _idx in range(0, 36, 1):
        _scope["speciality"] = (1, "Allergist / Immunologist")
     # avg salary: 275000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(247500, 302500, 2)
        else:
            _scope["salary"] = random.randrange(169400, 211750, 2)
            
        

    # Anesthesiologist:  5.7% of a population of 8000 = 456
    elif _idx in range(36, 492, 1):
        _scope["speciality"] = (2, "Anesthesiologist")
      # avg salary: 392000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] =  random.randrange(352800, 431200, 2)
        else:
            _scope["salary"] = random.randrange(246960, 301840, 2)
            
      

       
            
    # Dermatologist: 1.52% of a population of 8000 = 122
    elif _idx in range(492, 614):
        _scope["speciality"] = (3, "Dermatologist")
     # avg salary: 419000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(377100, 460900, 2)
        else:
            _scope["salary"] = random.randrange(263970, 322630, 2)
            
       
              
    # Emergency Doctor: 5.98% of a population of 8000 = 478
    elif _idx in range(614,1092):
        _scope["speciality"] = (4, "Emergency Doctor")
     # avg salary: 353000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(317700, 388300, 2)
        else:
            _scope["salary"] = random.randrange(222390, 271810, 2)
            
       
    
    # Family Doctor: 14% of a population of 8000 = 1120
    elif _idx in range(1092,2212):
        _scope["speciality"] = (5, "Family Doctor")
      #  avg salary: 230000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(207000, 253000, 2)
        else:
            _scope["salary"] = random.randrange(144900, 177100, 2)
    
      
   # Internist: 25.9% of a population of 8000 = 2072
    elif _idx in range(2212,4284):
        _scope["speciality"] = (6, "Internist")
    # avg salary: 243000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(218700, 267300, 2)
        else:
            _scope["salary"] = random.randrange(153090, 187110, 2)
    
      
    # Neurological Surgeon: 0.73% of a population of 8000 = 59
    elif _idx in range(4284,4343):
        _scope["speciality"] = (7, "Neurological Surgeon")

        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(697500, 852500, 2)
        else:
            _scope["salary"] = random.randrange(488250, 596750, 2)
            
      
            
    # Obstetrician / Gynecologist: 5.17% of a population of 8000 = 414
    elif _idx in range(4343,4757):
        _scope["speciality"] = (8, "Obstetrician / Gynecologist")
      # avg salary: 303000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(272700, 333300, 2)
        else:
            _scope["salary"] = random.randrange(190890, 233310, 2)
            
        
            
   # Orthopedic Surgeon: 3.26% of a population of 8000 = 261
    elif _idx in range(4757,5018):
        _scope["speciality"] = (9, "Orthopedic Surgeon")
      # avg salary: 482000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(433800, 530200, 2)
        else:
            _scope["salary"] = random.randrange(303660, 371140, 2)
            
        
  # Otolaryngologist: 1.29% of a population of 8000 = 103
    elif _idx in range(5018,5121):
        _scope["speciality"] = (10, "Otolaryngologist")
   # avg salary:461000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(414900, 507100, 2)
        else:
            _scope["salary"] = random.randrange(290430, 354970, 2)
            
     
  # Pathologist: 2.1% of a population of 8000 = 168
    elif _idx in range(5121,5289):
        _scope["speciality"] = (11, "Pathologist")
    # avg salary: 308000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(277200, 338800, 2)
        else:
            _scope["salary"] = random.randrange(194040, 237160, 2)
        
          
                
    # Pediatrician: 9.44% of a population of 8000 = 755
    elif _idx in range(5289,6044):
        _scope["speciality"] = (12, "Pediatrician")
     # avg salary: 225000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(202500, 247500, 2)
        else:
            _scope["salary"] = random.randrange(141750, 173250, 2)
            
       
            
   # Plastic Surgeons:  0.54% of a population of 8000 = 43
    elif _idx in range(6044,6087):
        _scope["speciality"] = (13, "Plastic Surgeons")
       # avg salary: 471000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(423900, 518100, 2)
        else:
            _scope["salary"] = random.randrange(296730, 362670, 2)
             
            
     # Psychiatrist/Neurologist:  7.93% of a population of 8000 = 635
    elif _idx in range(6087,6722):
        _scope["speciality"] = (14, "Psychiatrist/Neurologist")
     # avg salary: 260000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(234000, 286000, 2)
        else:
            _scope["salary"] = random.randrange(163800, 200200, 2)
            

                
   # Radiologist:   5.14% of a population of 8000 = 411
    elif _idx in range(6722,7133):
        _scope["speciality"] = (15, "Radiologist")
     # avg salary : 419000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(377100, 460900, 2)
        else:
            _scope["salary"] = random.randrange(263970, 322630, 2)
     
            
  # Surgeons: 4.24%  of a population of 8000 = 340
    elif _idx in range(7133,7473):
        _scope["speciality"] = (16, "Surgeons")
     # avg salary: 362000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(325800, 398200, 2)
        else:
            _scope["salary"] = random.randrange(228060, 278740, 2)
            
      
            
   # Urologist: 1.29%  of a population of 8000 = 103
    elif _idx in range(7473,7576):
        _scope["speciality"] = (17, "Urologist")
     # avg salary: 408000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(367200, 448800, 2)
        else:
            _scope["salary"] = random.randrange(257040, 314160, 2)
            
       
    #Optometrist: 5.6% of a population of 8000 = 448
    else:
        _scope["speciality"] = (18, "Optometrist")
     #avg salary: 366000
        if _data[_idx]["gender"] == 0:
            _scope["salary"] = random.randrange(329400, 402600, 2)
        else:
            _scope["salary"] = random.randrange(230580, 281820, 2)
            

    result = _.assign(_data[_idx], {"salary": _scope["salary"], "speciality": _scope["speciality"]})
    return result
