

from django.db import models
# Customer class
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Sales pearson dealership class
class Salesperson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Type of car in dealership
class Car(models.Model):
    serial_number = models.CharField(max_length=100)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    car_for_sale = models.BooleanField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.serial_number})"


class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length=20)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice #{self.invoice_number}"

#Mechanic in dealership 
class Mechanic(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.service_name


class ServiceTicket(models.Model):
    service_ticket_number = models.CharField(max_length=30)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    comments = models.TextField(blank=True)
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Ticket #{self.service_ticket_number}"


class ServiceMechanic(models.Model):
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Mechanic {self.mechanic} - Ticket {self.service_ticket}"


class Part(models.Model):
    part_number = models.CharField(max_length=30)
    description = models.TextField()
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    retail_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Part {self.part_number}"

#Dealership parts
class PartsUsed(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    number_used = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.number_used} x {self.part} for {self.service_ticket}"
