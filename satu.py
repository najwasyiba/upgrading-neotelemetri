laporan_minuman = [
    {
        'nama': 'kopi',
        'harga': '11000',
        'terjual': '10',
        'modal_satuan': 6000,
    },
    {
        'nama': 'teh_ES',
        'harga': '6000',
        'terjual': '12',
        'modal_satuan': '3500',
    },
    {
        'nama': 'jus',
        'harga': '10000',
        'terjual': '7',
        'modal_satuan': '6000',
    },
] # tidak ada yg perlu dibuah disini

# isi list makanan dan untuk nama, harga, terjual, modal satuan bebas tetapi diinput melalui terminal (cukup 2 makanan)
laporan_makanan = [] # format makanan sama dengan minuman
"""
format makanan
{
        'nama': '',
        'harga': '',
        'terjual': '',
        'modal_satuan': ,
}
"""

penjualan = {
    'minuman': laporan_minuman,
    'makanan': laporan_makanan,
    'summary': {
        'total_penjualan':{
            'makanan':'',
            'minuman':'',
            'semua':''
        },
        'keuntungan_penjualan':{
            'makanan':'',
            'minuman':'',
            'semua':'',
        },
        'special_case':'total_semua_penjualan+total_semua_keuntungan_penjualan+special_value+10000' # juga tidak ada yg perlu diubah dsn
    }
}

total_semua_penjualan = 0
total_semua_keuntungan_penjualan = 0
special_value = 0


# lakukan programn didalam fungsi ini
def main():
    global minuman, makanan, penjualan
    special_value = 1911212056 # ex: special_value = 2011512010
    print("Semangat Upgrading, Machine Learning Semangat")

    laporanMakanan = dict()
    for i in range(2):
        namaMakanan = input("Masukkan nama makanan: ")
        hargaMakanan = int(input("Harga makanan  : "))
        jumlahMakanan = int(input("Jumlah makanan : "))
        modalMakanan = int(input("Modal makanan  : "))
        laporanMakanan = {'nama': namaMakanan, 'harga': hargaMakanan, 'terjual': jumlahMakanan, 'modal_satuan': modalMakanan}
        laporan_makanan.append(laporanMakanan)

    penjualan['summary']['total_penjualan']['makanan'] = penjualan['makanan'][0]['terjual'] + penjualan['makanan'][1]['terjual']
    penjualan['summary']['total_penjualan']['minuman'] = int(penjualan ['minuman'][0]['terjual']) + \
        int(penjualan['minuman'][1]['terjual']) + \
        int(penjualan['minuman'][2]['terjual']) 
    penjualan['summary']['total_penjualan']['semua'] = int(penjualan['summary']['total_penjualan']['makanan']) + \
        int(penjualan['summary']['total_penjualan']['minuman'])

    print("=======")
    print("Penjualan makanan :", penjualan['summary']['total_penjualan']['makanan'])
    print("Penjualan minuman :", penjualan['summary']['total_penjualan']['minuman'])

    penjualan['summary']['keuntungan_penjualan']['makanan'] = (penjualan['makanan'][0]['terjual']*(penjualan['makanan'][0]['harga'] - \
        penjualan['makanan'][0]['modal_satuan'])) + \
        (penjualan['makanan'][1]['terjual']*(penjualan['makanan'][1]['harga'] - \
        penjualan['makanan'][1]['modal_satuan']))
    penjualan['summary']['keuntungan_penjualan']['minuman'] = int(penjualan['minuman'][0]['terjual']) * (int(penjualan['minuman'][0]['harga']) - \
        int(penjualan['minuman'][0]['modal_satuan'])) + \
        int(penjualan['minuman'][1]['terjual']) * (int(penjualan['minuman'][1]['harga']) - int(penjualan['minuman'][1]['modal_satuan'])) + int(penjualan['minuman'][2]['terjual']) * (int(penjualan['minuman'][2]['harga']) - int(penjualan['minuman'][2]['modal_satuan']))
    penjualan['summary']['keuntungan_penjualan']['semua'] = int(penjualan['summary']['keuntungan_penjualan']['makanan']) + \
        int(penjualan['summary']['keuntungan_penjualan']['minuman'])

    print("Keuntungan makanan :", penjualan['summary']['keuntungan_penjualan']['makanan'])
    print("Keuntungan minuman :", penjualan['summary']['keuntungan_penjualan']['minuman'])
    print('Laporan makanan :', penjualan['makanan'])
    print('Laporan minuman :', penjualan['minuman'])
    
    total_semua_penjualan = penjualan['summary']['total_penjualan']['semua'] # juga tidak ada yg perlu diubah dsn
    total_semua_keuntungan_penjualan = penjualan['summary']['keuntungan_penjualan']['semua'] # juga tidak ada yg perlu diubah dsn
    penjualan['summary']['special_case'] = total_semua_penjualan + total_semua_keuntungan_penjualan + special_value + 10000
    special_case = penjualan['summary']['special_case'] # perlu sedikit penambahan
    print("Total semua penjualan makanan dan minuman :", total_semua_penjualan)
    print("Total semua keuntungan penjualan :", total_semua_keuntungan_penjualan)
    print("Special case :", special_case)

if __name__ == "__main__":
    main()