
# This program implements a class "Student"
# and adds up the student's quiz scores,
# gets the total and the average of the scores.



class Student :
    
    # Constructor
    def __init__(self, studentName):
        self._name = (studentName)
        self._totalQuizScore = 0
        self._numOfQuizzes = 0

    # Get student name.
    def getName(self):
        return self._name

    # Add quiz score.
    def addQuiz(self, score):
        self._totalQuizScore += score
        self._numOfQuizzes += 1

    # Get total quiz score.
    def getTotalScore(self):
        return self._totalQuizScore

    # Get average score.
    def getAverageScore(self):
        return self._totalQuizScore / self._numOfQuizzes



def main():
    
    # Create instance of Student class.
    theStudent = Student("Bob ")

    # Display student name.
    print(theStudent.getName())

    # Add a quiz score. # ----- hardcode
    theStudent.addQuiz(90)
    theStudent.addQuiz(95)
    theStudent.addQuiz(78)

    # Get total and average score.
    print("The total score is: ", theStudent.getTotalScore())
    print("The average score is: ", "{:.2f}".format(theStudent.getAverageScore()))
    



main()
