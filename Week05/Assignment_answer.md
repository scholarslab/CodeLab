# Assignment 1 Answer

```python
import datetime

class Fellow:
    # Constructor. Name (in "firstname  lastname" format) and department are self-explanatory. Start_year is the year that the student started grad school.
    def __init__(self, name, department, start_year):
        # "self" refers to the instance of a class. This simple version just saves the parameters passed in to the constructor to the instance variables.
        self.name = name
        self.department = department
        self.start_year = start_year

        # But also initialize some internal instance variables that aren't passed in, but which we'll need to keep track of.
        # Here, we're going to assume that all fellows are students until we explicitly graduate() them.
        self.status = "student"

    def get_name(self):
        # Get the student's name that we stored to the instance in the constructor.
        return(self.name)
    
    def get_department(self):
        # Do the same for the department
        return(self.department)

    # Get the current status of the fellow. Fellows all start as "student", but can eventually become a "graduate". Let's not mention the third possibility.
    def get_status(self):
        return(self.status)

    # Sets the status of the student to "graduate" and caps get_year at a certain value
    def set_graduate(self, year):
        # Store year as instance variable graduate_year
        self.graduate_year = year
        # Set status to "graduate"
        self.status = "graduate"

    # Returns how many years the fellow has spent in their program (1 = "first year", etc) using the current, actual date. If the fellow has graduated, return how many years it took to graduate.
    # But if the student has already graduated, use that date instead of now.
    def get_year(self):
        # This is a little tricky. The computer knows what time it is and we can access it through the datetime module. But only use this if the student is a student
        if self.status == "student":
            end_date = datetime.date.today()
        else:
            # Here's the code for graduates. Not everyone graduates in the spring semester, but so this is not exactly right. But let's pretend that it is.
            end_date = datetime.datetime(self.graduate_year, 6, 1)
        # Create a date representing when the fellow started
        # datetime objects have built in arithmatic operator methods
        start_date = datetime.date(self.start_year, 9, 1)
        time_as_student = end_date - start_date
        # Return the days component of the time delta floor-divided by 365
        return(time_as_student.days // 365)

    # Invent a secret algorithm to based on some combination of the fellow's data (number of vowels in name, heiarchy of departments, etc) to generate a secret rating from 0-10 for a fellow. Be creative.
    def get_rating(self):
        if self.department == "History":
            return(11)
        return(10)

    # Return a string representing all the data for a student in as a single row of a CSV file.
    def printout(self):
        # There's a CSV module in the Python standard library, but let's just output it manually since it's easy enough.
        # Let's enumerate all the data in a list, cast as strings
        data = [self.name, self.department, self.status, str(self.start_year), str(self.get_year())]
        # Then let's use the string join method to enumerate the list as a long string delimited by quotes and commas.
        return '"'+'","'.join(data)+'"'

    # Compare two fellows. If they have all the same data, return true.
    def equals(self, f):
        # We just wrote a method to output all the data for a Fellow.
        # Let's be lazy and just compare that output.
        if self.printout() == f.printout():
            return(True)
        return(False)


class Fellowship:

    
    # Name is the name of the fellowship
    def __init__(self, name):
        self.name = name
        # initialize an empty dictionary to keep track of cohorts and fellows
        self.fellows = {}
    
    # Audit the program to check that there's been a cohort of 6 students every year and that no person appears multiple times in each cohort. Return True if the fellowship passes, False if it fails.
    def audit(self):
        # Cycle through all keys in the fellows dictionary
        for cohort_year in self.fellows:
            # if the number of fellows in the cohort isn't six, fail audit
            if len(self.fellows[cohort_year]) != 6:
                return False
            # nested-loop through the cohort to make sure that no fellow is equal to another
            for i in range(0, len(self.fellows[cohort_year])):
                for j in range(i+1, len(self.fellows[cohort_year])):
                    if self.fellows[cohort_year][i].equals(self.fellows[cohort_year][j]):
                        return(False)
        # If all that passes, return True to pass the audit.
        return(True)
    
    #Add fellow f to the fellowship in the cohort for year year
    def add_fellow(self, f, year):
        # Initialize the cohort as an empty list if the year is not a key in fellows
        if year not in self.fellows:
            self.fellows[year] = []
        # append the fellow to the end of the cohort list for that year
        self.fellows[year].append(f)

    # Return all the fellows for a particular year's cohort in a list. Figure out what to return if the cohort doesn't exist.
    def get_cohort(self, year):
        return(self.fellows[year])

    # Return the total rating for a cohort (add up all the students' individual ratings)
    def get_cohort_rating(self, year):
        rating = 0
        # Loop through the fellows for the cohort...
        for fellow in self.fellows[year]:
            # ... and add up all their ratings
            rating += fellow.get_rating()
        return(rating)

    # Return the best cohort or cohorts
    def get_best_cohort(self):
        # initialize best as None to start
        best_cohorts = None
        # Loop through the cohort
        for cohort_year in self.fellows:
            # if best is still None (e.g. this is the first iteration of this loop)
            if best_cohorts is None:
                # assign a list containing the current loop's cohort_year as the best
                best_cohorts = [cohort_year]
            else:
                # Otherwise, compare the current cohort_year to the best year's rating
                # and if it's better, replace best with a list containing the current
                if self.get_cohort_rating(cohort_year) > self.get_cohort_rating(best_cohorts[0]):
                    best_cohorts = [cohort_year]
                # If it's equal in rating, append that cohort_year
                elif self.get_cohort_rating(cohort_year) == self.get_cohort_rating(best_cohorts[0]):
                    best_cohorts.append(cohort_year)
        return(best_cohorts)

    # A new method for getting the departmental diversity (number of distinct departments) for each cohort.
    def get_diversity(self, year):
        # Create a set, which is like a list but only contains distinct members
        departments = set()
        # For each fellow in the cohort, add their department to the departments set.
        for fellow in self.fellows[year]:
            # Because of how the set works, duplicates are ignored
            departments.add(fellow.get_department())
        # return the length of the departments set, e.g. the number of nonduplicate departments
        return(len(departments))
            

    # Return the cohort or cohorts with fellows from the most number of departments
    def get_most_diverse(self):
        # Do the same flow as above, but for diversity
        # initialize most_diverse_year as None to start
        most_diverse_year = None
        for cohort_year in self.fellows:
            if most_diverse_year is None:
                most_diverse_year = [cohort_year]
            else:
                # Call the get_diversity method we defined above
                if self.get_diversity(cohort_year) > self.get_diversity(most_diverse_year[0]):
                    most_diverse_year = [cohort_year]
                # Call the get_diversity method we defined above
                if self.get_diversity(cohort_year) == self.get_diversity(most_diverse_year[0]):
                    most_diverse_year.append(cohort_year)
        return(most_diverse_year)
            
    # Return the cohort or cohorts with fellows from the least number of departments
    def get_least_diverse(self):
        # Do the same flow as above, but with < rather than >
        least_diverse_year = None
        for cohort_year in self.fellows:
            if least_diverse_year is None:
                least_diverse_year = [cohort_year]
            else:
                if self.get_diversity(cohort_year) < self.get_diversity(most_diverse):
                    least_diverse_year = [cohort_year]
                if self.get_diversity(cohort_year) == self.get_diversity(most_diverse):
                    least_diverse_year.append(cohort_year)
        return(least_diverse_year)

    # Return the department whose students are most frequently chosen
    def get_top_department(self):
        # Initialize a new dictionary for all departments to keep count of how many are in that department
        departments = {}
        # We're interested in fellows across all departments, so get all the values from the fellows dictionary and loop through them
        for fellow in self.fellows.values():
            # if fellow is found in departments, add one to its count
            if fellow.get_department() in departments:
                departments[fellow.get_department()] += 1
            # otherwise, assign it to 1, to reflect the fellow that we're currently cycling through
            else:
                departments[fellow.get_department()] == 1

    # Write the data for all the students to a CSV file using the filename parameter
    def write_to_file(self, filename):
        f = open(filename,"w")
        for cohort_year in self.fellows:
            for fellow in self.fellows[cohort_year]:
                # the "\n" is a charactger signalling a carriage return or new line.
                f.write(fellow.printout() + "\n")
        f.close()


praxis = Fellowship("Praxis")
praxis.add_fellow(Fellow("Brandon 'The Breaker' Walsh", "English", 2011), 2012)
praxis.add_fellow(Fellow("Shane Lin", "History", 2011), 2012)
praxis.add_fellow(Fellow("Chris Peck", "Music", 2010), 2012)
praxis.add_fellow(Fellow("Claire Maiers", "Sociology", 2010), 2012)
praxis.add_fellow(Fellow("Cecilia Márquez", "History", 2011), 2012)
praxis.add_fellow(Fellow("Gwen Nally", "Philosophy", 2007), 2012)

# I'm not actually sure when you all started
praxis.add_fellow(Fellow("Catherine Addington", "Spanish", 2016), 2018)
praxis.add_fellow(Fellow("Cho Jiang", "Urban and Environmental Planning", 2016), 2018)
praxis.add_fellow(Fellow("Chris Whitehead", "History", 2016), 2018)
praxis.add_fellow(
    Fellow("Eleanore Neumann", "Art and Architectural History", 2016), 2018)
praxis.add_fellow(Fellow("Emily Mellen", "Music", 2016), 2018)
praxis.add_fellow(Fellow("Mathilda Shepherd", "Spanish", 2016), 2018)


print(praxis.audit())
print(praxis.get_cohort(2012))
print(praxis.get_cohort_rating(2018))
print(praxis.get_best_cohort())
print(praxis.get_most_diverse())
praxis.write_to_file("praxis.txt")
```
