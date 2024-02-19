import random
import string
import datetime
import hashlib
import uuid

class PyForge:
    def __init__(self, seed=None):
        self.random = random.Random(seed)
        self.data = {
            'first_name': ['John', 'Jane', 'Michael', 'Emily', 'William', 'Emma', 'James', 'Olivia', 'Daniel', 'Sophia'],
            'last_name': ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson'],
            'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
            'state': ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA'],
            'street_suffix': ['St', 'Ave', 'Blvd', 'Dr', 'Rd'],
            'area_codes': ['201', '202', '203', '204', '205', '206', '207', '208', '209', '210'],
            'company_suffix': ['LLC', 'Inc', 'Corp', 'Ltd'],
            'email_domains': ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com'],
            'job_title': ['Software Engineer', 'Data Analyst', 'Marketing Manager', 'Product Manager', 'Sales Representative'],
            'country': ['USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'Japan', 'China', 'India', 'Brazil'],
            'domain_suffix': ['com', 'net', 'org', 'edu', 'gov'],
            'street_name': ['Maple', 'Oak', 'Pine', 'Cedar', 'Elm', 'Main', 'First', 'Second', 'Third', 'Park'],
            'postcode_formats': ['#####', '#####-####', 'A#A #A#', 'A#A# #A#', 'A#A-#A#'],
            'credit_card_types': ['Visa', 'MasterCard', 'American Express', 'Discover'],
            'month_names': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            'day_of_week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        }
        
    def random_element(self, key):
        return self.random.choice(self.data[key])
    
    def first_name(self):
        return self.random_element('first_name')
    
    def last_name(self):
        return self.random_element('last_name')
    
    def full_name(self):
        return f"{self.first_name()} {self.last_name()}"
    
    def city(self):
        return self.random_element('city')
    
    def state(self):
        return self.random_element('state')
    
    def street_address(self):
        return f"{self.random.randint(1, 9999)} {self.random_element('street_name')} {self.random_element('street_suffix')}"
    
    def phone_number(self):
        return f"({self.random.choice(self.data['area_codes'])}) {self.random.randint(100, 999)}-{self.random.randint(1000, 9999)}"
    
    def company_name(self):
        return f"{self.last_name()} {self.random_element('company_suffix')}"
    
    def email(self):
        username = self.first_name().lower() + '.' + self.last_name().lower() + str(self.random.randint(1, 999))
        return f"{username}@{self.random_element('email_domains')}"
    
    def job_title(self):
        return self.random_element('job_title')
    
    def country(self):
        return self.random_element('country')
    
    def postcode(self):
        return ''.join([self.random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(len(self.random_element('postcode_formats')))])
    
    def credit_card_number(self, card_type='Visa'):
        if card_type not in self.data['credit_card_types']:
            raise ValueError("Invalid credit card type.")
        
        if card_type == 'Visa':
            prefix = '4'
        elif card_type == 'MasterCard':
            prefix = '5'
        elif card_type == 'American Express':
            prefix = '3'
        elif card_type == 'Discover':
            prefix = '6'
        
        number = prefix + ''.join([self.random.choice('0123456789') for _ in range(15)])
        return number
    
    def credit_card_expiration_date(self):
        month = self.random.randint(1, 12)
        year = self.random.randint(2024, 2030)
        return f"{month}/{year}"
    
    def month_name(self, abbreviated=False):
        month = self.random_element('month_names')
        if abbreviated:
            return month[:3]
        return month
    
    def day_of_week(self, abbreviated=False):
        day = self.random_element('day_of_week')
        if abbreviated:
            return day[:3]
        return day
    
    def date_between(self, start_date, end_date):
        start_timestamp = start_date.timestamp()
        end_timestamp = end_date.timestamp()
        random_timestamp = self.random.uniform(start_timestamp, end_timestamp)
        return datetime.datetime.fromtimestamp(random_timestamp)
    
    def random_number(self, digits=None, fix_length=False):
        if digits is None:
            return self.random.randint(0, 999999)
        if fix_length:
            return self.random.randint(10 ** (digits - 1), (10 ** digits) - 1)
        return self.random.randint(0, 10 ** digits)
    
    def boolean(self, chance_of_getting_true=50):
        return self.random.choices([True, False], [chance_of_getting_true, 100 - chance_of_getting_true])[0]
    
    def random_letters(self, length=10, upper=False, lower=False):
        if not upper and not lower:
            upper = lower = True
        letters = string.ascii_uppercase if upper else ''
        letters += string.ascii_lowercase if lower else ''
        return ''.join(self.random.choice(letters) for _ in range(length))
    
    def random_digit(self):
        return self.random.randint(0, 9)
    
    def random_sample(self, population, length=1):
        return self.random.sample(population, length)
    
    def md5(self, text):
        return hashlib.md5(text.encode()).hexdigest()
    
    def sha1(self, text):
        return hashlib.sha1(text.encode()).hexdigest()
    
    def sha256(self, text):
        return hashlib.sha256(text.encode()).hexdigest()
    
    def uuid4(self):
        return str(uuid.uuid4())
        

# Example usage:
pyforge = PyForge(seed=42)
print(pyforge.first_name())
print(pyforge.last_name())
print(pyforge.full_name())
print(pyforge.city())
print(pyforge.state())
print(pyforge.street_address())
print(pyforge.phone_number())
print(pyforge.company_name())
print(pyforge.email())
print(pyforge.job_title())
print(pyforge.country())
print(pyforge.postcode())
print(pyforge.credit_card_number())
print(pyforge.credit_card_number('MasterCard'))
print(pyforge.credit_card_expiration_date())
print(pyforge.month_name())
print(pyforge.month_name(abbreviated=True))
print(pyforge.day_of_week())
print(pyforge.day_of_week(abbreviated=True))
print(pyforge.date_between(datetime.datetime(2020, 1, 1), datetime.datetime(2025, 12, 31)))
print(pyforge.random_number(6))
print(pyforge.boolean())
print(pyforge.random_letters(8, upper=True))
print(pyforge.random_digit())
print(pyforge.random_sample([1, 2, 3, 4, 5], 3))
print(pyforge.md5('Hello, World!'))
print(pyforge.sha1('Hello, World!'))
print(pyforge.sha256('Hello, World!'))
print(pyforge.uuid4())