# from django.db import models # Model Database NonSpasial
from django.contrib.gis.db import models # Model Database Spasial
from django.contrib.auth.models import User

# Create your models here.
class Facility(models.Model) :
    TYPE_CHOICES =[
        ('goverment','Pemerintahan'),
        ('public','Fasilitas Umum'),
        ('park', 'Taman'),
        ('house','Perumahan'),
        ('restaurant', 'Restoran')
    ]
    
    STATUS_CHOICES = [
        ('proposed', 'Proposed (Pengajuan)'),
        ('under_review', 'Under Review (Dalam Masa Peninjauan)'),
        ('planned', 'Planned (Sudah Direncakanan)'),
        ('cancelled', 'Cancelled (Dibatalkan)'),
        ('under_construction', 'Under Construction (Dalam Masa Pembangunan)'),
        ('completed', 'Completed (Selesai)')
    ]
    
    PRICE_CHOICES = [
        ('hourly', 'Per Jam'),
        ('daily', 'Per Hari'),
        ('weekly', 'Per Minggu'),
        ('monthly', 'Per Bulan'),
        ('annual', 'Per Tahun')
    ]
    name = models.CharField(max_length=50)
    types = models.CharField(max_length=30, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='proposed')
    open = models.BooleanField(default=False)
    location = models.PointField(srid=4326, spatial_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # didepan koma ada 8 angka, dibelakang koma ada 2
    price_unit = models.CharField(max_length=15, choices=PRICE_CHOICES)
    photo = models.ImageField(upload_to='facility')
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
