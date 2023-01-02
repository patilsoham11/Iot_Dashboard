from django.db import models

from twilio.rest import Client

# Create your models here.
class scan_data(models.Model):
    slave_id = models.IntegerField()
    first_scan = models.CharField(max_length=50)
    first_scan_datetime = models.DateTimeField()
    air_pressure = models.CharField(max_length=50)
    leak_rate = models.CharField(max_length=50)
    ok_signal = models.CharField(max_length=10)
    test_datetime = models.DateTimeField()
    second_scan = models.CharField(max_length=50)
    second_scan_datetime = models.DateTimeField()
    device_id = models.CharField(max_length=50)
    varient = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'scan_data'
    
        

class print_data(models.Model):
    piid = models.IntegerField()
    qrcode = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    extra1 = models.BigIntegerField()
    extra2 = models.CharField(max_length=20)
    extra3 = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    add_date = models.DateTimeField()
    device_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'print_data'



        
        
class Company_Info(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=10)
    company_address = models.CharField(max_length=50)
    company_logo = models.ImageField(upload_to='images',default="")
    company_image= models.ImageField(upload_to='images',default="")
    # created_date =  models.DateTimeField(auto_now_add=True)
    created_date =  models.DateField(blank=True,null= True)
    updated_date =  models.DateTimeField(auto_now_add=True)
    deleted_date =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.company_name 
        
        
class Device_Details(models.Model):
    device_id = models.AutoField(primary_key=True)
    
    company_id = models.ForeignKey(Company_Info, on_delete = models.CASCADE)
    
    device_name = models.CharField(max_length=20)
    time_stamp = models.TimeField(auto_now_add=True)
    installed_date =  models.DateField()
    # extra1 = models.CharField(max_length=20)
    # extra2 = models.CharField(max_length=20)
    # extra3 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.device_name
        
    
    

class Alert_Master(models.Model):
    alert_master_id = models.AutoField(primary_key=True)
    
    device_id = models.ForeignKey(Device_Details, on_delete=models.CASCADE)
    
    alert_massage = models.CharField(max_length=20)
    register = models.IntegerField()
    counts = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.register)
    
    # def save(self, *args, **kwargs):
        #if test_result is less than 80 execute this
        # if self.register < 1:
        #     #twilio code
        #     account_sid = 'ACbf006fd11a72689c80ec0bc8e8012c02'
        #     auth_token = 'd128f871cf42beae11e3dae639eadb9d'
        #     client = Client(account_sid, auth_token)

        #     message = client.messages.create(
        #                             body=f'your Plc register number is {self.register} and msg is {self.alert_massage} and count is {self.counts}',
        #                             from_='+13089373173',
        #                             to='+918329853765' 
        #                         )
        # return super().save(*args, **kwargs)
    
      
    
class User_Details(models.Model):
    user_id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company_Info, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length = 254,unique=True)
    phone_number = models.CharField(max_length=12,unique=True)
    address = models.CharField(max_length=50)


class Alert_Data(models.Model):
    alart_id = models.AutoField(primary_key=True)
    iot_id = models.ForeignKey(Company_Info, on_delete=models.CASCADE)
    device_id = models.IntegerField()
    register = models.IntegerField
    date_time = models.DateTimeField(auto_now_add=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    
    

        

    
    
    
    
  