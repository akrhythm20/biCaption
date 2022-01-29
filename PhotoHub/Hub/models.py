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

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)


class Photographer(models.Model):
   
    CATEGORY_OPTIONS = (
        ('Event', 'Event'),
        ('Fashion', 'Fashion'),
        ('Sports', 'Sports'),
        ('Food', 'Food'),
        ('Art and Portrait', 'Art and Portrait'),
        ('Architecture', 'Architecture'),
        ('Documentary', 'Documentary'),
        ('Travel', 'Travel'),
        ('Modelling and Lifestyle', 'Modelling and Lifestyle'),
        ('Nature and Wildlife', 'Natue and Wildlife'),
        ('Product', 'Product'),
        ('Photo Journalism', 'Photo journalism')
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

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    Photographer = models.ForeignKey(Photographer, on_delete=models.SET_NULL, blank=True, null=True)
    payment_status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.customer.name
