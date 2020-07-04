import os
import csv

class CarBase:
    car_type=""
    def __init__(self,brand,photo_file_name,carrying):
        if (photo_file_name.endswith(".jpg") or photo_file_name.endswith(".jpeg") or
            photo_file_name.endswith(".png") or photo_file_name.endswith(".gif")):
            self.photo_file_name=photo_file_name
        else:
            raise ValueError("Неверный путь к фотографии")
        self.brand=brand
        self.carrying=float(carrying)
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
    car_type="car"
    def __init__(self,brand,photo_file_name,carrying,passenger_seats_count):
        super().__init__(brand,photo_file_name,carrying)
        self.passenger_seats_count=int(passenger_seats_count)

class Truck(CarBase):
    car_type="truck"
    def __init__(self,brand,photo_file_name,carrying,body_whl):
        super().__init__(brand,photo_file_name,carrying)
        if not body_whl:
            self.init_zero_values()
        else:
            try:
                measure_list=body_whl.split("x")
                if len(measure_list)>3:
                    self.init_zero_values()
                else:
                    self.body_length=float(measure_list[0])
                    self.body_width=float(measure_list[1])
                    self.body_height=float(measure_list[2])
            except(ValueError,IndexError):
                self.init_zero_values()
    def init_zero_values(self):
         self.body_length = 0.0
         self.body_width = 0.0
         self.body_height = 0.0
    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height

class SpecMachine(CarBase):
    car_type="spec_machine"
    def __init__(self,brand,photo_file_name,carrying,extra):
        super().__init__(brand,photo_file_name,carrying)
        self.extra=extra

def get_car_list(csv_filename):
    car_list=[]
    with open(csv_filename) as csv_fd:
        reader=csv.reader(csv_fd,delimiter=";")
        next(reader)
        for row in reader:
            if not row:
                continue
            try:
                car_type=row[0]
                if not car_type:
                     continue
                photo_file_name=row[3]
                if not photo_file_name:
                    continue
                brand=row[1]
                if not brand:
                    continue
                carrying=row[5]
                if not carrying:
                    continue
                if car_type=="car":
                    passenger_seats_count=row[2]
                    if not passenger_seats_count:
                        continue
                    car=Car(brand,photo_file_name,carrying,passenger_seats_count)
                    car.car_type="car"
                    car_list.append(car)
                elif car_type=="truck":
                    body_whl=row[4]
                    car=Truck(brand,photo_file_name,carrying,body_whl)
                    car_list.append(car)
                elif car_type=="spec_machine":
                    extra=row[6]
                    if not extra:
                        continue
                    car=SpecMachine(brand,photo_file_name,carrying,extra)
                    car_list.append(car)
            except (ValueError,IndexError):
                continue
    return car_list

