import requests
import json
import re
from pprintpp import pprint as pp

#API key
openFECKey = 'qBdzC8kDP69devujUxIm8Xuh5aTIIhUZhejp6N1R'
#votesmart url
url = 'https://api.open.fec.gov/v1/candidates/search/'
#zipcode
zip = input('Enter 5-digit zip code: ')

#payload
params = {
    'api_key': openFECKey,
    'election_year': 2024,
    'state': 'NY',  # State code (e.g., 'NY' for New York)
    'zip': zip,
    'per_page': 100,  # Number of results per page
    'page': 1  # Page number for pagination
}

paramsPresidential = {
    'api_key': openFECKey,
    'election_year': 2024,
    'office': 'P',  # 'P' stands for presidential candidates
    'per_page': 50
}

#retrieve candidate policies from votesmart
def retrieveCandidateFEC():
    response = requests.get(url, params = params)
    if response.status_code == 200:
        print(response.json)
        return response.json()
    else:
        print(f'Error: {response.status.code}')
        return None

def retrieveCandidateFEC_Presidential():
    response = requests.get(url, params = paramsPresidential)
    if response.status_code == 200:
        print(response.json)
        return response.json()
    else:
        print(f'Error: {response.status.code}')
        return None


data = retrieveCandidateFEC()
candidates = data.get('results', [])
full_list = []
if candidates:
    print('Local Candidates:')
    for candidate in candidates:
        id = candidate.get('candidate_id','N/A')
        name = candidate.get('name', 'N/A')
        party = candidate.get('party_full','N/A')
        district = candidate.get('district','N/A')
        office = candidate.get('office_full','N/A')

        if district != '23':
            continue

        candidateDict = {
            'id' : id,
            'name' : name,
            'district' : district,
            'party' : party,
            'office' : office
        }

        if candidate.get('candidate_inactive') is False:
                full_list.append(candidateDict)

pp(full_list,indent=3,width=40,depth=2)

Presidentialdata = retrieveCandidateFEC_Presidential()
nomminees = Presidentialdata.get('results',[])
presidentialList = []

if nomminees:
    print('Presidential Candidates:')
    for nomminee in nomminees:
        #print(nomminee)
        idP = nomminee.get('candidate_id', 'N/A')
        nameP = nomminee.get('name', 'N/A')
        partyP = nomminee.get('party_full', 'N/A')

        PresidentialCandidateDict = {
            'id': idP,
            'name': nameP,
            'party': partyP
        }
        print(PresidentialCandidateDict)
        #if candidate.get('candidate_inactive') is False:
        full_list.append(PresidentialCandidateDict)

pp(presidentialList,indent=3,width=40,depth=2)






