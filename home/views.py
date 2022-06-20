from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.views import View

from .forms import IndexSendForm
from .models import IndexSendEmail
# Create your views here.

class homeIndex(View):
    def get(self , request):
        CE = IndexSendForm
        cursor = connection.cursor()
        cursor.execute("select properties_country.nameCountry,properties_province.nameProvince,properties_district.nameDistrict,properties_commune.nameCommune,properties_house.Price,properties_house.KindOfHouse,properties_house.State,properties_house.legalDocuments,properties_house.LandArea,properties_house.Size,properties_house.link_map,properties_house.urlFrame,properties_house.Description,properties_house.YearBuilt,properties_imagehouse.LinkImageFirst,properties_imagehouse.LinkImageSecond,properties_imagehouse.LinkImageThird,properties_imagehouse.LinkImageFourth,properties_imagehouse.LinkImageFifth,properties_imagehouse.NoteImage,properties_topprovince.FooterImage,properties_service.nameServiceFirst,properties_service.QuatityFirst,properties_service.nameServiceSecond,properties_service.QuatitySecond,properties_service.nameServiceThird,properties_service.QuatityThird,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook,properties_features.InteriorDetailsFirst,properties_features.InteriorDetailsSecond,properties_features.InteriorDetailsThird,properties_features.InteriorDetailsThird,properties_features.OutdoorFirst,properties_features.OutdoorSecond,properties_features.OutdoorThird,properties_features.UtilitiesFirst,properties_features.UtilitiesSecond,properties_features.UtilitiesThird,properties_features.OtherFirst,properties_features.OtherSecond from properties_house join properties_houselessor on properties_house.HouseLessor_id = properties_houselessor.id join properties_imagehouse on properties_imagehouse.House_id = properties_house.id join properties_province on properties_province.id = properties_house.Province_id join properties_district on properties_district.id = properties_house.District_id join properties_commune on properties_commune.id = properties_house.Commune_id join properties_servicehouse on properties_servicehouse.House_id = properties_house.id join properties_service on properties_service.id = properties_servicehouse.Service_id join properties_topprovince on properties_province.id = properties_topprovince.nameProvince_id JOIN properties_country on properties_house.Country_id = properties_country.id JOIN properties_features on properties_house.Features_id = properties_features.id order by properties_house.Price DESC")
        # trả về dữ liệu được lưu trữ bên trong bảng dưới dạng các hàng,có thể lặp lại kết quả để có được các hàng riêng lẻ.
        results = cursor.fetchall()
        cusorSecond = connection.cursor()
        cusorSecond.execute("select * from contact_feedback limit 3")
        resultSecond = cusorSecond.fetchall()
        
        cursorThird = connection.cursor()
        cursorThird.execute("select properties_houselessor.id,properties_houselessor.NameLessor,properties_houselessor.Sex,properties_houselessor.PhoneNumber,properties_houselessor.Image,properties_houselessor.Address,properties_houselessor.Email,properties_houselessor.Facebook from properties_houselessor")
        # trả về dữ liệu được lưu trữ bên trong bảng dưới dạng các hàng,có thể lặp lại kết quả để có được các hàng riêng lẻ.
        resultsThird = cursorThird.fetchall()
        
        return render(request, 'home/index.html',{'HouseList' : results , 'FeedBackLists' : resultSecond,'HouseLessor':resultsThird , 'CE': CE})

    def post(self,request):
        if request.method == "POST":
            CE = IndexSendForm(request.POST)
            if CE.is_valid():
                CE.save()
                return HttpResponse('Send Success')
        else:
            return HttpResponse('not Post')



def create(self,request):
    return HttpResponse('123')