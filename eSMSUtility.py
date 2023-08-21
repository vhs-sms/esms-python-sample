#
#   Author: Nguyen Huu Quy (quynh@vihatgroup.com)
#   DateCrate: 20/04/2019
#   DatePublish: 30/09/2021
#

#
#   Cac ban dang nhap vao trang tai khoan eSMS.vn de lay apikey & serectkey
#   Neu ban chua co tai khoan, click vao link ( https://account.esms.vn/Account/SignUp?referredInfo=35276 ) de tao tai khoan nhe
#   Voi tai khoan moi, ban se duoc tang 5k vao tai khoan khuyen mai & duoc cap BrandName QCAO_ONLINE dung thu
#

import json;
import requests;

class eSMSvn:
    ESMS_BASE_API = 'http://rest.esms.vn/MainService.svc/json/';

    def __init__(esms, apikey, serectkey):
        esms.apikey = apikey;
        esms.serectkey = serectkey;

    def send_sms_with_brandname_get(esms, phone, content, brandname):
        func_name = 'SendMultipleMessage_V4_get';
        smstype = '2';
        payload = {
            'APIKEY' : esms.apikey, 
            'SECRETKEY' : esms.serectkey, 
            'CONTENT' : content, 
            'SMSTYPE' : smstype, 
            'BRANDNAME' : brandname, 
            'PHONE' : phone
        };

        request = eSMSvn.ESMS_BASE_API + func_name;
        response = requests.get(request, params = payload);
        json_data = json.loads(response.text);

        print(response.url);
        print(response.json());
        print('SMSID = ' + json_data['SMSID']);
        print('CodeResult = ' + json_data['CodeResult']);

    def send_sms_with_brandname_post(esms, phone, content, brandname):
        func_name = 'SendMultipleMessage_V4_post/';
        smstype = '2';

        param = {
            'APIKEY' : esms.apikey, 
            'SECRETKEY' : esms.serectkey, 
            'CONTENT' : content, 
            'SMSTYPE' : smstype, 
            'BRANDNAME' : brandname, 
            'PHONE' : phone
        };

        request = eSMSvn.ESMS_BASE_API + func_name;
        response = requests.post(request, data = param);
        json_data = json.loads(response.text);

        print(response.url);
        print(response.json());
        print('SMSID = ' + json_data['SMSID']);
        print('CodeResult = ' + json_data['CodeResult']);

    def send_multi_channel_message_post(esms, phone, oaid, znstempid, dataZNStemp, smstype, brandname, smscontent):
        func_name = 'MultiChannelMessage/';

        headers = {
            'Content-Type': 'application/json'
        }

        param = {
            'ApiKey' : esms.apikey, 
            'SecretKey' : esms.serectkey, 
            'Phone' : phone,
            "Channels": [
                "zalo",
                "sms"
            ],
            "Data": [
                {
                    "OAID": oaid,
                    "TempID": znstempid,
                    "Params": dataZNStemp,
                },
                {
                    "Content": smscontent,
                    "IsUnicode": 0,
                    "SmsType": smstype,
                    "Brandname": brandname,
                }
            ]
        };

        request = eSMSvn.ESMS_BASE_API + func_name;
        response = requests.request("POST", request, headers=headers, json=param)
        json_data = json.loads(response.text);

        print(response.url);
        print(response.json());
        print('SMSID = ' + json_data['SMSID']);
        print('CodeResult = ' + json_data['CodeResult']);

# test api
test = eSMSvn('xxxx', 'xxxx');
# test.send_sms_with_brandname_get('076654161x', 'this is send get from puthon', 'Baotrixemay');
# test.send_sms_with_brandname_post('076654161x', 'this is send post from puthon', 'Baotrixemay');
test.send_multi_channel_message_post(phone='0766541618', oaid='4361812075662036180', znstempid='200300', dataZNStemp=[ "9786", "eSMS.vn" ], smstype=2, brandname='eSMS.vn', smscontent='Ma xac nhan dang ky tai khoan eSMS.vn cua ban la 892374 Hotline ho tro:0902.435.340');