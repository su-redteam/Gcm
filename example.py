from gcm import GCM
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

#This is the test key
#gcm = GCM("AIzaSyDejSxmynqJzzBdyrCS-IqMhp0BxiGWL1M", debug = True)

#This is a another weird key
#gcm = GCM("AIzaSyDtCiWydkcqzBWgl8PnLUwLpPCy8-SJ6cU")

#This is the actual key
#gcm = GCM("AIzaSyDKMsCy1UbeUQFWYNGMh0DIFhK8C8cwYsE", debug = True)

#another GCM key
gcm = GCM("AIzaSyB-DrluofQNo5Ov4YGxNrs6hpNuur2AfCI", debug = True)

#reg_id = 'APA91bF9NQIwUCQCF6rfjl9sRjvE75c52T5zD8J6rUCTSbXl9lsdL2QC8vQj66k-chZf0DuLLpz8sD3G9U1Gzb1HiPfnj2r10veJlS3Jw9uUKXxbR0vTlf8SEWpZBU2H09vO53qEJEn1'

reg_id = 'dyQRQGGWixM:APA91bFkdnWkFwvvsA5vDLoBU-J90hPsjR1lh1SwTmNWWnyYdh__GJpAvz94gXc-D8YXlTKT-wDewkaZ0SJAIPjeFy3btEoOv-cMsmJMAjUg5JvL3ipzHe_Pu-BU2GO0nJwsdEbBWasv'

data = {'the_message': 'You have x new friends', 'param2': 'value2'}

response = gcm.plaintext_request(registration_id=reg_id, data=data)

print(response)
