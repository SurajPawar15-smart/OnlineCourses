from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Harry</h1>''')

def about(request):
    return HttpResponse("<h1>About Harry Bhai<h1>")

def exl(request):
   s='''<h2 style="background-color:yellowgreen;color:white;"> 10 Best Free Online Certification Courses to take During Lockdown <br></h2>
   <h3 style="background-color:red;color:white;"> If you are a beginner, intermediate or expert and would like to upgrade your knowledge then you can start coding by taking free online coding courses during quarantine with a project by visiting the following links. <br></h3>
   <a  href="https://www.classcentral.com/report/coursera-free-certificate-covid-19">Coursera</a><br>
   <a  href="https://www.eduonix.com/dashboard">Eduonix</a><br>
   <a  href="https://learndigital.withgoogle.com/digitalgarage/courses">Google Digital Garage</a><br>
   <a  href="https://www.linkedin.com/learning/me">Linkedin</a><br>
   <a  href="https://courses.edx.org/courses/course-v1:edX+edx201+1T2020/course/?fbclid=IwAR0EcpZUewisAef7WT6_BHgh0ip5Rrjyw8YrwRDpqSSV7FTAiDZYW9Ln2ZU">Edx</a><br>
   <a  href="https://www.udemy.com/?utm_source=adwords&utm_medium=udemyads&utm_campaign=Generic-BMM_la.EN_cc.INDIA&utm_content=deal4584&utm_term=_._ag_85531602406_._ad_405912360676_._kw_%2Bcourses%20%2Bonline_._de_c_._dm__._pl__._ti_kwd-20014463542_._li_1007788_._pd__._&matchtype=b&gclid=EAIaIQobChMIqrXO8K-16gIVR7aWCh3yOwuIEAAYAiAAEgKWjfD_BwE">Udemy</a><br>
   <a  href="https://fslearning.nasscom.in/">NASSCOM</a><br>
   <a  href="http://free.aicte-india.org/index.html">AICTE</a><br>
   <a  href="https://www.learnvern.com/">Learn Vern</a><br>
   <a  href="https://in.insidesherpa.com/show-firm-programs/F9NstoYweMhrBLf2u/Microsoft#lp">Internship</a><br>
   <h2 style="background-color:orange;color:white;">Enhance your skills during lockdown! Enroll for free online courses and upgrade your skills... </h2>
   <h3><b><marquee width="100%" direction="left" height="100px" style="background-color:pink;color:black;">“People expect to be bored by eLearning —let’s show them it doesn’t have to be like that!” </marquee></b></h3>'''
   return HttpResponse(s)

#def exl(request):
 #   s='''<center><h1>Web-Site Directory<h1><table border="1">
  #  <tr><td>Web-Site Name</td><td>Information</td></tr>
  #  <tr><td><a href="https://www.google.com/">Google</a></td><td>Google,Googol was coined in the 1930s and is attributed to the nine-year-old nephew of American mathematician Edward Kasner.</td></tr>
   # <tr><td><a href="https://www.facebook.com/">Facebook</a></td><td>Facebook a popular social networking website</td></tr>
    #<tr><td><a href="https://www.youtube.com/">Youtube</a></td><td>Youtube upload a video of (someone or something) to the video-sharing website YouTube.</td></tr>
    #<tr><td><a href="https://www.youtube.com/playlist?list=PLC76DjA6t8-fwWxu6-EZ5FL5imxIzmL_L">Youtude codewithharry</a></td><td>Codewithharry Browse courses and find out the best course for you. Its free! Code With Harry is my attempt</td></tr>
    #<tr><td><a href="https://www.channelnewsasia.com/news/international">News</a></td><td>News,newly received or noteworthy information, especially about recent events.</td></tr>
    #<tr><td><a href="https://www.flipkart.com/?gclid=Cj0KCQiAyKrxBRDHARIsAKCzn8x2NJhjFNbPSPgnaaDSRNsDDzswxHASCB2sqvJ5dEzKDrscqLa1I5EaAs4nEALw_wcB&ef_id=Cj0KCQiAyKrxBRDHARIsAKCzn8x2NJhjFNbPSPgnaaDSRNsDDzswxHASCB2sqvJ5dEzKDrscqLa1I5EaAs4nEALw_wcB:G:s&s_kwcid=AL!739!3!265109269849!e!!g!!flipkart&semcmpid=sem_8024046704_brand_eta_goog">Flipkart</a></td><td>Flipkart,Flipkart Internet Private Limited is an e-commerce company based in Bengaluru, India.</td></tr></table></center>''')
    #return HttpResponse(s)
    
