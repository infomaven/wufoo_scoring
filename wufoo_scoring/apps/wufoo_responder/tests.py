"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

Good Times!
"""

from django.test import TestCase
import json, urllib


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class EmailResponseTest(TestCase):
    def setUp(self):
        self.data = {'CreatedBy': 'public',
            'DateCreated': '2011-12-24 08:48:21', 'EntryId': 8,
            'Field1' : 'R', 'Field2': 'G', 
            'Field3': 'rgraham@whitetailsoftware.com',
            'Field4': 'Both',
            'Field5': 'Manstein',
            'Field6': 'August 1944',
            'FieldStructure': {
                 "Fields": [
                 {
                      "ClassNames": "", 
                      "DefaultVal": "", 
                      "ID": "Field1", 
                      "Instructions": "", 
                      "IsRequired": "0", 
                      "Page": "1", 
                      "SubFields": [
                        {
                          "DefaultVal": "", 
                          "ID": "Field1", 
                          "Label": "First"
                        }, 
                        {
                          "DefaultVal": "", 
                          "ID": "Field2", 
                          "Label": "Last"
                        }
                      ], 
                      "Title": "Name", 
                      "Type": "shortname"
                    }, 
                    {
                      "ClassNames": "", 
                      "DefaultVal": "", 
                      "ID": "Field3", 
                      "Instructions": "", 
                      "IsRequired": "1", 
                      "Page": "1", 
                      "Title": "Email", 
                      "Type": "email"
                    }, 
                    {
                      "Choices": [
                        {
                          "Label": "Britain"
                        }, 
                        {
                          "Label": "Russia"
                        }, 
                        {
                          "Label": "Both"
                        }
                      ], 
                      "ClassNames": "", 
                      "DefaultVal": "", 
                      "ID": "Field4", 
                      "Instructions": "", 
                      "IsRequired": "0", 
                      "Page": "1", 
                      "Title": "Which country or countries benefitted from the Lend Lease Pact?", 
                      "Type": "radio"
                    }, 
                    {
                      "Choices": [
                        {
                          "Label": "Rommel"
                        }, 
                        {
                          "Label": "Manstein"
                        }, 
                        {
                          "Label": "Guderian"
                        }
                      ], 
                      "ClassNames": "", 
                      "DefaultVal": "", 
                      "ID": "Field5", 
                      "Instructions": "", 
                      "IsRequired": "0", 
                      "Page": "1", 
                      "Title": "Which is a German field commander who fought a brilliant campaign on the Eastern front?", 
                      "Type": "radio"
                    }, 
                    {
                      "Choices": [
                        {
                          "Label": "June 1944"
                        }, 
                        {
                          "Label": "July 1944"
                        }, 
                        {
                          "Label": "August 1944"
                        }
                      ], 
                      "ClassNames": "", 
                      "DefaultVal": "", 
                      "ID": "Field6", 
                      "Instructions": "", 
                      "IsRequired": "0", 
                      "Page": "1", 
                      "Title": "When did the Allies break out of Normandy?", 
                      "Type": "radio"
                    }
                  ]
                },
        'FormStructure': {
          "DateCreated": "2011-10-25 20:54:06", 
          "DateUpdated": "2011-12-18 22:32:38", 
          "Description": "Test your WWII knowledge.", 
          "Email": None, 
          "EndDate": "2030-01-01 12:00:00", 
          "EntryLimit": "0", 
          "Hash": "m7x3k1", 
          "IsPublic": "1", 
          "Language": "english", 
          "Name": "WWII History Quiz", 
          "RedirectMessage": "Success! Thanks for filling out my form!", 
          "StartDate": "2000-01-01 12:00:00", 
          "Url": "wwii-history-quiz"
        },
        'HandshakeKey': 'SoastaWufooProject',
        'IP': '99.156.89.47'}

        self.soasta = { 'FieldStructure':{
      "Fields": [    {
          "Title": "Name",
          "Instructions": "",
          "IsRequired": "0",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "SubFields": [        {
             "DefaultVal": "",
              "ID": "Field113",
              "Label": "First"
            },        {
              "DefaultVal": "",
              "ID": "Field114",
              "Label": "Last"
            }],
          "Type": "shortname",
          "ID": "Field113"
        },    {
          "Title": "Email",
          "Instructions": "We'll send you your quiz results and explanation immediately.",
          "IsRequired": "0",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Type": "email",
          "ID": "Field112"
        },    {
          "Title": "Production testing = live testing.",
          "Instructions": "",
          "IsRequired": "1",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Choices": [        {
              "Label": None
         },        {
              "Label": None
            }],
          "Type": "radio",
          "ID": "Field101"
        },    {
          "Title": "Production testing is too risky.",
          "Instructions": "",
          "IsRequired": "1",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Choices": [        {
              "Label": None
            },        {
              "Label": None
            }],
          "Type": "radio",
          "ID": "Field102"
        },    {
          "Title": "Production testing is not about breaking the site; performance testing is about baseline testing, spikes, endurance and diagnostic testing.",
          "Instructions": "",
          "IsRequired": "1",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Choices": [        {
              "Label": None
            },        {
              "Label": None
            }],
          "Type": "radio",
          "ID": "Field103"
        },    {
          "Title": "It takes too long; we're lucky to have time for QA testing.",
          "Instructions": "",
          "IsRequired": "1",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Choices": [        {
              "Label": None
            },        {
              "Label": None
            }],
          "Type": "radio",
          "ID": "Field104"
        },    {
          "Title": "The technology to do production performance testing has changed so you now have the expertise in house.",
          "Instructions": "",
          "IsRequired": "1",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Choices": [        {
              "Label": None
            },        {
              "Label": None
            }],
          "Type": "radio",
          "ID": "Field105"
        },    {
          "Title": "Production testing isn't necessary if we do thorough testing in the lab.",
          "Instructions": "",
          "IsRequired": "1",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Choices": [        {
              "Label": None
            },        {
              "Label": None
            }],
          "Type": "radio",
          "ID": "Field106"
        },    {
          "Title": "Management buy-in for production testing may be easier than you think.",
          "Instructions": "",
          "IsRequired": "1",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Choices": [        {
              "Label": None
            },        {
              "Label": None
            }],
          "Type": "radio",
          "ID": "Field107"
        },    {
          "Title": "It costs too much.",
          "Instructions": "",
          "IsRequired": "1",
          "ClassNames": "",
          "DefaultVal": "",
          "Page": "1",
          "Choices": [        {
              "Label": None
            },        {
              "Label": None
            }],
          "Type": "radio",
          "ID": "Field108"
        }]
    },
    'FormStructure':    {
      "Name": "Production Testing Myths",
      "Description": "8 Common Myths About Testing in Production",
      "RedirectMessage": "Great! Thanks for filling out my form!",
      "Url": "production-testing-myths",
      "Email": None,
      "IsPublic": "1",
      "Language": "english",
      "StartDate": "2000-01-01 12:00:00",
      "EndDate": "2030-01-01 12:00:00",
      "EntryLimit": "0",
      "DateCreated": "2011-12-28 22:44:06",
      "DateUpdated": "2011-12-28 22:56:32",
      "Hash": "m7x3s5"
    },
    'Field113': 'Rob',
    'Field114': 'Graham',
    'Field112': 'rgraham@whitetailsoftware.com',
    'Field101': False,
    'Field102': False,
    'Field103': True,
    'Field104': True,
    'Field105': True,
    'Field106': False,
    'Field107': True,
    'Field108': False,
    'CreatedBy':    'public',
    'DateCreated':  '2011-12-28 23:18:12',
    'EntryId':  2,
    'IP':   '99.156.89.47',
    'HandshakeKey': 'SoastaWufooProject' }

        self.ratingQuiz = { 'FieldStructure':{
              "Fields": [    {
                  "Title": "Name",
                  "Instructions": "",
                  "IsRequired": "1",
                  "ClassNames": "",
                  "DefaultVal": "",
                  "Page": "1",
                  "SubFields": [        {
                      "DefaultVal": "",
                      "ID": "Field113",
                      "Label": "First"
                    },        {
                      "DefaultVal": "",
                      "ID": "Field114",
                      "Label": "Last"
                    }],
                  "Type": "shortname",
                  "ID": "Field113"
                },    {
                  "Title": "Email",
                  "Instructions": "We'll send you your quiz results and explanation immediately.",
                  "IsRequired": "1",
                  "ClassNames": "",
                  "DefaultVal": "",
                  "Page": "1",
                  "Type": "email",
                  "ID": "Field112"
                },    {
                  "Title": "Please rate each of the following according to your organization's testing solutions.",
                  "Instructions": "",
                  "IsRequired": "1",
                  "ClassNames": "",
                  "DefaultVal": "0",
                  "Page": "1",
                  "SubFields": [        {
                      "DefaultVal": "0",
                      "ID": "Field116",
                      "Label": "1. Does your solution have the flexibility to generate load both internally and externally?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field117",
                      "Label": "2. Are you able to build and modify complex tests within hours?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field118",
                      "Label": "3. Can your test platform support dynamic web and mobile technologies and protocols?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field119",
                      "Label": "4. Is your test environment elastic and globally distributed?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field120",
                      "Label": "5. Are you able to do dynamic and fully automated test grid provisioning?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field121",
                      "Label": "6. Can you control test sessions to start, pause, stop, modify, re-start, and analyze?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field122",
                      "Label": "7. Does your solution have a single, integrated view of performance and monitoring metrics?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field123",
                      "Label": "8. Can you rapidly isolate performance issues in real-time at any scale?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field124",
                      "Label": "9. Does your test platform allow functional and load testing from lab to production?"
                    },        {
                      "DefaultVal": "0",
                      "ID": "Field125",
                      "Label": "10. Is your test platform affordable enough for everyday testing?"
                    }],
                  "Choices": [        {
                      "Score": 1,
                      "Label": 'null'
                    },        {
                      "Score": 2,
                      "Label": 'null'
                    },        {
                      "Score": 3,
                      "Label": 'null'
                    },        {
                      "Score": 4,
                      "Label": 'null'
                    },        {
                      "Score": 5,
                      "Label": 'null'
                    }],
                  "Type": "likert",
                  "ID": "Field116"
                }]
            },
            'FormStructure':    {
              "Name": "Decision Criteria For Your App Testing Platform",
              "Description": 'null',
              "RedirectMessage": "Great! Thanks for filling out our quiz!",
              "Url": "web-mobile-application-testing-criteria",
              "Email": 'null',
              "IsPublic": "1",
              "Language": "english",
              "StartDate": "2000-01-01 12:00:00",
              "EndDate": "2030-01-01 12:00:00",
              "EntryLimit": "0",
              "DateCreated": "2011-12-28 22:44:06",
              "DateUpdated": "2012-01-10 22:26:53",
              "Hash": "m7x3s5"
            },
            'Field113': 'Robert',
            'Field114': 'Graham',
            'Field112': 'rgraham@whitetailsoftware.com',
            'Field116': '5 - Yes, completely.',
            'Field117': '5 - Yes, completely.',
            'Field118': '5 - Yes, completely.',
            'Field119': '5 - Yes, completely.',
            'Field120': '5 - Yes, completely.',
            'Field121': '5 - Yes, completely.',
            'Field122': '5 - Yes, completely.',
            'Field123': '5 - Yes, completely.',
            'Field124': '5 - Yes, completely.',
            'Field125': '5 - Yes, completely.',
            'CreatedBy':    'public',
            'DateCreated':  '2012-01-10 22:45:03',
            'EntryId':  10,
            'IP':   '99.156.89.47',
            'HandshakeKey': 'SoastaWufooProject'}
    
    
    def test_response(self):
        """
        Check against a sample post from Wufoo.
        """
        response = self.client.post('/', {'form': json.dumps(self.ratingQuiz)})
        self.assertEqual(response.content,
         "Firing off an email to rgraham@whitetailsoftware.com.\n")
        self.assertEqual(response.status_code, 200)

    def test_bad_inputs(self):
        # Empty POST
        response = self.client.post('/', {})
        self.assertEqual(response.status_code, 200)

        # Empty 'form' POST var
        response = self.client.post('/', {'form' : json.dumps({})})
        self.assertEqual(response.status_code, 200)

        # No Fields
        data = self.soasta
        del data['FieldStructure']['Fields']
        response = self.client.post('/', {'form' : json.dumps(data)})
        self.assertEqual(response.status_code, 200)


