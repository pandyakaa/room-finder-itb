import os
from decouple import config
from flask import (
    Flask, request, abort
)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
app = Flask(__name__)
# get LINE_CHANNEL_ACCESS_TOKEN from your environment variable
line_bot_api = LineBotApi(
    config("LINE_CHANNEL_ACCESS_TOKEN",
           default=os.environ.get('LINE_ACCESS_TOKEN'))
)
# get LINE_CHANNEL_SECRET from your environment variable
handler = WebhookHandler(
    config("LINE_CHANNEL_SECRET",
           default=os.environ.get('LINE_CHANNEL_SECRET'))
)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
#########################################################
carapake = 'Bot ini dapat digunakan untuk mencari nama bangunan dari input kode ruangan yang kalian masukkan. Misal, kalian memasukkan input \"9127\", bot ini akan membalas dengan \"GKU Barat Lantai 2\". Ketik \"tutorial\" untuk lihat penggunaan.'

########################################################################################################
def balas(event, balasan):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=balasan))

########################################################################################################
ruang = {'9008' : 'Teknik Lingkungan (gedung lama)',
         '9009' : 'LFM Lantai I',
		 '9011' : 'Labtek VIII Lantai II',
		 '9012' : 'Labtek VII',
		 '9013' : 'Labtek VII',
		 '9014' : 'Labtek VII',
		 '9015' : 'Labtek VIII Lantai II',
		 '9016' : 'Oktagon Lantai I',
		 '9017' : 'Oktagon Lantai I',
		 '9018' : 'Oktagon Lantai I',
		 '9019' : 'Oktagon Lantai II',
         '9020' : 'Oktagon Lantai II',
         '9021' : 'Oktagon Lantai II',
         '9025' : 'Oktagon Lantai II',
         '9026' : 'Oktagon Lantai II',
         '9027' : 'Oktagon Lantai II',
         '9022' : 'TVST Lantai I',
         '9023' : 'TVST Lantai I',
         '9024' : 'TVST Lantai I',
         'TVST - A': 'TVST Lantai II',
         'TVST - B': 'TVST Lantai II',
         'TVST - C': 'TVST Lantai II',
         '9103': 'GKU Barat Lantai I',
         '9104': 'GKU Barat Lantai I',
         '9107': 'GKU Barat Lantai I',
         '9108': 'GKU Barat Lantai I',
         '9114': 'GKU Barat Lantai II',
         '9115': 'GKU Barat Lantai II',
         '9116': 'GKU Barat Lantai II',
         '9121': 'GKU Barat Lantai II',
         '9122': 'GKU Barat Lantai II',
         '9124': 'GKU Barat Lantai II',
         '9125': 'GKU Barat Lantai II',
         '9126': 'GKU Barat Lantai II',
         '9127': 'GKU Barat Lantai II',
         '9128': 'GKU Barat Lantai II',
         '9131': 'GKU Barat Lantai III',
         '9132': 'GKU Barat Lantai III',
         '9133': 'GKU Barat Lantai III',
         '9134': 'GKU Barat Lantai III',
         '9135': 'GKU Barat Lantai III',
         '9136': 'GKU Barat Lantai III',
         '9137': 'GKU Barat Lantai III',
         '9138': 'GKU Barat Lantai III',
         '9213': 'GKU Timur Lantai II',
         '9214': 'GKU Timur Lantai II',
         '9221': 'GKU Timur Lantai III',
         '9222': 'GKU Timur Lantai III',
         '9223': 'GKU Timur Lantai III',
         '9224': 'GKU Timur Lantai III',
         '9231': 'GKU Timur Lantai IV',
         '9232': 'GKU Timur Lantai IV',
         '9233': 'GKU Timur Lantai IV',
         '9234': 'GKU Timur Lantai IV',
         '9301': 'Labtek V',
         '9302': 'Labtek V',
         '9303': 'Labtek V',
         '9304': 'Labtek V',
         '9305': 'Labtek V',
         '9306': 'Labtek V',
         '9315': 'Labtek V',
         '9307': 'Labtek VI',
         '9308': 'Labtek VI',
         '9309': 'Labtek VI',
         '9311': 'Labtek VI',
         '9312': 'Labtek VI',
         '9313': 'Labtek VI',
         '9314': 'Labtek VI',
         '9401': 'Labtek I Lantai II',
         '9402': 'Labtek I Lantai II',
         '9404': 'Labtek I Lantai II',
         '9405': 'Labtek I Lantai II',
         'BSC - A': 'Basic Science A Lantai IV',

         '1318' : 'Prodi Kimia Lantai 3',
		 '2104' : 'Prodi Kimia Lantai 1',
		 '2201' : 'SITH Jembatan Labtek Biru, antara Labtek X dan XI',
		 '2202' : 'SITH Jembatan Labtek Biru, antara Labtek X dan XI',
		 '2203' : 'SITH Jembatan Labtek Biru, antara Labtek X dan XI',
		 '3101' : 'Sipil',
		 '3102' : 'Sipil',
		 '3103' : 'Sipil',
		 '3104' : 'Sipil',
		 '3105' : 'Sipil',
         '3201' : 'Sipil',
         '3202' : 'Sipil',
         '3203' : 'Sipil',
         '3204' : 'Sipil',
         '3205' : 'Sipil',
         '3206' : 'Sipil',
         '3209' : 'Sipil',
         '3210' : 'Sipil',
         '3211' : 'Sipil',
         '3213' : 'Sipil',
         '3214' : 'Sipil',
         '4101' : 'Gedung FTMD lantai 1',
         '4102' : 'Gedung FTMD lantai 1',
         '4103' : 'Gedung FTMD lantai 4',
         '4104' : 'Gedung FTMD lantai 4',
         '4105' : 'Gedung FTMD lantai 4',
         '4106' : 'Gedung FTMD lantai 4',
         '4201' : 'Basement Labtek 8 / Labtek 5',
         '5201' : 'Teknik Kimia',
         '5202' : 'Teknik Kimia',
         '6101' : 'Arsitektur / Labtek IX-B',
         '6102' : 'Arsitektur / Labtek IX-B',
         '6302' : 'Planologi / Labtek IX-A',
         '6303' : 'Planologi / Labtek IX-A',
         '6305' : 'Planologi / Labtek IX-A',
         '6306' : 'Planologi / Labtek IX-A',
         '7601' : 'Labtek 5 lantai 1',
         '7602' : 'Labtek 5 lantai 3',
         '7603' : 'Labtek 5 lantai 3',
         '7604' : 'Labtek 5 lantai 3',
         '7605' : 'Labtek 5 lantai 3',
         '7606' : 'Labtek 5 lantai 3',
         '7607' : 'Labtek 5 lantai 3',
         '7608' : 'Labtek 5 lantai 3',
         '7609' : 'Labtek 5 lantai 3',
         '7610' : 'Labtek 5 lantai 3',
         '9501' : 'Gedung Doping',
         '9502' : 'Gedung Doping',
         '9513' : 'CRCS Lantai 2',
         '9514' : 'CRCS Lantai 2',
         '9515' : 'CRCS Lantai 2',
         '9516' : 'CRCS Lantai 2',
         '9517' : 'CRCS Lantai 2',
         '9521' : 'CAS Lantai 3',
         '9522' : 'CAS Lantai 3',
         '9531' : 'CADL Lantai 2',
         '9532' : 'CADL Lantai 2',
         '9533' : 'CADL Lantai 2',

         '9601' : 'Gedung A ITB Jatinangor',
         '9602' : 'Gedung A ITB Jatinangor',
         '9603' : 'Gedung A ITB Jatinangor',
         '9604' : 'Gedung A ITB Jatinangor',
         '9605' : 'Gedung A ITB Jatinangor',
         '9606' : 'Gedung A ITB Jatinangor',

         '9616' : 'Gedung B ITB Jatinangor',
         '9617' : 'Gedung B ITB Jatinangor',

         '9624' : 'Gedung C ITB Jatinangor',
         '9625' : 'Gedung C ITB Jatinangor',
         '9626' : 'Gedung C ITB Jatinangor',
         '9627' : 'Gedung C ITB Jatinangor',
         '9628' : 'Gedung C ITB Jatinangor',
         '9629' : 'Gedung C ITB Jatinangor',
         '9630' : 'Gedung C ITB Jatinangor',
         '9631' : 'Gedung C ITB Jatinangor',
         '9632' : 'Gedung C ITB Jatinangor',

         '9639' : 'Gedung D ITB Jatinangor',
         '9640' : 'Gedung D ITB Jatinangor',
         '9641' : 'Gedung D ITB Jatinangor',
         '9642' : 'Gedung D ITB Jatinangor',
         '9634' : 'Gedung D ITB Jatinangor',
         '9635' : 'Gedung D ITB Jatinangor',
         '9636' : 'Gedung D ITB Jatinangor',

         '9649' : 'Gedung E ITB Jatinangor',
         '9650' : 'Gedung E ITB Jatinangor',
         '9651' : 'Gedung E ITB Jatinangor',
         '9652' : 'Gedung E ITB Jatinangor',

         '9675' : 'GKU-1 ITB Jatinangor',
         '9676' : 'GKU-1 ITB Jatinangor',
         '9677' : 'GKU-1 ITB Jatinangor',

         '9653' : 'GKU-2 ITB Jatinangor',
         '9654' : 'GKU-2 ITB Jatinangor',
         '9655' : 'GKU-2 ITB Jatinangor',
         '9656' : 'GKU-2 ITB Jatinangor',

         '9658' : 'Labtek 1-A ITB Jatinangor', 
         '9659' : 'Labtek 1-A ITB Jatinangor', 
         '9660' : 'Labtek 1-A ITB Jatinangor',

         '9667' : 'Labtek 1-B ITB Jatinangor',
         '9668' : 'Labtek 1-B ITB Jatinangor',
         '9669' : 'Labtek 1-B ITB Jatinangor',
         '9670' : 'Labtek 1-B ITB Jatinangor',
         '9671' : 'Labtek 1-B ITB Jatinangor',
         '9672' : 'Labtek 1-B ITB Jatinangor',
         '9673' : 'Labtek 1-B ITB Jatinangor',
         '9674' : 'Labtek 1-B ITB Jatinangor',

         'KOICA 1' : 'Gedung KOICA ITB Jatinangor',
         'KOICA 2' : 'Gedung KOICA ITB Jatinangor',
         }
########################################################################################################
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	pesan = event.message.text
	if (pesan in ruang):
		balas(event, ruang[pesan])
	elif (pesan == 'tutorial'):
		balas(event, carapake)
	else:
		balas(event, 'Kode ruangan salah, masukkan kode ruangan yang benar!')

########################################################################################################

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)