import { gql } from '@apollo/client';
import { doctorDetailFragment, patientDetailFragment, userDetailFragment } from './mutations';

const medicalRecordsFragment = gql`
    fragment MedicalRecordsDetail on MedicalRecords {
        recordId
        recordData
        dateCreated
        recordType {
            recordTypeId
            recordName
        }
    }
`;

export const medicalRecordsQuery = gql`
    query medicalRecords {
        medicalRecords {
            ...MedicalRecordsDetail
        }
    }
    ${medicalRecordsFragment}
`;

export const medicalRecordsByPatientIdQuery = gql`
    query MedicalRecordsByPatientId ($patientId: ID!) {
        medicalRecordsByPatientId (patientId: $patientId) {
            ...MedicalRecordsDetail
        }
    }
    ${medicalRecordsFragment}
`;

export const userQuery = gql`
    query User($id: ID!) {
        user(userId: $id) {
            ...UserDetail
            patient {
                ...PatientDetail
            }
            doctor {
                ...DoctorDetail
            }
        }
    }
    ${userDetailFragment}
    ${patientDetailFragment}
    ${doctorDetailFragment}
`;
