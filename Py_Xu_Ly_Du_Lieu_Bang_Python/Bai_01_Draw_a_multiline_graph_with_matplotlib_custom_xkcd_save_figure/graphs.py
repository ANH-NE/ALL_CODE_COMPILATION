from matplotlib import pyplot   #Python's plot
def draw_multiline():
    years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    companyA = [41596, 46000, 48510, 53310, 57200, 56000, 63316, 69741]
    companyB = [37596, 42000, 45510, 57310, 51200, 55000, 60316, 65741]
    companyC = [36596, 32000, 40510, 30310, 42200, 50000, 45316, 34741]

    # pyplot.xkcd() #sketch-style drawing mode: kiểu vẽ phát hoạ bằng tay
    pyplot.plot(years, companyA, color='red', linestyle='--', marker='.', markersize=20)
    pyplot.plot(years, companyB, color='#000BFF', linestyle='--', marker='p', markersize=10)
    pyplot.bar(years, companyC, color='#B40062')

    pyplot.xlabel('year')
    pyplot.ylabel('profit(usd)')
    pyplot.legend(["Company A", "Company B", "Company C"])
    # pyplot.grid(True)
    pyplot.savefig("multiline.png")

    pyplot.show()
    # print(pyplot.style.available) # in ra các kiểu đồ thị sẵn có trong phần terminal