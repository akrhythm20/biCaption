from django.db import models


class Customer(models.Model):
    customer_id = models.IntegerField(default=0, null=True, blank=True)
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    state = models.CharField(max_length=100, null=True,  blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank = True)

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)


class Photographer(models.Model):
   
    CATEGORY_OPTIONS = (
        ('Event', 'Event'),
        ('Fashion', 'Fashion'),
        ('Sports', 'Sports'),
        ('Food', 'Food'),
        ('Art_and_Portrait', 'Art_and_Portrait'),
        ('Architecture', 'Architecture'),
        ('Documentary', 'Documentary'),
        ('Travel', 'Travel'),
        ('Modelling_and_Lifestyle', 'Modelling_and_Lifestyle'),
        ('Nature_and_Wildlife', 'Natue_and_Wildlife'),
        ('Product', 'Product'),
        ('Photo_Journalism', 'Photo_journalism')
    )


    STATUS_OPTIONS = (
        ('Available', 'Available'),
        ('Busy', 'Busy')
    )

    photographer_id = models.IntegerField(default=0, null=True, blank=True)
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True,  blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    category = models.CharField(
        max_length=100,
        choices = CATEGORY_OPTIONS,
        null=True, 
        blank=True
    )
    area = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length = 20,
        choices = STATUS_OPTIONS,
        default = 'Available',
        null=True, 
        blank=True
    )
    image = models.ImageField(upload_to="images/", blank=True, null = True)

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)    
    photographer = models.ForeignKey(Photographer, on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    appointment_status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return str(self.customer.fname) + " " + str(self.customer.lname)