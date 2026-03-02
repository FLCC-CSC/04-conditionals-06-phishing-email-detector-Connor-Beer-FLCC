# FILE NAME - phishing_email_detector.py
# NAME: Connor Beer
# DATE: March 2, 2026
# BRIEF DESCRIPTION:  Scans an email and detects phishing

########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    phishing_detector()

def phishing_detector():
    phishing = str(input('Enter the email subject line: '))
    print()

    if 'urgent'.casefold() in phishing.casefold():
        print('SECURITY ASSESSMENT:')
        print('HIGH RISK: Possible phishing attempt.')
    elif 'immediate action required'.casefold() in phishing.casefold():
        print('SECURITY ASSESSMENT:')
        print('HIGH RISK: Possible phishing attempt.')
    elif 'win'.casefold() in phishing.casefold():
        print('SECURITY ASSESSMENT:')
        print('MEDIUM RISK: Suspicious offer detected.')
    elif 'free'.casefold() in phishing.casefold():
        print('SECURITY ASSESSMENT:')
        print('MEDIUM RISK: Suspicious offer detected.')
    elif 'password reset'.casefold() in phishing.casefold():
        print('SECURITY ASSESSMENT:')
        print('LOW RISK: Verify legitimacy with sender.')
    else:
        print('SECURITY ASSESSMENT:')
        print('No phishing indicators detected.')
    print('------------------------')
    print(f'Analyzed subject: "{phishing}"')
    
main()

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          REFLECTION QUESTIONS
########################################

'''
1. Was using `in` difficult or was it natural?
It was difficult to get it t work correctly
'''

########################################
#            ATTESTATION
########################################

'''
Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[X] I did not use AI at all for this lab.
[ ] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.

It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[X] I pretty much get it.
[ ] I'm solid. Totally got it.
'''