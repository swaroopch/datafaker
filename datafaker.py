#!/usr/bin/env python
# coding=utf8
# Port of http://search.cpan.org/~jasonk/Data-Faker/lib/Data/Faker.pm
# Same license as above original code (which in turn is same terms as Perl itself)
#       i.e. Artistic License and/or GPL >= v1.

import random
import re
import time as timemodule
import string

def name_suffix():
    return random.choice(
        '''Jr. Sr. I II III IV V M.S. MBBS PhD'''.split()
        )

def name_prefix():
    return random.choice(
        '''Mr. Mrs. Ms. Miss Dr.'''.split()
        )

def last_name():
    return random.choice(
        '''
Abbasi Achari Adiga Adyanthaya Agrawal Ahluwalia Ahuja Aickara Ajayan Ajmeria
Akhtar Alaparthy Alappallil Alavi Allana Alreja Ambalangadan Ananth Ananthuni
Andhak Anghan Athale Aulakh Awasthi Babbar Bafna Bagal Baghel Bahri Baig
Balasubramaniam Baliga Ballal Bamraulia Bana Banerjee Bangi Bapat Barad Bartwal
Basu Bedi Beniwal Bhadoriya Bhaduria Bhandary Bhardwaj Bhargava Bhat Bhati
Bhatia Bhatnagar Bhatt Bhaṭṭa Bhogireddy Bijania Bindra Bishnois Brahmbhatt
Burdak Buttar Chadaga Chahar Chakraborty Chakravartin Chakyar Chandavarkar
Chandola Chandra Chandrakar Channar Charan Chatterjee Chattopadhyay
Chattopadhyaya Chaturvedi Chauhan Chettiar Chhibber Chishti Chopra Chowallur
Chowla Chudasama Chughtai Dalal Damle Das Datla Datt Debbarma Deengar Deol Deora
Devadiga Dharker Dhillon Dikshit Doad Dogra Dosanjh Doshi Dravid Duggal Dumra
Dutta Dwivedi Erijarla Gaajula Gadhavi Gahoi Gakhar Ganguly Garodia Ghosh Gill
Gokhale Gothoskar Grover Guha Guhathakurta Gujadhur Gupta Gurunath Havyaka
Hoysala Iyengar Iyer Jadaun Jaitly Jakkamsetti Jampana Jawanda Jindal Jodha
Joshi Juthani Kaimal Kalbhor Kaler Kalsi Kamat Kanagala Kanakamedala Kanwat
Kapoor Karekar Karhade Karnik Kaseebhotla Khullar Khullung Kini Koilparampil
Kolekar Kotak Kotwal Krishnamurti Kudva Kuilta Kulkarni Kumpawat Kurisunkal
Kuruppanmar Kushwaha Labbay Lala Lau Lone Luthra Machingal Mahajan Maibam
Maisnam Makur Malhotra Mallya Manchukonda Mannava Mathai Medabalimi Medampudi
Mehta Menokki Menon Mers Methil Mhasde Minhas Mirdha Mirza Mishra Mittal Mohan
Mohyal Nair Prabhakar
        '''.split()
        )

def first_name():
    return random.choice(
        '''
Abha Abhay Abhaya Abhijat Abhijit Abhilasha Abhinav Abhishek Achala Achintya
Achyuta Aditi Aditya Aghanashini Ahladita Ajala Ajatashatru Ajay Ajit Ajitabh
Akash Akhila Akhilesh Akhilesh Akriti Akshat Akuti Alaknanda Alka Alok Alopa
Alpa Amal Amar Amba Ambar Ambu Ambuda Ambuja Ameya Amish Amit Amita Amitabh
Amitava Amitesh Amoda Amodini Amogh Amol Amrit Amrita Amshula Amulya Amulya
Anand Anandita Anant Anantram Ananya Anarghya Anchita Angada Anil Anirudhha
Anish Anisha Anita Anjali Anju Ankit  Ankita Ankur Anoop Anshul Anshuman Anupam
Anupama Anuprabha Anuradha Anurag Anuragini Anurati Anusha Anushri Apala
Aparajita Aparna Apoorva Aradhana Arati Archana Archisha Archita Arihant Arjun
Arnav Arun Aruna Arunima Arvind Aseem Asha Ashakiran Ashalata Ashavari Ashok
Ashvin Ashwatthama Ashwini Ashwini Atmajyoti Atul Atulya Avani Avanindra Avanish
Avantika Avinash Badrinath Badriprasad Bageshri Bakula Bala Balaaditya
Balachandra Balaji Balakrishna Balamani Balamohan Baldev Balram Bandhura Bansi
Bhadrak Bhadraksh Bhagirath Bhagyalakshmi Bhairavi Bhanu Bhanuja Bhanuprasad
Bharadwaj Bharat Bharati Bhaskar Bhavana Bhavani Bhavesh Bhavya Bhim Bhudev
Bhupen Bhupendra Bhushan Bhuvan Bhuvana Bhuvanesh Bina Bindiya Bindusar Bipin
Brijesh Brijmohan Brinda Buddhadev Cauvery Chaitaly Chaitanya Chakrika Chaman
Chameli Chanchala Chandan Chandana Chandani Chandra Chandrahas Chandrak
Chandraki Chandrashekhar Chandresh Chandrika Chapal Charan Charanjit Charu
Charudutta Charulata Charulekha Chetan Chhavvi Chhaya Chidambar Chinmay Chinmayi
Chintamani Chirag Chiranjeev Chitra Chitragandha Chitraksh Chitralekha Chitrani
Chittaprasad Chittaranjan Chittaswarup Chudamani Dakshesh Damini Darika Darpak
Daruka Dattatreya Daya Dayanand Dayita Debashish Deepa Deepak Deepali Deepankar
Deependra Deepika Deepti Devadutt Devaki Devanand Devang Devarsi Devdas Devendra
Devesh Devilal Deviprasad Devraj Dhananjay Dhanesh Dhanyata Dhara Dharini Dharma
Dharmadev Dharmendra Dharmesh Dhatri Dhaval Dhiren Dhirendra Dhriti Dhruv
Digamber Dilip Dinesh Dinkar Divakar Divya Divyendu Divyesh Dristi Duranjaya
Durga Durjaya Ecchumati Ekalinga Ekanga Eknath Ekta Ela Gagan Gaganvihari
Gajanan Gajendra Ganaraj Gangadhar Gangadutt Gaurang Gaurav Geet Giridhar
Girilal Giriraj Girish Gopal Gopan Govind Gulab Gunaratna Gurbachan Gurcharan
Gurdayal Gurdeep Gurmeet Gurnam Gursharan Guru Gurudas Gurudutt Hamsa Haresh
Hari Harihar Harilal Harinakshi Harinakshi Harish Harsha Harsha Harshad Harshal
Harshini Harshul Harshvardhan Hema Hemachandra Hemadri Hemang Hemangi Hemangini
Hemant Hemaraj Hemendra Hemlata Heramba Himagouri Himani Hiranmayi Hiranya
Hiresh Hita Hridayesh Hridaynath Hrishikesh Ibhanan Ikshu Ila Ilesh Indeever
Indira Indradutt Indrajit Indrakshi Indraneel Indrani Indu Induja Indukala
Indulala Induma Indumukhi Inesh Ishan Ishwar Jagadamba Jagadeep Jagadhidh
Jagajeet Jagajeevan Jagannath Jagmohan Jagrati Jahnavi Jaidev Jaladhija Janak
Janaki Janardan Jasraj Jasveer Jaswant Jawahar Jaya Jayadeep Jayaditya Jayani
Jayant Jayanti Jayaprada Jayashekhar Jayashri Jaysukh Jeevan Jeevika Jinendra
Jishnu Jitendra Jnyandeep Jnyaneshwar Juhi Jyoti Jyotsna Kailash Kajal Kala
Kalavati Kalidas Kalindi Kalpana Kalpita Kalyani Kamadev Kamakshi Kamal Kamala
Kamalika Kamini Kamlesh Kamna Kanak Kanaka Kanan Kanan Kanchana Kanha Kartik
Kartikeya Karuka Kasturi Kaumudi Kaushal Kaushik Kavi Kavita Keertana Kesar
Keshini Ketaki Kiran Kirti Kishori Kokila Komal Krishna Kriti Krupa Kshama Kumud
Kunda Kundanika Kunjal Kushala Kusuma Kusumita Lajwanti Lakshman Lakshmi Lalana
Lali Lalima Lalit Lalita Lalitaditya Lalitchandra Lalitmohan  Lata Latangi
Latika Lavali Lavanya Leela Lekha Lipika Lochana Lokesh Loknath Lokprakash Lona
Madan Madhav Madhavi Madhavilata Madhu Madhu Madhubala Madhukar Madhumalati
Madhumita Madhura Madhuri Madhusudhana Mahabala Mahadev Mahavir Maheepati
Mahendra Mahesh Mahima Maitreya Maitreyi Makarand Mala Malati Malavika Malini
Mallika Malti Mamata Manasi Manavendra Mandar Mandhatri Manendra Mangala Manik
Manik Manindra Manini Maniram Manish Manisha Manishankar Manjari Manju
Manjula Manjusha Manjusri Manohar Manoj Manorama Manoranjan Manprasad Mansukh
Manu Manushri Marala Mareechi Marisa Markandeya Martand Matangi Matsendra
Mausumi Maya Mayank Mayukhi Mayur Mayuri Medha Meena Meenakshi Meera Megha
Meghana Meghdutt Meghnad Mehul Menaka Mihir Milind Mitesh Mithil Mithun Mitul
Mohan Mohin Mohini Mohit Monish Mridula Mrinalini Mugdha Mukesh Mukul Mukunda
Mythily Nachiketa Nalin Nalini Namdev Namrata Nanda Nanda Nandakishor Nandan
Nandi Nandika Nandini Nandita Narayana Narendra Naresh Narhari Narmad Narmada
Narottam Narsimha Nartan Natraj Naveen Navin Navnit Nayan Nayana Neeharika Neel
Neela Neelam Neelam Neelkanth Neeraj Neeraja Neha Netra Nidhi Nidhish Nidra
Nihar Nikhil Nikhita Nikunj Nilay Nilesh Nilima Ninad Nirad Niraj Niral
Niramitra Niranjan Nirav Nirmal Nirmala Nirupa Nirupama Nisha Nishad Nishit
Nishtha Nita Niteesh Niti Nitya Nityanand Nityasundar Nivedita Nivrutti Niyati
Nripendra Nupura Nutan Ojas Omanand Omprakash Oojam Oorjit Padma Padmajai
Padmanabh Padmini Pallav Pallavi Panduranga Pankaj Pankaja Parag Paramartha
Paramjeet Parees Paresh Pari Pariket Parindra Parinita Paritosh Parnika Partha
Pavan Pavana Payal Phalgun Phaninath Phanindra Phanishwar Phoolendu Pinak Piyush
Pooja Poonam Poornima Poorvi Prabha Prabhakar Prabhat Prabir Prabodh Prabodhan
Prachi Pradeep Pradnesh Prafulla Pragati Pragya Prahlad Prajeet Prakash Pramath
Pramesh Pramit Pramod Pranav Pranay Pranet Prasad Prasanna Prasata Prashant
Prasoon Pratap Prateek Pratibha Pratigya Pratima Pratosh Pravar Praveen Prayag
Preetish Prem Prema Premal Premanand Prerana Pritam Pritha Prithu Prithvijaj
Priti Priya Priyadarshini Priyanka Priyaranjan Puja Pundarik Puneet Punita
Punthali Purnima Purujit Purumitra Purushottam Purva Puskara Pusti Rachna Radha
Radhika Raj Rajan Rajani Rajani Rajanigandha Rajanikant Rajata Rajeev Rajesh
Rajiv Rajkumar Rakesh Rakhi Ram Rama Raman Ramani Ramanuja Rambha Rameshwari
Ramita Ranjan Ranjana Ranjeet Rashmi Rati Ratna Ratnakar Ratnavali Ravi
Ravikiran Ravindra Rekha Renuka Revati Riddhi Rishabh Rishi Rochan Rohini Rohit
Roma Roshan Roshni Ruchi Ruchira Rudrani Rujul Rujula Rujuta Rukmini Rupa Rupak
Rupali Rupesh Rupin Rutajit Rutujit Sachetan Sachi Sachita Sadanand Sadhana
Sagar Saguna Sahana Salila Samarjit Samiksha Samir Samrat Samudra Sandeep
Sandhya Sangita Sanjog Sanjukta Sankara Santosh Sanyukta Sapan Saphala Sapna
Sarala Sarang Sarasa Sarasvat Sarasvati Saravati Sarika Sarita Saroja Saryu
Sashi Satish Satyajit Satyamurty Satyavati Satyavrat Satyendra Saumya Saurabh
Saurav Savarna Savita Savitri Seema Senajit Shaila Shailendra Shailesh Shakunt
Shalin Shalini Shankar Shanta Shanti Sharad Sharada Shardul Sharmila Sharmistha
Shashank Shashee Shashikant Shashwat Shatrunjay Sheetal Sheil Shikha Shilpa
Shishir Shiv Shobha Shobhna Shradhdha Shreya Shreyas Shruti Shubha Shulabh
Shvetang Shvetank Shyam Shyamal Siddharth Siddhi Smita Smriti Sneh Snehal
Snigdha Sohan Somatra Sona Sonia Srikant Srinivas Sriram Subhadra Subhaga
Subhash Subhuja Subodh Suchir Suchita Suchitra Sudama Sudarshan Sudesha Sudeva
Sudevi Sudha Sudhakar Sudhanssu Sudhir Sudhish Sugriva Sujata Sujit Sukhdev
Suksma Sukumar Sulalit Sumana Sumati Sumit Sundar Sunil Sunita Supriya Surabhi
Suravinda Suresh Surotama Suruchi Surupa Surya Suryakant Sushila Sushma Sushmita
Suvrata Swagat Swapnil Swaraj Swati Sweta Tanmay Tanushri Tanvi Tapan Tapas Tapi
Tapti Tara Tarak Taran Tarang Tarangini Tarulata Tarun Teerth Tej Teja Tejal
Tejas Tejaswini Tilak Timin Trilochan Trilochana Trilok Trishna Trupti Trusha
Tulasi Tulasidas Tungar Tungesh Tushar Tusti Uday Udaya Udeep Udit Ujesh Ujjwala
Ulhas Ulka Uma Umang Unmesh Upama  Upendra Urja Urmi Urmila Urvasi Urvi Usha
Ushakiran Ushma Utkarsh Utpal Utpalini Uttam Uttara Vachaspati Vaibhav Vaishali
Vajra Vajramani Vallabh Vallika Vandan Vandana Vani Vaninath Vanita Vanmala
Varija Varsha Varun Varuni Vasant Vasanta Vasava Vasu Vasudev Vasudhara Vasuman
Vasumati Vatsala Ved Veena Veer Vibha Vidhut Vidula Vidur Vidya Vidyacharan
Vidyadhar Vidyaranya Vijay Vijaya Vijayalakshmi Vikas Vikram Vikramendra Vikrant
Vimal Vimala Vinanti Vinata Vinay Vinaya Vineeta Vinita Vinod Vinodini Vipan
Viplav Vipul Viraj Virat Virochan Visala Vishal Vishnu Vishva Vishvajit
Vishvakarma Vishvatma Vishwamitra Vishwas Viswanath Vivek Vyomesh Waman Yamini
Yamuna Yash Yashawini Yashila Yashoda Yashodhan Yashodhara Yashpal Yashwant
Yatin Yogendra Yogesh Yogini Yogita Yudhajit Yudhisthir Yuvaraj Yuyutsu 
        '''.split()
        )

def name():
    return random.choice(
            (
                lambda : '%s %s %s' % (name_prefix(), first_name(), last_name()),
                lambda : '%s %s %s' % (first_name(), last_name(), name_suffix()),
                lambda : '%s %s' % (first_name(), last_name()),
                lambda : '%s %s' % (first_name(), last_name()),
                lambda : '%s %s' % (first_name(), last_name()),
                lambda : '%s %s' % (first_name(), last_name()),
                lambda : '%s %s' % (first_name(), last_name()),
            )
        )()

def company_suffix():
    return random.choice(
        ('Inc', 'and Sons', 'LLC', 'Group')
        )

def company():
    return random.choice(
            (
                lambda : '%s %s' % (last_name(), company_suffix()),
                lambda : '%s-%s' % (last_name(), last_name()),
                lambda : '%s, %s and %s' % (last_name(), last_name(), last_name())
            )
        )()

def randchars(format):
    '''Format example: @@_@@'''
    return re.sub('@', lambda match : random.choice(string.letters), format)

def randints(format):
    '''Format example: ##-##-## or $###.#0'''
    return re.sub('#', lambda match : str(random.randint(0, 9)), format)

def phone_number():
    return random.choice(
            (
                lambda : randints('9#########'),
                lambda : randints('0806#######')
            )
        )()

def password():
    '''Wanted to port http://search.cpan.org/~jwalt/Crypt-GeneratePassword/lib/Crypt/GeneratePassword.pm but turned out to be too complicated. Someday.'''
    return randints(randchars('@@@#@@##@@'))

def username():
    return re.sub(r'\W+', '', first_name().lower()).replace(' ', '') + randints('##')

def domain_suffix():
    return random.choice(
		'''
        ac ac.uk ad ae af ag ai al am an ao aq ar as at au aw az ba bb bd be
		bf bg bh bi bj bm bn bo br bs bt bv bw by bz ca cc cd cf cg ch ci ck
		cl cm cn co co.uk com cr cs cu cv cx cy cz de dj dk dm do dz ec edu ee
		eg eh er es et fi fj fk fm fo fr ga gd ge gf gg gh gi gl gm gn gov gp
		gq gr gs gt gu gw gy hk hm hn hr ht hu id ie il im in int io iq ir is
		it je jm jo jp ke kg kh ki km kn kp kr kw ky kz la lb lc li lk lr ls
		lt lu lv ly ma mc md mg mh mil mk ml mm mn mo mp mq mr ms mt mu mv mw
		mx my mz na nc ne net nf ng ni nl no np nr nt nu nz om org pa pe pf pg
		ph pk pl pm pn pr ps pt pw py qa re ro ru rw sa sb sc sd se sg sh si sj
		sk sl sm sn so sr sv st sy sz tc td tf tg th tj tk tm tn to tp tr tt tv
		tw tz ua ug uk um us uy uz va vc ve vg vi vn vu wf ws ye yt yu za zm zw

        com net org
		aero biz coop info museum name pro

        ac.in co.in org.in
        '''.split()
        )

def domain_word():
    return re.sub(r'\W+', '', company().lower())

def domain_name():
    return '%s.%s' % (domain_word(), domain_suffix())

def email():
    return '%s@%s' % (username(), domain_name())

def ip_address():
    def under255():
        return random.randint(1, 254)
    return '.'.join(( str(under255()), str(under255()), str(under255()), str(under255()) ))

def unixtime():
    return random.randint(0, int(timemodule.time()))

def _timestr(format):
    return timemodule.strftime(format, timemodule.localtime(unixtime()))

# These formats don't match Perl's strftime() as their directives are wildly different.
def date():
    return _timestr('%Y-%m-%d')

def time():
    return _timestr('%H:%M:%S')

def datetime():
    return '%s %s' % (date(), time())

# Can create more functions for random year, month, etc.
# Refer http://docs.python.org/dev/library/datetime.html?highlight=strftime#strftime-behavior

