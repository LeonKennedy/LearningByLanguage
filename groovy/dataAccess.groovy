import java.text.SimpleDateFormat

class Athlete{
    def firstname, lastname, gender, country, dateOfBirth
}

def asDate(dateStr) {
    new SimpleDateFormat("yyyy-MM-dd").parse(dateStr)
}

def athletes = [
    new Athlete(firstname: 'Paul', lastname: 'Tergat', dateOfBirth: '1969-06-17', gender: 'M', country: 'KEN'),
    new Athlete(firstname: 'Khalid', lastname: 'Khannouchi', dateOfBirth: '1971-12-22', gender: 'M', country: 'USA'),
    new Athlete(firstname: 'Sammy', lastname: 'Korir', dateOfBirth: '1971-12-12', gender: 'M', country: 'KEN'),
    new Athlete(firstname: 'Ronaldo', lastname: 'da Costa', dateOfBirth: '1970-06-07', gender: 'M', country: 'BRA'),
    new Athlete(firstname: 'Paula', lastname: 'Radcliffe', dateOfBirth: '1973-12-17', gender: 'F', country: 'GBR')
]

def bornSince70 = {
asDate(it.dateOfBirth) > asDate('1970-1-1') }
def excludingKh = { it.lastname <= 'Kg' ||
it.lastname >= 'Ki' }
def byGenderDescThenByCountry = { a, b ->
a.gender == b.gender ?
a.country <=> b.country : b.gender <=> a.gender }
def someYoungsters = athletes.
findAll(bornSince70).
findAll(excludingKh).
sort(byGenderDescThenByCountry)
someYoungsters.each {
def name = "$it.firstname $it.lastname".padRight(25)
println "$name ($it.gender) $it.country $it.dateOfBirth"
}

// ---XML---
println "------------------XML------------------"
def CAR_RECORDS = '''
<records>
<car name='HSV Maloo' make='Holden' year='2006'>
<country>Australia</country>
<record type='speed'>Production Pickup Truck with speed of 271kph</record>
</car>
<car name='P50' make='Peel' year='1962'>
<country>Isle of Man</country>
<record type='size'>Smallest Street-Legal Car at 99cm wide and 59 kg in weight</record>
</car>
<car name='Royale' make='Bugatti' year='1931'>
<country>France</country>
<record type='price'>Most Valuable Car at $15 million</record>
</car>
</records>
'''

def records = new XmlSlurper().parseText(CAR_RECORDS)
assert 3 == records.car.size()
assert 10 == records.depthFirst().collect{it}.size()
