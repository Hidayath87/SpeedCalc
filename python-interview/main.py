import csv

class DataSet:
    def __init__(self, distance, time):
        self.distance = distance
        self.time = time


class UserInput:
    def __init__(self, list_of_users):
        self.list_of_users = list_of_users

    def callback(self):
        return self.list_of_users


class Measure:

    def method_measure(self):
        user_distance = []
        user_time = []
        for length in range(0, 10):
            distance = input("Distance: ")
            distance_variable = UserInput(distance).list_of_users
            user_distance.append(distance_variable)
            time = input("Time: ")
            time_variable = UserInput(time).list_of_users
            user_time.append(time_variable)

        speed = []
        for position in range(0, 9):
            distance = int(user_distance[position])
            time = int(user_time[position])
            speed_answer = distance/time
            speed.append(speed_answer)
        print(speed)

        with open('exported_data.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(speed)


class ShowResults:
    def show_result(self):
        answer = Measure()
        answer.method_measure()


if __name__ == '__main__':
    show_result = ShowResults()
    show_result.show_result()
