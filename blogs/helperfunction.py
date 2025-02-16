from sqlalchemy.orm import Session
from .models import BlogModel
from uuid import UUID

def validateBlogData(data:dict,db:Session):
    validateData={}
    if not data.get('title') or str(data.get('titile')).isspace():
        return{
            'status':False,
            'message':'Please insert title',
            'code' : "TITLE-400001"
            
        }
    else:
        validateData.update(title=data.get('title'))
              
    if not data.get('body'):
       return{
           'status':False,
           'message':'Please insert body',
           'code':"BODY-400002"
       }
    else:   
        validateData.update(body=data.get('body'))
    if not data.get('articleName'):
        return{
            'status':False,
            'message':'please enter Article Name',
            'code':'ARTICLENAME-400003'
        }   
    else:   
        validateData.update(articleName=data.get('articleName'))
    return{
        'status':True,
        "message":"validate successful",
        'code': "VALIDATE-20000",
        'data':validateData
    }
def validateListData(data:dict,db:Session):
    validateData={}
    if str(data.get('blogId')).strip():
        if str(data.get('blogId')).isspace():
            return{
                'satus':False,
                'message':'Please select userId ',
                'code':'BLOGID-400004'
            } 
        try:
             UUID(str(data.get('blogId')).strip())
        except ValueError:
            return{
                'status':False,
                'message':'Invalid value',
                'code':'UUID-400005'
            }    
        print("!111111111111111111111111111111111111111")    
        try:
           validateData=db.query(BlogModel).filter(BlogModel.blogId==data.get('blogId')).first()
           if not validateData:
               return{
                 'status':False,
                 'message':'Blog doesnot exist',
                 'code':"VALIDATION-400006"
            }
        except Exception as error:
            return{
             'status':False,
             'message':f"User id is not found or {error}",
             'code':'VALIDATE DATA-400012'
            }             
    return{
            'status':True,
            'message':'Blog found sucessfully',
            'code':'VALIDATE-20001',
            'blogId':data.get('blogId')
        }     

def validateDeleteData(data:dict,db:Session):
    validatedata={}
    if str(data.get('blogId')).strip():
        if str(data.get('blogId')).isspace():
            return{
                'status':False,
                'message':'Please select blog Id',
                'code':'BLOGID-400013'
            }                  
        try:
            UUID(str(data.get('blogId')).strip())
        except ValueError:
            return{
                'status':False,
                'message':'Invalid value',
                'code':'UUID-400014'
            }
        try:
            validatedata=db.query(BlogModel).filter(BlogModel.blogId==data.get('blogId')).first()
            if not validatedata:
                return{
                    'status':False,
                    'message':'Blog doesnot exist',
                    'code':'VALIDATEDATA-400015'
                }
        except Exception as error:
            return{
                'status':False,
                'message':f'Blog not found or {str(error)}',
                'code':'VALIDATE DATA-400016'
            }    
    return{
        'status':True,
        'message':'Blog found successfully',
        'code':'DELETE BLOG-20002',
        'blogId':data.get('blogId')
    }                       
def validateUpdateData(data:dict,db:Session):
    validated={}
    if not data.get('title') or str(data.get('title')).isspace():
        return{
            'status':False,
            'message':'Please insert title',
            'code':'TITLE-400017'
        }
    else:
        validated.update(title=data.get('title'))
    if not data.get('body') or str(data.get('body')).isspace():
        return{
            'status':False,
            'message':'Please insert body',
            'code':'BODY-400018'
        }  
    else:
        validated.update(body=data.get('body'))
    if not data.get('published') or str(data.get('published')).isspace():
        return{
            'status':False,
            'message':'Please select published or on published',
            'code':'PUBLISHED-400019'            
        }
    else:
        validated.update(published=data.get('published'))
    if not data.get('articleName') or str(data.get('articleName')).isspace():
        return{
            'status':False,
            'message':'Please insert article name',
            'code':'ARTICLENAME-400020'            
        }  
    else:
        validated.update(articleName=data.get('articleName'))
    return{
        'status':True,
        'message':'Validated Sucessfully',
        'code':'VALIDATION-20003',
        'data':validated
    }    

def validateBlogExistance(blogId,db:Session):
    try:
        blog=db.query(BlogModel).filter(BlogModel.blogId==blogId).first()
        if not blog:
            return{
                'status':False,
                'message':'Blog not found ',
                'code':'NOTFOUND-400021'
                    
            }
        return{
            'status':True,
            'message':'Validated sucessfully',
            'code':'BLOGCHECK-20004',
            'blog':blog
        }  
    except Exception as e:
        return {
            'status': False,
            'message': f"Error checking blog existence: {str(e)}",
            'code': 'BLOGCHECK-400022'
        }
          
            
                
                  