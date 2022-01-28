from django.db import models

# Create your models here.
class Customer(models.Model):
    STATE_OPTION = (
        ("AN","Andaman and Nicobar Islands"),
        ("AP","Andhra Pradesh"),
        ("AR","Arunachal Pradesh"),
        ("AS","Assam"),
        ("BR","Bihar"),
        ("CG","Chhattisgarh"),
        ("CH","Chandigarh"),
        ("DN","Dadra and Nagar Haveli"),
        ("DD","Daman and Diu"),
        ("DL","Delhi"),
        ("GA","Goa"),
        ("GJ","Gujarat"),
        ("HR","Haryana"),
        ("HP","Himachal Pradesh"),
        ("JK","Jammu and Kashmir"),
        ("JH","Jharkhand"),
        ("KA","Karnataka"),
        ("KL","Kerala"),
        ("LA","Ladakh"),
        ("LD","Lakshadweep"),
        ("MP","Madhya Pradesh"),
        ("MH","Maharashtra"),
        ("MN","Manipur"),
        ("ML","Meghalaya"),
        ("MZ","Mizoram"),
        ("NL","Nagaland"),
        ("OD","Odisha"),
        ("PB","Punjab"),
        ("PY","Pondicherry"),
        ("RJ","Rajasthan"),
        ("SK","Sikkim"),
        ("TN","Tamil Nadu"),
        ("TS","Telangana"),
        ("TR","Tripura"),
        ("UP","Uttar Pradesh"),
        ("UK","Uttarakhand"),
        ("WB","West Bengal")
    )

    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    state = models.CharField(
        max_length=100,
        choices= STATE_OPTION,
        default=None
    )
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=200)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name


class Photographer(models.Model):
    STATE_OPTION = (
        ("AN","Andaman and Nicobar Islands"),
        ("AP","Andhra Pradesh"),
        ("AR","Arunachal Pradesh"),
        ("AS","Assam"),
        ("BR","Bihar"),
        ("CG","Chhattisgarh"),
        ("CH","Chandigarh"),
        ("DN","Dadra and Nagar Haveli"),
        ("DD","Daman and Diu"),
        ("DL","Delhi"),
        ("GA","Goa"),
        ("GJ","Gujarat"),
        ("HR","Haryana"),
        ("HP","Himachal Pradesh"),
        ("JK","Jammu and Kashmir"),
        ("JH","Jharkhand"),
        ("KA","Karnataka"),
        ("KL","Kerala"),
        ("LA","Ladakh"),
        ("LD","Lakshadweep"),
        ("MP","Madhya Pradesh"),
        ("MH","Maharashtra"),
        ("MN","Manipur"),
        ("ML","Meghalaya"),
        ("MZ","Mizoram"),
        ("NL","Nagaland"),
        ("OD","Odisha"),
        ("PB","Punjab"),
        ("PY","Pondicherry"),
        ("RJ","Rajasthan"),
        ("SK","Sikkim"),
        ("TN","Tamil Nadu"),
        ("TS","Telangana"),
        ("TR","Tripura"),
        ("UP","Uttar Pradesh"),
        ("UK","Uttarakhand"),
        ("WB","West Bengal")
    )

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

    GENDER_OPTIONS = (
        ('Male', '1'),
        ('Female', '0')
    )

    STATUS_OPTIONS = (
        ('Available', 'Available'),
        ('Busy', 'Busy')
    )

    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(
        max_length=10,
        choices = GENDER_OPTIONS,
        default='1'
    )
    dob = models.DateTimeField()
    category = models.CharField(
        max_length=100,
        choices = CATEGORY_OPTIONS
    )
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=50,
        choices = STATE_OPTION,
        default = "AN"
    )
    pincode = models.IntegerField()
    status = models.CharField(
        max_length = 20,
        choices = STATUS_OPTIONS,
        default = 'Available'
    )

    def __str__(self):
        return self.name


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    Photographer = models.ForeignKey(Photographer, on_delete=models.SET_NULL, blank=True, null=True)
    payment_status = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.customer.name
