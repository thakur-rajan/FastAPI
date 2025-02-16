from sqlalchemy.orm import Session
from.models import UserModel
from uuid import UUID
from auth import Hash
import re
def validateUserData(data:dict,db:Session):
    validateData={}
    if not data.get('firstName') or str(data.get('firstName')).isspace():
        return{
            'status':False,
            'message':'please insert first name',
            'code':'FIRST NAME-400001'
        
        }
    else:   
        validateData.update(firstName=data.get('firstName')) 
    if not data.get('lastName') or str(data.get('lastName')).isspace():
        return{
            'status':False,
            'message':'please insert last name',
            'code':'LAST NAME-400002'
        }
    else:
        validateData.update(lastName=data.get('lastName'))
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not data.get('email') or str((data.get('email'))).isspace():
        return{
            'status':False,
            'message':'please insert email',
            'code':'EMAIL-400003'
        }
    elif not re.match(pattern,data.get('email')):
        return{
            'status':False,
            'message':'invalid email',
            'code':'EMAIL-400004'
        } 
    else:
        if str(data.get('email')).isupper():
            return{
                 'status':False,
                'message':'Email not in upper case',
                'code':'EMAIL-400005'
            }
        else:
            validateData.update(email=data.get('email'))
    if not data.get('phoneNo') or str(data.get('phoneNo')).isspace():
        return{
            'status':False,
            'message':'please enter phone number',
            'code':'PHONENO-400006'
        }
    else:
        validateData.update(phoneNo=data.get('phoneNo')) 
    
    if not data.get('adharNo') or   str(data.get('adharNo')).isspace():
        
        return{
            'status':False,
            'message':'please enter adhar number',
            'code':'ADHARNO-400007'
        } 
    else:
        validateData.update(adharNo=data.get('adharNo'))
    if not data.get('password') or str(data.get('password')).isspace():
        return{
            'status':False,
            'message':'please insert password',
            'code':'PASSWORD-400008'
        }
    else:
        validateData.update(password=Hash.bycrypt(data.get('password')))
    
    return{
        'status':True,
        'message':'validated successful',
        'code':'VALIDATE-200001',
        'data':validateData
    }                                 
def validateListData(data:dict,db:Session):
    validateData={}
    if str(data.get('userId')).strip():
        if str(data.get('userId')).isspace():
            return{
            'status':False,
            'message':'Please select user',
            'code':'USERID-400009'
            
        }
           
        try:
            UUID(str(data.get('userId')).strip())
        except ValueError:
            return{
                'status':False,
                'message':'Invalid user',
                'code':'UUID-400010'
            }          
     
                  
        try:
            validateData=db.query(UserModel).filter(UserModel.userId==data.get('userId')).first()
            if not validateData:
                return{
                     'status':False,
                     'message':'user not exist',
                     'code':'VALIDATEDATA-11'
                }
                
        except Exception as error:
            return{
                'status':False,
                'message':f"User id is not found or {error}",
                'code':'VALIDATE DATA-400012'
            }  
            
    return{
        'status':True,
        'message':'validation sucessful',
        'code':'VALIDATE-20002',
        'userId':data.get('userId')   
    }
def validateDeleteData(data:dict,db:Session):
    validateData={}
    if str(data.get('userId')).strip():
        if str(data.get('userId')).isspace():
            return{
            'status':False,
            'message':'Please select user',
            'code':'USERID-4000013'
            
        }
           
        try:
            UUID(str(data.get('userId')).strip())
        except ValueError:
            return{
                'status':False,
                'message':'Invalid user',
                'code':'UUID-400014'
            }          
        try:
            print("000000000000000000000000000000000")         
            validateData=db.query(UserModel).filter(UserModel.userId==data.get('userId')).first()
            if not validateData:
                return{
                     'status':False,
                     'message':'user not exist',
                     'code':'VALIDATEDATA-400015'
                }
                
        except Exception as error:
            return{
                'status':False,
                'message':f"User id is not found or {error}",
                'code':'VALIDATE DATA-400016'
            }  
            
    return{
        'status':True,
        'message':'validation sucessful',
        'code':'VALIDATE-20002',
        'userId':data.get('userId')   
    }
    

def validateUpdateData(data: dict, db: Session):
    """
    Validates the user data during an update. Allows fields to be optional.
    Only the provided fields will be updated.
    """
    validateData = {}

    
    if not data.get('firstName') and str(data.get('firstName')).isspace():
        return{
            'status':False,
            'message':'Please insert first name',
            'code':'FIRSTNAME-400017'
        }
    
    else:    
       validateData.update(firstName=data.get('firstName'))

    
    if not data.get('lastName') and str(data.get('lastName')).isspace():
        return{
            'status':False,
            'message':'Please insert Last name',
            'code':'LASTNAME-400018'
        }
    else:    
        validateData.update(lastName=data.get('lastName'))

    if data.get('email'):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if str(data.get('email')).isspace():
            return {
                'status': False,
                'message': 'Please insert email',
                'code': 'EMAIL-400019'
            }
        elif not re.match(pattern, data.get('email')):
            return {
                'status': False,
                'message': 'Invalid email',
                'code': 'EMAIL-400020'
            }
        elif str(data.get('email')).isupper():
            return {
                'status': False,
                'message': 'Email should not be in upper case',
                'code': 'EMAIL-400021'
            }
        else:
            validateData.update(email=data.get('email'))


    if not data.get('phoneNo') and str(data.get('phoneNo')).isspace():
        return{
            'status':False,
            'message':'please insert phone Number',
            'code':'PHONE NUMBER-400022'
        }
    else:    
        validateData.update(phoneNo=data.get('phoneNo'))

    if not data.get('adharNo') and str(data.get('adharNo')).isspace():
        return{
            'status':False,
            'message':'please insert adharNo',
            'code':'ADAHARNUMBER-400023'           
        }
    else:    
        validateData.update(adharNo=data.get('adharNo'))
        
    if not data.get('password') and str(data.get('password')).isspace():
        return{
            'status':False,
            'message':'please insert password',
            'code':'PASSWORD-400023'            
        }
    else:    
        validateData.update(password=Hash.bycrypt(data.get('password')))

    return {
        'status': True,
        'message': 'Validation successful',
        'code': 'VALIDATE-200001',
        'data': validateData
    }


def validateUserExistence(userId: str, db: Session):
    """
    Validates if the user exists in the database.
    """
    try:
        user = db.query(UserModel).filter(UserModel.userId == userId).first()
        if not user:
            return {
                'status': False,
                'message': 'User not found',
                'code': 'USERNOTFOUND-400024'
            }
        return {
                'status': True,
                'message':'Vaalidated sucessfull',
                'code':'EXISTANCE-400025',
                'user': user
                }
    except Exception as e:
        return {
            'status': False,
            'message': f"Error checking user existence: {str(e)}",
            'code': 'USERCHECK-500001'
        }
    
def validateLoginData(data:dict,db:Session):
    validate={}    
    
    if str(data.get('userId')).strip():
        if str(data.get('userId')).isspace():
            return{
                'status':False,
                'message':'Please insert user id',
                'code':'LOGUSERID-400026'
                
            }
        try:
            UUID(str(data.get('userId')).strip())
        except ValueError:
            return{
                'status':False,
                'message':'Invalid user',
                'code':'UUID-400027'
                    
            }
            
        try:
            validate=db.query(UserModel).filter(UserModel.userId==data.get('userId')).first()
            if not validate:
                return{
                    'status':False,
                    'message':'User doesnot exist',
                    'code':'VALIDATE-400028'
                }            
        except Exception as error:
            return{
                'status':False,
                'message':f"User id is not found or {error}",
                'code':'VALIDATE DATA-400029'
            }  
    if not data.get('password') or str(data.get('password')).isspace():
        return{
                'status':False,
                'message':'Please insert password',
                'code':'PASSWORD-400030'
            }
    password=data.get('password')    
    if not Hash.verify(password,validate.password):
        return{
            'status':False,
            'message':'Incorrect password',
            'code':'INCORECTPASSWORD-400031'
        }
    return{
        'status':True,
        'message':'Validated sucessfully',
        'code':'VALIDATELOGINDATA-200002',
        'data':validate
    }    
             
                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












































    
    
# def validateLoginData(data:dict,db:Session):
#    try: 
#      if not data.get('userId') or str(data.get('userId')).isspace():
#          return{
#              'status':False,
#              'message':'Please select userId',
#              'code':'USERID-400017'
#          }  
#      userId= str(data.get('userId')).strip()
#      if not data.get('password') or str(data.get('password')).isspace():
#          return{
#              'status':False,
#              'message':'Please select password',
#              'code':'PASSWORD-400018'
#          }  
#      password=str(data.get('password')).strip()
#      try:
#          userData=db.query(UserModel).filter(UserModel.userId==userId)
#      except Exception as e:
#          return{
#              'status':False,
#              'message':f'Internal server error or {str(e)}',
#              'code':'USERDATA-400019'
#          }     
#      if not userData.first():
#          return{
#              'status':False,
#              'message':"Invalid Credentials" ,
#              'code':'USER-LOGIN-400020' 
             
#         }         
#      print(f"Verifying password: {password} with stored hash: {userData.first().password}")
#     #  if not Hash.verify(password,userData.first().password):
#     #       return{
#     #           'status':False,
#     #           'message':'Incorrect password',
#     #           'code':'VERIFY-400021'
              
#     #       }     
#      print("===============================================")    
#    except Exception as e:
#        return{
#             'status':False,
#              'message':f'Internal server error or {str(e)}',
#              'code':'VALIDATELOGIN-400022'
#        }
#    return{
#         'status':True,
#         'message':'Validated sucessful',
#         'code':'VALIDATE-20003',
#         'data':userData
        
#     }
    
    
    
    
    
# def validateLoginData(data:dict,db:Session):  
#     validateData={}
#     if not data.get('password') or str(data.get('password')).isspace():
#         return{
#             'status':False,
#             'message':'Pllease insert password',
#             'code':'PASSWORD-400016'
#         }   
#     else:
#         validateData.update(password=data.get('password'))
#     if str(data.get('userId')).strip():
#         if str(data.get('userId')).isspace():
#             return{
#                 'status':False,
#                 'message':'Please select user',
#                 'code':'USERID-4000017'
#             }
#         try:
#             UUID(str(data.get('userId')).strip()) 
#         except Exception as error:
#             return{
#                 'status':False,
#                 'message':'Invalid user',
#                 'code':'UUID-400018'
                
#             }  
#         try:
#             Data=db.query(UserModel).filter(UserModel.userId==data.get('userId')).first()
#             if not validateData:
#                 return{
#                     'status':False,
#                     'message':'User is not found',
#                     'code':'USERLOGIN-400019'
#                 }  
#         except Exception as error:
#             return{
#                 'status':False,
#                 'message':f"User id is not found or {error}",
#                 'code':'USERID-400020'
#             } 
#         if not Hash.verify(validateData.password,data.get('password')):
#             return{
#                 'status':False,
#                 'message':'Incorrect password',
#                 'code':'PASSWORD-400021'
#             }                
  
  

#     return{
#         'status':True,
#         'message':'validated successful ',
#         'code':'PASSWORD-20003',
#         'data':validateData
#     }        
        
                    
# def validateUpdateData(data:dict,db:Session):
#     validateData={}
#     if str(data.get('UserId')).strip():
#         if str(data.get('firstName')).isspace():
#             return{
#                 'status':False,
#                 'message':'Please select userid',
#                 'code':'USERID=400017'
#             }
#         try:
#             UUID(str(data.get('userId')).strip())
#         except Exception as error:
#             return{
#                 'status':False,
#                 'message':f'Internal server error or {str(error)}',
#                 'code':'UUID-400018'
                    
#             }
#     # userData=db.query(UserModel).filter(UserModel.userId==data.get('userId')).first()
#     # if userData is None:
#     #     return {
#     #         'status': False,
#     #         'message': 'User not found',
#     #         'code': 'USER_NOT_FOUND'
#     #     }
     
#     try:                
            
#         # if UserModel.userId==userData.userId:
#                if not data.get('firstName') or str(data.get('firstName')).isspace():
#                     return{
#                         'status':False,
#                         'message':'Please insert first name',
#                         'code':'FIRSTNAME-400019'
#                     }
#                else:
#                     validateData.update(firstName=data.get('firstName'))               
        
#                if not data.get('lastName') or str(data.get('lastName')).isspace():
#                     return{
#                         'status':False,
#                         'message':'please insert last name',
#                         'code':'LAST NAME-400020'
#                     }
#                else:
#                    validateData.update(lastName=data.get('lastName'))
#                pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#                if not data.get('email') or str((data.get('email'))).isspace():
#                    return{
#                        'status':False,
#                        'message':'please insert email',
#                        'code':'EMAIL-400021'
#                    }
#                elif not re.match(pattern,data.get('email')):
#                    return{
#                        'status':False,
#                        'message':'invalid email',
#                        'code':'EMAIL-400022'
#                    } 
#                else:
#                    if str(data.get('email')).isupper():
#                         return{
#                             'status':False,
#                            'message':'Email not in upper case',
#                            'code':'EMAIL-400023'
#                        }
#                    else:
#                        validateData.update(email=data.get('email'))
#                if not data.get('phoneNo') or str(data.get('phoneNo')).isspace():
#                    return{
#                           'status':False,
#                        'message':'please enter phone number',
#                        'code':'PHONENO-400024'
#                    }
#                else:
#                    validateData.update(phoneNo=data.get('phoneNo')) 
               
#                if not data.get('adharNo') or   str(data.get('adharNo')).isspace():
                   
#                    return{
#                        'status':False,
#                         'message':'please enter adhar number',
#                        'code':'ADHARNO-400025'
#                    } 
#                else:
#                    validateData.update(adharNo=data.get('adharNo'))
#                print('7777777777777777777777777777777777777777')
   
#                if not data.get('password') or str(data.get('password')).isspace():
#                    return{
#                        'status':False,
#                        'message':'please insert password',
#                        'code':'PASSWORD-400026'
#                                   }
#                else:
#                    validateData.update(password=data.get('password'))
#                return{
#                     'status':True,
#                     'message':'validated sucessfuly',
#                     'code':'VALIDATION-20003',
#                     'data':validateData
#                 }       
               
#     except Exception as error:
#         return{
#             'status':False,
#             'message':f'Internal server error or {str(error)}',
#             'code':'VALIDATE DATA-400027'
#         }
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                    