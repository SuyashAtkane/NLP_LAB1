'''
Name- Suyash S Atkane
Roll no.- 3
Batch - B1
Practical no.5 - Regular Expression
'''

import re

def find_entities(text):

    result = {
        'URLs': re.findall(r'https?://\S+|www\.\S+', text),
        'IP Addresses': re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text),
        'Dates': re.findall(r'([1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}', text),
        'PAN Numbers': re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]', text),
    }
    return result

# Example usage:
sample_text = """
First Dataset
Visit our website at https://www.Twitter.com.
For support, contact us at support@example.com.
IP address: 192.168.2.3
Date: 25/11/2023
PAN number: DYXPA9175B

Second Dataset
Visit our website at https://www.instagram.com.
For more info connect with  info@example.com.
IP address: 192.148.4.5
Date: 12/11/2023
PAN number: AZYNB6252C
"""

result = find_entities(sample_text)

for entity_type, entities in result.items():
    print(f"{entity_type}: {entities}")


"""
Output:

URLs: ['https://www.Twitter.com.', 'https://www.instagram.com.']
IP Addresses: ['192.168.2.3', '192.148.4.5']
Dates: [('25', '11', '20'), ('12', '11', '20')]
PAN Numbers: ['DYXPA9175B', 'AZYNB6252C']

"""