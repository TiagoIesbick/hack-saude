from ariadne import QueryType, ObjectType, MutationType
from datetime import datetime
from pytz import timezone
from db.queries import *
from db.mutations import *
from utils.utils import encrypt, validate_email, validate_password, \
    validate_name, generate_token
from auth import handle_login
import nh3


query = QueryType()
users = ObjectType("Users")
patients = ObjectType("Patients")
doctors = ObjectType("Doctors")
mutation = MutationType()
medical_records = ObjectType("MedicalRecords")
tokens = ObjectType("Tokens")
token_access = ObjectType("TokenAccess")

@query.field("user")
def resolve_user(*_, userId):
    return get_user(userId)

@users.field("patient")
def resolve_users_patient(users, *_):
    if not users['userId']:
        return None
    return get_users_patient(users['userId'])

@users.field("doctor")
def resolve_users_patient(users, *_):
    if not users['userId']:
        return None
    return get_users_doctor(users['userId'])

@patients.field("user")
def resolve_patients_user(patients, *_):
    if not patients['userId']:
        return None
    return get_user(patients['userId'])

@patients.field("tokens")
def resolve_patients_tokens(patients, info):
    if not info.context['authenticated'] or not patients['patientId']:
        return None
    return get_patients_tokens(patients['patientId'])

@doctors.field("user")
def resolve_doctors_user(doctors, *_):
    if not doctors['userId']:
        return None
    return get_user(doctors['userId'])

@doctors.field("tokensAccess")
def resolve_doctors_user(doctors, info):
    if not info.context['authenticated'] or not doctors['doctorId']:
        return None
    return get_doctors_tokens_access(doctors['userId'])

@mutation.field("createUser")
def resolve_create_user(*_, input):
    email, firstName, lastName, password, userType, acceptTerms = \
        input['email'], input['firstName'].strip().capitalize(), input['lastName'].strip().capitalize(), input['password'], input['userType'], input['acceptTerms']
    if not validate_email(email):
        return { 'userError': 'Invalid e-mail'}
    if not validate_name(firstName):
        return { 'userError': 'First name must start with at least 2 word characters' }
    if not validate_name(lastName):
        return { 'userError': 'Last name must start with at least 2 word characters' }
    if not validate_password(password):
        return { 'userError': 'Invalid password' }
    res = create_user(
        email,
        nh3.clean(firstName),
        nh3.clean(lastName),
        encrypt(password),
        userType,
        acceptTerms
    )
    if res['userConfirmation']:
        res['user'] = get_user_by_email_password(email, password)
    return res

@mutation.field("createPatientOrDoctorUser")
def resolve_create_patient_or_doctor_user(*_, userId, userType):
    res = create_patient_or_doctor_user(userId, userType)
    if res['userConfirmation']:
        res['user'] = get_user(userId)
    return res

@mutation.field("updateUser")
def resolve_update_user(_, info, input):
    if not info.context['authenticated']:
        return {'userError': 'Missing authentication'}
    email, firstName, lastName, userId = \
        input['email'], input['firstName'].strip().capitalize(), \
        input['lastName'].strip().capitalize(), info.context['user_detail']['userId']
    if not validate_email(email):
        return { 'userError': 'Invalid e-mail'}
    if not validate_name(firstName):
        return { 'userError': 'First name must start with at least 2 word characters' }
    if not validate_name(lastName):
        return { 'userError': 'Last name must start with at least 2 word characters' }
    res = update_user(email, nh3.clean(firstName), nh3.clean(lastName), userId)
    if res['userConfirmation']:
        res['user'] = get_user(userId)
        res['token'] = handle_login(res['user'])
    return res

@mutation.field("updatePatientUser")
def resolve_update_patient_user(_, info, input):
    if not info.context['authenticated']:
        return {'userError': 'Missing authentication'}
    patient = get_users_patient(info.context['user_detail']['userId'])
    if not patient:
        return {'userError': 'Missing patient credential'}
    # as my mysql database is recording dates in the Brazilian time zone, it is necessary to transform the date to my respective time zone,
    # if your mysql database is recording dates in different time zone, transform the 'dateOfBirth' variable into your respective time zone
    dateOfBirth = datetime.fromisoformat(input['dateOfBirth']).astimezone(timezone('America/Sao_Paulo')).strftime("%Y-%m-%d")
    res = update_patient_user(dateOfBirth, input['gender'], patient['patientId'])
    if res['userConfirmation']:
        res['user'] = get_user(info.context['user_detail']['userId'])
    return res

@mutation.field("updateDoctorUser")
def resolve_update_doctor_user(_, info, input):
    if not info.context['authenticated']:
        return {'userError': 'Missing authentication'}
    doctor = get_users_doctor(info.context['user_detail']['userId'])
    if not doctor:
        return {'userError': 'Missing doctor credential'}
    res = update_doctor_user(nh3.clean(input['specialty'].strip().capitalize()), nh3.clean(input['licenseNumber'].strip()), doctor['doctorId'])
    if res['userConfirmation']:
        res['user'] = get_user(info.context['user_detail']['userId'])
    return res

@mutation.field("login")
def resolve_login(*_, email, password):
    user = get_user_by_email_password(email, password)
    if user:
        token = handle_login(user)
        return { 'user': user, 'token': token }
    return { 'error': 'Invalid email or password' }

@query.field("medicalRecords")
def resolve_medical_records(_, info):
    if not info.context['authenticated']:
        return None
    if info.context['user_detail']['userType'] != 'Patient':
        return None
    patient = get_users_patient(info.context['user_detail']['userId'])
    if not patient:
        return None
    return get_medical_records_by_pacient(patient['patientId'])

@query.field("medicalRecordsByPatientId")
def resolve_medical_records_by_patient_id(_, info, patientId):
    if not info.context['authenticated']:
        return None
    if info.context['user_detail']['userType'] != 'Doctor':
        return None
    return get_medical_records_by_pacient(patientId)

@medical_records.field("recordType")
def resolve_medical_records_type(medicalRecords, *_):
    return get_medical_records_type(medicalRecords['recordTypeId'])

@query.field("activePatientTokens")
def resolve_patients_active_tokens(_, info):
    if not info.context['authenticated']:
        return None
    if info.context['user_detail']['userType'] != 'Patient':
        return None
    patient = get_users_patient(info.context['user_detail']['userId'])
    if not patient:
        return None
    return get_active_tokens_by_patient(patient['patientId'])

@query.field("activeDoctorTokens")
def resolve_doctors_active_tokens(_, info):
    if not info.context['authenticated']:
        return None
    if info.context['user_detail']['userType'] != 'Doctor':
        return None
    doctor = get_users_doctor(info.context['user_detail']['userId'])
    if not doctor:
        return None
    return get_active_tokens_by_doctor(doctor['doctorId'])

@mutation.field("generateToken")
def resolve_generate_token(_, info, expirationDate):
    if not info.context['authenticated']:
        return {'tokenError': 'Missing authentication'}
    patient = get_users_patient(info.context['user_detail']['userId'])
    if not patient:
        return {'tokenError': 'Missing patient credential'}
    # as my mysql database is recording dates in the Brazilian time zone, it is necessary to transform the date to my respective time zone,
    # if your mysql database is recording dates in different time zone, transform the 'exp' variable into your respective time zone
    exp = datetime.fromisoformat(expirationDate).astimezone(timezone('America/Sao_Paulo')).strftime("%Y-%m-%d %H:%M:%S")
    reserve_tokenId = reserve_token_id(patient['patientId'], exp)
    if reserve_tokenId['tokenError']:
        return {'tokenError': reserve_tokenId['tokenError']}
    token = generate_token(
        expirationDate,
        {
            'patientId': patient['patientId'],
            'userId': patient['userId'],
            'tokenId': reserve_tokenId['tokenId']
        }
        )
    res = create_token(reserve_tokenId['tokenId'], token)
    if res['tokenError']:
        return {'tokenError': res['tokenError']}
    if res['tokenConfirmation']:
        res['token'] = get_token(reserve_tokenId['tokenId'])
    return res

@mutation.field("saveTokenAccess")
def resolve_save_token_access(_, info, tokenId, doctorId):
    if not info.context['authenticated']:
        return {'acessError': 'Missing authentication'}
    if info.context['user_detail']['userType'] != 'Doctor':
        return {'acessError': 'Missing healthcare professional credential'}
    return create_token_access(tokenId, doctorId)

@tokens.field("patient")
def resolve_tokens_patient(tokens, info):
    if not info.context['authenticated'] or not tokens['patientId']:
        return None
    return get_patient(tokens['patientId'])

@tokens.field("tokenAccess")
def resolve_tokens_token_access(tokens, info):
    if not info.context['authenticated'] or not tokens['tokenId']:
        return None
    return get_tokens_token_access(tokens['tokenId'])

@token_access.field("token")
def resolve_token_access_token(tokenAccess, info):
    if not info.context['authenticated'] or not tokenAccess['tokenId']:
        return None
    return get_token_access_token(tokenAccess['tokenId'])

@token_access.field("doctor")
def resolve_token_access_doctor(tokenAccess, info):
    if not info.context['authenticated'] or not tokenAccess['tokenId']:
        return None
    return get_doctor(tokenAccess['doctorId'])
